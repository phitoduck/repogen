from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationFullPlan")


@attr.s(auto_attribs=True)
class OrganizationFullPlan:
    """
    Attributes:
        name (str):
        space (int):
        private_repos (int):
        filled_seats (Union[Unset, int]):
        seats (Union[Unset, int]):
    """

    name: str
    space: int
    private_repos: int
    filled_seats: Union[Unset, int] = UNSET
    seats: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        space = self.space
        private_repos = self.private_repos
        filled_seats = self.filled_seats
        seats = self.seats

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "space": space,
                "private_repos": private_repos,
            }
        )
        if filled_seats is not UNSET:
            field_dict["filled_seats"] = filled_seats
        if seats is not UNSET:
            field_dict["seats"] = seats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        space = d.pop("space")

        private_repos = d.pop("private_repos")

        filled_seats = d.pop("filled_seats", UNSET)

        seats = d.pop("seats", UNSET)

        organization_full_plan = cls(
            name=name,
            space=space,
            private_repos=private_repos,
            filled_seats=filled_seats,
            seats=seats,
        )

        organization_full_plan.additional_properties = d
        return organization_full_plan

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
