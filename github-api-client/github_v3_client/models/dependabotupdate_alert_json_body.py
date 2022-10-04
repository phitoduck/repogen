from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.dependabotupdate_alert_json_body_dismissed_reason import DependabotupdateAlertJsonBodyDismissedReason
from ..models.dependabotupdate_alert_json_body_state import DependabotupdateAlertJsonBodyState
from ..types import UNSET, Unset

T = TypeVar("T", bound="DependabotupdateAlertJsonBody")


@attr.s(auto_attribs=True)
class DependabotupdateAlertJsonBody:
    """
    Attributes:
        state (DependabotupdateAlertJsonBodyState): The state of the Dependabot alert.
            A `dismissed_reason` must be provided when setting the state to `dismissed`.
        dismissed_reason (Union[Unset, DependabotupdateAlertJsonBodyDismissedReason]): **Required when `state` is
            `dismissed`.** A reason for dismissing the alert.
        dismissed_comment (Union[Unset, str]): An optional comment associated with dismissing the alert.
    """

    state: DependabotupdateAlertJsonBodyState
    dismissed_reason: Union[Unset, DependabotupdateAlertJsonBodyDismissedReason] = UNSET
    dismissed_comment: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        state = self.state.value

        dismissed_reason: Union[Unset, str] = UNSET
        if not isinstance(self.dismissed_reason, Unset):
            dismissed_reason = self.dismissed_reason.value

        dismissed_comment = self.dismissed_comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "state": state,
            }
        )
        if dismissed_reason is not UNSET:
            field_dict["dismissed_reason"] = dismissed_reason
        if dismissed_comment is not UNSET:
            field_dict["dismissed_comment"] = dismissed_comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state = DependabotupdateAlertJsonBodyState(d.pop("state"))

        _dismissed_reason = d.pop("dismissed_reason", UNSET)
        dismissed_reason: Union[Unset, DependabotupdateAlertJsonBodyDismissedReason]
        if isinstance(_dismissed_reason, Unset):
            dismissed_reason = UNSET
        else:
            dismissed_reason = DependabotupdateAlertJsonBodyDismissedReason(_dismissed_reason)

        dismissed_comment = d.pop("dismissed_comment", UNSET)

        dependabotupdate_alert_json_body = cls(
            state=state,
            dismissed_reason=dismissed_reason,
            dismissed_comment=dismissed_comment,
        )

        return dependabotupdate_alert_json_body
