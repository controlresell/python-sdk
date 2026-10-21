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
        estimated_price (Money | None | Unset):
        purchase_price (Money | None | Unset):
        purchase_date (datetime.datetime | None | Unset):
        selling_price (Money | None | Unset):
        selling_date (datetime.datetime | None | Unset):
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
    estimated_price: Money | None | Unset = UNSET
    purchase_price: Money | None | Unset = UNSET
    purchase_date: datetime.datetime | None | Unset = UNSET
    selling_price: Money | None | Unset = UNSET
    selling_date: datetime.datetime | None | Unset = UNSET
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
        if estimated_price is not UNSET:
            field_dict["estimatedPrice"] = estimated_price
        if purchase_price is not UNSET:
            field_dict["purchasePrice"] = purchase_price
        if purchase_date is not UNSET:
            field_dict["purchaseDate"] = purchase_date
        if selling_price is not UNSET:
            field_dict["sellingPrice"] = selling_price
        if selling_date is not UNSET:
            field_dict["sellingDate"] = selling_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
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
            estimated_price=estimated_price,
            purchase_price=purchase_price,
            purchase_date=purchase_date,
            selling_price=selling_price,
            selling_date=selling_date,
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
