from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.teamsadd_or_update_repo_permissions_legacy_json_body_permission import (
    TeamsaddOrUpdateRepoPermissionsLegacyJsonBodyPermission,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamsaddOrUpdateRepoPermissionsLegacyJsonBody")


@attr.s(auto_attribs=True)
class TeamsaddOrUpdateRepoPermissionsLegacyJsonBody:
    """
    Attributes:
        permission (Union[Unset, TeamsaddOrUpdateRepoPermissionsLegacyJsonBodyPermission]): The permission to grant the
            team on this repository. If no permission is specified, the team's `permission` attribute will be used to
            determine what permission to grant the team on this repository.
    """

    permission: Union[Unset, TeamsaddOrUpdateRepoPermissionsLegacyJsonBodyPermission] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permission: Union[Unset, str] = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _permission = d.pop("permission", UNSET)
        permission: Union[Unset, TeamsaddOrUpdateRepoPermissionsLegacyJsonBodyPermission]
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = TeamsaddOrUpdateRepoPermissionsLegacyJsonBodyPermission(_permission)

        teamsadd_or_update_repo_permissions_legacy_json_body = cls(
            permission=permission,
        )

        teamsadd_or_update_repo_permissions_legacy_json_body.additional_properties = d
        return teamsadd_or_update_repo_permissions_legacy_json_body

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
