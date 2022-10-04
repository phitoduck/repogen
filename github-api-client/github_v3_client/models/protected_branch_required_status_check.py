from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.protected_branch_required_status_check_checks_item import ProtectedBranchRequiredStatusCheckChecksItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedBranchRequiredStatusCheck")


@attr.s(auto_attribs=True)
class ProtectedBranchRequiredStatusCheck:
    """Protected Branch Required Status Check

    Attributes:
        contexts (List[str]):
        checks (List[ProtectedBranchRequiredStatusCheckChecksItem]):
        url (Union[Unset, str]):
        enforcement_level (Union[Unset, str]):
        contexts_url (Union[Unset, str]):
        strict (Union[Unset, bool]):
    """

    contexts: List[str]
    checks: List[ProtectedBranchRequiredStatusCheckChecksItem]
    url: Union[Unset, str] = UNSET
    enforcement_level: Union[Unset, str] = UNSET
    contexts_url: Union[Unset, str] = UNSET
    strict: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contexts = self.contexts

        checks = []
        for checks_item_data in self.checks:
            checks_item = checks_item_data.to_dict()

            checks.append(checks_item)

        url = self.url
        enforcement_level = self.enforcement_level
        contexts_url = self.contexts_url
        strict = self.strict

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contexts": contexts,
                "checks": checks,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if enforcement_level is not UNSET:
            field_dict["enforcement_level"] = enforcement_level
        if contexts_url is not UNSET:
            field_dict["contexts_url"] = contexts_url
        if strict is not UNSET:
            field_dict["strict"] = strict

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contexts = cast(List[str], d.pop("contexts"))

        checks = []
        _checks = d.pop("checks")
        for checks_item_data in _checks:
            checks_item = ProtectedBranchRequiredStatusCheckChecksItem.from_dict(checks_item_data)

            checks.append(checks_item)

        url = d.pop("url", UNSET)

        enforcement_level = d.pop("enforcement_level", UNSET)

        contexts_url = d.pop("contexts_url", UNSET)

        strict = d.pop("strict", UNSET)

        protected_branch_required_status_check = cls(
            contexts=contexts,
            checks=checks,
            url=url,
            enforcement_level=enforcement_level,
            contexts_url=contexts_url,
            strict=strict,
        )

        protected_branch_required_status_check.additional_properties = d
        return protected_branch_required_status_check

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
