from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderLabel")


@_attrs_define
class OrderLabel:
    """
    Attributes:
        id (UUID):
        order_id (UUID):
        carrier (None | str | Unset):
        url (None | str | Unset):
        original_url (None | str | Unset):
        created_at (datetime.datetime | None | Unset):
    """

    id: UUID
    order_id: UUID
    carrier: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    original_url: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        order_id = str(self.order_id)

        carrier: None | str | Unset
        if isinstance(self.carrier, Unset):
            carrier = UNSET
        else:
            carrier = self.carrier

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        original_url: None | str | Unset
        if isinstance(self.original_url, Unset):
            original_url = UNSET
        else:
            original_url = self.original_url

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "orderId": order_id,
            }
        )
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if url is not UNSET:
            field_dict["url"] = url
        if original_url is not UNSET:
            field_dict["originalUrl"] = original_url
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        order_id = UUID(d.pop("orderId"))

        def _parse_carrier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        carrier = _parse_carrier(d.pop("carrier", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_original_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_url = _parse_original_url(d.pop("originalUrl", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        order_label = cls(
            id=id,
            order_id=order_id,
            carrier=carrier,
            url=url,
            original_url=original_url,
            created_at=created_at,
        )

        order_label.additional_properties = d
        return order_label

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
