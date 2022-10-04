import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.dependabot_alert_security_advisory_cvss import DependabotAlertSecurityAdvisoryCvss
from ..models.dependabot_alert_security_advisory_cwes_item import DependabotAlertSecurityAdvisoryCwesItem
from ..models.dependabot_alert_security_advisory_identifiers_item import DependabotAlertSecurityAdvisoryIdentifiersItem
from ..models.dependabot_alert_security_advisory_references_item import DependabotAlertSecurityAdvisoryReferencesItem
from ..models.dependabot_alert_security_advisory_severity import DependabotAlertSecurityAdvisorySeverity
from ..models.dependabot_alert_security_vulnerability import DependabotAlertSecurityVulnerability

T = TypeVar("T", bound="DependabotAlertSecurityAdvisory")


@attr.s(auto_attribs=True)
class DependabotAlertSecurityAdvisory:
    """Details for the GitHub Security Advisory.

    Attributes:
        ghsa_id (str): The unique GitHub Security Advisory ID assigned to the advisory.
        summary (str): A short, plain text summary of the advisory.
        description (str): A long-form Markdown-supported description of the advisory.
        vulnerabilities (List[DependabotAlertSecurityVulnerability]): Vulnerable version range information for the
            advisory.
        severity (DependabotAlertSecurityAdvisorySeverity): The severity of the advisory.
        cvss (DependabotAlertSecurityAdvisoryCvss): Details for the advisory pertaining to the Common Vulnerability
            Scoring System.
        cwes (List[DependabotAlertSecurityAdvisoryCwesItem]): Details for the advisory pertaining to Common Weakness
            Enumeration.
        identifiers (List[DependabotAlertSecurityAdvisoryIdentifiersItem]): Values that identify this advisory among
            security information sources.
        references (List[DependabotAlertSecurityAdvisoryReferencesItem]): Links to additional advisory information.
        published_at (datetime.datetime): The time that the advisory was published in ISO 8601 format: `YYYY-MM-
            DDTHH:MM:SSZ`.
        updated_at (datetime.datetime): The time that the advisory was last modified in ISO 8601 format: `YYYY-MM-
            DDTHH:MM:SSZ`.
        cve_id (Optional[str]): The unique CVE ID assigned to the advisory.
        withdrawn_at (Optional[datetime.datetime]): The time that the advisory was withdrawn in ISO 8601 format: `YYYY-
            MM-DDTHH:MM:SSZ`.
    """

    ghsa_id: str
    summary: str
    description: str
    vulnerabilities: List[DependabotAlertSecurityVulnerability]
    severity: DependabotAlertSecurityAdvisorySeverity
    cvss: DependabotAlertSecurityAdvisoryCvss
    cwes: List[DependabotAlertSecurityAdvisoryCwesItem]
    identifiers: List[DependabotAlertSecurityAdvisoryIdentifiersItem]
    references: List[DependabotAlertSecurityAdvisoryReferencesItem]
    published_at: datetime.datetime
    updated_at: datetime.datetime
    cve_id: Optional[str]
    withdrawn_at: Optional[datetime.datetime]

    def to_dict(self) -> Dict[str, Any]:
        ghsa_id = self.ghsa_id
        summary = self.summary
        description = self.description
        vulnerabilities = []
        for vulnerabilities_item_data in self.vulnerabilities:
            vulnerabilities_item = vulnerabilities_item_data.to_dict()

            vulnerabilities.append(vulnerabilities_item)

        severity = self.severity.value

        cvss = self.cvss.to_dict()

        cwes = []
        for cwes_item_data in self.cwes:
            cwes_item = cwes_item_data.to_dict()

            cwes.append(cwes_item)

        identifiers = []
        for identifiers_item_data in self.identifiers:
            identifiers_item = identifiers_item_data.to_dict()

            identifiers.append(identifiers_item)

        references = []
        for references_item_data in self.references:
            references_item = references_item_data.to_dict()

            references.append(references_item)

        published_at = self.published_at.isoformat()

        updated_at = self.updated_at.isoformat()

        cve_id = self.cve_id
        withdrawn_at = self.withdrawn_at.isoformat() if self.withdrawn_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "ghsa_id": ghsa_id,
                "summary": summary,
                "description": description,
                "vulnerabilities": vulnerabilities,
                "severity": severity,
                "cvss": cvss,
                "cwes": cwes,
                "identifiers": identifiers,
                "references": references,
                "published_at": published_at,
                "updated_at": updated_at,
                "cve_id": cve_id,
                "withdrawn_at": withdrawn_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ghsa_id = d.pop("ghsa_id")

        summary = d.pop("summary")

        description = d.pop("description")

        vulnerabilities = []
        _vulnerabilities = d.pop("vulnerabilities")
        for vulnerabilities_item_data in _vulnerabilities:
            vulnerabilities_item = DependabotAlertSecurityVulnerability.from_dict(vulnerabilities_item_data)

            vulnerabilities.append(vulnerabilities_item)

        severity = DependabotAlertSecurityAdvisorySeverity(d.pop("severity"))

        cvss = DependabotAlertSecurityAdvisoryCvss.from_dict(d.pop("cvss"))

        cwes = []
        _cwes = d.pop("cwes")
        for cwes_item_data in _cwes:
            cwes_item = DependabotAlertSecurityAdvisoryCwesItem.from_dict(cwes_item_data)

            cwes.append(cwes_item)

        identifiers = []
        _identifiers = d.pop("identifiers")
        for identifiers_item_data in _identifiers:
            identifiers_item = DependabotAlertSecurityAdvisoryIdentifiersItem.from_dict(identifiers_item_data)

            identifiers.append(identifiers_item)

        references = []
        _references = d.pop("references")
        for references_item_data in _references:
            references_item = DependabotAlertSecurityAdvisoryReferencesItem.from_dict(references_item_data)

            references.append(references_item)

        published_at = isoparse(d.pop("published_at"))

        updated_at = isoparse(d.pop("updated_at"))

        cve_id = d.pop("cve_id")

        _withdrawn_at = d.pop("withdrawn_at")
        withdrawn_at: Optional[datetime.datetime]
        if _withdrawn_at is None:
            withdrawn_at = None
        else:
            withdrawn_at = isoparse(_withdrawn_at)

        dependabot_alert_security_advisory = cls(
            ghsa_id=ghsa_id,
            summary=summary,
            description=description,
            vulnerabilities=vulnerabilities,
            severity=severity,
            cvss=cvss,
            cwes=cwes,
            identifiers=identifiers,
            references=references,
            published_at=published_at,
            updated_at=updated_at,
            cve_id=cve_id,
            withdrawn_at=withdrawn_at,
        )

        return dependabot_alert_security_advisory
