from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.code_scanning_alert_rule_summary_severity import CodeScanningAlertRuleSummarySeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodeScanningAlertRuleSummary")


@attr.s(auto_attribs=True)
class CodeScanningAlertRuleSummary:
    """
    Attributes:
        id (Union[Unset, None, str]): A unique identifier for the rule used to detect the alert.
        name (Union[Unset, str]): The name of the rule used to detect the alert.
        tags (Union[Unset, None, List[str]]): A set of tags applicable for the rule.
        severity (Union[Unset, None, CodeScanningAlertRuleSummarySeverity]): The severity of the alert.
        description (Union[Unset, str]): A short description of the rule used to detect the alert.
    """

    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    tags: Union[Unset, None, List[str]] = UNSET
    severity: Union[Unset, None, CodeScanningAlertRuleSummarySeverity] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = self.tags

        severity: Union[Unset, None, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value if self.severity else None

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if severity is not UNSET:
            field_dict["severity"] = severity
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, None, CodeScanningAlertRuleSummarySeverity]
        if _severity is None:
            severity = None
        elif isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = CodeScanningAlertRuleSummarySeverity(_severity)

        description = d.pop("description", UNSET)

        code_scanning_alert_rule_summary = cls(
            id=id,
            name=name,
            tags=tags,
            severity=severity,
            description=description,
        )

        code_scanning_alert_rule_summary.additional_properties = d
        return code_scanning_alert_rule_summary

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
