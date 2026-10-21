"""The client of the ControlResell public API."""

from __future__ import annotations

import os
import uuid
from collections.abc import Iterator
from types import ModuleType
from typing import Any
from uuid import UUID

import httpx

from . import __version__
from .errors import ControlResellConnectionError, error_of
from .generated.api.accounts import get_account, list_accounts
from .generated.api.conversations import (
    get_conversation,
    list_conversation_messages,
    list_conversations,
    send_message,
    send_offer,
)
from .generated.api.items import (
    delete_item,
    drop_item_price,
    get_item,
    list_item_listings,
    list_items,
    publish_item,
    republish_item,
)
from .generated.api.me import get_me
from .generated.client import AuthenticatedClient
from .generated.models import (
    Account,
    AccountPage,
    Conversation,
    ConversationPage,
    Item,
    ItemPage,
    ListingPage,
    Me,
    Message,
    MessagePage,
    PriceDropRequest,
    PublishRequest,
    RepublishRequest,
    ScheduledAction,
    SendMessageRequest,
    SendOfferRequest,
)
from .generated.types import UNSET
from .pagination import paginate
from .retry import RetryPolicy, RetryTransport

DEFAULT_BASE_URL = "https://api.controlresell.com"
"""The production address of the API."""

API_KEY_VARIABLE = "CONTROLRESELL_API_KEY"
"""The environment variable read when no API key is given."""


class ControlResell:
    """A client of the ControlResell public API, for one API key.

    >>> client = ControlResell(api_key="cr_live_...")  # or set CONTROLRESELL_API_KEY
    >>> me = client.me.get()
    >>> for item in client.items.iter(sold=False):
    ...     print(item.name)

    Calls are retried on a rate limit (after ``Retry-After``), on a gateway or availability error (502, 503, 504), on a
    409 ``idempotency_in_progress`` and on a network error; a ``POST`` always carries the same ``Idempotency-Key``
    across its retries. Any other error is raised as a ``ControlResellError``. The client holds no global state:
    create one per API key.
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        retry: RetryPolicy | None = None,
        timeout: float | None = 60.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        key = api_key or os.environ.get(API_KEY_VARIABLE)
        if not key:
            raise ValueError(f"No API key: pass api_key or set {API_KEY_VARIABLE}.")
        self._client = AuthenticatedClient(
            base_url=base_url,
            token=key,
            timeout=httpx.Timeout(timeout) if timeout is not None else None,
            headers={"User-Agent": f"controlresell-python/{__version__}"},
            httpx_args={"transport": RetryTransport(transport or httpx.HTTPTransport(), retry)},
        )
        self.me = _Me(self)
        self.accounts = _Accounts(self)
        self.items = _Items(self)
        self.conversations = _Conversations(self)

    @property
    def http(self) -> httpx.Client:
        """The underlying ``httpx.Client`` (retries and key included), for a route the SDK does not wrap yet."""
        return self._client.get_httpx_client()

    def close(self) -> None:
        self._client.get_httpx_client().close()

    def __enter__(self) -> ControlResell:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def _call(self, route: ModuleType, **arguments: Any) -> Any:
        """Calls a generated route; a 4xx or 5xx is raised as a ``ControlResellError``."""
        request = route._get_kwargs(**arguments)  # noqa: SLF001
        try:
            response = self.http.request(**request)
        except httpx.TransportError as cause:
            raise ControlResellConnectionError(cause) from cause
        if response.status_code >= 400:
            try:
                body = response.json()
            except ValueError:
                body = None
            raise error_of(response.status_code, body, response.headers)
        return route._parse_response(client=self._client, response=response)  # noqa: SLF001


def _query(**values: Any) -> dict[str, Any]:
    return {key: UNSET if value is None else value for key, value in values.items()}


def _key(idempotency_key: str | None) -> str:
    return idempotency_key or str(uuid.uuid4())


class _Me:
    def __init__(self, sdk: ControlResell) -> None:
        self._sdk = sdk

    def get(self) -> Me:
        """The seller the API key acts for."""
        return self._sdk._call(get_me)  # noqa: SLF001


class _Accounts:
    def __init__(self, sdk: ControlResell) -> None:
        self._sdk = sdk

    def list(self, *, limit: int | None = None, cursor: str | None = None) -> AccountPage:
        """One page of the seller's marketplace accounts."""
        return self._sdk._call(list_accounts, **_query(limit=limit, cursor=cursor))  # noqa: SLF001

    def get(self, id: UUID | str) -> Account:
        return self._sdk._call(get_account, id=UUID(str(id)))  # noqa: SLF001

    def iter(self, *, limit: int | None = None) -> Iterator[Account]:
        """Every account, page after page."""
        return paginate(lambda cursor: self.list(limit=limit, cursor=cursor))


