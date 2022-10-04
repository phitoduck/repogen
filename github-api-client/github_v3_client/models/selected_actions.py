from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SelectedActions")


@attr.s(auto_attribs=True)
class SelectedActions:
    """
    Attributes:
        github_owned_allowed (Union[Unset, bool]): Whether GitHub-owned actions are allowed. For example, this includes
            the actions in the `actions` organization.
        verified_allowed (Union[Unset, bool]): Whether actions from GitHub Marketplace verified creators are allowed.
            Set to `true` to allow all actions by GitHub Marketplace verified creators.
        patterns_allowed (Union[Unset, List[str]]): Specifies a list of string-matching patterns to allow specific
            action(s) and reusable workflow(s). Wildcards, tags, and SHAs are allowed. For example, `monalisa/octocat@*`,
            `monalisa/octocat@v2`, `monalisa/*`."
    """

    github_owned_allowed: Union[Unset, bool] = UNSET
    verified_allowed: Union[Unset, bool] = UNSET
    patterns_allowed: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        github_owned_allowed = self.github_owned_allowed
        verified_allowed = self.verified_allowed
        patterns_allowed: Union[Unset, List[str]] = UNSET
        if not isinstance(self.patterns_allowed, Unset):
            patterns_allowed = self.patterns_allowed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if github_owned_allowed is not UNSET:
            field_dict["github_owned_allowed"] = github_owned_allowed
        if verified_allowed is not UNSET:
            field_dict["verified_allowed"] = verified_allowed
        if patterns_allowed is not UNSET:
            field_dict["patterns_allowed"] = patterns_allowed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        github_owned_allowed = d.pop("github_owned_allowed", UNSET)

        verified_allowed = d.pop("verified_allowed", UNSET)

        patterns_allowed = cast(List[str], d.pop("patterns_allowed", UNSET))

        selected_actions = cls(
            github_owned_allowed=github_owned_allowed,
            verified_allowed=verified_allowed,
            patterns_allowed=patterns_allowed,
        )

        selected_actions.additional_properties = d
        return selected_actions

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
