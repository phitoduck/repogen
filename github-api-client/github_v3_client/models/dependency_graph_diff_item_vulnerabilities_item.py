from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DependencyGraphDiffItemVulnerabilitiesItem")


@attr.s(auto_attribs=True)
class DependencyGraphDiffItemVulnerabilitiesItem:
    """
    Attributes:
        severity (str):  Example: critical.
        advisory_ghsa_id (str):  Example: GHSA-rf4j-j272-fj86.
        advisory_summary (str):  Example: A summary of the advisory..
        advisory_url (str):  Example: https://github.com/advisories/GHSA-rf4j-j272-fj86.
    """

    severity: str
    advisory_ghsa_id: str
    advisory_summary: str
    advisory_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        severity = self.severity
        advisory_ghsa_id = self.advisory_ghsa_id
        advisory_summary = self.advisory_summary
        advisory_url = self.advisory_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "severity": severity,
                "advisory_ghsa_id": advisory_ghsa_id,
                "advisory_summary": advisory_summary,
                "advisory_url": advisory_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        severity = d.pop("severity")

        advisory_ghsa_id = d.pop("advisory_ghsa_id")

        advisory_summary = d.pop("advisory_summary")

        advisory_url = d.pop("advisory_url")

        dependency_graph_diff_item_vulnerabilities_item = cls(
            severity=severity,
            advisory_ghsa_id=advisory_ghsa_id,
            advisory_summary=advisory_summary,
            advisory_url=advisory_url,
        )

        dependency_graph_diff_item_vulnerabilities_item.additional_properties = d
        return dependency_graph_diff_item_vulnerabilities_item

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
