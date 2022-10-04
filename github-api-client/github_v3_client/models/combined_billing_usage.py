from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CombinedBillingUsage")


@attr.s(auto_attribs=True)
class CombinedBillingUsage:
    """
    Attributes:
        days_left_in_billing_cycle (int): Numbers of days left in billing cycle.
        estimated_paid_storage_for_month (int): Estimated storage space (GB) used in billing cycle.
        estimated_storage_for_month (int): Estimated sum of free and paid storage space (GB) used in billing cycle.
    """

    days_left_in_billing_cycle: int
    estimated_paid_storage_for_month: int
    estimated_storage_for_month: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        days_left_in_billing_cycle = self.days_left_in_billing_cycle
        estimated_paid_storage_for_month = self.estimated_paid_storage_for_month
        estimated_storage_for_month = self.estimated_storage_for_month

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "days_left_in_billing_cycle": days_left_in_billing_cycle,
                "estimated_paid_storage_for_month": estimated_paid_storage_for_month,
                "estimated_storage_for_month": estimated_storage_for_month,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        days_left_in_billing_cycle = d.pop("days_left_in_billing_cycle")

        estimated_paid_storage_for_month = d.pop("estimated_paid_storage_for_month")

        estimated_storage_for_month = d.pop("estimated_storage_for_month")

        combined_billing_usage = cls(
            days_left_in_billing_cycle=days_left_in_billing_cycle,
            estimated_paid_storage_for_month=estimated_paid_storage_for_month,
            estimated_storage_for_month=estimated_storage_for_month,
        )

        combined_billing_usage.additional_properties = d
        return combined_billing_usage

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
