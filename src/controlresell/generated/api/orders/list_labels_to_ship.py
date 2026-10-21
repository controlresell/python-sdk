from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.order_label_page import OrderLabelPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/public/v1/orders/labels",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OrderLabelPage:
    if response.status_code == 200:
        response_200 = OrderLabelPage.from_dict(response.json())

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
) -> Response[ErrorResponse | OrderLabelPage]:
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
) -> Response[ErrorResponse | OrderLabelPage]:
    """List the shipping labels still to ship

     The shipping labels of the seller's orders waiting to be shipped (label ordered or sent to the
    seller, order not marked prepared), oldest order first, one page at a time. Each label names its
    order. The links are signed and expire: read them again rather than storing them. Requires
    `orders:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | OrderLabelPage]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
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
) -> ErrorResponse | OrderLabelPage | None:
    """List the shipping labels still to ship

     The shipping labels of the seller's orders waiting to be shipped (label ordered or sent to the
    seller, order not marked prepared), oldest order first, one page at a time. Each label names its
    order. The links are signed and expire: read them again rather than storing them. Requires
    `orders:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | OrderLabelPage
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | OrderLabelPage]:
    """List the shipping labels still to ship

     The shipping labels of the seller's orders waiting to be shipped (label ordered or sent to the
    seller, order not marked prepared), oldest order first, one page at a time. Each label names its
    order. The links are signed and expire: read them again rather than storing them. Requires
    `orders:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | OrderLabelPage]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | OrderLabelPage | None:
    """List the shipping labels still to ship

     The shipping labels of the seller's orders waiting to be shipped (label ordered or sent to the
    seller, order not marked prepared), oldest order first, one page at a time. Each label names its
    order. The links are signed and expire: read them again rather than storing them. Requires
    `orders:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | OrderLabelPage
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
