from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reposupdate_invitation_json_body_permissions import ReposupdateInvitationJsonBodyPermissions
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdateInvitationJsonBody")


@attr.s(auto_attribs=True)
class ReposupdateInvitationJsonBody:
    """
    Attributes:
        permissions (Union[Unset, ReposupdateInvitationJsonBodyPermissions]): The permissions that the associated user
            will have on the repository. Valid values are `read`, `write`, `maintain`, `triage`, and `admin`.
    """

    permissions: Union[Unset, ReposupdateInvitationJsonBodyPermissions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permissions: Union[Unset, str] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, ReposupdateInvitationJsonBodyPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = ReposupdateInvitationJsonBodyPermissions(_permissions)

        reposupdate_invitation_json_body = cls(
            permissions=permissions,
        )

        reposupdate_invitation_json_body.additional_properties = d
        return reposupdate_invitation_json_body

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
