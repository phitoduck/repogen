from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.marketplace_listing_plan import MarketplaceListingPlan
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketplacePurchaseMarketplacePendingChange")


@attr.s(auto_attribs=True)
class MarketplacePurchaseMarketplacePendingChange:
    """
    Attributes:
        is_installed (Union[Unset, bool]):
        effective_date (Union[Unset, str]):
        unit_count (Union[Unset, None, int]):
        id (Union[Unset, int]):
        plan (Union[Unset, MarketplaceListingPlan]): Marketplace Listing Plan
    """

    is_installed: Union[Unset, bool] = UNSET
    effective_date: Union[Unset, str] = UNSET
    unit_count: Union[Unset, None, int] = UNSET
    id: Union[Unset, int] = UNSET
    plan: Union[Unset, MarketplaceListingPlan] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_installed = self.is_installed
        effective_date = self.effective_date
        unit_count = self.unit_count
        id = self.id
        plan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_installed is not UNSET:
            field_dict["is_installed"] = is_installed
        if effective_date is not UNSET:
            field_dict["effective_date"] = effective_date
        if unit_count is not UNSET:
            field_dict["unit_count"] = unit_count
        if id is not UNSET:
            field_dict["id"] = id
        if plan is not UNSET:
            field_dict["plan"] = plan

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_installed = d.pop("is_installed", UNSET)

        effective_date = d.pop("effective_date", UNSET)

        unit_count = d.pop("unit_count", UNSET)

        id = d.pop("id", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, MarketplaceListingPlan]
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = MarketplaceListingPlan.from_dict(_plan)

        marketplace_purchase_marketplace_pending_change = cls(
            is_installed=is_installed,
            effective_date=effective_date,
            unit_count=unit_count,
            id=id,
            plan=plan,
        )

        marketplace_purchase_marketplace_pending_change.additional_properties = d
        return marketplace_purchase_marketplace_pending_change

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
