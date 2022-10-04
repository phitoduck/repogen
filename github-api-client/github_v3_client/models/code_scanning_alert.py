import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.code_scanning_alert_dismissed_reason import CodeScanningAlertDismissedReason
from ..models.code_scanning_alert_instance import CodeScanningAlertInstance
from ..models.code_scanning_alert_rule import CodeScanningAlertRule
from ..models.code_scanning_alert_state import CodeScanningAlertState
from ..models.code_scanning_analysis_tool import CodeScanningAnalysisTool
from ..models.simple_user import SimpleUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodeScanningAlert")


@attr.s(auto_attribs=True)
class CodeScanningAlert:
    """
    Attributes:
        number (int): The security alert number.
        created_at (datetime.datetime): The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
        url (str): The REST API URL of the alert resource.
        html_url (str): The GitHub URL of the alert resource.
        instances_url (str): The REST API URL for fetching the list of instances for an alert.
        state (CodeScanningAlertState): State of a code scanning alert.
        rule (CodeScanningAlertRule):
        tool (CodeScanningAnalysisTool):
        most_recent_instance (CodeScanningAlertInstance):
        updated_at (Union[Unset, datetime.datetime]): The time that the alert was last updated in ISO 8601 format:
            `YYYY-MM-DDTHH:MM:SSZ`.
        fixed_at (Union[Unset, None, datetime.datetime]): The time that the alert was no longer detected and was
            considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
        dismissed_by (Optional[SimpleUser]): Simple User
        dismissed_at (Optional[datetime.datetime]): The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-
            DDTHH:MM:SSZ`.
        dismissed_reason (Optional[CodeScanningAlertDismissedReason]): **Required when the state is dismissed.** The
            reason for dismissing or closing the alert.
        dismissed_comment (Union[Unset, None, str]): The dismissal comment associated with the dismissal of the alert.
    """

    number: int
    created_at: datetime.datetime
    url: str
    html_url: str
    instances_url: str
    state: CodeScanningAlertState
    rule: CodeScanningAlertRule
    tool: CodeScanningAnalysisTool
    most_recent_instance: CodeScanningAlertInstance
    dismissed_by: Optional[SimpleUser]
    dismissed_at: Optional[datetime.datetime]
    dismissed_reason: Optional[CodeScanningAlertDismissedReason]
    updated_at: Union[Unset, datetime.datetime] = UNSET
    fixed_at: Union[Unset, None, datetime.datetime] = UNSET
    dismissed_comment: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        created_at = self.created_at.isoformat()

        url = self.url
        html_url = self.html_url
        instances_url = self.instances_url
        state = self.state.value

        rule = self.rule.to_dict()

        tool = self.tool.to_dict()

        most_recent_instance = self.most_recent_instance.to_dict()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        fixed_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.fixed_at, Unset):
            fixed_at = self.fixed_at.isoformat() if self.fixed_at else None

        dismissed_by = self.dismissed_by.to_dict() if self.dismissed_by else None

        dismissed_at = self.dismissed_at.isoformat() if self.dismissed_at else None

        dismissed_reason = self.dismissed_reason.value if self.dismissed_reason else None

        dismissed_comment = self.dismissed_comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "created_at": created_at,
                "url": url,
                "html_url": html_url,
                "instances_url": instances_url,
                "state": state,
                "rule": rule,
                "tool": tool,
                "most_recent_instance": most_recent_instance,
                "dismissed_by": dismissed_by,
                "dismissed_at": dismissed_at,
                "dismissed_reason": dismissed_reason,
            }
        )
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if fixed_at is not UNSET:
            field_dict["fixed_at"] = fixed_at
        if dismissed_comment is not UNSET:
            field_dict["dismissed_comment"] = dismissed_comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number")

        created_at = isoparse(d.pop("created_at"))

        url = d.pop("url")

        html_url = d.pop("html_url")

        instances_url = d.pop("instances_url")

        state = CodeScanningAlertState(d.pop("state"))

        rule = CodeScanningAlertRule.from_dict(d.pop("rule"))

        tool = CodeScanningAnalysisTool.from_dict(d.pop("tool"))

        most_recent_instance = CodeScanningAlertInstance.from_dict(d.pop("most_recent_instance"))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _fixed_at = d.pop("fixed_at", UNSET)
        fixed_at: Union[Unset, None, datetime.datetime]
        if _fixed_at is None:
            fixed_at = None
        elif isinstance(_fixed_at, Unset):
            fixed_at = UNSET
        else:
            fixed_at = isoparse(_fixed_at)

        _dismissed_by = d.pop("dismissed_by")
        dismissed_by: Optional[SimpleUser]
        if _dismissed_by is None:
            dismissed_by = None
        else:
            dismissed_by = SimpleUser.from_dict(_dismissed_by)

        _dismissed_at = d.pop("dismissed_at")
        dismissed_at: Optional[datetime.datetime]
        if _dismissed_at is None:
            dismissed_at = None
        else:
            dismissed_at = isoparse(_dismissed_at)

        _dismissed_reason = d.pop("dismissed_reason")
        dismissed_reason: Optional[CodeScanningAlertDismissedReason]
        if _dismissed_reason is None:
            dismissed_reason = None
        else:
            dismissed_reason = CodeScanningAlertDismissedReason(_dismissed_reason)

        dismissed_comment = d.pop("dismissed_comment", UNSET)

        code_scanning_alert = cls(
            number=number,
            created_at=created_at,
            url=url,
            html_url=html_url,
            instances_url=instances_url,
            state=state,
            rule=rule,
            tool=tool,
            most_recent_instance=most_recent_instance,
            updated_at=updated_at,
            fixed_at=fixed_at,
            dismissed_by=dismissed_by,
            dismissed_at=dismissed_at,
            dismissed_reason=dismissed_reason,
            dismissed_comment=dismissed_comment,
        )

        code_scanning_alert.additional_properties = d
        return code_scanning_alert

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
