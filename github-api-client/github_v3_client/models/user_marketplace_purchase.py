import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.marketplace_account import MarketplaceAccount
from ..models.marketplace_listing_plan import MarketplaceListingPlan

T = TypeVar("T", bound="UserMarketplacePurchase")


@attr.s(auto_attribs=True)
class UserMarketplacePurchase:
    """User Marketplace Purchase

    Attributes:
        billing_cycle (str):  Example: monthly.
        on_free_trial (bool):  Example: True.
        account (MarketplaceAccount):
        plan (MarketplaceListingPlan): Marketplace Listing Plan
        next_billing_date (Optional[datetime.datetime]):  Example: 2017-11-11T00:00:00Z.
        unit_count (Optional[int]):
        free_trial_ends_on (Optional[datetime.datetime]):  Example: 2017-11-11T00:00:00Z.
        updated_at (Optional[datetime.datetime]):  Example: 2017-11-02T01:12:12Z.
    """

    billing_cycle: str
    on_free_trial: bool
    account: MarketplaceAccount
    plan: MarketplaceListingPlan
    next_billing_date: Optional[datetime.datetime]
    unit_count: Optional[int]
    free_trial_ends_on: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billing_cycle = self.billing_cycle
        on_free_trial = self.on_free_trial
        account = self.account.to_dict()

        plan = self.plan.to_dict()

        next_billing_date = self.next_billing_date.isoformat() if self.next_billing_date else None

        unit_count = self.unit_count
        free_trial_ends_on = self.free_trial_ends_on.isoformat() if self.free_trial_ends_on else None

        updated_at = self.updated_at.isoformat() if self.updated_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billing_cycle": billing_cycle,
                "on_free_trial": on_free_trial,
                "account": account,
                "plan": plan,
                "next_billing_date": next_billing_date,
                "unit_count": unit_count,
                "free_trial_ends_on": free_trial_ends_on,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        billing_cycle = d.pop("billing_cycle")

        on_free_trial = d.pop("on_free_trial")

        account = MarketplaceAccount.from_dict(d.pop("account"))

        plan = MarketplaceListingPlan.from_dict(d.pop("plan"))

        _next_billing_date = d.pop("next_billing_date")
        next_billing_date: Optional[datetime.datetime]
        if _next_billing_date is None:
            next_billing_date = None
        else:
            next_billing_date = isoparse(_next_billing_date)

        unit_count = d.pop("unit_count")

        _free_trial_ends_on = d.pop("free_trial_ends_on")
        free_trial_ends_on: Optional[datetime.datetime]
        if _free_trial_ends_on is None:
            free_trial_ends_on = None
        else:
            free_trial_ends_on = isoparse(_free_trial_ends_on)

        _updated_at = d.pop("updated_at")
        updated_at: Optional[datetime.datetime]
        if _updated_at is None:
            updated_at = None
        else:
            updated_at = isoparse(_updated_at)

        user_marketplace_purchase = cls(
            billing_cycle=billing_cycle,
            on_free_trial=on_free_trial,
            account=account,
            plan=plan,
            next_billing_date=next_billing_date,
            unit_count=unit_count,
            free_trial_ends_on=free_trial_ends_on,
            updated_at=updated_at,
        )

        user_marketplace_purchase.additional_properties = d
        return user_marketplace_purchase

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
