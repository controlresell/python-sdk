from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogCategory")


@_attrs_define
class CatalogCategory:
    """
    Attributes:
        id (int):
        title (str):
        has_children (bool):
        size_group_ids (list[int]):
        platforms (list[str]):
        parent_id (int | None | Unset):
    """

    id: int
    title: str
    has_children: bool
    size_group_ids: list[int]
    platforms: list[str]
    parent_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        has_children = self.has_children

        size_group_ids = self.size_group_ids

        platforms = self.platforms

        parent_id: int | None | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "hasChildren": has_children,
                "sizeGroupIds": size_group_ids,
                "platforms": platforms,
            }
        )
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        has_children = d.pop("hasChildren")

        size_group_ids = cast(list[int], d.pop("sizeGroupIds"))

        platforms = cast(list[str], d.pop("platforms"))

        def _parse_parent_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        catalog_category = cls(
            id=id,
            title=title,
            has_children=has_children,
            size_group_ids=size_group_ids,
            platforms=platforms,
            parent_id=parent_id,
        )

        catalog_category.additional_properties = d
        return catalog_category

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
