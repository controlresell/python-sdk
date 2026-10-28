"""The client of the ControlResell public API."""

from __future__ import annotations

import datetime
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
    create_item,
    delete_item,
    drop_item_price,
    get_item,
    list_item_listings,
    list_items,
    publish_item,
    republish_item,
    update_item,
)
from .generated.api.catalogs import (
    get_catalog_category,
    get_catalog_category_fields,
    list_catalog_brands,
    list_catalog_categories,
    list_catalog_colors,
    list_catalog_conditions,
    list_catalog_materials,
    list_catalog_package_sizes,
    list_catalog_sizes,
)
from .generated.api.customers import get_customer, list_customers
from .generated.api.files import get_file, upload_file
from .generated.api.favorites import list_favorites, list_item_favorites
from .generated.api.webhooks import (
    create_webhook_endpoint,
    delete_webhook_endpoint,
    get_webhook_endpoint,
    get_webhook_secret,
    list_webhook_deliveries,
    list_webhook_endpoints,
    list_webhook_event_types,
    list_webhook_events,
    recover_webhook_deliveries,
    retry_webhook_delivery,
    rotate_webhook_secret,
    test_webhook_endpoint,
    update_webhook_endpoint,
)
from .generated.api.me import get_me
from .generated.api.orders import get_order, list_labels_to_ship, list_order_labels, list_orders
from .generated.client import AuthenticatedClient
from .generated.models import (
    Account,
    AccountPage,
    CatalogBrand,
    CatalogBrandPage,
    CatalogCategory,
    CatalogCategoryFields,
    CatalogCategoryPage,
    CatalogSize,
    CatalogSizePage,
    CatalogValue,
    CatalogValuePage,
    Conversation,
    ConversationPage,
    CreatedWebhookEndpoint,
    Customer,
    CustomerPage,
    Favorite,
    File,
    FileUpload,
    FileUploadRequest,
    FavoritePage,
    Item,
    ItemCreateRequest,
    ItemPage,
    ItemUpdateRequest,
    ListingPage,
    Me,
    Message,
    MessagePage,
    Order,
    OrderLabel,
    OrderLabelPage,
    OrderPage,
    PriceDropRequest,
    PublishRequest,
    RepublishRequest,
    ScheduledAction,
    SendMessageRequest,
    SendOfferRequest,
    WebhookDelivery,
    WebhookDeliveryPage,
    WebhookEndpoint,
    WebhookEndpointCreateRequest,
    WebhookEndpointPage,
    WebhookEndpointUpdateRequest,
    WebhookEvent,
    WebhookEventPage,
    WebhookEventTypeList,
    WebhookRecoverRequest,
    WebhookRecovery,
    WebhookSecret,
    WebhookSecretRotateRequest,
    WebhookTestResult,
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
        # The bytes of a file go to the storage address, which is signed: no API key there.
        self._storage = httpx.Client(
            timeout=httpx.Timeout(timeout) if timeout is not None else None,
            headers={"User-Agent": f"controlresell-python/{__version__}"},
            transport=RetryTransport(transport or httpx.HTTPTransport(), retry),
        )
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
        self.orders = _Orders(self)
        self.customers = _Customers(self)
        self.files = _Files(self)
        self.favorites = _Favorites(self)
        self.catalogs = _Catalogs(self)
        self.webhooks = _Webhooks(self)

    @property
    def http(self) -> httpx.Client:
        """The underlying ``httpx.Client`` (retries and key included), for a route the SDK does not wrap yet."""
        return self._client.get_httpx_client()

    def close(self) -> None:
        self._client.get_httpx_client().close()
        self._storage.close()

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


def _utc(value: datetime.datetime | None) -> datetime.datetime | None:
    """A naive datetime is read as UTC, so that it goes out with an offset."""
    if value is not None and value.tzinfo is None:
        return value.replace(tzinfo=datetime.timezone.utc)
    return value


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

    def create(self, body: ItemCreateRequest, *, idempotency_key: str | None = None) -> Item:
        """Creates an item in the stock, without publishing it (needs ``items:write``)."""
        return self._sdk._call(create_item, body=body, idempotency_key=_key(idempotency_key))  # noqa: SLF001

    def update(self, id: int, body: ItemUpdateRequest) -> Item:
        """Updates the given fields of an item (a ``PATCH``: the fields left out are kept)."""
        return self._sdk._call(update_item, id=id, body=body)  # noqa: SLF001

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
        from_: datetime.datetime | None = None,
        to: datetime.datetime | None = None,
        buyer_id: str | None = None,
        item_id: int | None = None,
        offer_status: str | None = None,
    ) -> ConversationPage:
        """One page of the conversations with buyers.

        ``from_`` (inclusive) and ``to`` (exclusive) bound the last message (a naive datetime is read as UTC).
        ``buyer_id`` keeps the conversations with one buyer, ``item_id`` those about one item, ``offer_status``
        those with an offer at this status (``PENDING``, ``ACCEPTED``, ``REJECTED`` or ``CANCELED``).
        """
        account = UUID(str(account_id)) if account_id is not None else None
        return self._sdk._call(  # noqa: SLF001
            list_conversations,
            **_query(
                limit=limit,
                cursor=cursor,
                unread=unread,
                account_id=account,
                from_=_utc(from_),
                to=_utc(to),
                buyer_id=buyer_id,
                item_id=item_id,
                offer_status=offer_status,
            ),
        )

    def get(self, id: UUID | str) -> Conversation:
        return self._sdk._call(get_conversation, id=UUID(str(id)))  # noqa: SLF001

    def messages(
        self,
        id: UUID | str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        from_: datetime.datetime | None = None,
        to: datetime.datetime | None = None,
    ) -> MessagePage:
        """One page of the messages of a conversation, oldest first.

        ``from_`` (inclusive) and ``to`` (exclusive) bound the period (a naive datetime is read as UTC).
        """
        return self._sdk._call(  # noqa: SLF001
            list_conversation_messages,
            id=UUID(str(id)),
            **_query(limit=limit, cursor=cursor, from_=_utc(from_), to=_utc(to)),
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
        self,
        *,
        limit: int | None = None,
        unread: bool | None = None,
        account_id: UUID | str | None = None,
        from_: datetime.datetime | None = None,
        to: datetime.datetime | None = None,
    ) -> Iterator[Conversation]:
        """Every conversation, page after page, with the same filters."""
        return paginate(
            lambda cursor: self.list(
                limit=limit, cursor=cursor, unread=unread, account_id=account_id, from_=from_, to=to
            )
        )

    def iter_messages(
        self,
        id: UUID | str,
        *,
        limit: int | None = None,
        from_: datetime.datetime | None = None,
        to: datetime.datetime | None = None,
    ) -> Iterator[Any]:
        """Every message of a conversation, page after page, with the same period."""
        return paginate(lambda cursor: self.messages(id, limit=limit, cursor=cursor, from_=from_, to=to))


