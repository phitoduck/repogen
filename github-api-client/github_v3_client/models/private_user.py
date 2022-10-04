import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.private_user_plan import PrivateUserPlan
from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateUser")


@attr.s(auto_attribs=True)
class PrivateUser:
    """Private User

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
        public_repos (int):  Example: 2.
        public_gists (int):  Example: 1.
        followers (int):  Example: 20.
        following (int):
        created_at (datetime.datetime):  Example: 2008-01-14T04:33:35Z.
        updated_at (datetime.datetime):  Example: 2008-01-14T04:33:35Z.
        private_gists (int):  Example: 81.
        total_private_repos (int):  Example: 100.
        owned_private_repos (int):  Example: 100.
        disk_usage (int):  Example: 10000.
        collaborators (int):  Example: 8.
        two_factor_authentication (bool):  Example: True.
        gravatar_id (Optional[str]):  Example: 41d064eb2195891e12d0413f63227ea7.
        name (Optional[str]):  Example: monalisa octocat.
        company (Optional[str]):  Example: GitHub.
        blog (Optional[str]):  Example: https://github.com/blog.
        location (Optional[str]):  Example: San Francisco.
        email (Optional[str]):  Example: octocat@github.com.
        hireable (Optional[bool]):
        bio (Optional[str]):  Example: There once was....
        twitter_username (Union[Unset, None, str]):  Example: monalisa.
        plan (Union[Unset, PrivateUserPlan]):
        suspended_at (Union[Unset, None, datetime.datetime]):
        business_plus (Union[Unset, bool]):
        ldap_dn (Union[Unset, str]):
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
    private_gists: int
    total_private_repos: int
    owned_private_repos: int
    disk_usage: int
    collaborators: int
    two_factor_authentication: bool
    gravatar_id: Optional[str]
    name: Optional[str]
    company: Optional[str]
    blog: Optional[str]
    location: Optional[str]
    email: Optional[str]
    hireable: Optional[bool]
    bio: Optional[str]
    twitter_username: Union[Unset, None, str] = UNSET
    plan: Union[Unset, PrivateUserPlan] = UNSET
    suspended_at: Union[Unset, None, datetime.datetime] = UNSET
    business_plus: Union[Unset, bool] = UNSET
    ldap_dn: Union[Unset, str] = UNSET
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
        public_repos = self.public_repos
        public_gists = self.public_gists
        followers = self.followers
        following = self.following
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        private_gists = self.private_gists
        total_private_repos = self.total_private_repos
        owned_private_repos = self.owned_private_repos
        disk_usage = self.disk_usage
        collaborators = self.collaborators
        two_factor_authentication = self.two_factor_authentication
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

        business_plus = self.business_plus
        ldap_dn = self.ldap_dn

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
                "public_repos": public_repos,
                "public_gists": public_gists,
                "followers": followers,
                "following": following,
                "created_at": created_at,
                "updated_at": updated_at,
                "private_gists": private_gists,
                "total_private_repos": total_private_repos,
                "owned_private_repos": owned_private_repos,
                "disk_usage": disk_usage,
                "collaborators": collaborators,
                "two_factor_authentication": two_factor_authentication,
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
        if business_plus is not UNSET:
            field_dict["business_plus"] = business_plus
        if ldap_dn is not UNSET:
            field_dict["ldap_dn"] = ldap_dn

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

        private_gists = d.pop("private_gists")

        total_private_repos = d.pop("total_private_repos")

        owned_private_repos = d.pop("owned_private_repos")

        disk_usage = d.pop("disk_usage")

        collaborators = d.pop("collaborators")

        two_factor_authentication = d.pop("two_factor_authentication")

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
        plan: Union[Unset, PrivateUserPlan]
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = PrivateUserPlan.from_dict(_plan)

        _suspended_at = d.pop("suspended_at", UNSET)
        suspended_at: Union[Unset, None, datetime.datetime]
        if _suspended_at is None:
            suspended_at = None
        elif isinstance(_suspended_at, Unset):
            suspended_at = UNSET
        else:
            suspended_at = isoparse(_suspended_at)

        business_plus = d.pop("business_plus", UNSET)

        ldap_dn = d.pop("ldap_dn", UNSET)

        private_user = cls(
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
            private_gists=private_gists,
            total_private_repos=total_private_repos,
            owned_private_repos=owned_private_repos,
            disk_usage=disk_usage,
            collaborators=collaborators,
            two_factor_authentication=two_factor_authentication,
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
            business_plus=business_plus,
            ldap_dn=ldap_dn,
        )

        private_user.additional_properties = d
        return private_user

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
