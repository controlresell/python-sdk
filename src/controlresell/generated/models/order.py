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
    from ..models.order_item import OrderItem


T = TypeVar("T", bound="Order")


@_attrs_define
class Order:
    """
    Attributes:
        id (UUID):
        account_id (UUID):
        type_ (str):
        status (str):
        platform_order_id (str):
        price (Money):
        prepared (bool):
        date (datetime.datetime):
        items (list[OrderItem]):
        conversation_id (None | Unset | UUID):
        transaction_id (None | Unset | UUID):
        platform_fee (Money | None | Unset):
        shipping_fee (Money | None | Unset):
        shipping_vat (Money | None | Unset):
        vat_amount (Money | None | Unset):
        total_amount (Money | None | Unset):
        refund_amount (Money | None | Unset):
    """

    id: UUID
    account_id: UUID
    type_: str
    status: str
    platform_order_id: str
    price: Money
    prepared: bool
    date: datetime.datetime
    items: list[OrderItem]
    conversation_id: None | Unset | UUID = UNSET
    transaction_id: None | Unset | UUID = UNSET
    platform_fee: Money | None | Unset = UNSET
    shipping_fee: Money | None | Unset = UNSET
    shipping_vat: Money | None | Unset = UNSET
    vat_amount: Money | None | Unset = UNSET
    total_amount: Money | None | Unset = UNSET
    refund_amount: Money | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.money import Money

        id = str(self.id)

        account_id = str(self.account_id)

        type_ = self.type_

        status = self.status

        platform_order_id = self.platform_order_id

        price = self.price.to_dict()

        prepared = self.prepared

        date = self.date.isoformat()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        conversation_id: None | str | Unset
        if isinstance(self.conversation_id, Unset):
            conversation_id = UNSET
        elif isinstance(self.conversation_id, UUID):
            conversation_id = str(self.conversation_id)
        else:
            conversation_id = self.conversation_id

        transaction_id: None | str | Unset
        if isinstance(self.transaction_id, Unset):
            transaction_id = UNSET
        elif isinstance(self.transaction_id, UUID):
            transaction_id = str(self.transaction_id)
        else:
            transaction_id = self.transaction_id

        platform_fee: dict[str, Any] | None | Unset
        if isinstance(self.platform_fee, Unset):
            platform_fee = UNSET
        elif isinstance(self.platform_fee, Money):
            platform_fee = self.platform_fee.to_dict()
        else:
            platform_fee = self.platform_fee

        shipping_fee: dict[str, Any] | None | Unset
        if isinstance(self.shipping_fee, Unset):
            shipping_fee = UNSET
        elif isinstance(self.shipping_fee, Money):
            shipping_fee = self.shipping_fee.to_dict()
        else:
            shipping_fee = self.shipping_fee

        shipping_vat: dict[str, Any] | None | Unset
        if isinstance(self.shipping_vat, Unset):
            shipping_vat = UNSET
        elif isinstance(self.shipping_vat, Money):
            shipping_vat = self.shipping_vat.to_dict()
        else:
            shipping_vat = self.shipping_vat

        vat_amount: dict[str, Any] | None | Unset
        if isinstance(self.vat_amount, Unset):
            vat_amount = UNSET
        elif isinstance(self.vat_amount, Money):
            vat_amount = self.vat_amount.to_dict()
        else:
            vat_amount = self.vat_amount

        total_amount: dict[str, Any] | None | Unset
        if isinstance(self.total_amount, Unset):
            total_amount = UNSET
        elif isinstance(self.total_amount, Money):
            total_amount = self.total_amount.to_dict()
        else:
            total_amount = self.total_amount

        refund_amount: dict[str, Any] | None | Unset
        if isinstance(self.refund_amount, Unset):
            refund_amount = UNSET
        elif isinstance(self.refund_amount, Money):
            refund_amount = self.refund_amount.to_dict()
        else:
            refund_amount = self.refund_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "accountId": account_id,
                "type": type_,
                "status": status,
                "platformOrderId": platform_order_id,
                "price": price,
                "prepared": prepared,
                "date": date,
                "items": items,
            }
        )
        if conversation_id is not UNSET:
            field_dict["conversationId"] = conversation_id
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if platform_fee is not UNSET:
            field_dict["platformFee"] = platform_fee
        if shipping_fee is not UNSET:
            field_dict["shippingFee"] = shipping_fee
        if shipping_vat is not UNSET:
            field_dict["shippingVat"] = shipping_vat
        if vat_amount is not UNSET:
            field_dict["vatAmount"] = vat_amount
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if refund_amount is not UNSET:
            field_dict["refundAmount"] = refund_amount

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.money import Money
        from ..models.order_item import OrderItem

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        account_id = UUID(d.pop("accountId"))

        type_ = d.pop("type")

        status = d.pop("status")

        platform_order_id = d.pop("platformOrderId")

        price = Money.from_dict(d.pop("price"))

        prepared = d.pop("prepared")

        date = datetime.datetime.fromisoformat(d.pop("date"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = OrderItem.from_dict(items_item_data)

            items.append(items_item)

        def _parse_conversation_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conversation_id_type_0 = UUID(data)

                return conversation_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        conversation_id = _parse_conversation_id(d.pop("conversationId", UNSET))

        def _parse_transaction_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                transaction_id_type_0 = UUID(data)

                return transaction_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        transaction_id = _parse_transaction_id(d.pop("transactionId", UNSET))

        def _parse_platform_fee(data: object) -> Money | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                platform_fee_type_0 = Money.from_dict(data)

                return platform_fee_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Money | None | Unset, data)

        platform_fee = _parse_platform_fee(d.pop("platformFee", UNSET))

        def _parse_shipping_fee(data: object) -> Money | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shipping_fee_type_0 = Money.from_dict(data)

                return shipping_fee_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Money | None | Unset, data)

        shipping_fee = _parse_shipping_fee(d.pop("shippingFee", UNSET))

        def _parse_shipping_vat(data: object) -> Money | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shipping_vat_type_0 = Money.from_dict(data)

                return shipping_vat_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Money | None | Unset, data)

        shipping_vat = _parse_shipping_vat(d.pop("shippingVat", UNSET))

        def _parse_vat_amount(data: object) -> Money | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vat_amount_type_0 = Money.from_dict(data)

                return vat_amount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Money | None | Unset, data)

        vat_amount = _parse_vat_amount(d.pop("vatAmount", UNSET))

        def _parse_total_amount(data: object) -> Money | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_amount_type_0 = Money.from_dict(data)

                return total_amount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Money | None | Unset, data)

        total_amount = _parse_total_amount(d.pop("totalAmount", UNSET))

        def _parse_refund_amount(data: object) -> Money | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                refund_amount_type_0 = Money.from_dict(data)

                return refund_amount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Money | None | Unset, data)

        refund_amount = _parse_refund_amount(d.pop("refundAmount", UNSET))

        order = cls(
            id=id,
            account_id=account_id,
            type_=type_,
            status=status,
            platform_order_id=platform_order_id,
            price=price,
            prepared=prepared,
            date=date,
            items=items,
            conversation_id=conversation_id,
            transaction_id=transaction_id,
            platform_fee=platform_fee,
            shipping_fee=shipping_fee,
            shipping_vat=shipping_vat,
            vat_amount=vat_amount,
            total_amount=total_amount,
            refund_amount=refund_amount,
        )

        order.additional_properties = d
        return order

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
