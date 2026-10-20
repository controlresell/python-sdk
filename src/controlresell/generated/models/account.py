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


T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """
    Attributes:
        id (UUID):
        platform (str):
        name (str):
        status (str):
        locale (None | str | Unset):
        status_changed_at (datetime.datetime | None | Unset):
        lock_reason (None | str | Unset):
        cooldown_ends_at (datetime.datetime | None | Unset):
        restricted_until (datetime.datetime | None | Unset):
        available_balance (Money | None | Unset):
        pending_balance (Money | None | Unset):
    """

    id: UUID
    platform: str
    name: str
    status: str
    locale: None | str | Unset = UNSET
    status_changed_at: datetime.datetime | None | Unset = UNSET
    lock_reason: None | str | Unset = UNSET
    cooldown_ends_at: datetime.datetime | None | Unset = UNSET
    restricted_until: datetime.datetime | None | Unset = UNSET
    available_balance: Money | None | Unset = UNSET
    pending_balance: Money | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.money import Money

        id = str(self.id)

        platform = self.platform

        name = self.name

        status = self.status

        locale: None | str | Unset
        if isinstance(self.locale, Unset):
            locale = UNSET
        else:
            locale = self.locale

        status_changed_at: None | str | Unset
        if isinstance(self.status_changed_at, Unset):
            status_changed_at = UNSET
        elif isinstance(self.status_changed_at, datetime.datetime):
            status_changed_at = self.status_changed_at.isoformat()
        else:
            status_changed_at = self.status_changed_at

        lock_reason: None | str | Unset
        if isinstance(self.lock_reason, Unset):
            lock_reason = UNSET
        else:
            lock_reason = self.lock_reason

        cooldown_ends_at: None | str | Unset
        if isinstance(self.cooldown_ends_at, Unset):
            cooldown_ends_at = UNSET
        elif isinstance(self.cooldown_ends_at, datetime.datetime):
            cooldown_ends_at = self.cooldown_ends_at.isoformat()
        else:
            cooldown_ends_at = self.cooldown_ends_at

        restricted_until: None | str | Unset
        if isinstance(self.restricted_until, Unset):
            restricted_until = UNSET
        elif isinstance(self.restricted_until, datetime.datetime):
            restricted_until = self.restricted_until.isoformat()
        else:
            restricted_until = self.restricted_until

        available_balance: dict[str, Any] | None | Unset
        if isinstance(self.available_balance, Unset):
            available_balance = UNSET
        elif isinstance(self.available_balance, Money):
            available_balance = self.available_balance.to_dict()
        else:
            available_balance = self.available_balance

        pending_balance: dict[str, Any] | None | Unset
        if isinstance(self.pending_balance, Unset):
            pending_balance = UNSET
        elif isinstance(self.pending_balance, Money):
            pending_balance = self.pending_balance.to_dict()
        else:
            pending_balance = self.pending_balance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "platform": platform,
                "name": name,
                "status": status,
            }
        )
        if locale is not UNSET:
            field_dict["locale"] = locale
        if status_changed_at is not UNSET:
            field_dict["statusChangedAt"] = status_changed_at
        if lock_reason is not UNSET:
            field_dict["lockReason"] = lock_reason
        if cooldown_ends_at is not UNSET:
            field_dict["cooldownEndsAt"] = cooldown_ends_at
        if restricted_until is not UNSET:
            field_dict["restrictedUntil"] = restricted_until
        if available_balance is not UNSET:
            field_dict["availableBalance"] = available_balance
        if pending_balance is not UNSET:
            field_dict["pendingBalance"] = pending_balance

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.money import Money

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        platform = d.pop("platform")

        name = d.pop("name")

        status = d.pop("status")

        def _parse_locale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locale = _parse_locale(d.pop("locale", UNSET))

        def _parse_status_changed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_changed_at_type_0 = datetime.datetime.fromisoformat(data)

                return status_changed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        status_changed_at = _parse_status_changed_at(d.pop("statusChangedAt", UNSET))

        def _parse_lock_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lock_reason = _parse_lock_reason(d.pop("lockReason", UNSET))

        def _parse_cooldown_ends_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cooldown_ends_at_type_0 = datetime.datetime.fromisoformat(data)

                return cooldown_ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        cooldown_ends_at = _parse_cooldown_ends_at(d.pop("cooldownEndsAt", UNSET))

        def _parse_restricted_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                restricted_until_type_0 = datetime.datetime.fromisoformat(data)

                return restricted_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        restricted_until = _parse_restricted_until(d.pop("restrictedUntil", UNSET))

        def _parse_available_balance(data: object) -> Money | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                available_balance_type_0 = Money.from_dict(data)

                return available_balance_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Money | None | Unset, data)

        available_balance = _parse_available_balance(d.pop("availableBalance", UNSET))

        def _parse_pending_balance(data: object) -> Money | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pending_balance_type_0 = Money.from_dict(data)

                return pending_balance_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Money | None | Unset, data)

        pending_balance = _parse_pending_balance(d.pop("pendingBalance", UNSET))

        account = cls(
            id=id,
            platform=platform,
            name=name,
            status=status,
            locale=locale,
            status_changed_at=status_changed_at,
            lock_reason=lock_reason,
            cooldown_ends_at=cooldown_ends_at,
            restricted_until=restricted_until,
            available_balance=available_balance,
            pending_balance=pending_balance,
        )

        account.additional_properties = d
        return account

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
