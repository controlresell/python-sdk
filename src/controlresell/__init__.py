"""Python client for the ControlResell public API."""

__version__ = "1.0.0"

from .client import API_KEY_VARIABLE, DEFAULT_BASE_URL, ControlResell
from .errors import (
    AuthenticationError,
    BadRequestError,
    ConflictError,
    ControlResellConnectionError,
    ControlResellError,
    NotFoundError,
    PaymentRequiredError,
    PermissionDeniedError,
    RateLimitError,
    ServerError,
    UnprocessableEntityError,
)
from .pagination import paginate
from .retry import IDEMPOTENCY_KEY_HEADER, RetryPolicy

__all__ = [
    "API_KEY_VARIABLE",
    "DEFAULT_BASE_URL",
    "IDEMPOTENCY_KEY_HEADER",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "ControlResell",
    "ControlResellConnectionError",
    "ControlResellError",
    "NotFoundError",
    "PaymentRequiredError",
    "PermissionDeniedError",
    "RateLimitError",
    "RetryPolicy",
    "ServerError",
    "UnprocessableEntityError",
    "__version__",
    "paginate",
]
