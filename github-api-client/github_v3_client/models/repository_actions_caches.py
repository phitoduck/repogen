from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.repository_actions_caches_actions_caches_item import RepositoryActionsCachesActionsCachesItem

T = TypeVar("T", bound="RepositoryActionsCaches")


@attr.s(auto_attribs=True)
class RepositoryActionsCaches:
    """Repository actions caches

    Attributes:
        total_count (int): Total number of caches Example: 2.
        actions_caches (List[RepositoryActionsCachesActionsCachesItem]): Array of caches
    """

    total_count: int
    actions_caches: List[RepositoryActionsCachesActionsCachesItem]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        actions_caches = []
        for actions_caches_item_data in self.actions_caches:
            actions_caches_item = actions_caches_item_data.to_dict()

            actions_caches.append(actions_caches_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_count": total_count,
                "actions_caches": actions_caches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_count = d.pop("total_count")

        actions_caches = []
        _actions_caches = d.pop("actions_caches")
        for actions_caches_item_data in _actions_caches:
            actions_caches_item = RepositoryActionsCachesActionsCachesItem.from_dict(actions_caches_item_data)

            actions_caches.append(actions_caches_item)

        repository_actions_caches = cls(
            total_count=total_count,
            actions_caches=actions_caches,
        )

        repository_actions_caches.additional_properties = d
        return repository_actions_caches

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
