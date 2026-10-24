from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message import Message


T = TypeVar("T", bound="Conversation")


@_attrs_define
class Conversation:
    """
    Attributes:
        id (UUID):
        account_id (UUID):
        unread (bool):
        pinned (bool):
        updated_at (datetime.datetime):
        platform (None | str | Unset):
        buyer_login (None | str | Unset):
        buyer_id (None | str | Unset):
        last_message (Message | None | Unset):
        last_message_at (datetime.datetime | None | Unset):
    """

    id: UUID
    account_id: UUID
    unread: bool
    pinned: bool
    updated_at: datetime.datetime
    platform: None | str | Unset = UNSET
    buyer_login: None | str | Unset = UNSET
    buyer_id: None | str | Unset = UNSET
    last_message: Message | None | Unset = UNSET
    last_message_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.message import Message

        id = str(self.id)

        account_id = str(self.account_id)

        unread = self.unread

        pinned = self.pinned

        updated_at = self.updated_at.isoformat()

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        buyer_login: None | str | Unset
        if isinstance(self.buyer_login, Unset):
            buyer_login = UNSET
        else:
            buyer_login = self.buyer_login

        buyer_id: None | str | Unset
        if isinstance(self.buyer_id, Unset):
            buyer_id = UNSET
        else:
            buyer_id = self.buyer_id

        last_message: dict[str, Any] | None | Unset
        if isinstance(self.last_message, Unset):
            last_message = UNSET
        elif isinstance(self.last_message, Message):
            last_message = self.last_message.to_dict()
        else:
            last_message = self.last_message

        last_message_at: None | str | Unset
        if isinstance(self.last_message_at, Unset):
            last_message_at = UNSET
        elif isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "accountId": account_id,
                "unread": unread,
                "pinned": pinned,
                "updatedAt": updated_at,
            }
        )
        if platform is not UNSET:
            field_dict["platform"] = platform
        if buyer_login is not UNSET:
            field_dict["buyerLogin"] = buyer_login
        if buyer_id is not UNSET:
            field_dict["buyerId"] = buyer_id
        if last_message is not UNSET:
            field_dict["lastMessage"] = last_message
        if last_message_at is not UNSET:
            field_dict["lastMessageAt"] = last_message_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.message import Message

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        account_id = UUID(d.pop("accountId"))

        unread = d.pop("unread")

        pinned = d.pop("pinned")

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))

        def _parse_buyer_login(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        buyer_login = _parse_buyer_login(d.pop("buyerLogin", UNSET))

        def _parse_buyer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        buyer_id = _parse_buyer_id(d.pop("buyerId", UNSET))

        def _parse_last_message(data: object) -> Message | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_message_type_0 = Message.from_dict(data)

                return last_message_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Message | None | Unset, data)

        last_message = _parse_last_message(d.pop("lastMessage", UNSET))

        def _parse_last_message_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_message_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_message_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_message_at = _parse_last_message_at(d.pop("lastMessageAt", UNSET))

        conversation = cls(
            id=id,
            account_id=account_id,
            unread=unread,
            pinned=pinned,
            updated_at=updated_at,
            platform=platform,
            buyer_login=buyer_login,
            buyer_id=buyer_id,
            last_message=last_message,
            last_message_at=last_message_at,
        )

        conversation.additional_properties = d
        return conversation

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
