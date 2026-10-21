from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.message import Message
from ...models.send_offer_request import SendOfferRequest
from ...types import Response


def _get_kwargs(
    id: UUID,
    *,
    body: SendOfferRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/public/v1/conversations/{id}/offers".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Message:
    if response.status_code == 201:
        response_201 = Message.from_dict(response.json())

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
) -> Response[ErrorResponse | Message]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SendOfferRequest,
    idempotency_key: str,
) -> Response[ErrorResponse | Message]:
    """Make the buyer a price offer

     Sends a price offer in one of the seller's conversations, in the currency of its account (EUR
    accounts only for now: `offer_currency_not_supported` otherwise). The offer is created at once and
    sent by the account's browser. Requires `conversations:write` and an `Idempotency-Key`.

    Args:
        id (UUID):
        idempotency_key (str):
        body (SendOfferRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Message]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SendOfferRequest,
    idempotency_key: str,
) -> ErrorResponse | Message | None:
    """Make the buyer a price offer

     Sends a price offer in one of the seller's conversations, in the currency of its account (EUR
    accounts only for now: `offer_currency_not_supported` otherwise). The offer is created at once and
    sent by the account's browser. Requires `conversations:write` and an `Idempotency-Key`.

    Args:
        id (UUID):
        idempotency_key (str):
        body (SendOfferRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Message
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SendOfferRequest,
    idempotency_key: str,
) -> Response[ErrorResponse | Message]:
    """Make the buyer a price offer

     Sends a price offer in one of the seller's conversations, in the currency of its account (EUR
    accounts only for now: `offer_currency_not_supported` otherwise). The offer is created at once and
    sent by the account's browser. Requires `conversations:write` and an `Idempotency-Key`.

    Args:
        id (UUID):
        idempotency_key (str):
        body (SendOfferRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Message]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SendOfferRequest,
    idempotency_key: str,
) -> ErrorResponse | Message | None:
    """Make the buyer a price offer

     Sends a price offer in one of the seller's conversations, in the currency of its account (EUR
    accounts only for now: `offer_currency_not_supported` otherwise). The offer is created at once and
    sent by the account's browser. Requires `conversations:write` and an `Idempotency-Key`.

    Args:
        id (UUID):
        idempotency_key (str):
        body (SendOfferRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Message
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