class _Items:
    def __init__(self, sdk: ControlResell) -> None:
        self._sdk = sdk

    def list(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        sold: bool | None = None,
        account_id: UUID | str | None = None,
    ) -> ItemPage:
        """One page of the items of the seller's stock."""
        account = UUID(str(account_id)) if account_id is not None else None
        return self._sdk._call(  # noqa: SLF001
            list_items, **_query(limit=limit, cursor=cursor, sold=sold, account_id=account)
        )

    def get(self, id: int) -> Item:
        return self._sdk._call(get_item, id=id)  # noqa: SLF001

    def listings(self, id: int) -> ListingPage:
        """The item's listings on the seller's marketplace accounts."""
        return self._sdk._call(list_item_listings, id=id)  # noqa: SLF001

    def delete(self, id: int) -> None:
        """Deletes an item of the stock; an item still online is refused (409 ``item_still_listed``)."""
        self._sdk._call(delete_item, id=id)  # noqa: SLF001

    def publish(self, id: int, body: PublishRequest, *, idempotency_key: str | None = None) -> ScheduledAction:
        """Schedules the publication of an item on the given accounts (needs ``items:write``)."""
        return self._sdk._call(publish_item, id=id, body=body, idempotency_key=_key(idempotency_key))  # noqa: SLF001

    def price_drop(self, id: int, body: PriceDropRequest, *, idempotency_key: str | None = None) -> ScheduledAction:
        """Schedules a price drop of the item's listings."""
        return self._sdk._call(drop_item_price, id=id, body=body, idempotency_key=_key(idempotency_key))  # noqa: SLF001

    def republish(
        self, id: int, body: RepublishRequest | None = None, *, idempotency_key: str | None = None
    ) -> ScheduledAction:
        """Schedules the republication of an item."""
        return self._sdk._call(  # noqa: SLF001
            republish_item, id=id, body=body or RepublishRequest(), idempotency_key=_key(idempotency_key)
        )

    def iter(
        self, *, limit: int | None = None, sold: bool | None = None, account_id: UUID | str | None = None
    ) -> Iterator[Item]:
        """Every item, page after page, with the same filters."""
        return paginate(lambda cursor: self.list(limit=limit, cursor=cursor, sold=sold, account_id=account_id))


class _Conversations:
    def __init__(self, sdk: ControlResell) -> None:
        self._sdk = sdk

    def list(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        unread: bool | None = None,
        account_id: UUID | str | None = None,
    ) -> ConversationPage:
        """One page of the conversations with buyers."""
        account = UUID(str(account_id)) if account_id is not None else None
        return self._sdk._call(  # noqa: SLF001
            list_conversations, **_query(limit=limit, cursor=cursor, unread=unread, account_id=account)
        )

    def get(self, id: UUID | str) -> Conversation:
        return self._sdk._call(get_conversation, id=UUID(str(id)))  # noqa: SLF001

    def messages(self, id: UUID | str, *, limit: int | None = None, cursor: str | None = None) -> MessagePage:
        """One page of the messages of a conversation, oldest first."""
        return self._sdk._call(  # noqa: SLF001
            list_conversation_messages, id=UUID(str(id)), **_query(limit=limit, cursor=cursor)
        )

    def send_message(self, id: UUID | str, body: SendMessageRequest, *, idempotency_key: str | None = None) -> Message:
        """Sends a message to the buyer (needs ``conversations:write``)."""
        return self._sdk._call(  # noqa: SLF001
            send_message, id=UUID(str(id)), body=body, idempotency_key=_key(idempotency_key)
        )

    def send_offer(self, id: UUID | str, body: SendOfferRequest, *, idempotency_key: str | None = None) -> Message:
        """Sends the buyer an offer."""
        return self._sdk._call(  # noqa: SLF001
            send_offer, id=UUID(str(id)), body=body, idempotency_key=_key(idempotency_key)
        )

    def iter(
        self, *, limit: int | None = None, unread: bool | None = None, account_id: UUID | str | None = None
    ) -> Iterator[Conversation]:
        """Every conversation, page after page, with the same filters."""
        return paginate(lambda cursor: self.list(limit=limit, cursor=cursor, unread=unread, account_id=account_id))

    def iter_messages(self, id: UUID | str, *, limit: int | None = None) -> Iterator[Any]:
        """Every message of a conversation, page after page."""
        return paginate(lambda cursor: self.messages(id, limit=limit, cursor=cursor))
