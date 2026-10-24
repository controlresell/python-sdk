from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookEndpoint")


@_attrs_define
class WebhookEndpoint:
    """
    Attributes:
        id (UUID):
        url (str):
        event_types (list[str]):
        payload_mode (str):
        status (str):
        api_version (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (None | str | Unset):
        disabled_reason (None | str | Unset):
        last_success_at (datetime.datetime | None | Unset):
    """

    id: UUID
    url: str
    event_types: list[str]
    payload_mode: str
    status: str
    api_version: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: None | str | Unset = UNSET
    disabled_reason: None | str | Unset = UNSET
    last_success_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        url = self.url

        event_types = self.event_types

        payload_mode = self.payload_mode

        status = self.status

        api_version = self.api_version

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        disabled_reason: None | str | Unset
        if isinstance(self.disabled_reason, Unset):
            disabled_reason = UNSET
        else:
            disabled_reason = self.disabled_reason

        last_success_at: None | str | Unset
        if isinstance(self.last_success_at, Unset):
            last_success_at = UNSET
        elif isinstance(self.last_success_at, datetime.datetime):
            last_success_at = self.last_success_at.isoformat()
        else:
            last_success_at = self.last_success_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "eventTypes": event_types,
                "payloadMode": payload_mode,
                "status": status,
                "apiVersion": api_version,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if disabled_reason is not UNSET:
            field_dict["disabledReason"] = disabled_reason
        if last_success_at is not UNSET:
            field_dict["lastSuccessAt"] = last_success_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        url = d.pop("url")

        event_types = cast(list[str], d.pop("eventTypes"))

        payload_mode = d.pop("payloadMode")

        status = d.pop("status")

        api_version = d.pop("apiVersion")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_disabled_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disabled_reason = _parse_disabled_reason(d.pop("disabledReason", UNSET))

        def _parse_last_success_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_success_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_success_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_success_at = _parse_last_success_at(d.pop("lastSuccessAt", UNSET))

        webhook_endpoint = cls(
            id=id,
            url=url,
            event_types=event_types,
            payload_mode=payload_mode,
            status=status,
            api_version=api_version,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            disabled_reason=disabled_reason,
            last_success_at=last_success_at,
        )

        webhook_endpoint.additional_properties = d
        return webhook_endpoint

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
