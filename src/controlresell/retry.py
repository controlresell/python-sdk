"""Retries and idempotency keys, as an httpx transport."""

from __future__ import annotations

import random
import re
import time
import uuid
from dataclasses import dataclass

import httpx

from .errors import ControlResellConnectionError

IDEMPOTENCY_KEY_HEADER = "Idempotency-Key"
"""The header that makes a ``POST`` safe to retry: the API replays the first answer to the same key."""

IDEMPOTENCY_IN_PROGRESS = "idempotency_in_progress"
"""The code of the 409 answered while the first request with the same key is still running."""

# A rate limit, a gateway or availability error. A 500 is never retried; a 409 only for a key still in flight.
_RETRIED_STATUSES = frozenset({429, 502, 503, 504})


@dataclass(frozen=True)
class RetryPolicy:
    """How a call is retried."""

    max_retries: int = 2
    """Retries after the first attempt; 0 turns them off."""
    base_delay: float = 0.5
    """The first delay in seconds, doubled at each retry, with a random part; a ``Retry-After`` takes precedence."""
    max_delay: float = 30.0
    """The longest delay between two attempts."""

    def backoff(self, attempt: int) -> float:
        return min(self.base_delay * 2**attempt + random.random() * self.base_delay / 2, self.max_delay)


def _delay(policy: RetryPolicy, response: httpx.Response | None, attempt: int) -> float:
    if response is not None:
        try:
            return min(float(response.headers["Retry-After"]), policy.max_delay)
        except (KeyError, ValueError):
            pass
    return policy.backoff(attempt)


def _in_progress(response: httpx.Response) -> bool:
    if response.status_code != 409:
        return False
    try:
        body = response.json()
        return body["error"]["code"] == IDEMPOTENCY_IN_PROGRESS
    except (ValueError, KeyError, TypeError):
        return False


def _should_retry(response: httpx.Response) -> bool:
    return response.status_code in _RETRIED_STATUSES or _in_progress(response)


_WEBHOOK_TEST_PATH = re.compile(r"/webhook-endpoints/[^/]+/test/?$")


def _is_webhook_test(request: httpx.Request) -> bool:
    """``POST /webhook-endpoints/{id}/test`` sends a real event and the API ignores its key: a replay would send a
    second event. It is retried on a 429 (answered before the event leaves) and on a failed connect, nothing else."""
    return request.method == "POST" and _WEBHOOK_TEST_PATH.search(request.url.path) is not None


def _with_key(request: httpx.Request) -> None:
    if request.method == "POST" and IDEMPOTENCY_KEY_HEADER not in request.headers:
        request.headers[IDEMPOTENCY_KEY_HEADER] = str(uuid.uuid4())


class RetryTransport(httpx.BaseTransport):
    """Gives each ``POST`` an ``Idempotency-Key`` (kept across its retries), retries the statuses above and network
    errors, and waits for ``Retry-After`` when the API sends it. The webhook test call is retried on a 429 and on a
    failed connect only."""

    def __init__(self, base: httpx.BaseTransport, policy: RetryPolicy | None = None) -> None:
        self._base = base
        self._policy = policy or RetryPolicy()

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        _with_key(request)
        replayable = not _is_webhook_test(request)
        attempt = 0
        while True:
            last = attempt >= self._policy.max_retries
            try:
                response = self._base.handle_request(request)
            except httpx.TransportError as cause:
                if last or (not replayable and not isinstance(cause, (httpx.ConnectError, httpx.ConnectTimeout))):
                    raise ControlResellConnectionError(cause) from cause
                time.sleep(self._policy.backoff(attempt))
                attempt += 1
                continue
            if last:
                return response
            response.read()
            if (not replayable and response.status_code != 429) or not _should_retry(response):
                return response
            time.sleep(_delay(self._policy, response, attempt))
            response.close()
            attempt += 1

    def close(self) -> None:
        self._base.close()
