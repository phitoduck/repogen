import datetime
from typing import Any, Dict, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.public_user_plan import PublicUserPlan
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicUser")


@attr.s(auto_attribs=True)
class PublicUser:
    """Public User

    Attributes:
        login (str):
        id (int):
        node_id (str):
        avatar_url (str):
        url (str):
        html_url (str):
        followers_url (str):
        following_url (str):
        gists_url (str):
        starred_url (str):
        subscriptions_url (str):
        organizations_url (str):
        repos_url (str):
        events_url (str):
        received_events_url (str):
        type (str):
        site_admin (bool):
        public_repos (int):
        public_gists (int):
        followers (int):
        following (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        gravatar_id (Optional[str]):
        name (Optional[str]):
        company (Optional[str]):
        blog (Optional[str]):
        location (Optional[str]):
        email (Optional[str]):
        hireable (Optional[bool]):
        bio (Optional[str]):
        twitter_username (Union[Unset, None, str]):
        plan (Union[Unset, PublicUserPlan]):
        suspended_at (Union[Unset, None, datetime.datetime]):
        private_gists (Union[Unset, int]):  Example: 1.
        total_private_repos (Union[Unset, int]):  Example: 2.
        owned_private_repos (Union[Unset, int]):  Example: 2.
        disk_usage (Union[Unset, int]):  Example: 1.
        collaborators (Union[Unset, int]):  Example: 3.
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
    public_repos: int
    public_gists: int
    followers: int
    following: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    gravatar_id: Optional[str]
    name: Optional[str]
    company: Optional[str]
    blog: Optional[str]
    location: Optional[str]
    email: Optional[str]
    hireable: Optional[bool]
    bio: Optional[str]
    twitter_username: Union[Unset, None, str] = UNSET
    plan: Union[Unset, PublicUserPlan] = UNSET
    suspended_at: Union[Unset, None, datetime.datetime] = UNSET
    private_gists: Union[Unset, int] = UNSET
    total_private_repos: Union[Unset, int] = UNSET
    owned_private_repos: Union[Unset, int] = UNSET
    disk_usage: Union[Unset, int] = UNSET
    collaborators: Union[Unset, int] = UNSET

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
        public_repos = self.public_repos
        public_gists = self.public_gists
        followers = self.followers
        following = self.following
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        gravatar_id = self.gravatar_id
        name = self.name
        company = self.company
        blog = self.blog
        location = self.location
        email = self.email
        hireable = self.hireable
        bio = self.bio
        twitter_username = self.twitter_username
        plan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        suspended_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.suspended_at, Unset):
            suspended_at = self.suspended_at.isoformat() if self.suspended_at else None

        private_gists = self.private_gists
        total_private_repos = self.total_private_repos
        owned_private_repos = self.owned_private_repos
        disk_usage = self.disk_usage
        collaborators = self.collaborators

        field_dict: Dict[str, Any] = {}
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
                "public_repos": public_repos,
                "public_gists": public_gists,
                "followers": followers,
                "following": following,
                "created_at": created_at,
                "updated_at": updated_at,
                "gravatar_id": gravatar_id,
                "name": name,
                "company": company,
                "blog": blog,
                "location": location,
                "email": email,
                "hireable": hireable,
                "bio": bio,
            }
        )
        if twitter_username is not UNSET:
            field_dict["twitter_username"] = twitter_username
        if plan is not UNSET:
            field_dict["plan"] = plan
        if suspended_at is not UNSET:
            field_dict["suspended_at"] = suspended_at
        if private_gists is not UNSET:
            field_dict["private_gists"] = private_gists
        if total_private_repos is not UNSET:
            field_dict["total_private_repos"] = total_private_repos
        if owned_private_repos is not UNSET:
            field_dict["owned_private_repos"] = owned_private_repos
        if disk_usage is not UNSET:
            field_dict["disk_usage"] = disk_usage
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators

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

        public_repos = d.pop("public_repos")

        public_gists = d.pop("public_gists")

        followers = d.pop("followers")

        following = d.pop("following")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        gravatar_id = d.pop("gravatar_id")

        name = d.pop("name")

        company = d.pop("company")

        blog = d.pop("blog")

        location = d.pop("location")

        email = d.pop("email")

        hireable = d.pop("hireable")

        bio = d.pop("bio")

        twitter_username = d.pop("twitter_username", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, PublicUserPlan]
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = PublicUserPlan.from_dict(_plan)

        _suspended_at = d.pop("suspended_at", UNSET)
        suspended_at: Union[Unset, None, datetime.datetime]
        if _suspended_at is None:
            suspended_at = None
        elif isinstance(_suspended_at, Unset):
            suspended_at = UNSET
        else:
            suspended_at = isoparse(_suspended_at)

        private_gists = d.pop("private_gists", UNSET)

        total_private_repos = d.pop("total_private_repos", UNSET)

        owned_private_repos = d.pop("owned_private_repos", UNSET)

        disk_usage = d.pop("disk_usage", UNSET)

        collaborators = d.pop("collaborators", UNSET)

        public_user = cls(
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
            public_repos=public_repos,
            public_gists=public_gists,
            followers=followers,
            following=following,
            created_at=created_at,
            updated_at=updated_at,
            gravatar_id=gravatar_id,
            name=name,
            company=company,
            blog=blog,
            location=location,
            email=email,
            hireable=hireable,
            bio=bio,
            twitter_username=twitter_username,
            plan=plan,
            suspended_at=suspended_at,
            private_gists=private_gists,
            total_private_repos=total_private_repos,
            owned_private_repos=owned_private_repos,
            disk_usage=disk_usage,
            collaborators=collaborators,
        )

        return public_user
