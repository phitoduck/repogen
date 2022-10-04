from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TeamPermissions")


@attr.s(auto_attribs=True)
class TeamPermissions:
    """
    Attributes:
        pull (bool):
        triage (bool):
        push (bool):
        maintain (bool):
        admin (bool):
    """

    pull: bool
    triage: bool
    push: bool
    maintain: bool
    admin: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pull = self.pull
        triage = self.triage
        push = self.push
        maintain = self.maintain
        admin = self.admin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pull": pull,
                "triage": triage,
                "push": push,
                "maintain": maintain,
                "admin": admin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pull = d.pop("pull")

        triage = d.pop("triage")

        push = d.pop("push")

        maintain = d.pop("maintain")

        admin = d.pop("admin")

        team_permissions = cls(
            pull=pull,
            triage=triage,
            push=push,
            maintain=maintain,
            admin=admin,
        )

        team_permissions.additional_properties = d
        return team_permissions

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
