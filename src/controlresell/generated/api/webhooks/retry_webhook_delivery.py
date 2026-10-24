from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.webhook_delivery import WebhookDelivery
from ...types import Response


def _get_kwargs(
    id: UUID,
    delivery_id: UUID,
    *,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/public/v1/webhook-endpoints/{id}/deliveries/{delivery_id}/retry".format(
            id=quote(str(id), safe=""),
            delivery_id=quote(str(delivery_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WebhookDelivery:
    if response.status_code == 202:
        response_202 = WebhookDelivery.from_dict(response.json())

        return response_202

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
) -> Response[ErrorResponse | WebhookDelivery]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    delivery_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str,
) -> Response[ErrorResponse | WebhookDelivery]:
    """Send a delivery again

     Sends this event to this endpoint again, with the same `webhook-id`: a `failed` or `delivered`
    delivery goes back to `pending`, its attempts from 1 again. A delivery still `pending` (a retry or a
    recovery in progress) is already queued: it is not queued a second time, and is returned as it is,
    its attempts unchanged. 409 when the endpoint is disabled, 410 `event_expired` past 7 days. Requires
    `webhooks:write` and an `Idempotency-Key`.

    Args:
        id (UUID):
        delivery_id (UUID):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookDelivery]
    """

    kwargs = _get_kwargs(
        id=id,
        delivery_id=delivery_id,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    delivery_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str,
) -> ErrorResponse | WebhookDelivery | None:
    """Send a delivery again

     Sends this event to this endpoint again, with the same `webhook-id`: a `failed` or `delivered`
    delivery goes back to `pending`, its attempts from 1 again. A delivery still `pending` (a retry or a
    recovery in progress) is already queued: it is not queued a second time, and is returned as it is,
    its attempts unchanged. 409 when the endpoint is disabled, 410 `event_expired` past 7 days. Requires
    `webhooks:write` and an `Idempotency-Key`.

    Args:
        id (UUID):
        delivery_id (UUID):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookDelivery
    """

    return sync_detailed(
        id=id,
        delivery_id=delivery_id,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    delivery_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str,
) -> Response[ErrorResponse | WebhookDelivery]:
    """Send a delivery again

     Sends this event to this endpoint again, with the same `webhook-id`: a `failed` or `delivered`
    delivery goes back to `pending`, its attempts from 1 again. A delivery still `pending` (a retry or a
    recovery in progress) is already queued: it is not queued a second time, and is returned as it is,
    its attempts unchanged. 409 when the endpoint is disabled, 410 `event_expired` past 7 days. Requires
    `webhooks:write` and an `Idempotency-Key`.

    Args:
        id (UUID):
        delivery_id (UUID):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookDelivery]
    """

    kwargs = _get_kwargs(
        id=id,
        delivery_id=delivery_id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    delivery_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str,
) -> ErrorResponse | WebhookDelivery | None:
    """Send a delivery again

     Sends this event to this endpoint again, with the same `webhook-id`: a `failed` or `delivered`
    delivery goes back to `pending`, its attempts from 1 again. A delivery still `pending` (a retry or a
    recovery in progress) is already queued: it is not queued a second time, and is returned as it is,
    its attempts unchanged. 409 when the endpoint is disabled, 410 `event_expired` past 7 days. Requires
    `webhooks:write` and an `Idempotency-Key`.

    Args:
        id (UUID):
        delivery_id (UUID):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookDelivery
    """

    return (
        await asyncio_detailed(
            id=id,
            delivery_id=delivery_id,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed
