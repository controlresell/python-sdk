from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookSecretRotateRequest")


@_attrs_define
class WebhookSecretRotateRequest:
    """
    Attributes:
        expires_in_hours (int | None | Unset):
    """

    expires_in_hours: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_in_hours: int | None | Unset
        if isinstance(self.expires_in_hours, Unset):
            expires_in_hours = UNSET
        else:
            expires_in_hours = self.expires_in_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_in_hours is not UNSET:
            field_dict["expiresInHours"] = expires_in_hours

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_expires_in_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_in_hours = _parse_expires_in_hours(d.pop("expiresInHours", UNSET))

        webhook_secret_rotate_request = cls(
            expires_in_hours=expires_in_hours,
        )

        webhook_secret_rotate_request.additional_properties = d
        return webhook_secret_rotate_request

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
