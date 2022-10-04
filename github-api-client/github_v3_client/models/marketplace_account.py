from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketplaceAccount")


@attr.s(auto_attribs=True)
class MarketplaceAccount:
    """
    Attributes:
        url (str):
        id (int):
        type (str):
        login (str):
        node_id (Union[Unset, str]):
        email (Union[Unset, None, str]):
        organization_billing_email (Union[Unset, None, str]):
    """

    url: str
    id: int
    type: str
    login: str
    node_id: Union[Unset, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    organization_billing_email: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        type = self.type
        login = self.login
        node_id = self.node_id
        email = self.email
        organization_billing_email = self.organization_billing_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "type": type,
                "login": login,
            }
        )
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if email is not UNSET:
            field_dict["email"] = email
        if organization_billing_email is not UNSET:
            field_dict["organization_billing_email"] = organization_billing_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        type = d.pop("type")

        login = d.pop("login")

        node_id = d.pop("node_id", UNSET)

        email = d.pop("email", UNSET)

        organization_billing_email = d.pop("organization_billing_email", UNSET)

        marketplace_account = cls(
            url=url,
            id=id,
            type=type,
            login=login,
            node_id=node_id,
            email=email,
            organization_billing_email=organization_billing_email,
        )

        marketplace_account.additional_properties = d
        return marketplace_account

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
