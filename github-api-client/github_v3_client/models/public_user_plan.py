from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PublicUserPlan")


@attr.s(auto_attribs=True)
class PublicUserPlan:
    """
    Attributes:
        collaborators (int):
        name (str):
        space (int):
        private_repos (int):
    """

    collaborators: int
    name: str
    space: int
    private_repos: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        collaborators = self.collaborators
        name = self.name
        space = self.space
        private_repos = self.private_repos

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collaborators": collaborators,
                "name": name,
                "space": space,
                "private_repos": private_repos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        collaborators = d.pop("collaborators")

        name = d.pop("name")

        space = d.pop("space")

        private_repos = d.pop("private_repos")

        public_user_plan = cls(
            collaborators=collaborators,
            name=name,
            space=space,
            private_repos=private_repos,
        )

        public_user_plan.additional_properties = d
        return public_user_plan

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
