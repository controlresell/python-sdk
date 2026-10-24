from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.webhook_secret import WebhookSecret
from ...models.webhook_secret_rotate_request import WebhookSecretRotateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: WebhookSecretRotateRequest | Unset = UNSET,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/public/v1/webhook-endpoints/{id}/rotate-secret".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WebhookSecret:
    if response.status_code == 200:
        response_200 = WebhookSecret.from_dict(response.json())

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
) -> Response[ErrorResponse | WebhookSecret]:
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
    body: WebhookSecretRotateRequest | Unset = UNSET,
    idempotency_key: str,
) -> Response[ErrorResponse | WebhookSecret]:
    """Rotate the signing secret of a webhook endpoint

     A new signing secret, in this response (`Cache-Control: no-store`). The previous one keeps signing
    too for `expiresInHours` (0 to 72, 24 by default), so the receiver can switch without losing a
    delivery. Needs a key that can read everything the endpoint receives; the seller is told by e-mail.
    Requires `webhooks:write` and an `Idempotency-Key`.

    Args:
        id (UUID):
        idempotency_key (str):
        body (WebhookSecretRotateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookSecret]
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
    body: WebhookSecretRotateRequest | Unset = UNSET,
    idempotency_key: str,
) -> ErrorResponse | WebhookSecret | None:
    """Rotate the signing secret of a webhook endpoint

     A new signing secret, in this response (`Cache-Control: no-store`). The previous one keeps signing
    too for `expiresInHours` (0 to 72, 24 by default), so the receiver can switch without losing a
    delivery. Needs a key that can read everything the endpoint receives; the seller is told by e-mail.
    Requires `webhooks:write` and an `Idempotency-Key`.

    Args:
        id (UUID):
        idempotency_key (str):
        body (WebhookSecretRotateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookSecret
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
    body: WebhookSecretRotateRequest | Unset = UNSET,
    idempotency_key: str,
) -> Response[ErrorResponse | WebhookSecret]:
    """Rotate the signing secret of a webhook endpoint

     A new signing secret, in this response (`Cache-Control: no-store`). The previous one keeps signing
    too for `expiresInHours` (0 to 72, 24 by default), so the receiver can switch without losing a
    delivery. Needs a key that can read everything the endpoint receives; the seller is told by e-mail.
    Requires `webhooks:write` and an `Idempotency-Key`.

    Args:
        id (UUID):
        idempotency_key (str):
        body (WebhookSecretRotateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookSecret]
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
    body: WebhookSecretRotateRequest | Unset = UNSET,
    idempotency_key: str,
) -> ErrorResponse | WebhookSecret | None:
    """Rotate the signing secret of a webhook endpoint

     A new signing secret, in this response (`Cache-Control: no-store`). The previous one keeps signing
    too for `expiresInHours` (0 to 72, 24 by default), so the receiver can switch without losing a
    delivery. Needs a key that can read everything the endpoint receives; the seller is told by e-mail.
    Requires `webhooks:write` and an `Idempotency-Key`.

    Args:
        id (UUID):
        idempotency_key (str):
        body (WebhookSecretRotateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookSecret
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
