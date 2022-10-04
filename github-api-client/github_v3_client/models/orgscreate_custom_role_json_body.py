from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.orgscreate_custom_role_json_body_base_role import OrgscreateCustomRoleJsonBodyBaseRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgscreateCustomRoleJsonBody")


@attr.s(auto_attribs=True)
class OrgscreateCustomRoleJsonBody:
    """
    Attributes:
        name (str): The name of the custom role.
        base_role (OrgscreateCustomRoleJsonBodyBaseRole): The system role from which this role inherits permissions.
        permissions (List[str]): A list of additional permissions included in this role.
        description (Union[Unset, str]): A short description about the intended usage of this role or what permissions
            it grants.
    """

    name: str
    base_role: OrgscreateCustomRoleJsonBodyBaseRole
    permissions: List[str]
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        base_role = self.base_role.value

        permissions = self.permissions

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "base_role": base_role,
                "permissions": permissions,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        base_role = OrgscreateCustomRoleJsonBodyBaseRole(d.pop("base_role"))

        permissions = cast(List[str], d.pop("permissions"))

        description = d.pop("description", UNSET)

        orgscreate_custom_role_json_body = cls(
            name=name,
            base_role=base_role,
            permissions=permissions,
            description=description,
        )

        orgscreate_custom_role_json_body.additional_properties = d
        return orgscreate_custom_role_json_body

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
