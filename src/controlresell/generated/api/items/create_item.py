from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.item import Item
from ...models.item_create_request import ItemCreateRequest
from ...types import Response


def _get_kwargs(
    *,
    body: ItemCreateRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/public/v1/items",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Item:
    if response.status_code == 201:
        response_201 = Item.from_dict(response.json())

        return response_201

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

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | Item]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ItemCreateRequest,
    idempotency_key: str,
) -> Response[ErrorResponse | Item]:
    """Create an item in the seller's stock

     Creates one item in the seller's ControlResell stock, unsold unless `sold` says otherwise, without
    publishing it: publish it with `POST /items/{id}/publish`. Only `name` is required. The amounts are
    `{amount, currency}` in the item's currency (EUR for a new item; another currency is refused with
    `422 currency_mismatch`). `photoIds` are files already in the seller's library: another seller's, or
    an unknown one, is `404 photo_not_found`. A label the seller does not have yet is created. Requires
    `items:write` and an `Idempotency-Key`.

    Args:
        idempotency_key (str):
        body (ItemCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Item]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ItemCreateRequest,
    idempotency_key: str,
) -> ErrorResponse | Item | None:
    """Create an item in the seller's stock

     Creates one item in the seller's ControlResell stock, unsold unless `sold` says otherwise, without
    publishing it: publish it with `POST /items/{id}/publish`. Only `name` is required. The amounts are
    `{amount, currency}` in the item's currency (EUR for a new item; another currency is refused with
    `422 currency_mismatch`). `photoIds` are files already in the seller's library: another seller's, or
    an unknown one, is `404 photo_not_found`. A label the seller does not have yet is created. Requires
    `items:write` and an `Idempotency-Key`.

    Args:
        idempotency_key (str):
        body (ItemCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Item
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ItemCreateRequest,
    idempotency_key: str,
) -> Response[ErrorResponse | Item]:
    """Create an item in the seller's stock

     Creates one item in the seller's ControlResell stock, unsold unless `sold` says otherwise, without
    publishing it: publish it with `POST /items/{id}/publish`. Only `name` is required. The amounts are
    `{amount, currency}` in the item's currency (EUR for a new item; another currency is refused with
    `422 currency_mismatch`). `photoIds` are files already in the seller's library: another seller's, or
    an unknown one, is `404 photo_not_found`. A label the seller does not have yet is created. Requires
    `items:write` and an `Idempotency-Key`.

    Args:
        idempotency_key (str):
        body (ItemCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Item]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ItemCreateRequest,
    idempotency_key: str,
) -> ErrorResponse | Item | None:
    """Create an item in the seller's stock

     Creates one item in the seller's ControlResell stock, unsold unless `sold` says otherwise, without
    publishing it: publish it with `POST /items/{id}/publish`. Only `name` is required. The amounts are
    `{amount, currency}` in the item's currency (EUR for a new item; another currency is refused with
    `422 currency_mismatch`). `photoIds` are files already in the seller's library: another seller's, or
    an unknown one, is `404 photo_not_found`. A label the seller does not have yet is created. Requires
    `items:write` and an `Idempotency-Key`.

    Args:
        idempotency_key (str):
        body (ItemCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Item
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
