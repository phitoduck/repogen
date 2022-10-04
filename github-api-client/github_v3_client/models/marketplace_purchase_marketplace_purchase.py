from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.marketplace_listing_plan import MarketplaceListingPlan
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketplacePurchaseMarketplacePurchase")


@attr.s(auto_attribs=True)
class MarketplacePurchaseMarketplacePurchase:
    """
    Attributes:
        billing_cycle (Union[Unset, str]):
        next_billing_date (Union[Unset, None, str]):
        is_installed (Union[Unset, bool]):
        unit_count (Union[Unset, None, int]):
        on_free_trial (Union[Unset, bool]):
        free_trial_ends_on (Union[Unset, None, str]):
        updated_at (Union[Unset, str]):
        plan (Union[Unset, MarketplaceListingPlan]): Marketplace Listing Plan
    """

    billing_cycle: Union[Unset, str] = UNSET
    next_billing_date: Union[Unset, None, str] = UNSET
    is_installed: Union[Unset, bool] = UNSET
    unit_count: Union[Unset, None, int] = UNSET
    on_free_trial: Union[Unset, bool] = UNSET
    free_trial_ends_on: Union[Unset, None, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    plan: Union[Unset, MarketplaceListingPlan] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billing_cycle = self.billing_cycle
        next_billing_date = self.next_billing_date
        is_installed = self.is_installed
        unit_count = self.unit_count
        on_free_trial = self.on_free_trial
        free_trial_ends_on = self.free_trial_ends_on
        updated_at = self.updated_at
        plan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_cycle is not UNSET:
            field_dict["billing_cycle"] = billing_cycle
        if next_billing_date is not UNSET:
            field_dict["next_billing_date"] = next_billing_date
        if is_installed is not UNSET:
            field_dict["is_installed"] = is_installed
        if unit_count is not UNSET:
            field_dict["unit_count"] = unit_count
        if on_free_trial is not UNSET:
            field_dict["on_free_trial"] = on_free_trial
        if free_trial_ends_on is not UNSET:
            field_dict["free_trial_ends_on"] = free_trial_ends_on
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if plan is not UNSET:
            field_dict["plan"] = plan

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        billing_cycle = d.pop("billing_cycle", UNSET)

        next_billing_date = d.pop("next_billing_date", UNSET)

        is_installed = d.pop("is_installed", UNSET)

        unit_count = d.pop("unit_count", UNSET)

        on_free_trial = d.pop("on_free_trial", UNSET)

        free_trial_ends_on = d.pop("free_trial_ends_on", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, MarketplaceListingPlan]
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = MarketplaceListingPlan.from_dict(_plan)

        marketplace_purchase_marketplace_purchase = cls(
            billing_cycle=billing_cycle,
            next_billing_date=next_billing_date,
            is_installed=is_installed,
            unit_count=unit_count,
            on_free_trial=on_free_trial,
            free_trial_ends_on=free_trial_ends_on,
            updated_at=updated_at,
            plan=plan,
        )

        marketplace_purchase_marketplace_purchase.additional_properties = d
        return marketplace_purchase_marketplace_purchase

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
