from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.advanced_security_active_committers_repository import AdvancedSecurityActiveCommittersRepository
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvancedSecurityActiveCommitters")


@attr.s(auto_attribs=True)
class AdvancedSecurityActiveCommitters:
    """
    Attributes:
        repositories (List[AdvancedSecurityActiveCommittersRepository]):
        total_advanced_security_committers (Union[Unset, int]):  Example: 25.
        total_count (Union[Unset, int]):  Example: 2.
    """

    repositories: List[AdvancedSecurityActiveCommittersRepository]
    total_advanced_security_committers: Union[Unset, int] = UNSET
    total_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repositories = []
        for repositories_item_data in self.repositories:
            repositories_item = repositories_item_data.to_dict()

            repositories.append(repositories_item)

        total_advanced_security_committers = self.total_advanced_security_committers
        total_count = self.total_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repositories": repositories,
            }
        )
        if total_advanced_security_committers is not UNSET:
            field_dict["total_advanced_security_committers"] = total_advanced_security_committers
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        repositories = []
        _repositories = d.pop("repositories")
        for repositories_item_data in _repositories:
            repositories_item = AdvancedSecurityActiveCommittersRepository.from_dict(repositories_item_data)

            repositories.append(repositories_item)

        total_advanced_security_committers = d.pop("total_advanced_security_committers", UNSET)

        total_count = d.pop("total_count", UNSET)

        advanced_security_active_committers = cls(
            repositories=repositories,
            total_advanced_security_committers=total_advanced_security_committers,
            total_count=total_count,
        )

        advanced_security_active_committers.additional_properties = d
        return advanced_security_active_committers

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
