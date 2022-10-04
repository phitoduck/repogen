from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchRestrictionPolicyAppsItemOwner")


@attr.s(auto_attribs=True)
class BranchRestrictionPolicyAppsItemOwner:
    """
    Attributes:
        login (Union[Unset, str]):
        id (Union[Unset, int]):
        node_id (Union[Unset, str]):
        url (Union[Unset, str]):
        repos_url (Union[Unset, str]):
        events_url (Union[Unset, str]):
        hooks_url (Union[Unset, str]):
        issues_url (Union[Unset, str]):
        members_url (Union[Unset, str]):
        public_members_url (Union[Unset, str]):
        avatar_url (Union[Unset, str]):
        description (Union[Unset, str]):
        gravatar_id (Union[Unset, str]):  Example: "".
        html_url (Union[Unset, str]):  Example: "https://github.com/testorg-ea8ec76d71c3af4b".
        followers_url (Union[Unset, str]):  Example: "https://api.github.com/users/testorg-ea8ec76d71c3af4b/followers".
        following_url (Union[Unset, str]):  Example: "https://api.github.com/users/testorg-
            ea8ec76d71c3af4b/following{/other_user}".
        gists_url (Union[Unset, str]):  Example: "https://api.github.com/users/testorg-
            ea8ec76d71c3af4b/gists{/gist_id}".
        starred_url (Union[Unset, str]):  Example: "https://api.github.com/users/testorg-
            ea8ec76d71c3af4b/starred{/owner}{/repo}".
        subscriptions_url (Union[Unset, str]):  Example: "https://api.github.com/users/testorg-
            ea8ec76d71c3af4b/subscriptions".
        organizations_url (Union[Unset, str]):  Example: "https://api.github.com/users/testorg-ea8ec76d71c3af4b/orgs".
        received_events_url (Union[Unset, str]):  Example: "https://api.github.com/users/testorg-
            ea8ec76d71c3af4b/received_events".
        type (Union[Unset, str]):  Example: "Organization".
        site_admin (Union[Unset, bool]):
    """

    login: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    node_id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    repos_url: Union[Unset, str] = UNSET
    events_url: Union[Unset, str] = UNSET
    hooks_url: Union[Unset, str] = UNSET
    issues_url: Union[Unset, str] = UNSET
    members_url: Union[Unset, str] = UNSET
    public_members_url: Union[Unset, str] = UNSET
    avatar_url: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    gravatar_id: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    followers_url: Union[Unset, str] = UNSET
    following_url: Union[Unset, str] = UNSET
    gists_url: Union[Unset, str] = UNSET
    starred_url: Union[Unset, str] = UNSET
    subscriptions_url: Union[Unset, str] = UNSET
    organizations_url: Union[Unset, str] = UNSET
    received_events_url: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    site_admin: Union[Unset, bool] = UNSET
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
        gravatar_id = self.gravatar_id
        html_url = self.html_url
        followers_url = self.followers_url
        following_url = self.following_url
        gists_url = self.gists_url
        starred_url = self.starred_url
        subscriptions_url = self.subscriptions_url
        organizations_url = self.organizations_url
        received_events_url = self.received_events_url
        type = self.type
        site_admin = self.site_admin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if login is not UNSET:
            field_dict["login"] = login
        if id is not UNSET:
            field_dict["id"] = id
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if url is not UNSET:
            field_dict["url"] = url
        if repos_url is not UNSET:
            field_dict["repos_url"] = repos_url
        if events_url is not UNSET:
            field_dict["events_url"] = events_url
        if hooks_url is not UNSET:
            field_dict["hooks_url"] = hooks_url
        if issues_url is not UNSET:
            field_dict["issues_url"] = issues_url
        if members_url is not UNSET:
            field_dict["members_url"] = members_url
        if public_members_url is not UNSET:
            field_dict["public_members_url"] = public_members_url
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if description is not UNSET:
            field_dict["description"] = description
        if gravatar_id is not UNSET:
            field_dict["gravatar_id"] = gravatar_id
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if followers_url is not UNSET:
            field_dict["followers_url"] = followers_url
        if following_url is not UNSET:
            field_dict["following_url"] = following_url
        if gists_url is not UNSET:
            field_dict["gists_url"] = gists_url
        if starred_url is not UNSET:
            field_dict["starred_url"] = starred_url
        if subscriptions_url is not UNSET:
            field_dict["subscriptions_url"] = subscriptions_url
        if organizations_url is not UNSET:
            field_dict["organizations_url"] = organizations_url
        if received_events_url is not UNSET:
            field_dict["received_events_url"] = received_events_url
        if type is not UNSET:
            field_dict["type"] = type
        if site_admin is not UNSET:
            field_dict["site_admin"] = site_admin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login = d.pop("login", UNSET)

        id = d.pop("id", UNSET)

        node_id = d.pop("node_id", UNSET)

        url = d.pop("url", UNSET)

        repos_url = d.pop("repos_url", UNSET)

        events_url = d.pop("events_url", UNSET)

        hooks_url = d.pop("hooks_url", UNSET)

        issues_url = d.pop("issues_url", UNSET)

        members_url = d.pop("members_url", UNSET)

        public_members_url = d.pop("public_members_url", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        description = d.pop("description", UNSET)

        gravatar_id = d.pop("gravatar_id", UNSET)

        html_url = d.pop("html_url", UNSET)

        followers_url = d.pop("followers_url", UNSET)

        following_url = d.pop("following_url", UNSET)

        gists_url = d.pop("gists_url", UNSET)

        starred_url = d.pop("starred_url", UNSET)

        subscriptions_url = d.pop("subscriptions_url", UNSET)

        organizations_url = d.pop("organizations_url", UNSET)

        received_events_url = d.pop("received_events_url", UNSET)

        type = d.pop("type", UNSET)

        site_admin = d.pop("site_admin", UNSET)

        branch_restriction_policy_apps_item_owner = cls(
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
            gravatar_id=gravatar_id,
            html_url=html_url,
            followers_url=followers_url,
            following_url=following_url,
            gists_url=gists_url,
            starred_url=starred_url,
            subscriptions_url=subscriptions_url,
            organizations_url=organizations_url,
            received_events_url=received_events_url,
            type=type,
            site_admin=site_admin,
        )

        branch_restriction_policy_apps_item_owner.additional_properties = d
        return branch_restriction_policy_apps_item_owner

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
