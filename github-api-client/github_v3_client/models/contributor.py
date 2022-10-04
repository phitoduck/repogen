from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Contributor")


@attr.s(auto_attribs=True)
class Contributor:
    """Contributor

    Attributes:
        type (str):
        contributions (int):
        login (Union[Unset, str]):
        id (Union[Unset, int]):
        node_id (Union[Unset, str]):
        avatar_url (Union[Unset, str]):
        gravatar_id (Union[Unset, None, str]):
        url (Union[Unset, str]):
        html_url (Union[Unset, str]):
        followers_url (Union[Unset, str]):
        following_url (Union[Unset, str]):
        gists_url (Union[Unset, str]):
        starred_url (Union[Unset, str]):
        subscriptions_url (Union[Unset, str]):
        organizations_url (Union[Unset, str]):
        repos_url (Union[Unset, str]):
        events_url (Union[Unset, str]):
        received_events_url (Union[Unset, str]):
        site_admin (Union[Unset, bool]):
        email (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    type: str
    contributions: int
    login: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    node_id: Union[Unset, str] = UNSET
    avatar_url: Union[Unset, str] = UNSET
    gravatar_id: Union[Unset, None, str] = UNSET
    url: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    followers_url: Union[Unset, str] = UNSET
    following_url: Union[Unset, str] = UNSET
    gists_url: Union[Unset, str] = UNSET
    starred_url: Union[Unset, str] = UNSET
    subscriptions_url: Union[Unset, str] = UNSET
    organizations_url: Union[Unset, str] = UNSET
    repos_url: Union[Unset, str] = UNSET
    events_url: Union[Unset, str] = UNSET
    received_events_url: Union[Unset, str] = UNSET
    site_admin: Union[Unset, bool] = UNSET
    email: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        contributions = self.contributions
        login = self.login
        id = self.id
        node_id = self.node_id
        avatar_url = self.avatar_url
        gravatar_id = self.gravatar_id
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
        site_admin = self.site_admin
        email = self.email
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "contributions": contributions,
            }
        )
        if login is not UNSET:
            field_dict["login"] = login
        if id is not UNSET:
            field_dict["id"] = id
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if gravatar_id is not UNSET:
            field_dict["gravatar_id"] = gravatar_id
        if url is not UNSET:
            field_dict["url"] = url
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
        if repos_url is not UNSET:
            field_dict["repos_url"] = repos_url
        if events_url is not UNSET:
            field_dict["events_url"] = events_url
        if received_events_url is not UNSET:
            field_dict["received_events_url"] = received_events_url
        if site_admin is not UNSET:
            field_dict["site_admin"] = site_admin
        if email is not UNSET:
            field_dict["email"] = email
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        contributions = d.pop("contributions")

        login = d.pop("login", UNSET)

        id = d.pop("id", UNSET)

        node_id = d.pop("node_id", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        gravatar_id = d.pop("gravatar_id", UNSET)

        url = d.pop("url", UNSET)

        html_url = d.pop("html_url", UNSET)

        followers_url = d.pop("followers_url", UNSET)

        following_url = d.pop("following_url", UNSET)

        gists_url = d.pop("gists_url", UNSET)

        starred_url = d.pop("starred_url", UNSET)

        subscriptions_url = d.pop("subscriptions_url", UNSET)

        organizations_url = d.pop("organizations_url", UNSET)

        repos_url = d.pop("repos_url", UNSET)

        events_url = d.pop("events_url", UNSET)

        received_events_url = d.pop("received_events_url", UNSET)

        site_admin = d.pop("site_admin", UNSET)

        email = d.pop("email", UNSET)

        name = d.pop("name", UNSET)

        contributor = cls(
            type=type,
            contributions=contributions,
            login=login,
            id=id,
            node_id=node_id,
            avatar_url=avatar_url,
            gravatar_id=gravatar_id,
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
            site_admin=site_admin,
            email=email,
            name=name,
        )

        contributor.additional_properties = d
        return contributor

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
