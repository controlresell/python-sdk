from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webhook_event_data import WebhookEventData


T = TypeVar("T", bound="WebhookEvent")


@_attrs_define
class WebhookEvent:
    """
    Attributes:
        id (UUID):
        type_ (str):
        created_at (datetime.datetime):
        api_version (str):
        seller_id (int):
        data (WebhookEventData):
    """

    id: UUID
    type_: str
    created_at: datetime.datetime
    api_version: str
    seller_id: int
    data: WebhookEventData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_

        created_at = self.created_at.isoformat()

        api_version = self.api_version

        seller_id = self.seller_id

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "createdAt": created_at,
                "apiVersion": api_version,
                "sellerId": seller_id,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_event_data import WebhookEventData

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = d.pop("type")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        api_version = d.pop("apiVersion")

        seller_id = d.pop("sellerId")

        data = WebhookEventData.from_dict(d.pop("data"))

        webhook_event = cls(
            id=id,
            type_=type_,
            created_at=created_at,
            api_version=api_version,
            seller_id=seller_id,
            data=data,
        )

        webhook_event.additional_properties = d
        return webhook_event

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
