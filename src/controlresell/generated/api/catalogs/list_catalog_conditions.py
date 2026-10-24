from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.catalog_value_page import CatalogValuePage
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    category_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["categoryId"] = category_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/public/v1/catalogs/conditions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogValuePage | ErrorResponse:
    if response.status_code == 200:
        response_200 = CatalogValuePage.from_dict(response.json())

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
) -> Response[CatalogValuePage | ErrorResponse]:
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
    category_id: int | Unset = UNSET,
) -> Response[CatalogValuePage | ErrorResponse]:
    """List the conditions

     The conditions an item's `state` takes (their `id`), by identifier; with `categoryId`, only those
    that apply to that category. Titles in the seller's language. Requires `items:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        category_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogValuePage | ErrorResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        category_id=category_id,
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
    category_id: int | Unset = UNSET,
) -> CatalogValuePage | ErrorResponse | None:
    """List the conditions

     The conditions an item's `state` takes (their `id`), by identifier; with `categoryId`, only those
    that apply to that category. Titles in the seller's language. Requires `items:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        category_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogValuePage | ErrorResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        category_id=category_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    category_id: int | Unset = UNSET,
) -> Response[CatalogValuePage | ErrorResponse]:
    """List the conditions

     The conditions an item's `state` takes (their `id`), by identifier; with `categoryId`, only those
    that apply to that category. Titles in the seller's language. Requires `items:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        category_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogValuePage | ErrorResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        category_id=category_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    category_id: int | Unset = UNSET,
) -> CatalogValuePage | ErrorResponse | None:
    """List the conditions

     The conditions an item's `state` takes (their `id`), by identifier; with `categoryId`, only those
    that apply to that category. Titles in the seller's language. Requires `items:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        category_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogValuePage | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            category_id=category_id,
        )
    ).parsed
