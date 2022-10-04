from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ActionsCacheUsageOrgEnterprise")


@attr.s(auto_attribs=True)
class ActionsCacheUsageOrgEnterprise:
    """
    Attributes:
        total_active_caches_count (int): The count of active caches across all repositories of an enterprise or an
            organization.
        total_active_caches_size_in_bytes (int): The total size in bytes of all active cache items across all
            repositories of an enterprise or an organization.
    """

    total_active_caches_count: int
    total_active_caches_size_in_bytes: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_active_caches_count = self.total_active_caches_count
        total_active_caches_size_in_bytes = self.total_active_caches_size_in_bytes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_active_caches_count": total_active_caches_count,
                "total_active_caches_size_in_bytes": total_active_caches_size_in_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_active_caches_count = d.pop("total_active_caches_count")

        total_active_caches_size_in_bytes = d.pop("total_active_caches_size_in_bytes")

        actions_cache_usage_org_enterprise = cls(
            total_active_caches_count=total_active_caches_count,
            total_active_caches_size_in_bytes=total_active_caches_size_in_bytes,
        )

        actions_cache_usage_org_enterprise.additional_properties = d
        return actions_cache_usage_org_enterprise

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
