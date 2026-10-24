from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookDelivery")


@_attrs_define
class WebhookDelivery:
    """
    Attributes:
        id (UUID):
        event_id (UUID):
        event_type (str):
        status (str):
        attempt (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        http_status (int | None | Unset):
        error (None | str | Unset):
        duration_ms (int | None | Unset):
        next_attempt_at (datetime.datetime | None | Unset):
    """

    id: UUID
    event_id: UUID
    event_type: str
    status: str
    attempt: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    http_status: int | None | Unset = UNSET
    error: None | str | Unset = UNSET
    duration_ms: int | None | Unset = UNSET
    next_attempt_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        event_id = str(self.event_id)

        event_type = self.event_type

        status = self.status

        attempt = self.attempt

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        http_status: int | None | Unset
        if isinstance(self.http_status, Unset):
            http_status = UNSET
        else:
            http_status = self.http_status

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        duration_ms: int | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        next_attempt_at: None | str | Unset
        if isinstance(self.next_attempt_at, Unset):
            next_attempt_at = UNSET
        elif isinstance(self.next_attempt_at, datetime.datetime):
            next_attempt_at = self.next_attempt_at.isoformat()
        else:
            next_attempt_at = self.next_attempt_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "eventId": event_id,
                "eventType": event_type,
                "status": status,
                "attempt": attempt,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if http_status is not UNSET:
            field_dict["httpStatus"] = http_status
        if error is not UNSET:
            field_dict["error"] = error
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms
        if next_attempt_at is not UNSET:
            field_dict["nextAttemptAt"] = next_attempt_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        event_id = UUID(d.pop("eventId"))

        event_type = d.pop("eventType")

        status = d.pop("status")

        attempt = d.pop("attempt")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        def _parse_http_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        http_status = _parse_http_status(d.pop("httpStatus", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("durationMs", UNSET))

        def _parse_next_attempt_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_attempt_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_attempt_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_attempt_at = _parse_next_attempt_at(d.pop("nextAttemptAt", UNSET))

        webhook_delivery = cls(
            id=id,
            event_id=event_id,
            event_type=event_type,
            status=status,
            attempt=attempt,
            created_at=created_at,
            updated_at=updated_at,
            http_status=http_status,
            error=error,
            duration_ms=duration_ms,
            next_attempt_at=next_attempt_at,
        )

        webhook_delivery.additional_properties = d
        return webhook_delivery

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
