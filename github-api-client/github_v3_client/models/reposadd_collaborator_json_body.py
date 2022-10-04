from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposaddCollaboratorJsonBody")


@attr.s(auto_attribs=True)
class ReposaddCollaboratorJsonBody:
    """
    Attributes:
        permission (Union[Unset, str]): The permission to grant the collaborator. **Only valid on organization-owned
            repositories.** We accept the following permissions to be set: `pull`, `triage`, `push`, `maintain`, `admin` and
            you can also specify a custom repository role name, if the owning organization has defined any. Default: 'push'.
    """

    permission: Union[Unset, str] = "push"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permission = self.permission

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        permission = d.pop("permission", UNSET)

        reposadd_collaborator_json_body = cls(
            permission=permission,
        )

        reposadd_collaborator_json_body.additional_properties = d
        return reposadd_collaborator_json_body

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
