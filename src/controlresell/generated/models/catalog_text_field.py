from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogTextField")


@_attrs_define
class CatalogTextField:
    """
    Attributes:
        key (str):
        type_ (str):
        required (bool):
        title (None | str | Unset):
        validation (None | str | Unset):
        platform (None | str | Unset):
    """

    key: str
    type_: str
    required: bool
    title: None | str | Unset = UNSET
    validation: None | str | Unset = UNSET
    platform: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        type_ = self.type_

        required = self.required

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        validation: None | str | Unset
        if isinstance(self.validation, Unset):
            validation = UNSET
        else:
            validation = self.validation

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "type": type_,
                "required": required,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if validation is not UNSET:
            field_dict["validation"] = validation
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        type_ = d.pop("type")

        required = d.pop("required")

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_validation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        validation = _parse_validation(d.pop("validation", UNSET))

        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))

        catalog_text_field = cls(
            key=key,
            type_=type_,
            required=required,
            title=title,
            validation=validation,
            platform=platform,
        )

        catalog_text_field.additional_properties = d
        return catalog_text_field

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
