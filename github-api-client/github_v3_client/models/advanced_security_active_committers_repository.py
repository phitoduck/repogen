from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.advanced_security_active_committers_user import AdvancedSecurityActiveCommittersUser

T = TypeVar("T", bound="AdvancedSecurityActiveCommittersRepository")


@attr.s(auto_attribs=True)
class AdvancedSecurityActiveCommittersRepository:
    """
    Attributes:
        name (str):  Example: octocat/Hello-World.
        advanced_security_committers (int):  Example: 25.
        advanced_security_committers_breakdown (List[AdvancedSecurityActiveCommittersUser]):
    """

    name: str
    advanced_security_committers: int
    advanced_security_committers_breakdown: List[AdvancedSecurityActiveCommittersUser]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        advanced_security_committers = self.advanced_security_committers
        advanced_security_committers_breakdown = []
        for advanced_security_committers_breakdown_item_data in self.advanced_security_committers_breakdown:
            advanced_security_committers_breakdown_item = advanced_security_committers_breakdown_item_data.to_dict()

            advanced_security_committers_breakdown.append(advanced_security_committers_breakdown_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "advanced_security_committers": advanced_security_committers,
                "advanced_security_committers_breakdown": advanced_security_committers_breakdown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        advanced_security_committers = d.pop("advanced_security_committers")

        advanced_security_committers_breakdown = []
        _advanced_security_committers_breakdown = d.pop("advanced_security_committers_breakdown")
        for advanced_security_committers_breakdown_item_data in _advanced_security_committers_breakdown:
            advanced_security_committers_breakdown_item = AdvancedSecurityActiveCommittersUser.from_dict(
                advanced_security_committers_breakdown_item_data
            )

            advanced_security_committers_breakdown.append(advanced_security_committers_breakdown_item)

        advanced_security_active_committers_repository = cls(
            name=name,
            advanced_security_committers=advanced_security_committers,
            advanced_security_committers_breakdown=advanced_security_committers_breakdown,
        )

        advanced_security_active_committers_repository.additional_properties = d
        return advanced_security_active_committers_repository

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
