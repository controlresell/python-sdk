from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookEndpointUpdateRequest")


@_attrs_define
class WebhookEndpointUpdateRequest:
    """
    Attributes:
        url (None | str | Unset):
        description (None | str | Unset):
        event_types (list[str] | None | Unset):
        payload_mode (None | str | Unset):
        status (None | str | Unset):
    """

    url: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    event_types: list[str] | None | Unset = UNSET
    payload_mode: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        event_types: list[str] | None | Unset
        if isinstance(self.event_types, Unset):
            event_types = UNSET
        elif isinstance(self.event_types, list):
            event_types = self.event_types

        else:
            event_types = self.event_types

        payload_mode: None | str | Unset
        if isinstance(self.payload_mode, Unset):
            payload_mode = UNSET
        else:
            payload_mode = self.payload_mode

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description
        if event_types is not UNSET:
            field_dict["eventTypes"] = event_types
        if payload_mode is not UNSET:
            field_dict["payloadMode"] = payload_mode
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_event_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_types_type_0 = cast(list[str], data)

                return event_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        event_types = _parse_event_types(d.pop("eventTypes", UNSET))

        def _parse_payload_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payload_mode = _parse_payload_mode(d.pop("payloadMode", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        webhook_endpoint_update_request = cls(
            url=url,
            description=description,
            event_types=event_types,
            payload_mode=payload_mode,
            status=status,
        )

        webhook_endpoint_update_request.additional_properties = d
        return webhook_endpoint_update_request

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
