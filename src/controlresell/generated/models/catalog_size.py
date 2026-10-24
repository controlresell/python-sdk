from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CatalogSize")


@_attrs_define
class CatalogSize:
    """
    Attributes:
        id (int):
        title (str):
        size_group_id (int):
        size_group_title (str):
    """

    id: int
    title: str
    size_group_id: int
    size_group_title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        size_group_id = self.size_group_id

        size_group_title = self.size_group_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "sizeGroupId": size_group_id,
                "sizeGroupTitle": size_group_title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        size_group_id = d.pop("sizeGroupId")

        size_group_title = d.pop("sizeGroupTitle")

        catalog_size = cls(
            id=id,
            title=title,
            size_group_id=size_group_id,
            size_group_title=size_group_title,
        )

        catalog_size.additional_properties = d
        return catalog_size

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
