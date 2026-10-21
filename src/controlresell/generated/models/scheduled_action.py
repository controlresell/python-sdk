from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ScheduledAction")


@_attrs_define
class ScheduledAction:
    """
    Attributes:
        item_id (int):
        action (str):
        account_ids (list[UUID]):
        scheduled_at (datetime.datetime):
    """

    item_id: int
    action: str
    account_ids: list[UUID]
    scheduled_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        action = self.action

        account_ids = []
        for account_ids_item_data in self.account_ids:
            account_ids_item = str(account_ids_item_data)
            account_ids.append(account_ids_item)

        scheduled_at = self.scheduled_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemId": item_id,
                "action": action,
                "accountIds": account_ids,
                "scheduledAt": scheduled_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        item_id = d.pop("itemId")

        action = d.pop("action")

        account_ids = []
        _account_ids = d.pop("accountIds")
        for account_ids_item_data in _account_ids:
            account_ids_item = UUID(account_ids_item_data)

            account_ids.append(account_ids_item)

        scheduled_at = datetime.datetime.fromisoformat(d.pop("scheduledAt"))

        scheduled_action = cls(
            item_id=item_id,
            action=action,
            account_ids=account_ids,
            scheduled_at=scheduled_at,
        )

        scheduled_action.additional_properties = d
        return scheduled_action

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