class _Orders:
    def __init__(self, sdk: ControlResell) -> None:
        self._sdk = sdk

    def list(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        bucket: str | None = None,
        platform: str | None = None,
        account_id: UUID | str | None = None,
        from_: datetime.datetime | None = None,
        to: datetime.datetime | None = None,
    ) -> OrderPage:
        """One page of the seller's orders, the most recent first.

        ``bucket`` is ``to_send`` or ``to_pickup``; ``from_`` is inclusive and ``to`` exclusive (a naive datetime is read as
        UTC).
        """
        account = UUID(str(account_id)) if account_id is not None else None
        return self._sdk._call(  # noqa: SLF001
            list_orders,
            **_query(
                limit=limit, cursor=cursor, bucket=bucket, platform=platform, account_id=account, from_=_utc(from_), to=_utc(to)
            ),
        )

    def get(self, id: UUID | str) -> Order:
        """One order by its identifier."""
        return self._sdk._call(get_order, id=UUID(str(id)))  # noqa: SLF001

    def labels(self, id: UUID | str) -> OrderLabelPage:
        """The shipping labels of an order."""
        return self._sdk._call(list_order_labels, id=UUID(str(id)))  # noqa: SLF001

    def labels_to_ship(self, *, limit: int | None = None, cursor: str | None = None) -> OrderLabelPage:
        """One page of the labels still to ship over all the orders, the oldest order first (each names its order)."""
        return self._sdk._call(list_labels_to_ship, **_query(limit=limit, cursor=cursor))  # noqa: SLF001

    def iter_labels_to_ship(self, *, limit: int | None = None) -> Iterator[OrderLabel]:
        """Every label still to ship, page after page."""
        return paginate(lambda cursor: self.labels_to_ship(limit=limit, cursor=cursor))

    def iter(
        self,
        *,
        limit: int | None = None,
        bucket: str | None = None,
        platform: str | None = None,
        account_id: UUID | str | None = None,
        from_: datetime.datetime | None = None,
        to: datetime.datetime | None = None,
    ) -> Iterator[Order]:
        """Every order, page after page, with the same filters."""
        return paginate(
            lambda cursor: self.list(
                limit=limit, cursor=cursor, bucket=bucket, platform=platform, account_id=account_id, from_=from_, to=to
            )
        )


class _Files:
    """The photos of the seller's library: register one, send its bytes, read it."""

    def __init__(self, sdk: ControlResell) -> None:
        self._sdk = sdk

    def register(
        self, filename: str, content_type: str, size: int, *, idempotency_key: str | None = None
    ) -> FileUpload:
        """Registers a file (jpeg, png, webp, heic or heif, at most 20 MiB): its identifier and the address where to
        ``PUT`` its bytes within 30 minutes (needs ``items:write``)."""
        body = FileUploadRequest(filename=filename, content_type=content_type, size=size)
        return self._sdk._call(upload_file, body=body, idempotency_key=_key(idempotency_key))  # noqa: SLF001

    def get(self, id: UUID | str) -> File:
        """One file of the library, with a signed link to read it; ``status`` is ``PENDING`` until its bytes are stored."""
        return self._sdk._call(get_file, id=UUID(str(id)))  # noqa: SLF001

    def upload(
        self, data: bytes, filename: str, content_type: str, *, idempotency_key: str | None = None
    ) -> FileUpload:
        """Registers a file and sends its bytes (an HTTP ``PUT`` with the same ``Content-Type``, no API key), and returns
        the registration: put its ``id`` in ``photo_ids``. The ``PUT`` is retried like any call; a refused one is raised
        as a ``ControlResellError`` (the file stays ``PENDING``)."""
        upload = self.register(filename, content_type, len(data), idempotency_key=idempotency_key)
        if not upload.upload_url:
            raise ValueError(f"The API returned no upload address for file {upload.id}.")
        # A network failure comes out of RetryTransport as a ControlResellConnectionError.
        response = self._sdk._storage.put(  # noqa: SLF001
            upload.upload_url, content=data, headers={"Content-Type": content_type}
        )
        if not response.is_success:
            raise error_of(response.status_code, None, response.headers)
        return upload


class _Customers:
    """The other parties of the seller's sales and purchases (needs the ``customers:read`` scope)."""

    def __init__(self, sdk: ControlResell) -> None:
        self._sdk = sdk

    def list(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        account_id: UUID | str | None = None,
        from_: datetime.datetime | None = None,
        to: datetime.datetime | None = None,
    ) -> CustomerPage:
        """One page of customers, the most recently created first.

        ``from_`` is inclusive and ``to`` exclusive, on the creation date (a naive datetime is read as UTC).
        """
        account = UUID(str(account_id)) if account_id is not None else None
        return self._sdk._call(  # noqa: SLF001
            list_customers, **_query(limit=limit, cursor=cursor, account_id=account, from_=_utc(from_), to=_utc(to))
        )

    def get(self, id: UUID | str) -> Customer:
        """One customer by its identifier."""
        return self._sdk._call(get_customer, id=UUID(str(id)))  # noqa: SLF001

    def iter(
        self,
        *,
        limit: int | None = None,
        account_id: UUID | str | None = None,
        from_: datetime.datetime | None = None,
        to: datetime.datetime | None = None,
    ) -> Iterator[Customer]:
        """Every customer, page after page, with the same filters."""
        return paginate(lambda cursor: self.list(limit=limit, cursor=cursor, account_id=account_id, from_=from_, to=to))


