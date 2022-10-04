from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.orgscreate_invitation_json_body_role import OrgscreateInvitationJsonBodyRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgscreateInvitationJsonBody")


@attr.s(auto_attribs=True)
class OrgscreateInvitationJsonBody:
    """
    Attributes:
        invitee_id (Union[Unset, int]): **Required unless you provide `email`**. GitHub user ID for the person you are
            inviting.
        email (Union[Unset, str]): **Required unless you provide `invitee_id`**. Email address of the person you are
            inviting, which can be an existing GitHub user.
        role (Union[Unset, OrgscreateInvitationJsonBodyRole]): The role for the new member.
            \* `admin` - Organization owners with full administrative rights to the organization and complete access to all
            repositories and teams.
            \* `direct_member` - Non-owner organization members with ability to see other members and join teams by
            invitation.
            \* `billing_manager` - Non-owner organization members with ability to manage the billing settings of your
            organization. Default: OrgscreateInvitationJsonBodyRole.DIRECT_MEMBER.
        team_ids (Union[Unset, List[int]]): Specify IDs for the teams you want to invite new members to.
    """

    invitee_id: Union[Unset, int] = UNSET
    email: Union[Unset, str] = UNSET
    role: Union[Unset, OrgscreateInvitationJsonBodyRole] = OrgscreateInvitationJsonBodyRole.DIRECT_MEMBER
    team_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invitee_id = self.invitee_id
        email = self.email
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        team_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.team_ids, Unset):
            team_ids = self.team_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invitee_id is not UNSET:
            field_dict["invitee_id"] = invitee_id
        if email is not UNSET:
            field_dict["email"] = email
        if role is not UNSET:
            field_dict["role"] = role
        if team_ids is not UNSET:
            field_dict["team_ids"] = team_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invitee_id = d.pop("invitee_id", UNSET)

        email = d.pop("email", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, OrgscreateInvitationJsonBodyRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = OrgscreateInvitationJsonBodyRole(_role)

        team_ids = cast(List[int], d.pop("team_ids", UNSET))

        orgscreate_invitation_json_body = cls(
            invitee_id=invitee_id,
            email=email,
            role=role,
            team_ids=team_ids,
        )

        orgscreate_invitation_json_body.additional_properties = d
        return orgscreate_invitation_json_body

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
