from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.code_scanning_alert_rule_security_severity_level import CodeScanningAlertRuleSecuritySeverityLevel
from ..models.code_scanning_alert_rule_severity import CodeScanningAlertRuleSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodeScanningAlertRule")


@attr.s(auto_attribs=True)
class CodeScanningAlertRule:
    """
    Attributes:
        id (Union[Unset, None, str]): A unique identifier for the rule used to detect the alert.
        name (Union[Unset, str]): The name of the rule used to detect the alert.
        severity (Union[Unset, None, CodeScanningAlertRuleSeverity]): The severity of the alert.
        security_severity_level (Union[Unset, None, CodeScanningAlertRuleSecuritySeverityLevel]): The security severity
            of the alert.
        description (Union[Unset, str]): A short description of the rule used to detect the alert.
        full_description (Union[Unset, str]): description of the rule used to detect the alert.
        tags (Union[Unset, None, List[str]]): A set of tags applicable for the rule.
        help_ (Union[Unset, None, str]): Detailed documentation for the rule as GitHub Flavored Markdown.
        help_uri (Union[Unset, None, str]): A link to the documentation for the rule used to detect the alert.
    """

    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    severity: Union[Unset, None, CodeScanningAlertRuleSeverity] = UNSET
    security_severity_level: Union[Unset, None, CodeScanningAlertRuleSecuritySeverityLevel] = UNSET
    description: Union[Unset, str] = UNSET
    full_description: Union[Unset, str] = UNSET
    tags: Union[Unset, None, List[str]] = UNSET
    help_: Union[Unset, None, str] = UNSET
    help_uri: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        severity: Union[Unset, None, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value if self.severity else None

        security_severity_level: Union[Unset, None, str] = UNSET
        if not isinstance(self.security_severity_level, Unset):
            security_severity_level = self.security_severity_level.value if self.security_severity_level else None

        description = self.description
        full_description = self.full_description
        tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = self.tags

        help_ = self.help_
        help_uri = self.help_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if severity is not UNSET:
            field_dict["severity"] = severity
        if security_severity_level is not UNSET:
            field_dict["security_severity_level"] = security_severity_level
        if description is not UNSET:
            field_dict["description"] = description
        if full_description is not UNSET:
            field_dict["full_description"] = full_description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if help_ is not UNSET:
            field_dict["help"] = help_
        if help_uri is not UNSET:
            field_dict["help_uri"] = help_uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, None, CodeScanningAlertRuleSeverity]
        if _severity is None:
            severity = None
        elif isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = CodeScanningAlertRuleSeverity(_severity)

        _security_severity_level = d.pop("security_severity_level", UNSET)
        security_severity_level: Union[Unset, None, CodeScanningAlertRuleSecuritySeverityLevel]
        if _security_severity_level is None:
            security_severity_level = None
        elif isinstance(_security_severity_level, Unset):
            security_severity_level = UNSET
        else:
            security_severity_level = CodeScanningAlertRuleSecuritySeverityLevel(_security_severity_level)

        description = d.pop("description", UNSET)

        full_description = d.pop("full_description", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        help_ = d.pop("help", UNSET)

        help_uri = d.pop("help_uri", UNSET)

        code_scanning_alert_rule = cls(
            id=id,
            name=name,
            severity=severity,
            security_severity_level=security_severity_level,
            description=description,
            full_description=full_description,
            tags=tags,
            help_=help_,
            help_uri=help_uri,
        )

        code_scanning_alert_rule.additional_properties = d
        return code_scanning_alert_rule

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
