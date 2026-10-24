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


FAVORITE = {
    "id": "11111111-1111-1111-1111-111111111111",
    "accountId": "11111111-1111-1111-1111-111111111111",
    "platform": "VINTED",
    "buyerId": "b1",
    "createdAt": "2026-10-24T00:00:00Z",
    "messageSentAt": None,
    "listingId": "L1",
    "item": {"id": 42, "name": "Jacket", "price": {"amount": "12.50", "currency": "EUR"}, "sold": False},
}


def test_favorites_iter_follows_the_cursor_with_the_same_filters():
    import datetime

    seen = []

    def handler(request):
        seen.append(request.url)
        if request.url.params.get("cursor"):
            return reply({"data": [{**FAVORITE, "buyerId": "b2", "item": None}], "nextCursor": None})
        return reply({"data": [FAVORITE], "nextCursor": "c2"})

    _, sdk = client(handler)
    start = datetime.datetime(2026, 10, 1, tzinfo=datetime.timezone.utc)
    favorites = list(sdk.favorites.iter(account_id=ACCOUNT, item_id=42, from_=start, limit=1))
    assert [f.buyer_id for f in favorites] == ["b1", "b2"]
    assert favorites[0].item.name == "Jacket" and favorites[1].item is None
    assert [u.path for u in seen] == ["/api/public/v1/favorites"] * 2
    assert [u.params["itemId"] for u in seen] == ["42", "42"] and [u.params["accountId"] for u in seen] == [ACCOUNT] * 2
    assert seen[0].params["from"] == start.isoformat() and seen[1].params["cursor"] == "c2"


def test_favorites_iter_item_reads_the_favorites_of_one_item():
    requests, sdk = client(lambda r: reply({"data": [FAVORITE], "nextCursor": None}))
    assert [f.buyer_id for f in sdk.favorites.iter_item(42)] == ["b1"]
    assert requests[0].url.path == "/api/public/v1/items/42/favorites"


def test_conversations_list_sends_the_buyer_item_and_offer_status_filters():
    requests, sdk = client(lambda r: reply({"data": [], "nextCursor": None}))
    sdk.conversations.list(buyer_id="b-1", item_id=42, offer_status="PENDING")
    params = requests[0].url.params
    assert params["buyerId"] == "b-1" and params["itemId"] == "42" and params["offerStatus"] == "PENDING"


def test_catalogs_iter_brands_follows_the_cursor_with_the_same_query():
    seen = []

    def handler(request):
        seen.append(request.url)
        if request.url.params.get("cursor"):
            return reply({"data": [{"id": 2, "name": "Nikon", "custom": True}], "nextCursor": None})
        return reply({"data": [{"id": 1, "name": "Nike", "custom": False}], "nextCursor": "c2"})

    _, sdk = client(handler)
    assert [b.name for b in sdk.catalogs.iter_brands(q="nik")] == ["Nike", "Nikon"]
    assert [u.path for u in seen] == ["/api/public/v1/catalogs/brands"] * 2
    assert [u.params["q"] for u in seen] == ["nik", "nik"] and seen[1].params["cursor"] == "c2"


def test_catalogs_colors_send_the_category_and_read_the_values():
    requests, sdk = client(lambda r: reply({"data": [{"id": 3, "key": "red", "title": "Red"}], "nextCursor": None}))
    assert sdk.catalogs.colors(category_id=12).data[0].title == "Red"
    assert requests[0].url.path == "/api/public/v1/catalogs/colors" and requests[0].url.params["categoryId"] == "12"


def test_catalogs_category_fields_reads_the_fields_of_one_category():
    body = {"categoryId": 12, "sizeGroupIds": [1], "enumFields": [], "textFields": [], "measurements": []}
    requests, sdk = client(lambda r: reply(body))
    assert sdk.catalogs.category_fields(12).category_id == 12
    assert requests[0].url.path == "/api/public/v1/catalogs/categories/12/fields"


def test_conversations_messages_and_list_send_the_from_and_to_window():
    import datetime

    requests, sdk = client(lambda r: reply({"data": [], "nextCursor": None}))
    start = datetime.datetime(2026, 10, 1, tzinfo=datetime.timezone.utc)
    sdk.conversations.messages(ACCOUNT, from_=start, to=datetime.datetime(2026, 10, 2))
    sdk.conversations.list(from_=start)
    first, second = (r.url.params for r in requests)
    assert first["from"] == "2026-10-01T00:00:00+00:00" and first["to"] == "2026-10-02T00:00:00+00:00"
    assert second["from"] == "2026-10-01T00:00:00+00:00" and "to" not in second


