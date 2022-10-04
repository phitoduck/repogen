from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviewsBypassPullRequestAllowances")


@attr.s(auto_attribs=True)
class ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviewsBypassPullRequestAllowances:
    """Allow specific users, teams, or apps to bypass pull request requirements.

    Attributes:
        users (Union[Unset, List[str]]): The list of user `login`s allowed to bypass pull request requirements.
        teams (Union[Unset, List[str]]): The list of team `slug`s allowed to bypass pull request requirements.
        apps (Union[Unset, List[str]]): The list of app `slug`s allowed to bypass pull request requirements.
    """

    users: Union[Unset, List[str]] = UNSET
    teams: Union[Unset, List[str]] = UNSET
    apps: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        teams: Union[Unset, List[str]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams

        apps: Union[Unset, List[str]] = UNSET
        if not isinstance(self.apps, Unset):
            apps = self.apps

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users
        if teams is not UNSET:
            field_dict["teams"] = teams
        if apps is not UNSET:
            field_dict["apps"] = apps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        users = cast(List[str], d.pop("users", UNSET))

        teams = cast(List[str], d.pop("teams", UNSET))

        apps = cast(List[str], d.pop("apps", UNSET))

        reposupdate_branch_protection_json_body_required_pull_request_reviews_bypass_pull_request_allowances = cls(
            users=users,
            teams=teams,
            apps=apps,
        )

        reposupdate_branch_protection_json_body_required_pull_request_reviews_bypass_pull_request_allowances.additional_properties = (
            d
        )
        return reposupdate_branch_protection_json_body_required_pull_request_reviews_bypass_pull_request_allowances

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
