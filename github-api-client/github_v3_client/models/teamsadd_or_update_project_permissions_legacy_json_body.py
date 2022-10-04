from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.teamsadd_or_update_project_permissions_legacy_json_body_permission import (
    TeamsaddOrUpdateProjectPermissionsLegacyJsonBodyPermission,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamsaddOrUpdateProjectPermissionsLegacyJsonBody")


@attr.s(auto_attribs=True)
class TeamsaddOrUpdateProjectPermissionsLegacyJsonBody:
    """
    Attributes:
        permission (Union[Unset, TeamsaddOrUpdateProjectPermissionsLegacyJsonBodyPermission]): The permission to grant
            to the team for this project. Default: the team's `permission` attribute will be used to determine what
            permission to grant the team on this project. Note that, if you choose not to pass any parameters, you'll need
            to set `Content-Length` to zero when calling this endpoint. For more information, see "[HTTP
            verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)."
    """

    permission: Union[Unset, TeamsaddOrUpdateProjectPermissionsLegacyJsonBodyPermission] = UNSET
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
        permission: Union[Unset, TeamsaddOrUpdateProjectPermissionsLegacyJsonBodyPermission]
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = TeamsaddOrUpdateProjectPermissionsLegacyJsonBodyPermission(_permission)

        teamsadd_or_update_project_permissions_legacy_json_body = cls(
            permission=permission,
        )

        teamsadd_or_update_project_permissions_legacy_json_body.additional_properties = d
        return teamsadd_or_update_project_permissions_legacy_json_body

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
