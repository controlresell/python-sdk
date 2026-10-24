from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.webhook_endpoint import WebhookEndpoint
from ...models.webhook_endpoint_update_request import WebhookEndpointUpdateRequest
from ...types import Response


def _get_kwargs(
    id: UUID,
    *,
    body: WebhookEndpointUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/public/v1/webhook-endpoints/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WebhookEndpoint:
    if response.status_code == 200:
        response_200 = WebhookEndpoint.from_dict(response.json())

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
) -> Response[ErrorResponse | WebhookEndpoint]:
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
    body: WebhookEndpointUpdateRequest,
) -> Response[ErrorResponse | WebhookEndpoint]:
    """Change a webhook endpoint

     A JSON merge patch: a field left out keeps its value, `description: null` clears it. Changing `url`
    or `payloadMode` needs a key that can read everything the endpoint receives. `status` `disabled`
    stops the deliveries (pending ones fail); `enabled` turns it back on, its failures reset. Only
    `{"status": "disabled"}` is open without the plan. Requires `webhooks:write`.

    Args:
        id (UUID):
        body (WebhookEndpointUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookEndpoint]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: WebhookEndpointUpdateRequest,
) -> ErrorResponse | WebhookEndpoint | None:
    """Change a webhook endpoint

     A JSON merge patch: a field left out keeps its value, `description: null` clears it. Changing `url`
    or `payloadMode` needs a key that can read everything the endpoint receives. `status` `disabled`
    stops the deliveries (pending ones fail); `enabled` turns it back on, its failures reset. Only
    `{"status": "disabled"}` is open without the plan. Requires `webhooks:write`.

    Args:
        id (UUID):
        body (WebhookEndpointUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookEndpoint
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: WebhookEndpointUpdateRequest,
) -> Response[ErrorResponse | WebhookEndpoint]:
    """Change a webhook endpoint

     A JSON merge patch: a field left out keeps its value, `description: null` clears it. Changing `url`
    or `payloadMode` needs a key that can read everything the endpoint receives. `status` `disabled`
    stops the deliveries (pending ones fail); `enabled` turns it back on, its failures reset. Only
    `{"status": "disabled"}` is open without the plan. Requires `webhooks:write`.

    Args:
        id (UUID):
        body (WebhookEndpointUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookEndpoint]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: WebhookEndpointUpdateRequest,
) -> ErrorResponse | WebhookEndpoint | None:
    """Change a webhook endpoint

     A JSON merge patch: a field left out keeps its value, `description: null` clears it. Changing `url`
    or `payloadMode` needs a key that can read everything the endpoint receives. `status` `disabled`
    stops the deliveries (pending ones fail); `enabled` turns it back on, its failures reset. Only
    `{"status": "disabled"}` is open without the plan. Requires `webhooks:write`.

    Args:
        id (UUID):
        body (WebhookEndpointUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookEndpoint
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
