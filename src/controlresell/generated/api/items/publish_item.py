from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.publish_request import PublishRequest
from ...models.scheduled_action import ScheduledAction
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: PublishRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/public/v1/items/{id}/publish".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ScheduledAction:
    if response.status_code == 202:
        response_202 = ScheduledAction.from_dict(response.json())

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
) -> Response[ErrorResponse | ScheduledAction]:
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
    body: PublishRequest,
    idempotency_key: str,
) -> Response[ErrorResponse | ScheduledAction]:
    """Publish an item on the seller's accounts

     Schedules the publication of one item of the seller's stock on the given marketplace accounts, now
    or at `scheduledAt` (at most 30 days ahead). The publication runs on the account's browser: read its
    result on `GET /items/{id}/listings`. To cross-list an item ("list it on eBay"), call this route
    with that account: this API never relays a marketplace's own API. Publishing one item on several
    accounts of the same marketplace risks a strike from it: name only the accounts you mean. Requires
    `items:write` and an `Idempotency-Key`.

    Args:
        id (int):
        idempotency_key (str):
        body (PublishRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ScheduledAction]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PublishRequest,
    idempotency_key: str,
) -> ErrorResponse | ScheduledAction | None:
    """Publish an item on the seller's accounts

     Schedules the publication of one item of the seller's stock on the given marketplace accounts, now
    or at `scheduledAt` (at most 30 days ahead). The publication runs on the account's browser: read its
    result on `GET /items/{id}/listings`. To cross-list an item ("list it on eBay"), call this route
    with that account: this API never relays a marketplace's own API. Publishing one item on several
    accounts of the same marketplace risks a strike from it: name only the accounts you mean. Requires
    `items:write` and an `Idempotency-Key`.

    Args:
        id (int):
        idempotency_key (str):
        body (PublishRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ScheduledAction
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PublishRequest,
    idempotency_key: str,
) -> Response[ErrorResponse | ScheduledAction]:
    """Publish an item on the seller's accounts

     Schedules the publication of one item of the seller's stock on the given marketplace accounts, now
    or at `scheduledAt` (at most 30 days ahead). The publication runs on the account's browser: read its
    result on `GET /items/{id}/listings`. To cross-list an item ("list it on eBay"), call this route
    with that account: this API never relays a marketplace's own API. Publishing one item on several
    accounts of the same marketplace risks a strike from it: name only the accounts you mean. Requires
    `items:write` and an `Idempotency-Key`.

    Args:
        id (int):
        idempotency_key (str):
        body (PublishRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ScheduledAction]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PublishRequest,
    idempotency_key: str,
) -> ErrorResponse | ScheduledAction | None:
    """Publish an item on the seller's accounts

     Schedules the publication of one item of the seller's stock on the given marketplace accounts, now
    or at `scheduledAt` (at most 30 days ahead). The publication runs on the account's browser: read its
    result on `GET /items/{id}/listings`. To cross-list an item ("list it on eBay"), call this route
    with that account: this API never relays a marketplace's own API. Publishing one item on several
    accounts of the same marketplace risks a strike from it: name only the accounts you mean. Requires
    `items:write` and an `Idempotency-Key`.

    Args:
        id (int):
        idempotency_key (str):
        body (PublishRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ScheduledAction
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
