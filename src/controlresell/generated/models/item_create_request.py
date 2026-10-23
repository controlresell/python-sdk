from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_attribute import ItemAttribute
    from ..models.item_custom_field import ItemCustomField
    from ..models.item_enum_value import ItemEnumValue
    from ..models.money import Money


T = TypeVar("T", bound="ItemCreateRequest")


@_attrs_define
class ItemCreateRequest:
    """
    Attributes:
        name (str):
        sku (None | str | Unset):
        description (None | str | Unset):
        photo_ids (list[UUID] | Unset):
        category_id (int | None | Unset):
        brand_id (int | None | Unset):
        size_id (int | None | Unset):
        color_ids (list[int] | Unset):
        state (int | None | Unset):
        sex (None | str | Unset):
        labels (list[str] | Unset):
        sold (bool | Unset):
        package_size_id (int | None | Unset):
        material_ids (list[int] | Unset):
        measurement_length (float | None | Unset):
        measurement_width (float | None | Unset):
        enum_values (list[ItemEnumValue] | Unset):
        attributes (list[ItemAttribute] | Unset):
        custom_fields (list[ItemCustomField] | Unset):
        estimated_price (Money | None | Unset):
        purchase_price (Money | None | Unset):
        purchase_date (datetime.datetime | None | Unset):
        purchase_place_id (int | None | Unset):
        selling_price (Money | None | Unset):
        selling_date (datetime.datetime | None | Unset):
        selling_place_id (int | None | Unset):
    """

    name: str
    sku: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    photo_ids: list[UUID] | Unset = UNSET
    category_id: int | None | Unset = UNSET
    brand_id: int | None | Unset = UNSET
    size_id: int | None | Unset = UNSET
    color_ids: list[int] | Unset = UNSET
    state: int | None | Unset = UNSET
    sex: None | str | Unset = UNSET
    labels: list[str] | Unset = UNSET
    sold: bool | Unset = UNSET
    package_size_id: int | None | Unset = UNSET
    material_ids: list[int] | Unset = UNSET
    measurement_length: float | None | Unset = UNSET
    measurement_width: float | None | Unset = UNSET
    enum_values: list[ItemEnumValue] | Unset = UNSET
    attributes: list[ItemAttribute] | Unset = UNSET
    custom_fields: list[ItemCustomField] | Unset = UNSET
    estimated_price: Money | None | Unset = UNSET
    purchase_price: Money | None | Unset = UNSET
    purchase_date: datetime.datetime | None | Unset = UNSET
    purchase_place_id: int | None | Unset = UNSET
    selling_price: Money | None | Unset = UNSET
    selling_date: datetime.datetime | None | Unset = UNSET
    selling_place_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.money import Money

        name = self.name

        sku: None | str | Unset
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        photo_ids: list[str] | Unset = UNSET
        if not isinstance(self.photo_ids, Unset):
            photo_ids = []
            for photo_ids_item_data in self.photo_ids:
                photo_ids_item = str(photo_ids_item_data)
                photo_ids.append(photo_ids_item)

        category_id: int | None | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

        brand_id: int | None | Unset
        if isinstance(self.brand_id, Unset):
            brand_id = UNSET
        else:
            brand_id = self.brand_id

        size_id: int | None | Unset
        if isinstance(self.size_id, Unset):
            size_id = UNSET
        else:
            size_id = self.size_id

        color_ids: list[int] | Unset = UNSET
        if not isinstance(self.color_ids, Unset):
            color_ids = self.color_ids

        state: int | None | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        sex: None | str | Unset
        if isinstance(self.sex, Unset):
            sex = UNSET
        else:
            sex = self.sex

        labels: list[str] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        sold = self.sold

        package_size_id: int | None | Unset
        if isinstance(self.package_size_id, Unset):
            package_size_id = UNSET
        else:
            package_size_id = self.package_size_id

        material_ids: list[int] | Unset = UNSET
        if not isinstance(self.material_ids, Unset):
            material_ids = self.material_ids

        measurement_length: float | None | Unset
        if isinstance(self.measurement_length, Unset):
            measurement_length = UNSET
        else:
            measurement_length = self.measurement_length

        measurement_width: float | None | Unset
        if isinstance(self.measurement_width, Unset):
            measurement_width = UNSET
        else:
            measurement_width = self.measurement_width

        enum_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.enum_values, Unset):
            enum_values = []
            for enum_values_item_data in self.enum_values:
                enum_values_item = enum_values_item_data.to_dict()
                enum_values.append(enum_values_item)

        attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        custom_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        estimated_price: dict[str, Any] | None | Unset
        if isinstance(self.estimated_price, Unset):
            estimated_price = UNSET
        elif isinstance(self.estimated_price, Money):
            estimated_price = self.estimated_price.to_dict()
        else:
            estimated_price = self.estimated_price

        purchase_price: dict[str, Any] | None | Unset
        if isinstance(self.purchase_price, Unset):
            purchase_price = UNSET
        elif isinstance(self.purchase_price, Money):
            purchase_price = self.purchase_price.to_dict()
        else:
            purchase_price = self.purchase_price

        purchase_date: None | str | Unset
        if isinstance(self.purchase_date, Unset):
            purchase_date = UNSET
        elif isinstance(self.purchase_date, datetime.datetime):
            purchase_date = self.purchase_date.isoformat()
        else:
            purchase_date = self.purchase_date

        purchase_place_id: int | None | Unset
        if isinstance(self.purchase_place_id, Unset):
            purchase_place_id = UNSET
        else:
            purchase_place_id = self.purchase_place_id

        selling_price: dict[str, Any] | None | Unset
        if isinstance(self.selling_price, Unset):
            selling_price = UNSET
        elif isinstance(self.selling_price, Money):
            selling_price = self.selling_price.to_dict()
        else:
            selling_price = self.selling_price

        selling_date: None | str | Unset
        if isinstance(self.selling_date, Unset):
            selling_date = UNSET
        elif isinstance(self.selling_date, datetime.datetime):
            selling_date = self.selling_date.isoformat()
        else:
            selling_date = self.selling_date

        selling_place_id: int | None | Unset
        if isinstance(self.selling_place_id, Unset):
            selling_place_id = UNSET
        else:
            selling_place_id = self.selling_place_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if sku is not UNSET:
            field_dict["sku"] = sku
        if description is not UNSET:
            field_dict["description"] = description
        if photo_ids is not UNSET:
            field_dict["photoIds"] = photo_ids
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if brand_id is not UNSET:
            field_dict["brandId"] = brand_id
        if size_id is not UNSET:
            field_dict["sizeId"] = size_id
        if color_ids is not UNSET:
            field_dict["colorIds"] = color_ids
        if state is not UNSET:
            field_dict["state"] = state
        if sex is not UNSET:
            field_dict["sex"] = sex
        if labels is not UNSET:
            field_dict["labels"] = labels
        if sold is not UNSET:
            field_dict["sold"] = sold
        if package_size_id is not UNSET:
            field_dict["packageSizeId"] = package_size_id
        if material_ids is not UNSET:
            field_dict["materialIds"] = material_ids
        if measurement_length is not UNSET:
            field_dict["measurementLength"] = measurement_length
        if measurement_width is not UNSET:
            field_dict["measurementWidth"] = measurement_width
        if enum_values is not UNSET:
            field_dict["enumValues"] = enum_values
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if estimated_price is not UNSET:
            field_dict["estimatedPrice"] = estimated_price
        if purchase_price is not UNSET:
            field_dict["purchasePrice"] = purchase_price
        if purchase_date is not UNSET:
            field_dict["purchaseDate"] = purchase_date
        if purchase_place_id is not UNSET:
            field_dict["purchasePlaceId"] = purchase_place_id
        if selling_price is not UNSET:
            field_dict["sellingPrice"] = selling_price
        if selling_date is not UNSET:
            field_dict["sellingDate"] = selling_date
        if selling_place_id is not UNSET:
            field_dict["sellingPlaceId"] = selling_place_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.item_attribute import ItemAttribute
        from ..models.item_custom_field import ItemCustomField
        from ..models.item_enum_value import ItemEnumValue
        from ..models.money import Money

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_sku(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sku = _parse_sku(d.pop("sku", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _photo_ids = d.pop("photoIds", UNSET)
        photo_ids: list[UUID] | Unset = UNSET
        if _photo_ids is not UNSET:
            photo_ids = []
            for photo_ids_item_data in _photo_ids:
                photo_ids_item = UUID(photo_ids_item_data)

                photo_ids.append(photo_ids_item)

        def _parse_category_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        category_id = _parse_category_id(d.pop("categoryId", UNSET))

        def _parse_brand_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        brand_id = _parse_brand_id(d.pop("brandId", UNSET))

        def _parse_size_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_id = _parse_size_id(d.pop("sizeId", UNSET))

        color_ids = cast(list[int], d.pop("colorIds", UNSET))

        def _parse_state(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_sex(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sex = _parse_sex(d.pop("sex", UNSET))

        labels = cast(list[str], d.pop("labels", UNSET))

        sold = d.pop("sold", UNSET)

        def _parse_package_size_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        package_size_id = _parse_package_size_id(d.pop("packageSizeId", UNSET))

        material_ids = cast(list[int], d.pop("materialIds", UNSET))

        def _parse_measurement_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        measurement_length = _parse_measurement_length(
            d.pop("measurementLength", UNSET)
        )

        def _parse_measurement_width(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        measurement_width = _parse_measurement_width(d.pop("measurementWidth", UNSET))

        _enum_values = d.pop("enumValues", UNSET)
        enum_values: list[ItemEnumValue] | Unset = UNSET
        if _enum_values is not UNSET:
            enum_values = []
            for enum_values_item_data in _enum_values:
                enum_values_item = ItemEnumValue.from_dict(enum_values_item_data)

                enum_values.append(enum_values_item)

        _attributes = d.pop("attributes", UNSET)
        attributes: list[ItemAttribute] | Unset = UNSET
        if _attributes is not UNSET:
            attributes = []
            for attributes_item_data in _attributes:
                attributes_item = ItemAttribute.from_dict(attributes_item_data)

                attributes.append(attributes_item)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: list[ItemCustomField] | Unset = UNSET
        if _custom_fields is not UNSET:
            custom_fields = []
            for custom_fields_item_data in _custom_fields:
                custom_fields_item = ItemCustomField.from_dict(custom_fields_item_data)

                custom_fields.append(custom_fields_item)

        def _parse_estimated_price(data: object) -> Money | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                estimated_price_type_0 = Money.from_dict(data)

                return estimated_price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Money | None | Unset, data)

        estimated_price = _parse_estimated_price(d.pop("estimatedPrice", UNSET))

        def _parse_purchase_price(data: object) -> Money | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                purchase_price_type_0 = Money.from_dict(data)

                return purchase_price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Money | None | Unset, data)

        purchase_price = _parse_purchase_price(d.pop("purchasePrice", UNSET))

        def _parse_purchase_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purchase_date_type_0 = datetime.datetime.fromisoformat(data)

                return purchase_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        purchase_date = _parse_purchase_date(d.pop("purchaseDate", UNSET))

        def _parse_purchase_place_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        purchase_place_id = _parse_purchase_place_id(d.pop("purchasePlaceId", UNSET))

        def _parse_selling_price(data: object) -> Money | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                selling_price_type_0 = Money.from_dict(data)

                return selling_price_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Money | None | Unset, data)

        selling_price = _parse_selling_price(d.pop("sellingPrice", UNSET))

        def _parse_selling_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                selling_date_type_0 = datetime.datetime.fromisoformat(data)

                return selling_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        selling_date = _parse_selling_date(d.pop("sellingDate", UNSET))

        def _parse_selling_place_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        selling_place_id = _parse_selling_place_id(d.pop("sellingPlaceId", UNSET))

        item_create_request = cls(
            name=name,
            sku=sku,
            description=description,
            photo_ids=photo_ids,
            category_id=category_id,
            brand_id=brand_id,
            size_id=size_id,
            color_ids=color_ids,
            state=state,
            sex=sex,
            labels=labels,
            sold=sold,
            package_size_id=package_size_id,
            material_ids=material_ids,
            measurement_length=measurement_length,
            measurement_width=measurement_width,
            enum_values=enum_values,
            attributes=attributes,
            custom_fields=custom_fields,
            estimated_price=estimated_price,
            purchase_price=purchase_price,
            purchase_date=purchase_date,
            purchase_place_id=purchase_place_id,
            selling_price=selling_price,
            selling_date=selling_date,
            selling_place_id=selling_place_id,
        )

        item_create_request.additional_properties = d
        return item_create_request

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
