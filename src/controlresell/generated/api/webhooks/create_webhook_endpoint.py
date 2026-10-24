from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.created_webhook_endpoint import CreatedWebhookEndpoint
from ...models.error_response import ErrorResponse
from ...models.webhook_endpoint_create_request import WebhookEndpointCreateRequest
from ...types import Response


def _get_kwargs(
    *,
    body: WebhookEndpointCreateRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/public/v1/webhook-endpoints",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreatedWebhookEndpoint | ErrorResponse:
    if response.status_code == 201:
        response_201 = CreatedWebhookEndpoint.from_dict(response.json())

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
) -> Response[CreatedWebhookEndpoint | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WebhookEndpointCreateRequest,
    idempotency_key: str,
) -> Response[CreatedWebhookEndpoint | ErrorResponse]:
    """Create a webhook endpoint

     Registers an `https` URL that receives the seller's events, signed with the secret this response
    gives (`Cache-Control: no-store`; read it again with `GET /webhook-endpoints/{id}/secret`).
    `eventTypes` lists the types (`GET /webhook-event-types`) or is `["*"]` for all; the key must be
    able to read the object of each type. `payloadMode` is `light` (the default) or `full`. 5 endpoints
    at most per seller. Requires `webhooks:write` and an `Idempotency-Key`.

    Args:
        idempotency_key (str):
        body (WebhookEndpointCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedWebhookEndpoint | ErrorResponse]
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
    body: WebhookEndpointCreateRequest,
    idempotency_key: str,
) -> CreatedWebhookEndpoint | ErrorResponse | None:
    """Create a webhook endpoint

     Registers an `https` URL that receives the seller's events, signed with the secret this response
    gives (`Cache-Control: no-store`; read it again with `GET /webhook-endpoints/{id}/secret`).
    `eventTypes` lists the types (`GET /webhook-event-types`) or is `["*"]` for all; the key must be
    able to read the object of each type. `payloadMode` is `light` (the default) or `full`. 5 endpoints
    at most per seller. Requires `webhooks:write` and an `Idempotency-Key`.

    Args:
        idempotency_key (str):
        body (WebhookEndpointCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedWebhookEndpoint | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WebhookEndpointCreateRequest,
    idempotency_key: str,
) -> Response[CreatedWebhookEndpoint | ErrorResponse]:
    """Create a webhook endpoint

     Registers an `https` URL that receives the seller's events, signed with the secret this response
    gives (`Cache-Control: no-store`; read it again with `GET /webhook-endpoints/{id}/secret`).
    `eventTypes` lists the types (`GET /webhook-event-types`) or is `["*"]` for all; the key must be
    able to read the object of each type. `payloadMode` is `light` (the default) or `full`. 5 endpoints
    at most per seller. Requires `webhooks:write` and an `Idempotency-Key`.

    Args:
        idempotency_key (str):
        body (WebhookEndpointCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedWebhookEndpoint | ErrorResponse]
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
    body: WebhookEndpointCreateRequest,
    idempotency_key: str,
) -> CreatedWebhookEndpoint | ErrorResponse | None:
    """Create a webhook endpoint

     Registers an `https` URL that receives the seller's events, signed with the secret this response
    gives (`Cache-Control: no-store`; read it again with `GET /webhook-endpoints/{id}/secret`).
    `eventTypes` lists the types (`GET /webhook-event-types`) or is `["*"]` for all; the key must be
    able to read the object of each type. `payloadMode` is `light` (the default) or `full`. 5 endpoints
    at most per seller. Requires `webhooks:write` and an `Idempotency-Key`.

    Args:
        idempotency_key (str):
        body (WebhookEndpointCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedWebhookEndpoint | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