class _Favorites:
    """The buyers who put the seller's listings in their favorites (needs the ``items:read`` scope)."""

    def __init__(self, sdk: ControlResell) -> None:
        self._sdk = sdk

    def list(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        account_id: UUID | str | None = None,
        item_id: int | None = None,
        from_: datetime.datetime | None = None,
        to: datetime.datetime | None = None,
    ) -> FavoritePage:
        """One page of favorites, the most recent first.

        ``from_`` is inclusive and ``to`` exclusive, on the date of the favorite (a naive datetime is read as UTC).
        """
        account = UUID(str(account_id)) if account_id is not None else None
        return self._sdk._call(  # noqa: SLF001
            list_favorites,
            **_query(limit=limit, cursor=cursor, account_id=account, item_id=item_id, from_=_utc(from_), to=_utc(to)),
        )

    def iter(
        self,
        *,
        limit: int | None = None,
        account_id: UUID | str | None = None,
        item_id: int | None = None,
        from_: datetime.datetime | None = None,
        to: datetime.datetime | None = None,
    ) -> Iterator[Favorite]:
        """Every favorite, page after page, with the same filters."""
        return paginate(
            lambda cursor: self.list(
                limit=limit, cursor=cursor, account_id=account_id, item_id=item_id, from_=from_, to=to
            )
        )

    def list_item(
        self,
        id: int,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        from_: datetime.datetime | None = None,
        to: datetime.datetime | None = None,
    ) -> FavoritePage:
        """One page of the favorites of an item, on every account it is listed on, the most recent first."""
        return self._sdk._call(  # noqa: SLF001
            list_item_favorites, id=id, **_query(limit=limit, cursor=cursor, from_=_utc(from_), to=_utc(to))
        )

    def iter_item(
        self,
        id: int,
        *,
        limit: int | None = None,
        from_: datetime.datetime | None = None,
        to: datetime.datetime | None = None,
    ) -> Iterator[Favorite]:
        """Every favorite of an item, page after page, with the same period."""
        return paginate(lambda cursor: self.list_item(id, limit=limit, cursor=cursor, from_=from_, to=to))


