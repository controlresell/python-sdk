import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.order_page import OrderPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    bucket: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["bucket"] = bucket

    params["platform"] = platform

    json_account_id: str | Unset = UNSET
    if not isinstance(account_id, Unset):
        json_account_id = str(account_id)
    params["accountId"] = json_account_id

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/public/v1/orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OrderPage:
    if response.status_code == 200:
        response_200 = OrderPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | OrderPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    bucket: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[ErrorResponse | OrderPage]:
    """List the seller's orders

     The seller's sales and purchases, every status, the most recent first (by `date`, then `id`), one
    page at a time: pass the `nextCursor` of a page as `cursor` to read the next one, with the same
    filters (a cursor reused with other filters is an `invalid_cursor`). `bucket` narrows the list to
    the orders to ship or to pick up, as the app's Orders tab shows them. `from` and `to` go straight to
    a period: `from` is inclusive, `to` exclusive, and the period is read page by page like the whole
    list. An unknown filter value is a 400 `bad_request`. Requires `orders:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        bucket (str | Unset):
        platform (str | Unset):
        account_id (UUID | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | OrderPage]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        bucket=bucket,
        platform=platform,
        account_id=account_id,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    bucket: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> ErrorResponse | OrderPage | None:
    """List the seller's orders

     The seller's sales and purchases, every status, the most recent first (by `date`, then `id`), one
    page at a time: pass the `nextCursor` of a page as `cursor` to read the next one, with the same
    filters (a cursor reused with other filters is an `invalid_cursor`). `bucket` narrows the list to
    the orders to ship or to pick up, as the app's Orders tab shows them. `from` and `to` go straight to
    a period: `from` is inclusive, `to` exclusive, and the period is read page by page like the whole
    list. An unknown filter value is a 400 `bad_request`. Requires `orders:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        bucket (str | Unset):
        platform (str | Unset):
        account_id (UUID | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | OrderPage
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        bucket=bucket,
        platform=platform,
        account_id=account_id,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    bucket: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[ErrorResponse | OrderPage]:
    """List the seller's orders

     The seller's sales and purchases, every status, the most recent first (by `date`, then `id`), one
    page at a time: pass the `nextCursor` of a page as `cursor` to read the next one, with the same
    filters (a cursor reused with other filters is an `invalid_cursor`). `bucket` narrows the list to
    the orders to ship or to pick up, as the app's Orders tab shows them. `from` and `to` go straight to
    a period: `from` is inclusive, `to` exclusive, and the period is read page by page like the whole
    list. An unknown filter value is a 400 `bad_request`. Requires `orders:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        bucket (str | Unset):
        platform (str | Unset):
        account_id (UUID | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | OrderPage]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        bucket=bucket,
        platform=platform,
        account_id=account_id,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    bucket: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> ErrorResponse | OrderPage | None:
    """List the seller's orders

     The seller's sales and purchases, every status, the most recent first (by `date`, then `id`), one
    page at a time: pass the `nextCursor` of a page as `cursor` to read the next one, with the same
    filters (a cursor reused with other filters is an `invalid_cursor`). `bucket` narrows the list to
    the orders to ship or to pick up, as the app's Orders tab shows them. `from` and `to` go straight to
    a period: `from` is inclusive, `to` exclusive, and the period is read page by page like the whole
    list. An unknown filter value is a 400 `bad_request`. Requires `orders:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        bucket (str | Unset):
        platform (str | Unset):
        account_id (UUID | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | OrderPage
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            bucket=bucket,
            platform=platform,
            account_id=account_id,
            from_=from_,
            to=to,
        )
    ).parsed
