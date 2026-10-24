import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.webhook_event_page import WebhookEventPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    since: datetime.datetime | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    params["type"] = type_

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/public/v1/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WebhookEventPage:
    if response.status_code == 200:
        response_200 = WebhookEventPage.from_dict(response.json())

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
) -> Response[ErrorResponse | WebhookEventPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: datetime.datetime | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | WebhookEventPage]:
    """List the seller's events

     The events of the last 7 days, the oldest first from `since`, in the envelope of a light webhook
    body: the way to catch up after being offline. Only the types the key can read (a type asked without
    its scope is a 403); `type` takes several types, comma separated.

    Args:
        since (datetime.datetime | Unset):
        type_ (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookEventPage]
    """

    kwargs = _get_kwargs(
        since=since,
        type_=type_,
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
    since: datetime.datetime | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | WebhookEventPage | None:
    """List the seller's events

     The events of the last 7 days, the oldest first from `since`, in the envelope of a light webhook
    body: the way to catch up after being offline. Only the types the key can read (a type asked without
    its scope is a 403); `type` takes several types, comma separated.

    Args:
        since (datetime.datetime | Unset):
        type_ (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookEventPage
    """

    return sync_detailed(
        client=client,
        since=since,
        type_=type_,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: datetime.datetime | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | WebhookEventPage]:
    """List the seller's events

     The events of the last 7 days, the oldest first from `since`, in the envelope of a light webhook
    body: the way to catch up after being offline. Only the types the key can read (a type asked without
    its scope is a 403); `type` takes several types, comma separated.

    Args:
        since (datetime.datetime | Unset):
        type_ (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookEventPage]
    """

    kwargs = _get_kwargs(
        since=since,
        type_=type_,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    since: datetime.datetime | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | WebhookEventPage | None:
    """List the seller's events

     The events of the last 7 days, the oldest first from `since`, in the envelope of a light webhook
    body: the way to catch up after being offline. Only the types the key can read (a type asked without
    its scope is a 403); `type` takes several types, comma separated.

    Args:
        since (datetime.datetime | Unset):
        type_ (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookEventPage
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
            type_=type_,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
