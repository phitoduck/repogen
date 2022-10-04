from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.orgsupdate_custom_role_json_body_base_role import OrgsupdateCustomRoleJsonBodyBaseRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgsupdateCustomRoleJsonBody")


@attr.s(auto_attribs=True)
class OrgsupdateCustomRoleJsonBody:
    """
    Attributes:
        name (Union[Unset, str]): The name of the custom role.
        description (Union[Unset, str]): A short description about who this role is for or what permissions it grants.
        base_role (Union[Unset, OrgsupdateCustomRoleJsonBodyBaseRole]): The system role from which this role inherits
            permissions.
        permissions (Union[Unset, List[str]]): A list of additional permissions included in this role. If specified,
            these permissions will replace any currently set on the role.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    base_role: Union[Unset, OrgsupdateCustomRoleJsonBodyBaseRole] = UNSET
    permissions: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        base_role: Union[Unset, str] = UNSET
        if not isinstance(self.base_role, Unset):
            base_role = self.base_role.value

        permissions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if base_role is not UNSET:
            field_dict["base_role"] = base_role
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _base_role = d.pop("base_role", UNSET)
        base_role: Union[Unset, OrgsupdateCustomRoleJsonBodyBaseRole]
        if isinstance(_base_role, Unset):
            base_role = UNSET
        else:
            base_role = OrgsupdateCustomRoleJsonBodyBaseRole(_base_role)

        permissions = cast(List[str], d.pop("permissions", UNSET))

        orgsupdate_custom_role_json_body = cls(
            name=name,
            description=description,
            base_role=base_role,
            permissions=permissions,
        )

        orgsupdate_custom_role_json_body.additional_properties = d
        return orgsupdate_custom_role_json_body

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
