from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.branch_restriction_policy_apps_item import BranchRestrictionPolicyAppsItem
from ..models.branch_restriction_policy_teams_item import BranchRestrictionPolicyTeamsItem
from ..models.branch_restriction_policy_users_item import BranchRestrictionPolicyUsersItem

T = TypeVar("T", bound="BranchRestrictionPolicy")


@attr.s(auto_attribs=True)
class BranchRestrictionPolicy:
    """Branch Restriction Policy

    Attributes:
        url (str):
        users_url (str):
        teams_url (str):
        apps_url (str):
        users (List[BranchRestrictionPolicyUsersItem]):
        teams (List[BranchRestrictionPolicyTeamsItem]):
        apps (List[BranchRestrictionPolicyAppsItem]):
    """

    url: str
    users_url: str
    teams_url: str
    apps_url: str
    users: List[BranchRestrictionPolicyUsersItem]
    teams: List[BranchRestrictionPolicyTeamsItem]
    apps: List[BranchRestrictionPolicyAppsItem]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        users_url = self.users_url
        teams_url = self.teams_url
        apps_url = self.apps_url
        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()

            users.append(users_item)

        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()

            teams.append(teams_item)

        apps = []
        for apps_item_data in self.apps:
            apps_item = apps_item_data.to_dict()

            apps.append(apps_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "users_url": users_url,
                "teams_url": teams_url,
                "apps_url": apps_url,
                "users": users,
                "teams": teams,
                "apps": apps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        users_url = d.pop("users_url")

        teams_url = d.pop("teams_url")

        apps_url = d.pop("apps_url")

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = BranchRestrictionPolicyUsersItem.from_dict(users_item_data)

            users.append(users_item)

        teams = []
        _teams = d.pop("teams")
        for teams_item_data in _teams:
            teams_item = BranchRestrictionPolicyTeamsItem.from_dict(teams_item_data)

            teams.append(teams_item)

        apps = []
        _apps = d.pop("apps")
        for apps_item_data in _apps:
            apps_item = BranchRestrictionPolicyAppsItem.from_dict(apps_item_data)

            apps.append(apps_item)

        branch_restriction_policy = cls(
            url=url,
            users_url=users_url,
            teams_url=teams_url,
            apps_url=apps_url,
            users=users,
            teams=teams,
            apps=apps,
        )

        branch_restriction_policy.additional_properties = d
        return branch_restriction_policy

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
