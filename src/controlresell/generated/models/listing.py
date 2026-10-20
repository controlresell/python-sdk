from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="Listing")


@_attrs_define
class Listing:
    """
    Attributes:
        id (UUID):
        item_id (int):
        account_id (UUID):
        platform_id (str):
        url (str):
        price (Money):
        status (str):
        published_at (datetime.datetime):
        updated_at (datetime.datetime):
        platform (None | str | Unset):
        views_count (int | None | Unset):
        favorites_count (int | None | Unset):
        boosted_until (datetime.datetime | None | Unset):
    """

    id: UUID
    item_id: int
    account_id: UUID
    platform_id: str
    url: str
    price: Money
    status: str
    published_at: datetime.datetime
    updated_at: datetime.datetime
    platform: None | str | Unset = UNSET
    views_count: int | None | Unset = UNSET
    favorites_count: int | None | Unset = UNSET
    boosted_until: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        item_id = self.item_id

        account_id = str(self.account_id)

        platform_id = self.platform_id

        url = self.url

        price = self.price.to_dict()

        status = self.status

        published_at = self.published_at.isoformat()

        updated_at = self.updated_at.isoformat()

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        views_count: int | None | Unset
        if isinstance(self.views_count, Unset):
            views_count = UNSET
        else:
            views_count = self.views_count

        favorites_count: int | None | Unset
        if isinstance(self.favorites_count, Unset):
            favorites_count = UNSET
        else:
            favorites_count = self.favorites_count

        boosted_until: None | str | Unset
        if isinstance(self.boosted_until, Unset):
            boosted_until = UNSET
        elif isinstance(self.boosted_until, datetime.datetime):
            boosted_until = self.boosted_until.isoformat()
        else:
            boosted_until = self.boosted_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "itemId": item_id,
                "accountId": account_id,
                "platformId": platform_id,
                "url": url,
                "price": price,
                "status": status,
                "publishedAt": published_at,
                "updatedAt": updated_at,
            }
        )
        if platform is not UNSET:
            field_dict["platform"] = platform
        if views_count is not UNSET:
            field_dict["viewsCount"] = views_count
        if favorites_count is not UNSET:
            field_dict["favoritesCount"] = favorites_count
        if boosted_until is not UNSET:
            field_dict["boostedUntil"] = boosted_until

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.money import Money

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        item_id = d.pop("itemId")

        account_id = UUID(d.pop("accountId"))

        platform_id = d.pop("platformId")

        url = d.pop("url")

        price = Money.from_dict(d.pop("price"))

        status = d.pop("status")

        published_at = datetime.datetime.fromisoformat(d.pop("publishedAt"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))

        def _parse_views_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        views_count = _parse_views_count(d.pop("viewsCount", UNSET))

        def _parse_favorites_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        favorites_count = _parse_favorites_count(d.pop("favoritesCount", UNSET))

        def _parse_boosted_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                boosted_until_type_0 = datetime.datetime.fromisoformat(data)

                return boosted_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        boosted_until = _parse_boosted_until(d.pop("boostedUntil", UNSET))

        listing = cls(
            id=id,
            item_id=item_id,
            account_id=account_id,
            platform_id=platform_id,
            url=url,
            price=price,
            status=status,
            published_at=published_at,
            updated_at=updated_at,
            platform=platform,
            views_count=views_count,
            favorites_count=favorites_count,
            boosted_until=boosted_until,
        )

        listing.additional_properties = d
        return listing

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
