"""Typed errors of the ControlResell API."""

from __future__ import annotations

from typing import Any


class ControlResellError(Exception):
    """An error answered by the API, read from its envelope ``{"error": {code, message, params, requestId}}``.

    ``code`` is an open string (``item_not_found``, ``rate_limited``...): match the codes you handle and treat any
    other one by its ``status``.
    """

    def __init__(
        self,
        message: str,
        status: int,
        code: str,
        params: dict[str, str] | None = None,
        request_id: str | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
        self.code = code
        self.params = params or {}
        self.request_id = request_id


class BadRequestError(ControlResellError):
    """400: the request is malformed."""


class AuthenticationError(ControlResellError):
    """401: no credential, or an unknown, revoked or expired one."""


class PaymentRequiredError(ControlResellError):
    """402: the seller's plan does not include this."""


class PermissionDeniedError(ControlResellError):
    """403: the API key does not grant the scope the route requires."""


class NotFoundError(ControlResellError):
    """404: no such resource for this seller."""


class ConflictError(ControlResellError):
    """409: an ``Idempotency-Key`` used with another request, or still in flight."""


class UnprocessableEntityError(ControlResellError):
    """422: the request is well formed but refused."""


class RateLimitError(ControlResellError):
    """429: the rate limit of the API key is reached. ``retry_after`` is the ``Retry-After`` in seconds, when sent."""

    retry_after: float | None = None


class ServerError(ControlResellError):
    """5xx: an error of the API; retry later."""


class ControlResellConnectionError(Exception):
    """The API could not be reached (network, DNS, TLS), after the retries."""

    def __init__(self, cause: BaseException) -> None:
        super().__init__(f"Could not reach the ControlResell API: {cause}")
        self.__cause__ = cause


_BY_STATUS: dict[int, type[ControlResellError]] = {
    400: BadRequestError,
    401: AuthenticationError,
    402: PaymentRequiredError,
    403: PermissionDeniedError,
    404: NotFoundError,
    409: ConflictError,
    422: UnprocessableEntityError,
    429: RateLimitError,
}


def error_of(status: int, body: Any, headers: Any) -> ControlResellError:
    """The typed error of a response of ``status`` whose JSON body is ``body`` (the API's envelope, or anything)."""
    envelope = body.get("error") if isinstance(body, dict) else None
    if not isinstance(envelope, dict):
        envelope = {}
    code = envelope.get("code") if isinstance(envelope.get("code"), str) else f"http_{status}"
    message = envelope.get("message") if isinstance(envelope.get("message"), str) else f"HTTP {status}"
    params = envelope.get("params") if isinstance(envelope.get("params"), dict) else {}
    request_id = envelope.get("requestId") if isinstance(envelope.get("requestId"), str) else None
    cls = _BY_STATUS.get(status) or (ServerError if status >= 500 else ControlResellError)
    error = cls(message, status, code, params, request_id)
    if isinstance(error, RateLimitError):
        try:
            error.retry_after = float(headers.get("Retry-After"))
        except (TypeError, ValueError):
            error.retry_after = None
    return error
