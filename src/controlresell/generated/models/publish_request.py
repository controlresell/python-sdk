from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishRequest")


@_attrs_define
class PublishRequest:
    """
    Attributes:
        account_ids (list[UUID]):
        cancel_before_proceeding (bool | None | Unset):
        scheduled_at (datetime.datetime | None | Unset):
    """

    account_ids: list[UUID]
    cancel_before_proceeding: bool | None | Unset = UNSET
    scheduled_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_ids = []
        for account_ids_item_data in self.account_ids:
            account_ids_item = str(account_ids_item_data)
            account_ids.append(account_ids_item)

        cancel_before_proceeding: bool | None | Unset
        if isinstance(self.cancel_before_proceeding, Unset):
            cancel_before_proceeding = UNSET
        else:
            cancel_before_proceeding = self.cancel_before_proceeding

        scheduled_at: None | str | Unset
        if isinstance(self.scheduled_at, Unset):
            scheduled_at = UNSET
        elif isinstance(self.scheduled_at, datetime.datetime):
            scheduled_at = self.scheduled_at.isoformat()
        else:
            scheduled_at = self.scheduled_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountIds": account_ids,
            }
        )
        if cancel_before_proceeding is not UNSET:
            field_dict["cancelBeforeProceeding"] = cancel_before_proceeding
        if scheduled_at is not UNSET:
            field_dict["scheduledAt"] = scheduled_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        account_ids = []
        _account_ids = d.pop("accountIds")
        for account_ids_item_data in _account_ids:
            account_ids_item = UUID(account_ids_item_data)

            account_ids.append(account_ids_item)

        def _parse_cancel_before_proceeding(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        cancel_before_proceeding = _parse_cancel_before_proceeding(
            d.pop("cancelBeforeProceeding", UNSET)
        )

        def _parse_scheduled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_at_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scheduled_at = _parse_scheduled_at(d.pop("scheduledAt", UNSET))

        publish_request = cls(
            account_ids=account_ids,
            cancel_before_proceeding=cancel_before_proceeding,
            scheduled_at=scheduled_at,
        )

        publish_request.additional_properties = d
        return publish_request

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
