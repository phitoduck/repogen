import datetime
from typing import Any, Dict, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.dependabot_alert_dependency import DependabotAlertDependency
from ..models.dependabot_alert_dismissed_reason import DependabotAlertDismissedReason
from ..models.dependabot_alert_security_advisory import DependabotAlertSecurityAdvisory
from ..models.dependabot_alert_security_vulnerability import DependabotAlertSecurityVulnerability
from ..models.dependabot_alert_state import DependabotAlertState
from ..models.simple_user import SimpleUser

T = TypeVar("T", bound="DependabotAlert")


@attr.s(auto_attribs=True)
class DependabotAlert:
    """A Dependabot alert.

    Attributes:
        number (int): The security alert number.
        state (DependabotAlertState): The state of the Dependabot alert.
        dependency (DependabotAlertDependency): Details for the vulnerable dependency.
        security_advisory (DependabotAlertSecurityAdvisory): Details for the GitHub Security Advisory.
        security_vulnerability (DependabotAlertSecurityVulnerability): Details pertaining to one vulnerable version
            range for the advisory.
        url (str): The REST API URL of the alert resource.
        html_url (str): The GitHub URL of the alert resource.
        created_at (datetime.datetime): The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
        updated_at (datetime.datetime): The time that the alert was last updated in ISO 8601 format: `YYYY-MM-
            DDTHH:MM:SSZ`.
        dismissed_at (Optional[datetime.datetime]): The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-
            DDTHH:MM:SSZ`.
        dismissed_by (Optional[SimpleUser]): Simple User
        dismissed_reason (Optional[DependabotAlertDismissedReason]): The reason that the alert was dismissed.
        dismissed_comment (Optional[str]): An optional comment associated with the alert's dismissal.
        fixed_at (Optional[datetime.datetime]): The time that the alert was no longer detected and was considered fixed
            in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    number: int
    state: DependabotAlertState
    dependency: DependabotAlertDependency
    security_advisory: DependabotAlertSecurityAdvisory
    security_vulnerability: DependabotAlertSecurityVulnerability
    url: str
    html_url: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    dismissed_at: Optional[datetime.datetime]
    dismissed_by: Optional[SimpleUser]
    dismissed_reason: Optional[DependabotAlertDismissedReason]
    dismissed_comment: Optional[str]
    fixed_at: Optional[datetime.datetime]

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        state = self.state.value

        dependency = self.dependency.to_dict()

        security_advisory = self.security_advisory.to_dict()

        security_vulnerability = self.security_vulnerability.to_dict()

        url = self.url
        html_url = self.html_url
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        dismissed_at = self.dismissed_at.isoformat() if self.dismissed_at else None

        dismissed_by = self.dismissed_by.to_dict() if self.dismissed_by else None

        dismissed_reason = self.dismissed_reason.value if self.dismissed_reason else None

        dismissed_comment = self.dismissed_comment
        fixed_at = self.fixed_at.isoformat() if self.fixed_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "number": number,
                "state": state,
                "dependency": dependency,
                "security_advisory": security_advisory,
                "security_vulnerability": security_vulnerability,
                "url": url,
                "html_url": html_url,
                "created_at": created_at,
                "updated_at": updated_at,
                "dismissed_at": dismissed_at,
                "dismissed_by": dismissed_by,
                "dismissed_reason": dismissed_reason,
                "dismissed_comment": dismissed_comment,
                "fixed_at": fixed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number")

        state = DependabotAlertState(d.pop("state"))

        dependency = DependabotAlertDependency.from_dict(d.pop("dependency"))

        security_advisory = DependabotAlertSecurityAdvisory.from_dict(d.pop("security_advisory"))

        security_vulnerability = DependabotAlertSecurityVulnerability.from_dict(d.pop("security_vulnerability"))

        url = d.pop("url")

        html_url = d.pop("html_url")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        _dismissed_at = d.pop("dismissed_at")
        dismissed_at: Optional[datetime.datetime]
        if _dismissed_at is None:
            dismissed_at = None
        else:
            dismissed_at = isoparse(_dismissed_at)

        _dismissed_by = d.pop("dismissed_by")
        dismissed_by: Optional[SimpleUser]
        if _dismissed_by is None:
            dismissed_by = None
        else:
            dismissed_by = SimpleUser.from_dict(_dismissed_by)

        _dismissed_reason = d.pop("dismissed_reason")
        dismissed_reason: Optional[DependabotAlertDismissedReason]
        if _dismissed_reason is None:
            dismissed_reason = None
        else:
            dismissed_reason = DependabotAlertDismissedReason(_dismissed_reason)

        dismissed_comment = d.pop("dismissed_comment")

        _fixed_at = d.pop("fixed_at")
        fixed_at: Optional[datetime.datetime]
        if _fixed_at is None:
            fixed_at = None
        else:
            fixed_at = isoparse(_fixed_at)

        dependabot_alert = cls(
            number=number,
            state=state,
            dependency=dependency,
            security_advisory=security_advisory,
            security_vulnerability=security_vulnerability,
            url=url,
            html_url=html_url,
            created_at=created_at,
            updated_at=updated_at,
            dismissed_at=dismissed_at,
            dismissed_by=dismissed_by,
            dismissed_reason=dismissed_reason,
            dismissed_comment=dismissed_comment,
            fixed_at=fixed_at,
        )

        return dependabot_alert
