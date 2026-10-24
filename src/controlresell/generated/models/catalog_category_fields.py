from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_enum_field import CatalogEnumField
    from ..models.catalog_measurement import CatalogMeasurement
    from ..models.catalog_text_field import CatalogTextField


T = TypeVar("T", bound="CatalogCategoryFields")


@_attrs_define
class CatalogCategoryFields:
    """
    Attributes:
        category_id (int):
        size_group_ids (list[int]):
        enum_fields (list[CatalogEnumField]):
        text_fields (list[CatalogTextField]):
        measurements (list[CatalogMeasurement]):
    """

    category_id: int
    size_group_ids: list[int]
    enum_fields: list[CatalogEnumField]
    text_fields: list[CatalogTextField]
    measurements: list[CatalogMeasurement]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        size_group_ids = self.size_group_ids

        enum_fields = []
        for enum_fields_item_data in self.enum_fields:
            enum_fields_item = enum_fields_item_data.to_dict()
            enum_fields.append(enum_fields_item)

        text_fields = []
        for text_fields_item_data in self.text_fields:
            text_fields_item = text_fields_item_data.to_dict()
            text_fields.append(text_fields_item)

        measurements = []
        for measurements_item_data in self.measurements:
            measurements_item = measurements_item_data.to_dict()
            measurements.append(measurements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "categoryId": category_id,
                "sizeGroupIds": size_group_ids,
                "enumFields": enum_fields,
                "textFields": text_fields,
                "measurements": measurements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_enum_field import CatalogEnumField
        from ..models.catalog_measurement import CatalogMeasurement
        from ..models.catalog_text_field import CatalogTextField

        d = dict(src_dict)
        category_id = d.pop("categoryId")

        size_group_ids = cast(list[int], d.pop("sizeGroupIds"))

        enum_fields = []
        _enum_fields = d.pop("enumFields")
        for enum_fields_item_data in _enum_fields:
            enum_fields_item = CatalogEnumField.from_dict(enum_fields_item_data)

            enum_fields.append(enum_fields_item)

        text_fields = []
        _text_fields = d.pop("textFields")
        for text_fields_item_data in _text_fields:
            text_fields_item = CatalogTextField.from_dict(text_fields_item_data)

            text_fields.append(text_fields_item)

        measurements = []
        _measurements = d.pop("measurements")
        for measurements_item_data in _measurements:
            measurements_item = CatalogMeasurement.from_dict(measurements_item_data)

            measurements.append(measurements_item)

        catalog_category_fields = cls(
            category_id=category_id,
            size_group_ids=size_group_ids,
            enum_fields=enum_fields,
            text_fields=text_fields,
            measurements=measurements,
        )

        catalog_category_fields.additional_properties = d
        return catalog_category_fields

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
