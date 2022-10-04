from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdatePullRequestReviewProtectionJsonBodyDismissalRestrictions")


@attr.s(auto_attribs=True)
class ReposupdatePullRequestReviewProtectionJsonBodyDismissalRestrictions:
    """Specify which users, teams, and apps can dismiss pull request reviews. Pass an empty `dismissal_restrictions` object
    to disable. User and team `dismissal_restrictions` are only available for organization-owned repositories. Omit this
    parameter for personal repositories.

        Attributes:
            users (Union[Unset, List[str]]): The list of user `login`s with dismissal access
            teams (Union[Unset, List[str]]): The list of team `slug`s with dismissal access
            apps (Union[Unset, List[str]]): The list of app `slug`s with dismissal access
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

        reposupdate_pull_request_review_protection_json_body_dismissal_restrictions = cls(
            users=users,
            teams=teams,
            apps=apps,
        )

        reposupdate_pull_request_review_protection_json_body_dismissal_restrictions.additional_properties = d
        return reposupdate_pull_request_review_protection_json_body_dismissal_restrictions

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