class _Catalogs:
    """The catalog an item is written with: categories, brands, sizes, colors... (needs the ``items:read`` scope).

    The ``category_id`` filter of a list keeps only the values that apply to that category.
    """

    def __init__(self, sdk: ControlResell) -> None:
        self._sdk = sdk

    def categories(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        parent_id: int | None = None,
        platform: str | None = None,
    ) -> CatalogCategoryPage:
        """One page of categories, flat, by identifier; ``parent_id`` keeps the children of one, ``platform`` one marketplace."""
        return self._sdk._call(  # noqa: SLF001
            list_catalog_categories, **_query(limit=limit, cursor=cursor, parent_id=parent_id, platform=platform)
        )

    def iter_categories(
        self, *, limit: int | None = None, parent_id: int | None = None, platform: str | None = None
    ) -> Iterator[CatalogCategory]:
        """Every category, page after page, with the same filters."""
        return paginate(
            lambda cursor: self.categories(limit=limit, cursor=cursor, parent_id=parent_id, platform=platform)
        )

    def category(self, id: int) -> CatalogCategory:
        """One category by its identifier."""
        return self._sdk._call(get_catalog_category, id=id)  # noqa: SLF001

    def category_fields(self, id: int) -> CatalogCategoryFields:
        """What an item of a category is filled with: its size groups, enumerated and text fields, measurements."""
        return self._sdk._call(get_catalog_category_fields, id=id)  # noqa: SLF001

    def brands(self, *, limit: int | None = None, cursor: str | None = None, q: str | None = None) -> CatalogBrandPage:
        """One page of brands, by identifier or, with ``q``, those whose name starts with it."""
        return self._sdk._call(list_catalog_brands, **_query(limit=limit, cursor=cursor, q=q))  # noqa: SLF001

    def iter_brands(self, *, limit: int | None = None, q: str | None = None) -> Iterator[CatalogBrand]:
        """Every brand, page after page, with the same filters."""
        return paginate(lambda cursor: self.brands(limit=limit, cursor=cursor, q=q))

    def sizes(
        self, *, limit: int | None = None, cursor: str | None = None, category_id: int | None = None
    ) -> CatalogSizePage:
        """One page of sizes, each with its size group."""
        return self._sdk._call(  # noqa: SLF001
            list_catalog_sizes, **_query(limit=limit, cursor=cursor, category_id=category_id)
        )

    def iter_sizes(self, *, limit: int | None = None, category_id: int | None = None) -> Iterator[CatalogSize]:
        """Every size, page after page, with the same filters."""
        return paginate(lambda cursor: self.sizes(limit=limit, cursor=cursor, category_id=category_id))

    def colors(
        self, *, limit: int | None = None, cursor: str | None = None, category_id: int | None = None
    ) -> CatalogValuePage:
        """One page of colors."""
        return self._sdk._call(  # noqa: SLF001
            list_catalog_colors, **_query(limit=limit, cursor=cursor, category_id=category_id)
        )

    def iter_colors(self, *, limit: int | None = None, category_id: int | None = None) -> Iterator[CatalogValue]:
        """Every one of the colors, page after page, with the same filters."""
        return paginate(lambda cursor: self.colors(limit=limit, cursor=cursor, category_id=category_id))

    def conditions(
        self, *, limit: int | None = None, cursor: str | None = None, category_id: int | None = None
    ) -> CatalogValuePage:
        """One page of conditions."""
        return self._sdk._call(  # noqa: SLF001
            list_catalog_conditions, **_query(limit=limit, cursor=cursor, category_id=category_id)
        )

    def iter_conditions(self, *, limit: int | None = None, category_id: int | None = None) -> Iterator[CatalogValue]:
        """Every one of the conditions, page after page, with the same filters."""
        return paginate(lambda cursor: self.conditions(limit=limit, cursor=cursor, category_id=category_id))

    def package_sizes(
        self, *, limit: int | None = None, cursor: str | None = None, category_id: int | None = None
    ) -> CatalogValuePage:
        """One page of package sizes."""
        return self._sdk._call(  # noqa: SLF001
            list_catalog_package_sizes, **_query(limit=limit, cursor=cursor, category_id=category_id)
        )

    def iter_package_sizes(self, *, limit: int | None = None, category_id: int | None = None) -> Iterator[CatalogValue]:
        """Every one of the package sizes, page after page, with the same filters."""
        return paginate(lambda cursor: self.package_sizes(limit=limit, cursor=cursor, category_id=category_id))

    def materials(
        self, *, limit: int | None = None, cursor: str | None = None, category_id: int | None = None
    ) -> CatalogValuePage:
        """One page of materials."""
        return self._sdk._call(  # noqa: SLF001
            list_catalog_materials, **_query(limit=limit, cursor=cursor, category_id=category_id)
        )

    def iter_materials(self, *, limit: int | None = None, category_id: int | None = None) -> Iterator[CatalogValue]:
        """Every one of the materials, page after page, with the same filters."""
        return paginate(lambda cursor: self.materials(limit=limit, cursor=cursor, category_id=category_id))


