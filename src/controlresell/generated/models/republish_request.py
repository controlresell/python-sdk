from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_drop_request import PriceDropRequest


T = TypeVar("T", bound="RepublishRequest")


@_attrs_define
class RepublishRequest:
    """
    Attributes:
        account_ids (list[UUID] | None | Unset):
        price_drop (None | PriceDropRequest | Unset):
        price_variation (None | str | Unset):
        allow_if_deleted (bool | None | Unset):
    """

    account_ids: list[UUID] | None | Unset = UNSET
    price_drop: None | PriceDropRequest | Unset = UNSET
    price_variation: None | str | Unset = UNSET
    allow_if_deleted: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.price_drop_request import PriceDropRequest

        account_ids: list[str] | None | Unset
        if isinstance(self.account_ids, Unset):
            account_ids = UNSET
        elif isinstance(self.account_ids, list):
            account_ids = []
            for account_ids_type_0_item_data in self.account_ids:
                account_ids_type_0_item = str(account_ids_type_0_item_data)
                account_ids.append(account_ids_type_0_item)

        else:
            account_ids = self.account_ids

        price_drop: dict[str, Any] | None | Unset
        if isinstance(self.price_drop, Unset):
            price_drop = UNSET
        elif isinstance(self.price_drop, PriceDropRequest):
            price_drop = self.price_drop.to_dict()
        else:
            price_drop = self.price_drop

        price_variation: None | str | Unset
        if isinstance(self.price_variation, Unset):
            price_variation = UNSET
        else:
            price_variation = self.price_variation

        allow_if_deleted: bool | None | Unset
        if isinstance(self.allow_if_deleted, Unset):
            allow_if_deleted = UNSET
        else:
            allow_if_deleted = self.allow_if_deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_ids is not UNSET:
            field_dict["accountIds"] = account_ids
        if price_drop is not UNSET:
            field_dict["priceDrop"] = price_drop
        if price_variation is not UNSET:
            field_dict["priceVariation"] = price_variation
        if allow_if_deleted is not UNSET:
            field_dict["allowIfDeleted"] = allow_if_deleted

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.price_drop_request import PriceDropRequest

        d = dict(src_dict)

        def _parse_account_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                account_ids_type_0 = []
                _account_ids_type_0 = data
                for account_ids_type_0_item_data in _account_ids_type_0:
                    account_ids_type_0_item = UUID(account_ids_type_0_item_data)

                    account_ids_type_0.append(account_ids_type_0_item)

                return account_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        account_ids = _parse_account_ids(d.pop("accountIds", UNSET))

        def _parse_price_drop(data: object) -> None | PriceDropRequest | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                price_drop_type_0 = PriceDropRequest.from_dict(data)

                return price_drop_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PriceDropRequest | Unset, data)

        price_drop = _parse_price_drop(d.pop("priceDrop", UNSET))

        def _parse_price_variation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_variation = _parse_price_variation(d.pop("priceVariation", UNSET))

        def _parse_allow_if_deleted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_if_deleted = _parse_allow_if_deleted(d.pop("allowIfDeleted", UNSET))

        republish_request = cls(
            account_ids=account_ids,
            price_drop=price_drop,
            price_variation=price_variation,
            allow_if_deleted=allow_if_deleted,
        )

        republish_request.additional_properties = d
        return republish_request

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
