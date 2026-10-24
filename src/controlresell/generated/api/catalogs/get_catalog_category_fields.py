from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.catalog_category_fields import CatalogCategoryFields
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/public/v1/catalogs/categories/{id}/fields".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogCategoryFields | ErrorResponse:
    if response.status_code == 200:
        response_200 = CatalogCategoryFields.from_dict(response.json())

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
) -> Response[CatalogCategoryFields | ErrorResponse]:
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
) -> Response[CatalogCategoryFields | ErrorResponse]:
    """Read what an item of a category is filled with

     Everything an item of this category takes beyond its common fields: its size groups (`sizeId`), its
    enumerated fields with their values, each naming the item field it is written in (`colorIds`,
    `materialIds`, `state`, `packageSizeId`, or an `enumValues` entry `{"enumKey": field.key,
    "enumValue": value.key}`), its free-text fields (`attributes`, with whether a marketplace requires
    them) and the measurements. A field used on one marketplace only names it in `platform`. Requires
    `items:read`.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogCategoryFields | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
) -> CatalogCategoryFields | ErrorResponse | None:
    """Read what an item of a category is filled with

     Everything an item of this category takes beyond its common fields: its size groups (`sizeId`), its
    enumerated fields with their values, each naming the item field it is written in (`colorIds`,
    `materialIds`, `state`, `packageSizeId`, or an `enumValues` entry `{"enumKey": field.key,
    "enumValue": value.key}`), its free-text fields (`attributes`, with whether a marketplace requires
    them) and the measurements. A field used on one marketplace only names it in `platform`. Requires
    `items:read`.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogCategoryFields | ErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CatalogCategoryFields | ErrorResponse]:
    """Read what an item of a category is filled with

     Everything an item of this category takes beyond its common fields: its size groups (`sizeId`), its
    enumerated fields with their values, each naming the item field it is written in (`colorIds`,
    `materialIds`, `state`, `packageSizeId`, or an `enumValues` entry `{"enumKey": field.key,
    "enumValue": value.key}`), its free-text fields (`attributes`, with whether a marketplace requires
    them) and the measurements. A field used on one marketplace only names it in `platform`. Requires
    `items:read`.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogCategoryFields | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
) -> CatalogCategoryFields | ErrorResponse | None:
    """Read what an item of a category is filled with

     Everything an item of this category takes beyond its common fields: its size groups (`sizeId`), its
    enumerated fields with their values, each naming the item field it is written in (`colorIds`,
    `materialIds`, `state`, `packageSizeId`, or an `enumValues` entry `{"enumKey": field.key,
    "enumValue": value.key}`), its free-text fields (`attributes`, with whether a marketplace requires
    them) and the measurements. A field used on one marketplace only names it in `platform`. Requires
    `items:read`.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogCategoryFields | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
