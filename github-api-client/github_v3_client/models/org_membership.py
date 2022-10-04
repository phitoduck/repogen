from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.org_membership_permissions import OrgMembershipPermissions
from ..models.org_membership_role import OrgMembershipRole
from ..models.org_membership_state import OrgMembershipState
from ..models.organization_simple import OrganizationSimple
from ..models.simple_user import SimpleUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgMembership")


@attr.s(auto_attribs=True)
class OrgMembership:
    """Org Membership

    Attributes:
        url (str):  Example: https://api.github.com/orgs/octocat/memberships/defunkt.
        state (OrgMembershipState): The state of the member in the organization. The `pending` state indicates the user
            has not yet accepted an invitation. Example: active.
        role (OrgMembershipRole): The user's membership type in the organization. Example: admin.
        organization_url (str):  Example: https://api.github.com/orgs/octocat.
        organization (OrganizationSimple): Organization Simple
        user (Optional[SimpleUser]): Simple User
        permissions (Union[Unset, OrgMembershipPermissions]):
    """

    url: str
    state: OrgMembershipState
    role: OrgMembershipRole
    organization_url: str
    organization: OrganizationSimple
    user: Optional[SimpleUser]
    permissions: Union[Unset, OrgMembershipPermissions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        state = self.state.value

        role = self.role.value

        organization_url = self.organization_url
        organization = self.organization.to_dict()

        user = self.user.to_dict() if self.user else None

        permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "state": state,
                "role": role,
                "organization_url": organization_url,
                "organization": organization,
                "user": user,
            }
        )
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        state = OrgMembershipState(d.pop("state"))

        role = OrgMembershipRole(d.pop("role"))

        organization_url = d.pop("organization_url")

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        _user = d.pop("user")
        user: Optional[SimpleUser]
        if _user is None:
            user = None
        else:
            user = SimpleUser.from_dict(_user)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, OrgMembershipPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = OrgMembershipPermissions.from_dict(_permissions)

        org_membership = cls(
            url=url,
            state=state,
            role=role,
            organization_url=organization_url,
            organization=organization,
            user=user,
            permissions=permissions,
        )

        org_membership.additional_properties = d
        return org_membership

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
