from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.marketplace_purchase_marketplace_pending_change import MarketplacePurchaseMarketplacePendingChange
from ..models.marketplace_purchase_marketplace_purchase import MarketplacePurchaseMarketplacePurchase
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketplacePurchase")


@attr.s(auto_attribs=True)
class MarketplacePurchase:
    """Marketplace Purchase

    Attributes:
        url (str):
        type (str):
        id (int):
        login (str):
        marketplace_purchase (MarketplacePurchaseMarketplacePurchase):
        organization_billing_email (Union[Unset, str]):
        email (Union[Unset, None, str]):
        marketplace_pending_change (Union[Unset, None, MarketplacePurchaseMarketplacePendingChange]):
    """

    url: str
    type: str
    id: int
    login: str
    marketplace_purchase: MarketplacePurchaseMarketplacePurchase
    organization_billing_email: Union[Unset, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    marketplace_pending_change: Union[Unset, None, MarketplacePurchaseMarketplacePendingChange] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        type = self.type
        id = self.id
        login = self.login
        marketplace_purchase = self.marketplace_purchase.to_dict()

        organization_billing_email = self.organization_billing_email
        email = self.email
        marketplace_pending_change: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.marketplace_pending_change, Unset):
            marketplace_pending_change = (
                self.marketplace_pending_change.to_dict() if self.marketplace_pending_change else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "type": type,
                "id": id,
                "login": login,
                "marketplace_purchase": marketplace_purchase,
            }
        )
        if organization_billing_email is not UNSET:
            field_dict["organization_billing_email"] = organization_billing_email
        if email is not UNSET:
            field_dict["email"] = email
        if marketplace_pending_change is not UNSET:
            field_dict["marketplace_pending_change"] = marketplace_pending_change

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        type = d.pop("type")

        id = d.pop("id")

        login = d.pop("login")

        marketplace_purchase = MarketplacePurchaseMarketplacePurchase.from_dict(d.pop("marketplace_purchase"))

        organization_billing_email = d.pop("organization_billing_email", UNSET)

        email = d.pop("email", UNSET)

        _marketplace_pending_change = d.pop("marketplace_pending_change", UNSET)
        marketplace_pending_change: Union[Unset, None, MarketplacePurchaseMarketplacePendingChange]
        if _marketplace_pending_change is None:
            marketplace_pending_change = None
        elif isinstance(_marketplace_pending_change, Unset):
            marketplace_pending_change = UNSET
        else:
            marketplace_pending_change = MarketplacePurchaseMarketplacePendingChange.from_dict(
                _marketplace_pending_change
            )

        marketplace_purchase = cls(
            url=url,
            type=type,
            id=id,
            login=login,
            marketplace_purchase=marketplace_purchase,
            organization_billing_email=organization_billing_email,
            email=email,
            marketplace_pending_change=marketplace_pending_change,
        )

        marketplace_purchase.additional_properties = d
        return marketplace_purchase

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
