from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PriceDropRequest")


@_attrs_define
class PriceDropRequest:
    """
    Attributes:
        type_ (str):
        value (str):
        round_type (None | str | Unset):
        round_step (None | str | Unset):
        account_ids (list[UUID] | None | Unset):
    """

    type_: str
    value: str
    round_type: None | str | Unset = UNSET
    round_step: None | str | Unset = UNSET
    account_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        value = self.value

        round_type: None | str | Unset
        if isinstance(self.round_type, Unset):
            round_type = UNSET
        else:
            round_type = self.round_type

        round_step: None | str | Unset
        if isinstance(self.round_step, Unset):
            round_step = UNSET
        else:
            round_step = self.round_step

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "value": value,
            }
        )
        if round_type is not UNSET:
            field_dict["roundType"] = round_type
        if round_step is not UNSET:
            field_dict["roundStep"] = round_step
        if account_ids is not UNSET:
            field_dict["accountIds"] = account_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        value = d.pop("value")

        def _parse_round_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        round_type = _parse_round_type(d.pop("roundType", UNSET))

        def _parse_round_step(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        round_step = _parse_round_step(d.pop("roundStep", UNSET))

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

        price_drop_request = cls(
            type_=type_,
            value=value,
            round_type=round_type,
            round_step=round_step,
            account_ids=account_ids,
        )

        price_drop_request.additional_properties = d
        return price_drop_request

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
