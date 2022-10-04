from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ActionsCacheUsageByRepository")


@attr.s(auto_attribs=True)
class ActionsCacheUsageByRepository:
    """GitHub Actions Cache Usage by repository.

    Attributes:
        full_name (str): The repository owner and name for the cache usage being shown. Example: octo-org/Hello-World.
        active_caches_size_in_bytes (int): The sum of the size in bytes of all the active cache items in the repository.
            Example: 2322142.
        active_caches_count (int): The number of active caches in the repository. Example: 3.
    """

    full_name: str
    active_caches_size_in_bytes: int
    active_caches_count: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        full_name = self.full_name
        active_caches_size_in_bytes = self.active_caches_size_in_bytes
        active_caches_count = self.active_caches_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "full_name": full_name,
                "active_caches_size_in_bytes": active_caches_size_in_bytes,
                "active_caches_count": active_caches_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        full_name = d.pop("full_name")

        active_caches_size_in_bytes = d.pop("active_caches_size_in_bytes")

        active_caches_count = d.pop("active_caches_count")

        actions_cache_usage_by_repository = cls(
            full_name=full_name,
            active_caches_size_in_bytes=active_caches_size_in_bytes,
            active_caches_count=active_caches_count,
        )

        actions_cache_usage_by_repository.additional_properties = d
        return actions_cache_usage_by_repository

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
