from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_address import CustomerAddress


T = TypeVar("T", bound="Customer")


@_attrs_define
class Customer:
    """
    Attributes:
        id (UUID):
        first_name (str):
        last_name (str):
        address (CustomerAddress):
        created_at (datetime.datetime):
        email (None | str | Unset):
    """

    id: UUID
    first_name: str
    last_name: str
    address: CustomerAddress
    created_at: datetime.datetime
    email: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        first_name = self.first_name

        last_name = self.last_name

        address = self.address.to_dict()

        created_at = self.created_at.isoformat()

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "firstName": first_name,
                "lastName": last_name,
                "address": address,
                "createdAt": created_at,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.customer_address import CustomerAddress

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        address = CustomerAddress.from_dict(d.pop("address"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        customer = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            address=address,
            created_at=created_at,
            email=email,
        )

        customer.additional_properties = d
        return customer

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
