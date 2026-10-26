# ControlResell Python SDK

Python client for the [ControlResell](https://controlresell.com) public API (Python 3.11+).

## Install

From the 0.1.0 release, on [PyPI](https://pypi.org/project/controlresell/):

```sh
pip install controlresell
```


```python
from controlresell import ControlResell

client = ControlResell(api_key="cr_live_...")  # or set CONTROLRESELL_API_KEY
me = client.me.get()
for item in client.items.iter(sold=False):
    print(item.name)
for order in client.orders.iter(bucket="to_send"):  # needs the orders:read scope; also orders.get(id), orders.labels(id)
    print(order.id)
for brand in client.catalogs.iter_brands(q="nik"):  # the identifiers an item is written with (items:read): categories, category, category_fields, brands, sizes, colors, conditions, package_sizes, materials
    print(brand.id, brand.name)

for favorite in client.favorites.iter(item_id=42):  # the buyers who favorited a listing (items:read); also favorites.iter_item(42), list, list_item
    print(favorite.buyer_id)
client.conversations.list(buyer_id="<buyer id>", offer_status="PENDING")  # buyer_id, item_id and offer_status filter the conversations

# Writes (API key with `items:write` / `conversations:write`); `idempotency_key=` chooses the key.
from controlresell.generated.models import ItemCreateRequest, ItemUpdateRequest, PublishRequest, SendMessageRequest

client.items.create(ItemCreateRequest(name="Jacket"))  # client.items.update(42, ItemUpdateRequest(...)) patches

client.items.publish(42, PublishRequest(account_ids=["<account id>"]))
client.conversations.send_message("<conversation id>", SendMessageRequest(text="Hello!"))

# Webhooks (`webhooks:read` / `webhooks:write`): endpoints, endpoint, create_endpoint, update_endpoint, delete_endpoint,
# secret, rotate_secret, test, deliveries, retry_delivery, recover, event_types; iter_events catches up the last 7 days.
from controlresell.generated.models import WebhookEndpointCreateRequest

created = client.webhooks.create_endpoint(WebhookEndpointCreateRequest(url="https://example.com/hooks", event_types=["item.sold"]))
print(created.endpoint.id, created.secret)  # the signing secret, shown once (client.webhooks.secret(id) reads it again)
for event in client.webhooks.iter_events(types=["item.sold"]):
    print(event.type_, event.data["itemId"])
```

Retries (rate limits, 502/503/504, network errors), `Idempotency-Key` on every `POST`, cursor pagination with plain iterators and typed errors (`NotFoundError`, `RateLimitError`...) are built in. The client is generated from the API's OpenAPI document (`scripts/generate.sh`, code in `src/controlresell/generated`).

```sh
pip install -e ".[test]"
pytest
```

Licensed under the Apache License 2.0.