ENDPOINT_ID = "0b6f3c1e-8d43-4a4c-9a55-7f1f2c3d4e5f"
ENDPOINT = {
    "id": ENDPOINT_ID, "url": "https://example.com/hook", "description": None, "eventTypes": ["item.sold"],
    "payloadMode": "light", "status": "enabled", "apiVersion": "v1", "createdAt": "2026-10-24T00:00:00Z",
    "updatedAt": "2026-10-24T00:00:00Z",
}


def test_webhooks_create_endpoint_posts_with_a_key_and_returns_the_secret():
    from controlresell.generated.models import WebhookEndpointCreateRequest

    requests, sdk = client(lambda r: reply({"endpoint": ENDPOINT, "secret": "whsec_abc"}, 201))
    created = sdk.webhooks.create_endpoint(WebhookEndpointCreateRequest(url="https://example.com/hook", event_types=["item.sold"]))
    assert created.secret == "whsec_abc" and created.endpoint.status == "enabled"
    request = requests[0]
    assert request.method == "POST" and request.url.path == "/api/public/v1/webhook-endpoints"
    assert request.headers[IDEMPOTENCY_KEY_HEADER] and json.loads(request.content)["eventTypes"] == ["item.sold"]


def test_webhooks_update_endpoint_sends_an_explicit_null_to_clear_the_description():
    from controlresell.generated.models import WebhookEndpointUpdateRequest

    requests, sdk = client(lambda r: reply(ENDPOINT))
    sdk.webhooks.update_endpoint(ENDPOINT_ID, WebhookEndpointUpdateRequest(description=None))
    assert requests[0].method == "PATCH" and json.loads(requests[0].content) == {"description": None}


def test_webhooks_iter_events_follows_the_cursor_with_the_same_types_and_reads_any_data():
    def handler(request):
        if "cursor" not in request.url.params:
            return reply({"data": [{"id": "0192f3c1-0000-7000-8000-000000000001", "type": "item.sold",
                                    "createdAt": "2026-10-24T00:00:00Z", "apiVersion": "v1", "sellerId": 7,
                                    "data": {"itemId": 42, "source": "order", "object": None}}], "nextCursor": "c2"})
        return reply({"data": [{"id": "0192f3c1-0000-7000-8000-000000000002", "type": "order.created",
                                "createdAt": "2026-10-24T00:01:00Z", "apiVersion": "v1", "sellerId": 7,
                                "data": {"orderId": "o1", "items": [1, 2]}}], "nextCursor": None})

    requests, sdk = client(handler)
    events = list(sdk.webhooks.iter_events(types=["item.sold", "order.created"]))
    assert [e.type_ for e in events] == ["item.sold", "order.created"]
    assert events[0].data["itemId"] == 42 and events[1].data["items"] == [1, 2]
    assert [r.url.params["type"] for r in requests] == ["item.sold,order.created"] * 2
    assert requests[1].url.params["cursor"] == "c2"


def test_webhooks_deliveries_send_the_filters_and_retry_posts_to_the_delivery():
    delivery = {"id": "11111111-2222-3333-4444-555555555555", "eventId": "11111111-2222-3333-4444-666666666666",
                "eventType": "item.sold", "status": "failed", "attempt": 3, "createdAt": "2026-10-24T00:00:00Z",
                "updatedAt": "2026-10-24T00:00:00Z"}

    def handler(request):
        if request.method == "GET":
            return reply({"data": [delivery], "nextCursor": None})
        return reply(delivery, 202)

    requests, sdk = client(handler)
    assert sdk.webhooks.deliveries(ENDPOINT_ID, status="failed").data[0].attempt == 3
    sdk.webhooks.retry_delivery(ENDPOINT_ID, delivery["id"])
    assert requests[0].url.path == f"/api/public/v1/webhook-endpoints/{ENDPOINT_ID}/deliveries"
    assert requests[0].url.params["status"] == "failed"
    assert requests[1].url.path == f"/api/public/v1/webhook-endpoints/{ENDPOINT_ID}/deliveries/{delivery['id']}/retry"


def test_webhooks_rotate_secret_sends_the_overlap_and_delete_resolves_on_204():
    def handler(request):
        if request.method == "DELETE":
            return httpx.Response(204)
        return reply({"secret": "whsec_new", "previousSecretExpiresAt": "2026-10-25T00:00:00Z"})

    requests, sdk = client(handler)
    assert sdk.webhooks.rotate_secret(ENDPOINT_ID, expires_in_hours=0).secret == "whsec_new"
    assert json.loads(requests[0].content) == {"expiresInHours": 0}
    assert sdk.webhooks.delete_endpoint(ENDPOINT_ID) is None
