from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollaboratorPermissions")


@attr.s(auto_attribs=True)
class CollaboratorPermissions:
    """
    Attributes:
        pull (bool):
        push (bool):
        admin (bool):
        triage (Union[Unset, bool]):
        maintain (Union[Unset, bool]):
    """

    pull: bool
    push: bool
    admin: bool
    triage: Union[Unset, bool] = UNSET
    maintain: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pull = self.pull
        push = self.push
        admin = self.admin
        triage = self.triage
        maintain = self.maintain

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pull": pull,
                "push": push,
                "admin": admin,
            }
        )
        if triage is not UNSET:
            field_dict["triage"] = triage
        if maintain is not UNSET:
            field_dict["maintain"] = maintain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pull = d.pop("pull")

        push = d.pop("push")

        admin = d.pop("admin")

        triage = d.pop("triage", UNSET)

        maintain = d.pop("maintain", UNSET)

        collaborator_permissions = cls(
            pull=pull,
            push=push,
            admin=admin,
            triage=triage,
            maintain=maintain,
        )

        collaborator_permissions.additional_properties = d
        return collaborator_permissions

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
