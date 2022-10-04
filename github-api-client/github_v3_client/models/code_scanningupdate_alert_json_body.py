from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.code_scanning_alert_dismissed_reason import CodeScanningAlertDismissedReason
from ..models.code_scanning_alert_set_state import CodeScanningAlertSetState
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodeScanningupdateAlertJsonBody")


@attr.s(auto_attribs=True)
class CodeScanningupdateAlertJsonBody:
    """
    Attributes:
        state (CodeScanningAlertSetState): Sets the state of the code scanning alert. You must provide
            `dismissed_reason` when you set the state to `dismissed`.
        dismissed_reason (Union[Unset, None, CodeScanningAlertDismissedReason]): **Required when the state is
            dismissed.** The reason for dismissing or closing the alert.
        dismissed_comment (Union[Unset, None, str]): The dismissal comment associated with the dismissal of the alert.
    """

    state: CodeScanningAlertSetState
    dismissed_reason: Union[Unset, None, CodeScanningAlertDismissedReason] = UNSET
    dismissed_comment: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state.value

        dismissed_reason: Union[Unset, None, str] = UNSET
        if not isinstance(self.dismissed_reason, Unset):
            dismissed_reason = self.dismissed_reason.value if self.dismissed_reason else None

        dismissed_comment = self.dismissed_comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        state = CodeScanningAlertSetState(d.pop("state"))

        _dismissed_reason = d.pop("dismissed_reason", UNSET)
        dismissed_reason: Union[Unset, None, CodeScanningAlertDismissedReason]
        if _dismissed_reason is None:
            dismissed_reason = None
        elif isinstance(_dismissed_reason, Unset):
            dismissed_reason = UNSET
        else:
            dismissed_reason = CodeScanningAlertDismissedReason(_dismissed_reason)

        dismissed_comment = d.pop("dismissed_comment", UNSET)

        code_scanningupdate_alert_json_body = cls(
            state=state,
            dismissed_reason=dismissed_reason,
            dismissed_comment=dismissed_comment,
        )

        code_scanningupdate_alert_json_body.additional_properties = d
        return code_scanningupdate_alert_json_body

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
