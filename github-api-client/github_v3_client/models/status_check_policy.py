from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.status_check_policy_checks_item import StatusCheckPolicyChecksItem

T = TypeVar("T", bound="StatusCheckPolicy")


@attr.s(auto_attribs=True)
class StatusCheckPolicy:
    """Status Check Policy

    Attributes:
        url (str):  Example: https://api.github.com/repos/octocat/Hello-
            World/branches/master/protection/required_status_checks.
        strict (bool):  Example: True.
        contexts (List[str]):  Example: ['continuous-integration/travis-ci'].
        checks (List[StatusCheckPolicyChecksItem]):
        contexts_url (str):  Example: https://api.github.com/repos/octocat/Hello-
            World/branches/master/protection/required_status_checks/contexts.
    """

    url: str
    strict: bool
    contexts: List[str]
    checks: List[StatusCheckPolicyChecksItem]
    contexts_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        strict = self.strict
        contexts = self.contexts

        checks = []
        for checks_item_data in self.checks:
            checks_item = checks_item_data.to_dict()

            checks.append(checks_item)

        contexts_url = self.contexts_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "strict": strict,
                "contexts": contexts,
                "checks": checks,
                "contexts_url": contexts_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        strict = d.pop("strict")

        contexts = cast(List[str], d.pop("contexts"))

        checks = []
        _checks = d.pop("checks")
        for checks_item_data in _checks:
            checks_item = StatusCheckPolicyChecksItem.from_dict(checks_item_data)

            checks.append(checks_item)

        contexts_url = d.pop("contexts_url")

        status_check_policy = cls(
            url=url,
            strict=strict,
            contexts=contexts,
            checks=checks,
            contexts_url=contexts_url,
        )

        status_check_policy.additional_properties = d
        return status_check_policy

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
