from typing import Any, Dict, List, Optional, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="MarketplaceListingPlan")


@attr.s(auto_attribs=True)
class MarketplaceListingPlan:
    """Marketplace Listing Plan

    Attributes:
        url (str):  Example: https://api.github.com/marketplace_listing/plans/1313.
        accounts_url (str):  Example: https://api.github.com/marketplace_listing/plans/1313/accounts.
        id (int):  Example: 1313.
        number (int):  Example: 3.
        name (str):  Example: Pro.
        description (str):  Example: A professional-grade CI solution.
        monthly_price_in_cents (int):  Example: 1099.
        yearly_price_in_cents (int):  Example: 11870.
        price_model (str):  Example: flat-rate.
        has_free_trial (bool):  Example: True.
        state (str):  Example: published.
        bullets (List[str]):  Example: ['Up to 25 private repositories', '11 concurrent builds'].
        unit_name (Optional[str]):
    """

    url: str
    accounts_url: str
    id: int
    number: int
    name: str
    description: str
    monthly_price_in_cents: int
    yearly_price_in_cents: int
    price_model: str
    has_free_trial: bool
    state: str
    bullets: List[str]
    unit_name: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        accounts_url = self.accounts_url
        id = self.id
        number = self.number
        name = self.name
        description = self.description
        monthly_price_in_cents = self.monthly_price_in_cents
        yearly_price_in_cents = self.yearly_price_in_cents
        price_model = self.price_model
        has_free_trial = self.has_free_trial
        state = self.state
        bullets = self.bullets

        unit_name = self.unit_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "accounts_url": accounts_url,
                "id": id,
                "number": number,
                "name": name,
                "description": description,
                "monthly_price_in_cents": monthly_price_in_cents,
                "yearly_price_in_cents": yearly_price_in_cents,
                "price_model": price_model,
                "has_free_trial": has_free_trial,
                "state": state,
                "bullets": bullets,
                "unit_name": unit_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        accounts_url = d.pop("accounts_url")

        id = d.pop("id")

        number = d.pop("number")

        name = d.pop("name")

        description = d.pop("description")

        monthly_price_in_cents = d.pop("monthly_price_in_cents")

        yearly_price_in_cents = d.pop("yearly_price_in_cents")

        price_model = d.pop("price_model")

        has_free_trial = d.pop("has_free_trial")

        state = d.pop("state")

        bullets = cast(List[str], d.pop("bullets"))

        unit_name = d.pop("unit_name")

        marketplace_listing_plan = cls(
            url=url,
            accounts_url=accounts_url,
            id=id,
            number=number,
            name=name,
            description=description,
            monthly_price_in_cents=monthly_price_in_cents,
            yearly_price_in_cents=yearly_price_in_cents,
            price_model=price_model,
            has_free_trial=has_free_trial,
            state=state,
            bullets=bullets,
            unit_name=unit_name,
        )

        marketplace_listing_plan.additional_properties = d
        return marketplace_listing_plan

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
