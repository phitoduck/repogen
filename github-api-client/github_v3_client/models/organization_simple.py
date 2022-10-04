from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="OrganizationSimple")


@attr.s(auto_attribs=True)
class OrganizationSimple:
    """Organization Simple

    Attributes:
        login (str):  Example: github.
        id (int):  Example: 1.
        node_id (str):  Example: MDEyOk9yZ2FuaXphdGlvbjE=.
        url (str):  Example: https://api.github.com/orgs/github.
        repos_url (str):  Example: https://api.github.com/orgs/github/repos.
        events_url (str):  Example: https://api.github.com/orgs/github/events.
        hooks_url (str):  Example: https://api.github.com/orgs/github/hooks.
        issues_url (str):  Example: https://api.github.com/orgs/github/issues.
        members_url (str):  Example: https://api.github.com/orgs/github/members{/member}.
        public_members_url (str):  Example: https://api.github.com/orgs/github/public_members{/member}.
        avatar_url (str):  Example: https://github.com/images/error/octocat_happy.gif.
        description (Optional[str]):  Example: A great organization.
    """

    login: str
    id: int
    node_id: str
    url: str
    repos_url: str
    events_url: str
    hooks_url: str
    issues_url: str
    members_url: str
    public_members_url: str
    avatar_url: str
    description: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login = self.login
        id = self.id
        node_id = self.node_id
        url = self.url
        repos_url = self.repos_url
        events_url = self.events_url
        hooks_url = self.hooks_url
        issues_url = self.issues_url
        members_url = self.members_url
        public_members_url = self.public_members_url
        avatar_url = self.avatar_url
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "login": login,
                "id": id,
                "node_id": node_id,
                "url": url,
                "repos_url": repos_url,
                "events_url": events_url,
                "hooks_url": hooks_url,
                "issues_url": issues_url,
                "members_url": members_url,
                "public_members_url": public_members_url,
                "avatar_url": avatar_url,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login = d.pop("login")

        id = d.pop("id")

        node_id = d.pop("node_id")

        url = d.pop("url")

        repos_url = d.pop("repos_url")

        events_url = d.pop("events_url")

        hooks_url = d.pop("hooks_url")

        issues_url = d.pop("issues_url")

        members_url = d.pop("members_url")

        public_members_url = d.pop("public_members_url")

        avatar_url = d.pop("avatar_url")

        description = d.pop("description")

        organization_simple = cls(
            login=login,
            id=id,
            node_id=node_id,
            url=url,
            repos_url=repos_url,
            events_url=events_url,
            hooks_url=hooks_url,
            issues_url=issues_url,
            members_url=members_url,
            public_members_url=public_members_url,
            avatar_url=avatar_url,
            description=description,
        )

        organization_simple.additional_properties = d
        return organization_simple

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
