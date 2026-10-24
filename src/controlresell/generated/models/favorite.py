from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.favorite_item import FavoriteItem


T = TypeVar("T", bound="Favorite")


@_attrs_define
class Favorite:
    """
    Attributes:
        id (UUID):
        account_id (UUID):
        buyer_id (str):
        created_at (datetime.datetime):
        platform (None | str | Unset):
        message_sent_at (datetime.datetime | None | Unset):
        listing_id (None | Unset | UUID):
        item (FavoriteItem | None | Unset):
    """

    id: UUID
    account_id: UUID
    buyer_id: str
    created_at: datetime.datetime
    platform: None | str | Unset = UNSET
    message_sent_at: datetime.datetime | None | Unset = UNSET
    listing_id: None | Unset | UUID = UNSET
    item: FavoriteItem | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.favorite_item import FavoriteItem

        id = str(self.id)

        account_id = str(self.account_id)

        buyer_id = self.buyer_id

        created_at = self.created_at.isoformat()

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        message_sent_at: None | str | Unset
        if isinstance(self.message_sent_at, Unset):
            message_sent_at = UNSET
        elif isinstance(self.message_sent_at, datetime.datetime):
            message_sent_at = self.message_sent_at.isoformat()
        else:
            message_sent_at = self.message_sent_at

        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        elif isinstance(self.listing_id, UUID):
            listing_id = str(self.listing_id)
        else:
            listing_id = self.listing_id

        item: dict[str, Any] | None | Unset
        if isinstance(self.item, Unset):
            item = UNSET
        elif isinstance(self.item, FavoriteItem):
            item = self.item.to_dict()
        else:
            item = self.item

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "accountId": account_id,
                "buyerId": buyer_id,
                "createdAt": created_at,
            }
        )
        if platform is not UNSET:
            field_dict["platform"] = platform
        if message_sent_at is not UNSET:
            field_dict["messageSentAt"] = message_sent_at
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.favorite_item import FavoriteItem

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        account_id = UUID(d.pop("accountId"))

        buyer_id = d.pop("buyerId")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))

        def _parse_message_sent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                message_sent_at_type_0 = datetime.datetime.fromisoformat(data)

                return message_sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        message_sent_at = _parse_message_sent_at(d.pop("messageSentAt", UNSET))

        def _parse_listing_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                listing_id_type_0 = UUID(data)

                return listing_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))

        def _parse_item(data: object) -> FavoriteItem | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_0 = FavoriteItem.from_dict(data)

                return item_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FavoriteItem | None | Unset, data)

        item = _parse_item(d.pop("item", UNSET))

        favorite = cls(
            id=id,
            account_id=account_id,
            buyer_id=buyer_id,
            created_at=created_at,
            platform=platform,
            message_sent_at=message_sent_at,
            listing_id=listing_id,
            item=item,
        )

        favorite.additional_properties = d
        return favorite

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
