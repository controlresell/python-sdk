from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offer import Offer


T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """
    Attributes:
        id (UUID):
        conversation_id (UUID):
        author (str):
        type_ (str):
        status (str):
        created_at (datetime.datetime):
        body (None | str | Unset):
        offer (None | Offer | Unset):
    """

    id: UUID
    conversation_id: UUID
    author: str
    type_: str
    status: str
    created_at: datetime.datetime
    body: None | str | Unset = UNSET
    offer: None | Offer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.offer import Offer

        id = str(self.id)

        conversation_id = str(self.conversation_id)

        author = self.author

        type_ = self.type_

        status = self.status

        created_at = self.created_at.isoformat()

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        offer: dict[str, Any] | None | Unset
        if isinstance(self.offer, Unset):
            offer = UNSET
        elif isinstance(self.offer, Offer):
            offer = self.offer.to_dict()
        else:
            offer = self.offer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "conversationId": conversation_id,
                "author": author,
                "type": type_,
                "status": status,
                "createdAt": created_at,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body
        if offer is not UNSET:
            field_dict["offer"] = offer

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.offer import Offer

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        conversation_id = UUID(d.pop("conversationId"))

        author = d.pop("author")

        type_ = d.pop("type")

        status = d.pop("status")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        def _parse_offer(data: object) -> None | Offer | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                offer_type_0 = Offer.from_dict(data)

                return offer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Offer | Unset, data)

        offer = _parse_offer(d.pop("offer", UNSET))

        message = cls(
            id=id,
            conversation_id=conversation_id,
            author=author,
            type_=type_,
            status=status,
            created_at=created_at,
            body=body,
            offer=offer,
        )

        message.additional_properties = d
        return message

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
