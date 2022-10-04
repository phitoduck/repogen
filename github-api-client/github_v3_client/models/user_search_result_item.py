import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.search_result_text_matches_item import SearchResultTextMatchesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSearchResultItem")


@attr.s(auto_attribs=True)
class UserSearchResultItem:
    """User Search Result Item

    Attributes:
        login (str):
        id (int):
        node_id (str):
        avatar_url (str):
        url (str):
        html_url (str):
        followers_url (str):
        subscriptions_url (str):
        organizations_url (str):
        repos_url (str):
        received_events_url (str):
        type (str):
        score (float):
        following_url (str):
        gists_url (str):
        starred_url (str):
        events_url (str):
        site_admin (bool):
        gravatar_id (Optional[str]):
        public_repos (Union[Unset, int]):
        public_gists (Union[Unset, int]):
        followers (Union[Unset, int]):
        following (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        name (Union[Unset, None, str]):
        bio (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        location (Union[Unset, None, str]):
        hireable (Union[Unset, None, bool]):
        text_matches (Union[Unset, List[SearchResultTextMatchesItem]]):
        blog (Union[Unset, None, str]):
        company (Union[Unset, None, str]):
        suspended_at (Union[Unset, None, datetime.datetime]):
    """

    login: str
    id: int
    node_id: str
    avatar_url: str
    url: str
    html_url: str
    followers_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    received_events_url: str
    type: str
    score: float
    following_url: str
    gists_url: str
    starred_url: str
    events_url: str
    site_admin: bool
    gravatar_id: Optional[str]
    public_repos: Union[Unset, int] = UNSET
    public_gists: Union[Unset, int] = UNSET
    followers: Union[Unset, int] = UNSET
    following: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, None, str] = UNSET
    bio: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    location: Union[Unset, None, str] = UNSET
    hireable: Union[Unset, None, bool] = UNSET
    text_matches: Union[Unset, List[SearchResultTextMatchesItem]] = UNSET
    blog: Union[Unset, None, str] = UNSET
    company: Union[Unset, None, str] = UNSET
    suspended_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login = self.login
        id = self.id
        node_id = self.node_id
        avatar_url = self.avatar_url
        url = self.url
        html_url = self.html_url
        followers_url = self.followers_url
        subscriptions_url = self.subscriptions_url
        organizations_url = self.organizations_url
        repos_url = self.repos_url
        received_events_url = self.received_events_url
        type = self.type
        score = self.score
        following_url = self.following_url
        gists_url = self.gists_url
        starred_url = self.starred_url
        events_url = self.events_url
        site_admin = self.site_admin
        gravatar_id = self.gravatar_id
        public_repos = self.public_repos
        public_gists = self.public_gists
        followers = self.followers
        following = self.following
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        name = self.name
        bio = self.bio
        email = self.email
        location = self.location
        hireable = self.hireable
        text_matches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.text_matches, Unset):
            text_matches = []
            for componentsschemassearch_result_text_matches_item_data in self.text_matches:
                componentsschemassearch_result_text_matches_item = (
                    componentsschemassearch_result_text_matches_item_data.to_dict()
                )

                text_matches.append(componentsschemassearch_result_text_matches_item)

        blog = self.blog
        company = self.company
        suspended_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.suspended_at, Unset):
            suspended_at = self.suspended_at.isoformat() if self.suspended_at else None

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
                "subscriptions_url": subscriptions_url,
                "organizations_url": organizations_url,
                "repos_url": repos_url,
                "received_events_url": received_events_url,
                "type": type,
                "score": score,
                "following_url": following_url,
                "gists_url": gists_url,
                "starred_url": starred_url,
                "events_url": events_url,
                "site_admin": site_admin,
                "gravatar_id": gravatar_id,
            }
        )
        if public_repos is not UNSET:
            field_dict["public_repos"] = public_repos
        if public_gists is not UNSET:
            field_dict["public_gists"] = public_gists
        if followers is not UNSET:
            field_dict["followers"] = followers
        if following is not UNSET:
            field_dict["following"] = following
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if name is not UNSET:
            field_dict["name"] = name
        if bio is not UNSET:
            field_dict["bio"] = bio
        if email is not UNSET:
            field_dict["email"] = email
        if location is not UNSET:
            field_dict["location"] = location
        if hireable is not UNSET:
            field_dict["hireable"] = hireable
        if text_matches is not UNSET:
            field_dict["text_matches"] = text_matches
        if blog is not UNSET:
            field_dict["blog"] = blog
        if company is not UNSET:
            field_dict["company"] = company
        if suspended_at is not UNSET:
            field_dict["suspended_at"] = suspended_at

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

        subscriptions_url = d.pop("subscriptions_url")

        organizations_url = d.pop("organizations_url")

        repos_url = d.pop("repos_url")

        received_events_url = d.pop("received_events_url")

        type = d.pop("type")

        score = d.pop("score")

        following_url = d.pop("following_url")

        gists_url = d.pop("gists_url")

        starred_url = d.pop("starred_url")

        events_url = d.pop("events_url")

        site_admin = d.pop("site_admin")

        gravatar_id = d.pop("gravatar_id")

        public_repos = d.pop("public_repos", UNSET)

        public_gists = d.pop("public_gists", UNSET)

        followers = d.pop("followers", UNSET)

        following = d.pop("following", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        name = d.pop("name", UNSET)

        bio = d.pop("bio", UNSET)

        email = d.pop("email", UNSET)

        location = d.pop("location", UNSET)

        hireable = d.pop("hireable", UNSET)

        text_matches = []
        _text_matches = d.pop("text_matches", UNSET)
        for componentsschemassearch_result_text_matches_item_data in _text_matches or []:
            componentsschemassearch_result_text_matches_item = SearchResultTextMatchesItem.from_dict(
                componentsschemassearch_result_text_matches_item_data
            )

            text_matches.append(componentsschemassearch_result_text_matches_item)

        blog = d.pop("blog", UNSET)

        company = d.pop("company", UNSET)

        _suspended_at = d.pop("suspended_at", UNSET)
        suspended_at: Union[Unset, None, datetime.datetime]
        if _suspended_at is None:
            suspended_at = None
        elif isinstance(_suspended_at, Unset):
            suspended_at = UNSET
        else:
            suspended_at = isoparse(_suspended_at)

        user_search_result_item = cls(
            login=login,
            id=id,
            node_id=node_id,
            avatar_url=avatar_url,
            url=url,
            html_url=html_url,
            followers_url=followers_url,
            subscriptions_url=subscriptions_url,
            organizations_url=organizations_url,
            repos_url=repos_url,
            received_events_url=received_events_url,
            type=type,
            score=score,
            following_url=following_url,
            gists_url=gists_url,
            starred_url=starred_url,
            events_url=events_url,
            site_admin=site_admin,
            gravatar_id=gravatar_id,
            public_repos=public_repos,
            public_gists=public_gists,
            followers=followers,
            following=following,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            bio=bio,
            email=email,
            location=location,
            hireable=hireable,
            text_matches=text_matches,
            blog=blog,
            company=company,
            suspended_at=suspended_at,
        )

        user_search_result_item.additional_properties = d
        return user_search_result_item

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
