from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdateBranchProtectionJsonBodyRestrictions")


@attr.s(auto_attribs=True)
class ReposupdateBranchProtectionJsonBodyRestrictions:
    """Restrict who can push to the protected branch. User, app, and team `restrictions` are only available for
    organization-owned repositories. Set to `null` to disable.

        Attributes:
            users (List[str]): The list of user `login`s with push access
            teams (List[str]): The list of team `slug`s with push access
            apps (Union[Unset, List[str]]): The list of app `slug`s with push access
    """

    users: List[str]
    teams: List[str]
    apps: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        users = self.users

        teams = self.teams

        apps: Union[Unset, List[str]] = UNSET
        if not isinstance(self.apps, Unset):
            apps = self.apps

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "users": users,
                "teams": teams,
            }
        )
        if apps is not UNSET:
            field_dict["apps"] = apps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        users = cast(List[str], d.pop("users"))

        teams = cast(List[str], d.pop("teams"))

        apps = cast(List[str], d.pop("apps", UNSET))

        reposupdate_branch_protection_json_body_restrictions = cls(
            users=users,
            teams=teams,
            apps=apps,
        )

        reposupdate_branch_protection_json_body_restrictions.additional_properties = d
        return reposupdate_branch_protection_json_body_restrictions

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
