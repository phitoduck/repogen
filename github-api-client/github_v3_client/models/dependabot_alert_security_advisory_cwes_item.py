from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="DependabotAlertSecurityAdvisoryCwesItem")


@attr.s(auto_attribs=True)
class DependabotAlertSecurityAdvisoryCwesItem:
    """A CWE weakness assigned to the advisory.

    Attributes:
        cwe_id (str): The unique CWE ID.
        name (str): The short, plain text name of the CWE.
    """

    cwe_id: str
    name: str

    def to_dict(self) -> Dict[str, Any]:
        cwe_id = self.cwe_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "cwe_id": cwe_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cwe_id = d.pop("cwe_id")

        name = d.pop("name")

        dependabot_alert_security_advisory_cwes_item = cls(
            cwe_id=cwe_id,
            name=name,
        )

        return dependabot_alert_security_advisory_cwes_item
