from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="OrgMembershipPermissions")


@attr.s(auto_attribs=True)
class OrgMembershipPermissions:
    """
    Attributes:
        can_create_repository (bool):
    """

    can_create_repository: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        can_create_repository = self.can_create_repository

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "can_create_repository": can_create_repository,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        can_create_repository = d.pop("can_create_repository")

        org_membership_permissions = cls(
            can_create_repository=can_create_repository,
        )

        org_membership_permissions.additional_properties = d
        return org_membership_permissions

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
