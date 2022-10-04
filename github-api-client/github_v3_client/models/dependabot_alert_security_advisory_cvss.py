from typing import Any, Dict, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="DependabotAlertSecurityAdvisoryCvss")


@attr.s(auto_attribs=True)
class DependabotAlertSecurityAdvisoryCvss:
    """Details for the advisory pertaining to the Common Vulnerability Scoring System.

    Attributes:
        score (float): The overall CVSS score of the advisory.
        vector_string (Optional[str]): The full CVSS vector string for the advisory.
    """

    score: float
    vector_string: Optional[str]

    def to_dict(self) -> Dict[str, Any]:
        score = self.score
        vector_string = self.vector_string

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "score": score,
                "vector_string": vector_string,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        score = d.pop("score")

        vector_string = d.pop("vector_string")

        dependabot_alert_security_advisory_cvss = cls(
            score=score,
            vector_string=vector_string,
        )

        return dependabot_alert_security_advisory_cvss
