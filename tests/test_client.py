import json

import httpx
import pytest

from controlresell import (
    IDEMPOTENCY_KEY_HEADER,
    ConflictError,
    ControlResell,
    NotFoundError,
    RateLimitError,
    RetryPolicy,
    ServerError,
    __version__,
)

KEY = "cr_test_secret"
FAST = RetryPolicy(base_delay=0.001, max_delay=0.005)


def reply(body, status=200, headers=None):
    return httpx.Response(status, json=body, headers=headers or {})


def envelope(code):
    return {"error": {"code": code, "message": "m", "params": {}, "requestId": "req-1"}}


def item(id, sex="WOMEN"):
    return {
        "id": id, "name": "n", "sku": None, "description": None, "photos": [], "categoryId": None, "brandId": None,
        "sizeId": None, "colorIds": [], "state": None, "sex": sex, "labels": [], "sold": False,
        "estimatedPrice": {"amount": "12.50", "currency": "EUR"}, "purchasePrice": None, "purchaseDate": None,
        "sellingPrice": None, "sellingDate": None, "createdAt": "2026-10-20T10:00:00Z",
        "updatedAt": "2026-10-20T10:00:00Z", "unknownField": 1,
    }


def client(handler):
    requests = []

    def record(request):
        requests.append(request)
        return handler(request)

    return requests, ControlResell(api_key=KEY, base_url="https://api.test", retry=FAST, transport=httpx.MockTransport(record))


def test_a_call_sends_the_key_and_the_user_agent():
    requests, sdk = client(lambda r: reply({"id": 1, "username": "seller", "currency": "EUR", "unknownField": True}))
    assert sdk.me.get().username == "seller"
    assert requests[0].headers["Authorization"] == f"Bearer {KEY}"
    assert requests[0].headers["User-Agent"] == f"controlresell-python/{__version__}"


def test_an_error_is_typed_by_its_status_with_its_code_and_request_id():
    _, sdk = client(lambda r: reply(envelope("item_not_found"), 404))
    with pytest.raises(NotFoundError) as caught:
        sdk.items.get(1)
    assert caught.value.code == "item_not_found"
    assert caught.value.request_id == "req-1"
    assert KEY not in str(caught.value)


def test_a_rate_limit_is_retried_after_retry_after_then_succeeds():
    calls = []

    def handler(request):
        calls.append(request)
        return reply(envelope("rate_limited"), 429, {"Retry-After": "0"}) if len(calls) == 1 else reply({"data": [], "nextCursor": None})

    _, sdk = client(handler)
    sdk.accounts.list()
    assert len(calls) == 2


def test_a_rate_limit_after_the_retries_is_a_rate_limit_error():
    calls = []

    def handler(request):
        calls.append(request)
        return reply(envelope("rate_limited"), 429, {"Retry-After": "0"})

    _, sdk = client(handler)
    with pytest.raises(RateLimitError) as caught:
        sdk.accounts.list()
    assert caught.value.retry_after == 0
    assert len(calls) == 3, "the first attempt and two retries"


def test_a_post_keeps_the_same_idempotency_key_across_retries():
    keys = []

    def handler(request):
        keys.append(request.headers.get(IDEMPOTENCY_KEY_HEADER))
        return reply(envelope("idempotency_unavailable"), 503) if len(keys) < 3 else reply({}, 201)

    _, sdk = client(handler)
    response = sdk.http.post("/api/public/v1/anything", json={"a": 1})
    assert response.status_code == 201
    assert len(keys) == 3
    assert keys[0] and all(k == keys[0] for k in keys), keys


def test_a_500_of_a_post_is_not_retried():
    calls = []

    def handler(request):
        calls.append(request)
        return reply(envelope("internal_error"), 500)

    _, sdk = client(handler)
    assert sdk.http.post("/x", json={}).status_code == 500
    assert len(calls) == 1


def test_a_5xx_through_a_route_is_a_server_error():
    _, sdk = client(lambda r: reply(envelope("internal_error"), 500))
    with pytest.raises(ServerError):
        sdk.me.get()


def test_iter_reads_every_page_with_the_same_filters():
    seen = []

    def handler(request):
        cursor = request.url.params.get("cursor")
        seen.append((cursor, request.url.params.get("sold")))
        return reply({"data": [item(1)], "nextCursor": "c2"} if cursor is None else {"data": [item(2)], "nextCursor": None})

    _, sdk = client(handler)
    assert [i.id for i in sdk.items.iter(sold=False)] == [1, 2]
    assert seen == [(None, "false"), ("c2", "false")]


def test_an_amount_keeps_its_decimal_string_and_an_unknown_value_is_tolerated():
    _, sdk = client(lambda r: reply(item(7, "A_NEW_VALUE")))
    found = sdk.items.get(7)
    assert found.estimated_price.amount == "12.50"
    assert found.sex == "A_NEW_VALUE"
    assert found.purchase_price is None


def test_only_the_409_idempotency_in_progress_is_retried():
    calls = []

    def other(request):
        calls.append(request)
        return reply(envelope("idempotency_key_reused"), 409)

    _, sdk = client(other)
    with pytest.raises(ConflictError):
        sdk.me.get()
    assert len(calls) == 1, "another 409 is not retried"

    calls.clear()

    def in_progress(request):
        calls.append(request)
        return reply(envelope("idempotency_in_progress"), 409) if len(calls) == 1 else reply({"id": 1, "username": "u", "currency": "EUR"})

    _, sdk = client(in_progress)
    sdk.me.get()
    assert len(calls) == 2


def test_the_key_is_read_from_the_environment(monkeypatch):
    monkeypatch.setenv("CONTROLRESELL_API_KEY", "cr_test_env")
    requests = []
    sdk = ControlResell(
        base_url="https://api.test",
        transport=httpx.MockTransport(lambda r: requests.append(r) or reply({"id": 1, "username": "u", "currency": "EUR"})),
    )
    sdk.me.get()
    assert requests[0].headers["Authorization"] == "Bearer cr_test_env"
    monkeypatch.delenv("CONTROLRESELL_API_KEY")
    with pytest.raises(ValueError):
        ControlResell()
