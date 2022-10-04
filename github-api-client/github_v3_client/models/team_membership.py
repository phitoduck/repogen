from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.team_membership_role import TeamMembershipRole
from ..models.team_membership_state import TeamMembershipState

T = TypeVar("T", bound="TeamMembership")


@attr.s(auto_attribs=True)
class TeamMembership:
    """Team Membership

    Attributes:
        url (str):
        role (TeamMembershipRole): The role of the user in the team. Default: TeamMembershipRole.MEMBER. Example:
            member.
        state (TeamMembershipState): The state of the user's membership in the team.
    """

    url: str
    state: TeamMembershipState
    role: TeamMembershipRole = TeamMembershipRole.MEMBER
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        role = self.role.value

        state = self.state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "role": role,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        role = TeamMembershipRole(d.pop("role"))

        state = TeamMembershipState(d.pop("state"))

        team_membership = cls(
            url=url,
            role=role,
            state=state,
        )

        team_membership.additional_properties = d
        return team_membership

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
