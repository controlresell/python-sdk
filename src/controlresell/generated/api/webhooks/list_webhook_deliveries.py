from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.webhook_delivery_page import WebhookDeliveryPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["status"] = status

    params["type"] = type_

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/public/v1/webhook-endpoints/{id}/deliveries".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WebhookDeliveryPage:
    if response.status_code == 200:
        response_200 = WebhookDeliveryPage.from_dict(response.json())

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
) -> Response[ErrorResponse | WebhookDeliveryPage]:
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
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | WebhookDeliveryPage]:
    """List the deliveries of a webhook endpoint

     The delivery log of the last 7 days, the most recent first, one page at a time: status, attempt,
    HTTP status, duration and error, never the payload. Filters `status` (`pending`, `delivered`,
    `failed`) and `type`. Requires `webhooks:read`.

    Args:
        id (UUID):
        status (str | Unset):
        type_ (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookDeliveryPage]
    """

    kwargs = _get_kwargs(
        id=id,
        status=status,
        type_=type_,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | WebhookDeliveryPage | None:
    """List the deliveries of a webhook endpoint

     The delivery log of the last 7 days, the most recent first, one page at a time: status, attempt,
    HTTP status, duration and error, never the payload. Filters `status` (`pending`, `delivered`,
    `failed`) and `type`. Requires `webhooks:read`.

    Args:
        id (UUID):
        status (str | Unset):
        type_ (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookDeliveryPage
    """

    return sync_detailed(
        id=id,
        client=client,
        status=status,
        type_=type_,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | WebhookDeliveryPage]:
    """List the deliveries of a webhook endpoint

     The delivery log of the last 7 days, the most recent first, one page at a time: status, attempt,
    HTTP status, duration and error, never the payload. Filters `status` (`pending`, `delivered`,
    `failed`) and `type`. Requires `webhooks:read`.

    Args:
        id (UUID):
        status (str | Unset):
        type_ (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookDeliveryPage]
    """

    kwargs = _get_kwargs(
        id=id,
        status=status,
        type_=type_,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | WebhookDeliveryPage | None:
    """List the deliveries of a webhook endpoint

     The delivery log of the last 7 days, the most recent first, one page at a time: status, attempt,
    HTTP status, duration and error, never the payload. Filters `status` (`pending`, `delivered`,
    `failed`) and `type`. Requires `webhooks:read`.

    Args:
        id (UUID):
        status (str | Unset):
        type_ (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookDeliveryPage
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            status=status,
            type_=type_,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
