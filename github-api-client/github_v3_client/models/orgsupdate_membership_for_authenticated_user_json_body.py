from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.orgsupdate_membership_for_authenticated_user_json_body_state import (
    OrgsupdateMembershipForAuthenticatedUserJsonBodyState,
)

T = TypeVar("T", bound="OrgsupdateMembershipForAuthenticatedUserJsonBody")


@attr.s(auto_attribs=True)
class OrgsupdateMembershipForAuthenticatedUserJsonBody:
    """
    Attributes:
        state (OrgsupdateMembershipForAuthenticatedUserJsonBodyState): The state that the membership should be in. Only
            `"active"` will be accepted.
    """

    state: OrgsupdateMembershipForAuthenticatedUserJsonBodyState
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state = OrgsupdateMembershipForAuthenticatedUserJsonBodyState(d.pop("state"))

        orgsupdate_membership_for_authenticated_user_json_body = cls(
            state=state,
        )

        orgsupdate_membership_for_authenticated_user_json_body.additional_properties = d
        return orgsupdate_membership_for_authenticated_user_json_body

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
