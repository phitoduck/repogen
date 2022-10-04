from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PackagesBillingUsage")


@attr.s(auto_attribs=True)
class PackagesBillingUsage:
    """
    Attributes:
        total_gigabytes_bandwidth_used (int): Sum of the free and paid storage space (GB) for GitHuub Packages.
        total_paid_gigabytes_bandwidth_used (int): Total paid storage space (GB) for GitHuub Packages.
        included_gigabytes_bandwidth (int): Free storage space (GB) for GitHub Packages.
    """

    total_gigabytes_bandwidth_used: int
    total_paid_gigabytes_bandwidth_used: int
    included_gigabytes_bandwidth: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_gigabytes_bandwidth_used = self.total_gigabytes_bandwidth_used
        total_paid_gigabytes_bandwidth_used = self.total_paid_gigabytes_bandwidth_used
        included_gigabytes_bandwidth = self.included_gigabytes_bandwidth

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_gigabytes_bandwidth_used": total_gigabytes_bandwidth_used,
                "total_paid_gigabytes_bandwidth_used": total_paid_gigabytes_bandwidth_used,
                "included_gigabytes_bandwidth": included_gigabytes_bandwidth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_gigabytes_bandwidth_used = d.pop("total_gigabytes_bandwidth_used")

        total_paid_gigabytes_bandwidth_used = d.pop("total_paid_gigabytes_bandwidth_used")

        included_gigabytes_bandwidth = d.pop("included_gigabytes_bandwidth")

        packages_billing_usage = cls(
            total_gigabytes_bandwidth_used=total_gigabytes_bandwidth_used,
            total_paid_gigabytes_bandwidth_used=total_paid_gigabytes_bandwidth_used,
            included_gigabytes_bandwidth=included_gigabytes_bandwidth,
        )

        packages_billing_usage.additional_properties = d
        return packages_billing_usage

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
