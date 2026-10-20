from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.conversation_page import ConversationPage
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    unread: bool | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["unread"] = unread

    json_account_id: str | Unset = UNSET
    if not isinstance(account_id, Unset):
        json_account_id = str(account_id)
    params["accountId"] = json_account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/public/v1/conversations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConversationPage | ErrorResponse:
    if response.status_code == 200:
        response_200 = ConversationPage.from_dict(response.json())

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
) -> Response[ConversationPage | ErrorResponse]:
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
    unread: bool | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
) -> Response[ConversationPage | ErrorResponse]:
    """List the seller's conversations

     The conversations with buyers on the seller's marketplace accounts, latest activity first, one page
    at a time. A conversation that receives a message while you read moves to the head: read again from
    the first page to see it. Requires `conversations:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        unread (bool | Unset):
        account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationPage | ErrorResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        unread=unread,
        account_id=account_id,
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
    unread: bool | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
) -> ConversationPage | ErrorResponse | None:
    """List the seller's conversations

     The conversations with buyers on the seller's marketplace accounts, latest activity first, one page
    at a time. A conversation that receives a message while you read moves to the head: read again from
    the first page to see it. Requires `conversations:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        unread (bool | Unset):
        account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationPage | ErrorResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        unread=unread,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    unread: bool | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
) -> Response[ConversationPage | ErrorResponse]:
    """List the seller's conversations

     The conversations with buyers on the seller's marketplace accounts, latest activity first, one page
    at a time. A conversation that receives a message while you read moves to the head: read again from
    the first page to see it. Requires `conversations:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        unread (bool | Unset):
        account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationPage | ErrorResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        unread=unread,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    unread: bool | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
) -> ConversationPage | ErrorResponse | None:
    """List the seller's conversations

     The conversations with buyers on the seller's marketplace accounts, latest activity first, one page
    at a time. A conversation that receives a message while you read moves to the head: read again from
    the first page to see it. Requires `conversations:read`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        unread (bool | Unset):
        account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationPage | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            unread=unread,
            account_id=account_id,
        )
    ).parsed
