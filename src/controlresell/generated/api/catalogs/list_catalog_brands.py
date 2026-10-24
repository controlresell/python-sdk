from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.catalog_brand_page import CatalogBrandPage
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/public/v1/catalogs/brands",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogBrandPage | ErrorResponse:
    if response.status_code == 200:
        response_200 = CatalogBrandPage.from_dict(response.json())

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
) -> Response[CatalogBrandPage | ErrorResponse]:
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
    q: str | Unset = UNSET,
) -> Response[CatalogBrandPage | ErrorResponse]:
    """List the brands

     The brands an item's `brandId` takes: the global ones and the seller's own (`custom`), by
    identifier, or with `q` the brands whose name starts with it, by name (case and accents ignored).
    Requires `items:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogBrandPage | ErrorResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        q=q,
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
    q: str | Unset = UNSET,
) -> CatalogBrandPage | ErrorResponse | None:
    """List the brands

     The brands an item's `brandId` takes: the global ones and the seller's own (`custom`), by
    identifier, or with `q` the brands whose name starts with it, by name (case and accents ignored).
    Requires `items:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogBrandPage | ErrorResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Response[CatalogBrandPage | ErrorResponse]:
    """List the brands

     The brands an item's `brandId` takes: the global ones and the seller's own (`custom`), by
    identifier, or with `q` the brands whose name starts with it, by name (case and accents ignored).
    Requires `items:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogBrandPage | ErrorResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> CatalogBrandPage | ErrorResponse | None:
    """List the brands

     The brands an item's `brandId` takes: the global ones and the seller's own (`custom`), by
    identifier, or with `q` the brands whose name starts with it, by name (case and accents ignored).
    Requires `items:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogBrandPage | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            q=q,
        )
    ).parsed
