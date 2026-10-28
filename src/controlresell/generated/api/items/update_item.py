from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.item import Item
from ...models.item_update_request import ItemUpdateRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: ItemUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/public/v1/items/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Item:
    if response.status_code == 200:
        response_200 = Item.from_dict(response.json())

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

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

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
) -> Response[ErrorResponse | Item]:
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
    body: ItemUpdateRequest,
) -> Response[ErrorResponse | Item]:
    """Change an item of the seller's stock

     Changes one item of the seller's stock with a JSON merge patch: a field left out keeps its value, a
    field set to `null` is cleared (not `name`, `sold`, nor a list: send `[]` to empty a list), a list
    replaces the whole list. It changes the item in ControlResell only, not its listings on the
    marketplaces. The amounts are `{amount, currency}` in the item's currency (EUR for a new item;
    another currency is refused with `422 currency_mismatch`). `photoIds` are files already in the
    seller's library (`POST /files`): another seller's, an unknown one, or one whose bytes were never
    sent is `404 photo_not_found`. A label the seller does not have yet is created. The fields a
    marketplace asks for are written with the item: `packageSizeId`, `materialIds`, `measurementLength`
    and `measurementWidth` (centimeters), `enumValues` (the category's enumerated fields, `{enumKey,
    enumValue}`, one entry per picked value), `attributes` (its free-text fields, `{fieldKey, value}`,
    one per key) and `customFields` (the seller's own fields, `{fieldId, value}`); each list replaces
    the item's whole list. A place (`purchasePlaceId`, `sellingPlaceId`) or a custom field of another
    seller, or an unknown one, is `404 place_not_found` or `404 field_not_found`. `categoryId`, `sizeId`
    and `state` are ids from 1 (`0` is a 400, `null` clears them). Keys and enumerated values are
    trimmed and counted in characters (UTF-16 units), 1 to 100 for a key and 1 to 255 for a value; two
    entries that differ only by case or accents (as the database compares them) are a 400. At most 100
    entries per list, and 65,535 bytes (UTF-8) per free-text value. Read back, `enumValues`,
    `attributes` and `customFields` are sorted by key (then value, or field id), as plain strings (upper
    case before lower case). Requires `items:write`.

    Args:
        id (int):
        body (ItemUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Item]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ItemUpdateRequest,
) -> ErrorResponse | Item | None:
    """Change an item of the seller's stock

     Changes one item of the seller's stock with a JSON merge patch: a field left out keeps its value, a
    field set to `null` is cleared (not `name`, `sold`, nor a list: send `[]` to empty a list), a list
    replaces the whole list. It changes the item in ControlResell only, not its listings on the
    marketplaces. The amounts are `{amount, currency}` in the item's currency (EUR for a new item;
    another currency is refused with `422 currency_mismatch`). `photoIds` are files already in the
    seller's library (`POST /files`): another seller's, an unknown one, or one whose bytes were never
    sent is `404 photo_not_found`. A label the seller does not have yet is created. The fields a
    marketplace asks for are written with the item: `packageSizeId`, `materialIds`, `measurementLength`
    and `measurementWidth` (centimeters), `enumValues` (the category's enumerated fields, `{enumKey,
    enumValue}`, one entry per picked value), `attributes` (its free-text fields, `{fieldKey, value}`,
    one per key) and `customFields` (the seller's own fields, `{fieldId, value}`); each list replaces
    the item's whole list. A place (`purchasePlaceId`, `sellingPlaceId`) or a custom field of another
    seller, or an unknown one, is `404 place_not_found` or `404 field_not_found`. `categoryId`, `sizeId`
    and `state` are ids from 1 (`0` is a 400, `null` clears them). Keys and enumerated values are
    trimmed and counted in characters (UTF-16 units), 1 to 100 for a key and 1 to 255 for a value; two
    entries that differ only by case or accents (as the database compares them) are a 400. At most 100
    entries per list, and 65,535 bytes (UTF-8) per free-text value. Read back, `enumValues`,
    `attributes` and `customFields` are sorted by key (then value, or field id), as plain strings (upper
    case before lower case). Requires `items:write`.

    Args:
        id (int):
        body (ItemUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Item
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ItemUpdateRequest,
) -> Response[ErrorResponse | Item]:
    """Change an item of the seller's stock

     Changes one item of the seller's stock with a JSON merge patch: a field left out keeps its value, a
    field set to `null` is cleared (not `name`, `sold`, nor a list: send `[]` to empty a list), a list
    replaces the whole list. It changes the item in ControlResell only, not its listings on the
    marketplaces. The amounts are `{amount, currency}` in the item's currency (EUR for a new item;
    another currency is refused with `422 currency_mismatch`). `photoIds` are files already in the
    seller's library (`POST /files`): another seller's, an unknown one, or one whose bytes were never
    sent is `404 photo_not_found`. A label the seller does not have yet is created. The fields a
    marketplace asks for are written with the item: `packageSizeId`, `materialIds`, `measurementLength`
    and `measurementWidth` (centimeters), `enumValues` (the category's enumerated fields, `{enumKey,
    enumValue}`, one entry per picked value), `attributes` (its free-text fields, `{fieldKey, value}`,
    one per key) and `customFields` (the seller's own fields, `{fieldId, value}`); each list replaces
    the item's whole list. A place (`purchasePlaceId`, `sellingPlaceId`) or a custom field of another
    seller, or an unknown one, is `404 place_not_found` or `404 field_not_found`. `categoryId`, `sizeId`
    and `state` are ids from 1 (`0` is a 400, `null` clears them). Keys and enumerated values are
    trimmed and counted in characters (UTF-16 units), 1 to 100 for a key and 1 to 255 for a value; two
    entries that differ only by case or accents (as the database compares them) are a 400. At most 100
    entries per list, and 65,535 bytes (UTF-8) per free-text value. Read back, `enumValues`,
    `attributes` and `customFields` are sorted by key (then value, or field id), as plain strings (upper
    case before lower case). Requires `items:write`.

    Args:
        id (int):
        body (ItemUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Item]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ItemUpdateRequest,
) -> ErrorResponse | Item | None:
    """Change an item of the seller's stock

     Changes one item of the seller's stock with a JSON merge patch: a field left out keeps its value, a
    field set to `null` is cleared (not `name`, `sold`, nor a list: send `[]` to empty a list), a list
    replaces the whole list. It changes the item in ControlResell only, not its listings on the
    marketplaces. The amounts are `{amount, currency}` in the item's currency (EUR for a new item;
    another currency is refused with `422 currency_mismatch`). `photoIds` are files already in the
    seller's library (`POST /files`): another seller's, an unknown one, or one whose bytes were never
    sent is `404 photo_not_found`. A label the seller does not have yet is created. The fields a
    marketplace asks for are written with the item: `packageSizeId`, `materialIds`, `measurementLength`
    and `measurementWidth` (centimeters), `enumValues` (the category's enumerated fields, `{enumKey,
    enumValue}`, one entry per picked value), `attributes` (its free-text fields, `{fieldKey, value}`,
    one per key) and `customFields` (the seller's own fields, `{fieldId, value}`); each list replaces
    the item's whole list. A place (`purchasePlaceId`, `sellingPlaceId`) or a custom field of another
    seller, or an unknown one, is `404 place_not_found` or `404 field_not_found`. `categoryId`, `sizeId`
    and `state` are ids from 1 (`0` is a 400, `null` clears them). Keys and enumerated values are
    trimmed and counted in characters (UTF-16 units), 1 to 100 for a key and 1 to 255 for a value; two
    entries that differ only by case or accents (as the database compares them) are a 400. At most 100
    entries per list, and 65,535 bytes (UTF-8) per free-text value. Read back, `enumValues`,
    `attributes` and `customFields` are sorted by key (then value, or field id), as plain strings (upper
    case before lower case). Requires `items:write`.

    Args:
        id (int):
        body (ItemUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Item
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
