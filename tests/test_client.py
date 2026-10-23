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


CUSTOMER = {
    "id": "11111111-1111-1111-1111-111111111111",
    "firstName": "Ann",
    "lastName": "Doe",
    "email": None,
    "address": {"country": "FR"},
    "createdAt": "2026-10-21T10:00:00Z",
}


def reply(body, status=200, headers=None):
    return httpx.Response(status, json=body, headers=headers or {})


def envelope(code):
    return {"error": {"code": code, "message": "m", "params": {}, "requestId": "req-1"}}


def item(id, sex="WOMEN"):
    return {
        "id": id, "name": "n", "sku": None, "description": None, "photos": [], "categoryId": None, "brandId": None,
        "sizeId": None, "colorIds": [], "state": None, "sex": sex, "labels": [], "sold": False,
        "materialIds": [], "enumValues": [], "attributes": [], "customFields": [],
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


ACTION = {"itemId": 7, "action": "PUBLISH", "accountIds": [], "scheduledAt": "2026-10-21T10:00:00Z"}
ACCOUNT = "3f0c2a52-0b0c-4d65-9f40-2d2d3b1f4a10"


def test_publish_posts_the_accounts_with_an_idempotency_key():
    from controlresell.generated.models import PublishRequest

    requests, sdk = client(lambda r: reply(ACTION, 202))
    action = sdk.items.publish(7, PublishRequest(account_ids=[ACCOUNT]))
    assert action.item_id == 7
    assert requests[0].method == "POST"
    assert requests[0].url.path == "/api/public/v1/items/7/publish"
    assert json.loads(requests[0].content) == {"accountIds": [ACCOUNT]}
    assert requests[0].headers[IDEMPOTENCY_KEY_HEADER]


def test_a_write_uses_the_idempotency_key_it_is_given():
    requests, sdk = client(lambda r: reply(ACTION, 202))
    sdk.items.republish(7, idempotency_key="my-key")
    assert requests[0].url.path == "/api/public/v1/items/7/republish"
    assert requests[0].headers[IDEMPOTENCY_KEY_HEADER] == "my-key"


def test_price_drop_posts_to_the_price_drop_route():
    from controlresell.generated.models import PriceDropRequest

    requests, sdk = client(lambda r: reply(ACTION, 202))
    sdk.items.price_drop(7, PriceDropRequest(type_="PERCENT", value="10"))
    assert requests[0].url.path == "/api/public/v1/items/7/price-drop"
    assert json.loads(requests[0].content) == {"type": "PERCENT", "value": "10"}


def test_delete_resolves_on_204_and_raises_a_typed_error_on_409():
    requests, sdk = client(lambda r: httpx.Response(204))
    assert sdk.items.delete(7) is None
    assert requests[0].method == "DELETE"
    _, refused = client(lambda r: reply(envelope("item_still_listed"), 409))
    with pytest.raises(ConflictError) as caught:
        refused.items.delete(7)
    assert caught.value.code == "item_still_listed"


def test_send_message_and_send_offer_post_to_the_conversation():
    from controlresell.generated.models import Money, SendMessageRequest, SendOfferRequest

    message = {
        "id": ACCOUNT, "conversationId": ACCOUNT, "author": "SELLER", "type": "TEXT", "status": "SENT",
        "body": "hi", "createdAt": "2026-10-21T10:00:00Z",
    }
    requests, sdk = client(lambda r: reply(message, 201))
    sdk.conversations.send_message(ACCOUNT, SendMessageRequest(text="hi"))
    sdk.conversations.send_offer(ACCOUNT, SendOfferRequest(price=Money(amount="12.50", currency="EUR")))
    assert [r.url.path for r in requests] == [
        f"/api/public/v1/conversations/{ACCOUNT}/messages",
        f"/api/public/v1/conversations/{ACCOUNT}/offers",
    ]
    assert json.loads(requests[1].content) == {"price": {"amount": "12.50", "currency": "EUR"}}


def test_a_write_keeps_the_same_idempotency_key_across_its_retries():
    from controlresell.generated.models import SendMessageRequest

    calls = []

    def handler(request):
        calls.append(request.headers[IDEMPOTENCY_KEY_HEADER])
        if len(calls) < 2:
            return reply(envelope("idempotency_unavailable"), 503)
        return reply(
            {
                "id": ACCOUNT, "conversationId": ACCOUNT, "author": "SELLER", "type": "TEXT", "status": "SENT",
                "createdAt": "2026-10-21T10:00:00Z",
            },
            201,
        )

    _, sdk = client(handler)
    sdk.conversations.send_message(ACCOUNT, SendMessageRequest(text="hi"))
    assert len(calls) == 2 and calls[0] and calls[0] == calls[1]


def test_create_posts_the_item_with_a_key_and_update_patches_it_without_one():
    from controlresell.generated.models import ItemCreateRequest, ItemUpdateRequest

    requests, sdk = client(lambda r: reply(item(7), 201 if r.method == "POST" else 200))
    created = sdk.items.create(ItemCreateRequest(name="n"), idempotency_key="k1")
    updated = sdk.items.update(7, ItemUpdateRequest(name="m"))
    assert created.id == 7 and updated.id == 7
    assert requests[0].method == "POST" and requests[0].url.path == "/api/public/v1/items"
    assert requests[0].headers[IDEMPOTENCY_KEY_HEADER] == "k1"
    assert json.loads(requests[0].content) == {"name": "n"}
    assert requests[1].method == "PATCH" and requests[1].url.path == "/api/public/v1/items/7"
    assert json.loads(requests[1].content) == {"name": "m"}
    assert IDEMPOTENCY_KEY_HEADER not in requests[1].headers


ORDER = {
    "id": ACCOUNT, "accountId": ACCOUNT, "type": "SALE", "status": "PAID", "platformOrderId": "p1",
    "price": {"amount": "12.50", "currency": "EUR"}, "prepared": False, "date": "2026-10-21T10:00:00Z", "items": [],
}


def test_orders_get_and_labels_read_the_order_and_its_labels():
    requests, sdk = client(lambda r: reply({"data": [], "nextCursor": None}) if r.url.path.endswith("/labels") else reply(ORDER))
    assert str(sdk.orders.get(ACCOUNT).id) == ACCOUNT
    assert sdk.orders.labels(ACCOUNT).data == []
    assert [r.url.path for r in requests] == [f"/api/public/v1/orders/{ACCOUNT}", f"/api/public/v1/orders/{ACCOUNT}/labels"]


def test_orders_iter_follows_the_cursor_with_the_same_filters():
    import datetime

    seen = []

    def handler(request):
        seen.append(request.url)
        if request.url.params.get("cursor"):
            return reply({"data": [{**ORDER, "platformOrderId": "b"}], "nextCursor": None})
        return reply({"data": [ORDER], "nextCursor": "c2"})

    _, sdk = client(handler)
    start = datetime.datetime(2026, 10, 1, tzinfo=datetime.timezone.utc)
    ids = [o.platform_order_id for o in sdk.orders.iter(bucket="to_send", platform="VINTED", from_=start, limit=1)]
    assert ids == ["p1", "b"]
    assert [u.params["bucket"] for u in seen] == ["to_send", "to_send"]
    assert seen[0].params["from"] == start.isoformat() and seen[1].params["cursor"] == "c2"


def test_orders_list_reads_a_naive_datetime_as_utc():
    import datetime

    requests, sdk = client(lambda r: reply({"data": [], "nextCursor": None}))
    sdk.orders.list(from_=datetime.datetime(2026, 10, 1), to=datetime.datetime(2026, 10, 2, tzinfo=datetime.timezone.utc))
    params = requests[0].url.params
    assert params["from"] == "2026-10-01T00:00:00+00:00" and params["to"] == "2026-10-02T00:00:00+00:00"


def test_orders_iter_labels_to_ship_follows_the_cursor_on_orders_labels():
    seen = []

    def handler(request):
        seen.append(request.url)
        if request.url.params.get("cursor"):
            return reply({"data": [{"id": ACCOUNT, "orderId": ACCOUNT}], "nextCursor": None})
        return reply({"data": [{"id": ACCOUNT, "orderId": ACCOUNT}], "nextCursor": "c2"})

    _, sdk = client(handler)
    labels = list(sdk.orders.iter_labels_to_ship(limit=1))
    assert len(labels) == 2 and str(labels[0].order_id) == ACCOUNT
    assert [u.path for u in seen] == ["/api/public/v1/orders/labels"] * 2
    assert seen[1].params["cursor"] == "c2"


def test_customers_iter_follows_the_cursor_with_the_same_filters():
    import datetime

    seen = []

    def handler(request):
        seen.append(request.url)
        if request.url.params.get("cursor"):
            return reply({"data": [{**CUSTOMER, "firstName": "Bob"}], "nextCursor": None})
        return reply({"data": [CUSTOMER], "nextCursor": "c2"})

    _, sdk = client(handler)
    start = datetime.datetime(2026, 10, 1, tzinfo=datetime.timezone.utc)
    names = [c.first_name for c in sdk.customers.iter(account_id=ACCOUNT, from_=start, limit=1)]
    assert names == ["Ann", "Bob"]
    assert [u.path for u in seen] == ["/api/public/v1/customers"] * 2
    assert [u.params["accountId"] for u in seen] == [ACCOUNT, ACCOUNT]
    assert seen[0].params["from"] == start.isoformat() and seen[1].params["cursor"] == "c2"


def test_customers_get_reads_one_customer():
    requests, sdk = client(lambda r: reply(CUSTOMER))
    assert sdk.customers.get(ACCOUNT).first_name == "Ann"
    assert requests[0].url.path == f"/api/public/v1/customers/{ACCOUNT}"


def test_conversations_messages_and_list_send_the_from_and_to_window():
    import datetime

    requests, sdk = client(lambda r: reply({"data": [], "nextCursor": None}))
    start = datetime.datetime(2026, 10, 1, tzinfo=datetime.timezone.utc)
    sdk.conversations.messages(ACCOUNT, from_=start, to=datetime.datetime(2026, 10, 2))
    sdk.conversations.list(from_=start)
    first, second = (r.url.params for r in requests)
    assert first["from"] == "2026-10-01T00:00:00+00:00" and first["to"] == "2026-10-02T00:00:00+00:00"
    assert second["from"] == "2026-10-01T00:00:00+00:00" and "to" not in second
