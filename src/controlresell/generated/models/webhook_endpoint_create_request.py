from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookEndpointCreateRequest")


@_attrs_define
class WebhookEndpointCreateRequest:
    """
    Attributes:
        url (str):
        event_types (list[str]):
        description (None | str | Unset):
        payload_mode (None | str | Unset):
    """

    url: str
    event_types: list[str]
    description: None | str | Unset = UNSET
    payload_mode: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        event_types = self.event_types

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        payload_mode: None | str | Unset
        if isinstance(self.payload_mode, Unset):
            payload_mode = UNSET
        else:
            payload_mode = self.payload_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "eventTypes": event_types,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if payload_mode is not UNSET:
            field_dict["payloadMode"] = payload_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url")

        event_types = cast(list[str], d.pop("eventTypes"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_payload_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payload_mode = _parse_payload_mode(d.pop("payloadMode", UNSET))

        webhook_endpoint_create_request = cls(
            url=url,
            event_types=event_types,
            description=description,
            payload_mode=payload_mode,
        )

        webhook_endpoint_create_request.additional_properties = d
        return webhook_endpoint_create_request

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
