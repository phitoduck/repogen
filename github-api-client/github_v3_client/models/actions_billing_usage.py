from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.actions_billing_usage_minutes_used_breakdown import ActionsBillingUsageMinutesUsedBreakdown

T = TypeVar("T", bound="ActionsBillingUsage")


@attr.s(auto_attribs=True)
class ActionsBillingUsage:
    """
    Attributes:
        total_minutes_used (int): The sum of the free and paid GitHub Actions minutes used.
        total_paid_minutes_used (int): The total paid GitHub Actions minutes used.
        included_minutes (int): The amount of free GitHub Actions minutes available.
        minutes_used_breakdown (ActionsBillingUsageMinutesUsedBreakdown):
    """

    total_minutes_used: int
    total_paid_minutes_used: int
    included_minutes: int
    minutes_used_breakdown: ActionsBillingUsageMinutesUsedBreakdown
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_minutes_used = self.total_minutes_used
        total_paid_minutes_used = self.total_paid_minutes_used
        included_minutes = self.included_minutes
        minutes_used_breakdown = self.minutes_used_breakdown.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_minutes_used": total_minutes_used,
                "total_paid_minutes_used": total_paid_minutes_used,
                "included_minutes": included_minutes,
                "minutes_used_breakdown": minutes_used_breakdown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_minutes_used = d.pop("total_minutes_used")

        total_paid_minutes_used = d.pop("total_paid_minutes_used")

        included_minutes = d.pop("included_minutes")

        minutes_used_breakdown = ActionsBillingUsageMinutesUsedBreakdown.from_dict(d.pop("minutes_used_breakdown"))

        actions_billing_usage = cls(
            total_minutes_used=total_minutes_used,
            total_paid_minutes_used=total_paid_minutes_used,
            included_minutes=included_minutes,
            minutes_used_breakdown=minutes_used_breakdown,
        )

        actions_billing_usage.additional_properties = d
        return actions_billing_usage

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
