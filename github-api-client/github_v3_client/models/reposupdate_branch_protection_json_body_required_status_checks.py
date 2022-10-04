from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.reposupdate_branch_protection_json_body_required_status_checks_checks_item import (
    ReposupdateBranchProtectionJsonBodyRequiredStatusChecksChecksItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdateBranchProtectionJsonBodyRequiredStatusChecks")


@attr.s(auto_attribs=True)
class ReposupdateBranchProtectionJsonBodyRequiredStatusChecks:
    """Require status checks to pass before merging. Set to `null` to disable.

    Attributes:
        strict (bool): Require branches to be up to date before merging.
        contexts (List[str]): **Deprecated**: The list of status checks to require in order to merge into this branch.
            If any of these checks have recently been set by a particular GitHub App, they will be required to come from
            that app in future for the branch to merge. Use `checks` instead of `contexts` for more fine-grained control.
        checks (Union[Unset, List[ReposupdateBranchProtectionJsonBodyRequiredStatusChecksChecksItem]]): The list of
            status checks to require in order to merge into this branch.
    """

    strict: bool
    contexts: List[str]
    checks: Union[Unset, List[ReposupdateBranchProtectionJsonBodyRequiredStatusChecksChecksItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        strict = self.strict
        contexts = self.contexts

        checks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.checks, Unset):
            checks = []
            for checks_item_data in self.checks:
                checks_item = checks_item_data.to_dict()

                checks.append(checks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strict": strict,
                "contexts": contexts,
            }
        )
        if checks is not UNSET:
            field_dict["checks"] = checks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        strict = d.pop("strict")

        contexts = cast(List[str], d.pop("contexts"))

        checks = []
        _checks = d.pop("checks", UNSET)
        for checks_item_data in _checks or []:
            checks_item = ReposupdateBranchProtectionJsonBodyRequiredStatusChecksChecksItem.from_dict(checks_item_data)

            checks.append(checks_item)

        reposupdate_branch_protection_json_body_required_status_checks = cls(
            strict=strict,
            contexts=contexts,
            checks=checks,
        )

        reposupdate_branch_protection_json_body_required_status_checks.additional_properties = d
        return reposupdate_branch_protection_json_body_required_status_checks

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
