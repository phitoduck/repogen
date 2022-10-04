from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.orgsset_membership_for_user_json_body_role import OrgssetMembershipForUserJsonBodyRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgssetMembershipForUserJsonBody")


@attr.s(auto_attribs=True)
class OrgssetMembershipForUserJsonBody:
    """
    Attributes:
        role (Union[Unset, OrgssetMembershipForUserJsonBodyRole]): The role to give the user in the organization. Can be
            one of:
            \* `admin` - The user will become an owner of the organization.
            \* `member` - The user will become a non-owner member of the organization. Default:
            OrgssetMembershipForUserJsonBodyRole.MEMBER.
    """

    role: Union[Unset, OrgssetMembershipForUserJsonBodyRole] = OrgssetMembershipForUserJsonBodyRole.MEMBER
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _role = d.pop("role", UNSET)
        role: Union[Unset, OrgssetMembershipForUserJsonBodyRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = OrgssetMembershipForUserJsonBodyRole(_role)

        orgsset_membership_for_user_json_body = cls(
            role=role,
        )

        orgsset_membership_for_user_json_body.additional_properties = d
        return orgsset_membership_for_user_json_body

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
