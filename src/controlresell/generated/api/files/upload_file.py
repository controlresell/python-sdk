from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.file_upload import FileUpload
from ...models.file_upload_request import FileUploadRequest
from ...types import Response


def _get_kwargs(
    *,
    body: FileUploadRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/public/v1/files",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | FileUpload:
    if response.status_code == 201:
        response_201 = FileUpload.from_dict(response.json())

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
) -> Response[ErrorResponse | FileUpload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FileUploadRequest,
    idempotency_key: str,
) -> Response[ErrorResponse | FileUpload]:
    """Register a file to send

     Registers a file in the seller's library and returns its identifier and the address where to send
    its bytes: an HTTP `PUT` of the file to `uploadUrl`, with the same `Content-Type` and exactly `size`
    bytes as the body, and no `Authorization` header, within 30 minutes. Photos only (`image/jpeg`,
    `image/png`, `image/webp`, `image/heic`, `image/heif`), at most 20 MiB. Then put the identifier in
    `photoIds` of `POST /items` or `PATCH /items/{id}`; an identifier whose bytes were never sent is
    refused there (`404 photo_not_found`). The address is valid for 30 minutes: a replay of the same
    `Idempotency-Key` returns the same address, so register the file again with a new key once it has
    expired. Requires `items:write` and an `Idempotency-Key`.

    Args:
        idempotency_key (str):
        body (FileUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FileUpload]
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
    body: FileUploadRequest,
    idempotency_key: str,
) -> ErrorResponse | FileUpload | None:
    """Register a file to send

     Registers a file in the seller's library and returns its identifier and the address where to send
    its bytes: an HTTP `PUT` of the file to `uploadUrl`, with the same `Content-Type` and exactly `size`
    bytes as the body, and no `Authorization` header, within 30 minutes. Photos only (`image/jpeg`,
    `image/png`, `image/webp`, `image/heic`, `image/heif`), at most 20 MiB. Then put the identifier in
    `photoIds` of `POST /items` or `PATCH /items/{id}`; an identifier whose bytes were never sent is
    refused there (`404 photo_not_found`). The address is valid for 30 minutes: a replay of the same
    `Idempotency-Key` returns the same address, so register the file again with a new key once it has
    expired. Requires `items:write` and an `Idempotency-Key`.

    Args:
        idempotency_key (str):
        body (FileUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FileUpload
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FileUploadRequest,
    idempotency_key: str,
) -> Response[ErrorResponse | FileUpload]:
    """Register a file to send

     Registers a file in the seller's library and returns its identifier and the address where to send
    its bytes: an HTTP `PUT` of the file to `uploadUrl`, with the same `Content-Type` and exactly `size`
    bytes as the body, and no `Authorization` header, within 30 minutes. Photos only (`image/jpeg`,
    `image/png`, `image/webp`, `image/heic`, `image/heif`), at most 20 MiB. Then put the identifier in
    `photoIds` of `POST /items` or `PATCH /items/{id}`; an identifier whose bytes were never sent is
    refused there (`404 photo_not_found`). The address is valid for 30 minutes: a replay of the same
    `Idempotency-Key` returns the same address, so register the file again with a new key once it has
    expired. Requires `items:write` and an `Idempotency-Key`.

    Args:
        idempotency_key (str):
        body (FileUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FileUpload]
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
    body: FileUploadRequest,
    idempotency_key: str,
) -> ErrorResponse | FileUpload | None:
    """Register a file to send

     Registers a file in the seller's library and returns its identifier and the address where to send
    its bytes: an HTTP `PUT` of the file to `uploadUrl`, with the same `Content-Type` and exactly `size`
    bytes as the body, and no `Authorization` header, within 30 minutes. Photos only (`image/jpeg`,
    `image/png`, `image/webp`, `image/heic`, `image/heif`), at most 20 MiB. Then put the identifier in
    `photoIds` of `POST /items` or `PATCH /items/{id}`; an identifier whose bytes were never sent is
    refused there (`404 photo_not_found`). The address is valid for 30 minutes: a replay of the same
    `Idempotency-Key` returns the same address, so register the file again with a new key once it has
    expired. Requires `items:write` and an `Idempotency-Key`.

    Args:
        idempotency_key (str):
        body (FileUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FileUpload
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
