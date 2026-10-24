import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.favorite_page import FavoritePage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

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
        "url": "/api/public/v1/items/{id}/favorites".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | FavoritePage:
    if response.status_code == 200:
        response_200 = FavoritePage.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

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
) -> Response[ErrorResponse | FavoritePage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[ErrorResponse | FavoritePage]:
    """List the favorites of an item

     The favorites of the item's listings, on every account it is listed on. A favorite is a buyer of the
    marketplace who put one of the seller's listings in their favorites, named by their identifier on
    the marketplace (`buyerId`). Its `item` is a summary of the item of the listing, `null` when
    ControlResell does not follow the listing. The most recent first (by `createdAt`, then `id`), one
    page at a time: pass the `nextCursor` of a page as `cursor` to read the next one, with the same
    filters (a cursor reused with other filters is an `invalid_cursor`). `from` and `to` go straight to
    a period of the favorite's date: `from` is inclusive, `to` exclusive. Requires `items:read`.

    Args:
        id (int):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FavoritePage]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> ErrorResponse | FavoritePage | None:
    """List the favorites of an item

     The favorites of the item's listings, on every account it is listed on. A favorite is a buyer of the
    marketplace who put one of the seller's listings in their favorites, named by their identifier on
    the marketplace (`buyerId`). Its `item` is a summary of the item of the listing, `null` when
    ControlResell does not follow the listing. The most recent first (by `createdAt`, then `id`), one
    page at a time: pass the `nextCursor` of a page as `cursor` to read the next one, with the same
    filters (a cursor reused with other filters is an `invalid_cursor`). `from` and `to` go straight to
    a period of the favorite's date: `from` is inclusive, `to` exclusive. Requires `items:read`.

    Args:
        id (int):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FavoritePage
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
        cursor=cursor,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[ErrorResponse | FavoritePage]:
    """List the favorites of an item

     The favorites of the item's listings, on every account it is listed on. A favorite is a buyer of the
    marketplace who put one of the seller's listings in their favorites, named by their identifier on
    the marketplace (`buyerId`). Its `item` is a summary of the item of the listing, `null` when
    ControlResell does not follow the listing. The most recent first (by `createdAt`, then `id`), one
    page at a time: pass the `nextCursor` of a page as `cursor` to read the next one, with the same
    filters (a cursor reused with other filters is an `invalid_cursor`). `from` and `to` go straight to
    a period of the favorite's date: `from` is inclusive, `to` exclusive. Requires `items:read`.

    Args:
        id (int):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FavoritePage]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> ErrorResponse | FavoritePage | None:
    """List the favorites of an item

     The favorites of the item's listings, on every account it is listed on. A favorite is a buyer of the
    marketplace who put one of the seller's listings in their favorites, named by their identifier on
    the marketplace (`buyerId`). Its `item` is a summary of the item of the listing, `null` when
    ControlResell does not follow the listing. The most recent first (by `createdAt`, then `id`), one
    page at a time: pass the `nextCursor` of a page as `cursor` to read the next one, with the same
    filters (a cursor reused with other filters is an `invalid_cursor`). `from` and `to` go straight to
    a period of the favorite's date: `from` is inclusive, `to` exclusive. Requires `items:read`.

    Args:
        id (int):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FavoritePage
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
            cursor=cursor,
            from_=from_,
            to=to,
        )
    ).parsed
