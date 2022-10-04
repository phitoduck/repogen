from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.actions_cache_usage_by_repository import ActionsCacheUsageByRepository

T = TypeVar("T", bound="ActionsgetActionsCacheUsageByRepoForOrgResponse200")


@attr.s(auto_attribs=True)
class ActionsgetActionsCacheUsageByRepoForOrgResponse200:
    """
    Attributes:
        total_count (int):
        repository_cache_usages (List[ActionsCacheUsageByRepository]):
    """

    total_count: int
    repository_cache_usages: List[ActionsCacheUsageByRepository]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        repository_cache_usages = []
        for repository_cache_usages_item_data in self.repository_cache_usages:
            repository_cache_usages_item = repository_cache_usages_item_data.to_dict()

            repository_cache_usages.append(repository_cache_usages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_count": total_count,
                "repository_cache_usages": repository_cache_usages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_count = d.pop("total_count")

        repository_cache_usages = []
        _repository_cache_usages = d.pop("repository_cache_usages")
        for repository_cache_usages_item_data in _repository_cache_usages:
            repository_cache_usages_item = ActionsCacheUsageByRepository.from_dict(repository_cache_usages_item_data)

            repository_cache_usages.append(repository_cache_usages_item)

        actionsget_actions_cache_usage_by_repo_for_org_response_200 = cls(
            total_count=total_count,
            repository_cache_usages=repository_cache_usages,
        )

        actionsget_actions_cache_usage_by_repo_for_org_response_200.additional_properties = d
        return actionsget_actions_cache_usage_by_repo_for_org_response_200

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
