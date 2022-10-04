from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.collaborator_permissions import CollaboratorPermissions
from ..types import UNSET, Unset

T = TypeVar("T", bound="Collaborator")


@attr.s(auto_attribs=True)
class Collaborator:
    """Collaborator

    Attributes:
        login (str):  Example: octocat.
        id (int):  Example: 1.
        node_id (str):  Example: MDQ6VXNlcjE=.
        avatar_url (str):  Example: https://github.com/images/error/octocat_happy.gif.
        url (str):  Example: https://api.github.com/users/octocat.
        html_url (str):  Example: https://github.com/octocat.
        followers_url (str):  Example: https://api.github.com/users/octocat/followers.
        following_url (str):  Example: https://api.github.com/users/octocat/following{/other_user}.
        gists_url (str):  Example: https://api.github.com/users/octocat/gists{/gist_id}.
        starred_url (str):  Example: https://api.github.com/users/octocat/starred{/owner}{/repo}.
        subscriptions_url (str):  Example: https://api.github.com/users/octocat/subscriptions.
        organizations_url (str):  Example: https://api.github.com/users/octocat/orgs.
        repos_url (str):  Example: https://api.github.com/users/octocat/repos.
        events_url (str):  Example: https://api.github.com/users/octocat/events{/privacy}.
        received_events_url (str):  Example: https://api.github.com/users/octocat/received_events.
        type (str):  Example: User.
        site_admin (bool):
        role_name (str):  Example: admin.
        email (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        gravatar_id (Optional[str]):  Example: 41d064eb2195891e12d0413f63227ea7.
        permissions (Union[Unset, CollaboratorPermissions]):
    """

    login: str
    id: int
    node_id: str
    avatar_url: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool
    role_name: str
    gravatar_id: Optional[str]
    email: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    permissions: Union[Unset, CollaboratorPermissions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login = self.login
        id = self.id
        node_id = self.node_id
        avatar_url = self.avatar_url
        url = self.url
        html_url = self.html_url
        followers_url = self.followers_url
        following_url = self.following_url
        gists_url = self.gists_url
        starred_url = self.starred_url
        subscriptions_url = self.subscriptions_url
        organizations_url = self.organizations_url
        repos_url = self.repos_url
        events_url = self.events_url
        received_events_url = self.received_events_url
        type = self.type
        site_admin = self.site_admin
        role_name = self.role_name
        email = self.email
        name = self.name
        gravatar_id = self.gravatar_id
        permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "login": login,
                "id": id,
                "node_id": node_id,
                "avatar_url": avatar_url,
                "url": url,
                "html_url": html_url,
                "followers_url": followers_url,
                "following_url": following_url,
                "gists_url": gists_url,
                "starred_url": starred_url,
                "subscriptions_url": subscriptions_url,
                "organizations_url": organizations_url,
                "repos_url": repos_url,
                "events_url": events_url,
                "received_events_url": received_events_url,
                "type": type,
                "site_admin": site_admin,
                "role_name": role_name,
                "gravatar_id": gravatar_id,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if name is not UNSET:
            field_dict["name"] = name
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login = d.pop("login")

        id = d.pop("id")

        node_id = d.pop("node_id")

        avatar_url = d.pop("avatar_url")

        url = d.pop("url")

        html_url = d.pop("html_url")

        followers_url = d.pop("followers_url")

        following_url = d.pop("following_url")

        gists_url = d.pop("gists_url")

        starred_url = d.pop("starred_url")

        subscriptions_url = d.pop("subscriptions_url")

        organizations_url = d.pop("organizations_url")

        repos_url = d.pop("repos_url")

        events_url = d.pop("events_url")

        received_events_url = d.pop("received_events_url")

        type = d.pop("type")

        site_admin = d.pop("site_admin")

        role_name = d.pop("role_name")

        email = d.pop("email", UNSET)

        name = d.pop("name", UNSET)

        gravatar_id = d.pop("gravatar_id")

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, CollaboratorPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = CollaboratorPermissions.from_dict(_permissions)

        collaborator = cls(
            login=login,
            id=id,
            node_id=node_id,
            avatar_url=avatar_url,
            url=url,
            html_url=html_url,
            followers_url=followers_url,
            following_url=following_url,
            gists_url=gists_url,
            starred_url=starred_url,
            subscriptions_url=subscriptions_url,
            organizations_url=organizations_url,
            repos_url=repos_url,
            events_url=events_url,
            received_events_url=received_events_url,
            type=type,
            site_admin=site_admin,
            role_name=role_name,
            email=email,
            name=name,
            gravatar_id=gravatar_id,
            permissions=permissions,
        )

        collaborator.additional_properties = d
        return collaborator

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
