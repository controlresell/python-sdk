# ControlResell Python SDK

Python client for the [ControlResell](https://controlresell.com) public API (Python 3.11+).

```python
from controlresell import ControlResell

client = ControlResell(api_key="cr_live_...")  # or set CONTROLRESELL_API_KEY
me = client.me.get()
for item in client.items.iter(sold=False):
    print(item.name)
```

Retries (rate limits, 502/503/504, network errors), `Idempotency-Key` on every `POST`, cursor pagination with plain iterators and typed errors (`NotFoundError`, `RateLimitError`...) are built in. The client is generated from the API's OpenAPI document (`scripts/generate.sh`, code in `src/controlresell/generated`).

```sh
pip install -e ".[test]"
pytest
```

Not published yet. Licensed under the Apache License 2.0.
