from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.rate_limit import RateLimit
from ..models.rate_limit_overview_resources import RateLimitOverviewResources

T = TypeVar("T", bound="RateLimitOverview")


@attr.s(auto_attribs=True)
class RateLimitOverview:
    """Rate Limit Overview

    Attributes:
        resources (RateLimitOverviewResources):
        rate (RateLimit):
    """

    resources: RateLimitOverviewResources
    rate: RateLimit
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resources = self.resources.to_dict()

        rate = self.rate.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resources": resources,
                "rate": rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        resources = RateLimitOverviewResources.from_dict(d.pop("resources"))

        rate = RateLimit.from_dict(d.pop("rate"))

        rate_limit_overview = cls(
            resources=resources,
            rate=rate,
        )

        rate_limit_overview.additional_properties = d
        return rate_limit_overview

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
