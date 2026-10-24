from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookSecret")


@_attrs_define
class WebhookSecret:
    """
    Attributes:
        secret (str):
        previous_secret_expires_at (datetime.datetime | None | Unset):
    """

    secret: str
    previous_secret_expires_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret = self.secret

        previous_secret_expires_at: None | str | Unset
        if isinstance(self.previous_secret_expires_at, Unset):
            previous_secret_expires_at = UNSET
        elif isinstance(self.previous_secret_expires_at, datetime.datetime):
            previous_secret_expires_at = self.previous_secret_expires_at.isoformat()
        else:
            previous_secret_expires_at = self.previous_secret_expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secret": secret,
            }
        )
        if previous_secret_expires_at is not UNSET:
            field_dict["previousSecretExpiresAt"] = previous_secret_expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        secret = d.pop("secret")

        def _parse_previous_secret_expires_at(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                previous_secret_expires_at_type_0 = datetime.datetime.fromisoformat(
                    data
                )

                return previous_secret_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        previous_secret_expires_at = _parse_previous_secret_expires_at(
            d.pop("previousSecretExpiresAt", UNSET)
        )

        webhook_secret = cls(
            secret=secret,
            previous_secret_expires_at=previous_secret_expires_at,
        )

        webhook_secret.additional_properties = d
        return webhook_secret

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