class _Webhooks:
    """The seller's webhook endpoints, their secrets and deliveries, and the recent events.

    Reads need the ``webhooks:read`` scope, writes ``webhooks:write``.
    """

    def __init__(self, sdk: ControlResell) -> None:
        self._sdk = sdk

    def endpoints(self) -> WebhookEndpointPage:
        """The seller's endpoints, without their secrets (at most 5: a single page)."""
        return self._sdk._call(list_webhook_endpoints)  # noqa: SLF001

    def endpoint(self, id: UUID | str) -> WebhookEndpoint:
        """One endpoint by its identifier."""
        return self._sdk._call(get_webhook_endpoint, id=UUID(str(id)))  # noqa: SLF001

    def create_endpoint(
        self, body: WebhookEndpointCreateRequest, *, idempotency_key: str | None = None
    ) -> CreatedWebhookEndpoint:
        """Creates an endpoint; the answer carries its signing secret (``secret`` reads it again)."""
        return self._sdk._call(  # noqa: SLF001
            create_webhook_endpoint, body=body, idempotency_key=_key(idempotency_key)
        )

    def update_endpoint(self, id: UUID | str, body: WebhookEndpointUpdateRequest) -> WebhookEndpoint:
        """Updates the given fields of an endpoint (a JSON merge patch: ``description=None`` clears it).

        ``status="enabled"`` re-enables a disabled endpoint and resets its health.
        """
        return self._sdk._call(update_webhook_endpoint, id=UUID(str(id)), body=body)  # noqa: SLF001

    def delete_endpoint(self, id: UUID | str) -> None:
        """Deletes an endpoint; its pending deliveries are dropped."""
        self._sdk._call(delete_webhook_endpoint, id=UUID(str(id)))  # noqa: SLF001

    def secret(self, id: UUID | str) -> WebhookSecret:
        """The current signing secret of an endpoint."""
        return self._sdk._call(get_webhook_secret, id=UUID(str(id)))  # noqa: SLF001

    def rotate_secret(
        self,
        id: UUID | str,
        *,
        expires_in_hours: int | None = None,
        idempotency_key: str | None = None,
    ) -> WebhookSecret:
        """Gives an endpoint a new secret; the previous one stays valid ``expires_in_hours`` (24 by default, 0 at once)."""
        body = WebhookSecretRotateRequest() if expires_in_hours is None else WebhookSecretRotateRequest(
            expires_in_hours=expires_in_hours
        )
        return self._sdk._call(  # noqa: SLF001
            rotate_webhook_secret, id=UUID(str(id)), body=body, idempotency_key=_key(idempotency_key)
        )

    def test(self, id: UUID | str) -> WebhookTestResult:
        """Sends a ``webhook.test`` event to the endpoint now and returns how it answered."""
        return self._sdk._call(test_webhook_endpoint, id=UUID(str(id)))  # noqa: SLF001

    def deliveries(
        self,
        id: UUID | str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        status: str | None = None,
        type: str | None = None,  # noqa: A002
    ) -> WebhookDeliveryPage:
        """One page of the deliveries of an endpoint over the last 7 days, the most recent first."""
        return self._sdk._call(  # noqa: SLF001
            list_webhook_deliveries,
            id=UUID(str(id)),
            **_query(limit=limit, cursor=cursor, status=status, type_=type),
        )

    def iter_deliveries(
        self,
        id: UUID | str,
        *,
        limit: int | None = None,
        status: str | None = None,
        type: str | None = None,  # noqa: A002
    ) -> Iterator[WebhookDelivery]:
        """Every delivery of an endpoint, page after page, with the same filters."""
        return paginate(lambda cursor: self.deliveries(id, limit=limit, cursor=cursor, status=status, type=type))

    def retry_delivery(
        self, id: UUID | str, delivery_id: UUID | str, *, idempotency_key: str | None = None
    ) -> WebhookDelivery:
        """Sends one event to the endpoint again, with the same ``webhook-id``."""
        return self._sdk._call(  # noqa: SLF001
            retry_webhook_delivery,
            id=UUID(str(id)),
            delivery_id=UUID(str(delivery_id)),
            idempotency_key=_key(idempotency_key),
        )

    def recover(
        self, id: UUID | str, since: datetime.datetime, *, idempotency_key: str | None = None
    ) -> WebhookRecovery:
        """Sends again the failed deliveries since ``since`` (7 days at most, 1,000 per call: call again while ``has_more``)."""
        return self._sdk._call(  # noqa: SLF001
            recover_webhook_deliveries,
            id=UUID(str(id)),
            body=WebhookRecoverRequest(since=_utc(since)),
            idempotency_key=_key(idempotency_key),
        )

    def events(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        since: datetime.datetime | None = None,
        types: list[str] | None = None,
    ) -> WebhookEventPage:
        """One page of the events of the last 7 days, the oldest first: what a client that was offline catches up."""
        return self._sdk._call(  # noqa: SLF001
            list_webhook_events,
            **_query(limit=limit, cursor=cursor, since=_utc(since), type_=",".join(types) if types else None),
        )

    def iter_events(
        self, *, limit: int | None = None, since: datetime.datetime | None = None, types: list[str] | None = None
    ) -> Iterator[WebhookEvent]:
        """Every event, page after page, with the same filters."""
        return paginate(lambda cursor: self.events(limit=limit, cursor=cursor, since=since, types=types))

    def event_types(self) -> WebhookEventTypeList:
        """The catalog of event types and the scope each one needs."""
        return self._sdk._call(list_webhook_event_types)  # noqa: SLF001
