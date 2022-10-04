import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.team_organization_plan import TeamOrganizationPlan
from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamOrganization")


@attr.s(auto_attribs=True)
class TeamOrganization:
    """Team Organization

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
        has_organization_projects (bool):  Example: True.
        has_repository_projects (bool):  Example: True.
        public_repos (int):  Example: 2.
        public_gists (int):  Example: 1.
        followers (int):  Example: 20.
        following (int):
        html_url (str):  Example: https://github.com/octocat.
        created_at (datetime.datetime):  Example: 2008-01-14T04:33:35Z.
        type (str):  Example: Organization.
        updated_at (datetime.datetime):
        description (Optional[str]):  Example: A great organization.
        name (Union[Unset, str]):  Example: github.
        company (Union[Unset, str]):  Example: GitHub.
        blog (Union[Unset, str]):  Example: https://github.com/blog.
        location (Union[Unset, str]):  Example: San Francisco.
        email (Union[Unset, str]):  Example: octocat@github.com.
        twitter_username (Union[Unset, None, str]):  Example: github.
        is_verified (Union[Unset, bool]):  Example: True.
        total_private_repos (Union[Unset, int]):  Example: 100.
        owned_private_repos (Union[Unset, int]):  Example: 100.
        private_gists (Union[Unset, None, int]):  Example: 81.
        disk_usage (Union[Unset, None, int]):  Example: 10000.
        collaborators (Union[Unset, None, int]):  Example: 8.
        billing_email (Union[Unset, None, str]):  Example: org@example.com.
        plan (Union[Unset, TeamOrganizationPlan]):
        default_repository_permission (Union[Unset, None, str]):
        members_can_create_repositories (Union[Unset, None, bool]):  Example: True.
        two_factor_requirement_enabled (Union[Unset, None, bool]):  Example: True.
        members_allowed_repository_creation_type (Union[Unset, str]):  Example: all.
        members_can_create_public_repositories (Union[Unset, bool]):  Example: True.
        members_can_create_private_repositories (Union[Unset, bool]):  Example: True.
        members_can_create_internal_repositories (Union[Unset, bool]):  Example: True.
        members_can_create_pages (Union[Unset, bool]):  Example: True.
        members_can_create_public_pages (Union[Unset, bool]):  Example: True.
        members_can_create_private_pages (Union[Unset, bool]):  Example: True.
        members_can_fork_private_repositories (Union[Unset, None, bool]):
        web_commit_signoff_required (Union[Unset, bool]):
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
    has_organization_projects: bool
    has_repository_projects: bool
    public_repos: int
    public_gists: int
    followers: int
    following: int
    html_url: str
    created_at: datetime.datetime
    type: str
    updated_at: datetime.datetime
    description: Optional[str]
    name: Union[Unset, str] = UNSET
    company: Union[Unset, str] = UNSET
    blog: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    twitter_username: Union[Unset, None, str] = UNSET
    is_verified: Union[Unset, bool] = UNSET
    total_private_repos: Union[Unset, int] = UNSET
    owned_private_repos: Union[Unset, int] = UNSET
    private_gists: Union[Unset, None, int] = UNSET
    disk_usage: Union[Unset, None, int] = UNSET
    collaborators: Union[Unset, None, int] = UNSET
    billing_email: Union[Unset, None, str] = UNSET
    plan: Union[Unset, TeamOrganizationPlan] = UNSET
    default_repository_permission: Union[Unset, None, str] = UNSET
    members_can_create_repositories: Union[Unset, None, bool] = UNSET
    two_factor_requirement_enabled: Union[Unset, None, bool] = UNSET
    members_allowed_repository_creation_type: Union[Unset, str] = UNSET
    members_can_create_public_repositories: Union[Unset, bool] = UNSET
    members_can_create_private_repositories: Union[Unset, bool] = UNSET
    members_can_create_internal_repositories: Union[Unset, bool] = UNSET
    members_can_create_pages: Union[Unset, bool] = UNSET
    members_can_create_public_pages: Union[Unset, bool] = UNSET
    members_can_create_private_pages: Union[Unset, bool] = UNSET
    members_can_fork_private_repositories: Union[Unset, None, bool] = UNSET
    web_commit_signoff_required: Union[Unset, bool] = UNSET
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
        has_organization_projects = self.has_organization_projects
        has_repository_projects = self.has_repository_projects
        public_repos = self.public_repos
        public_gists = self.public_gists
        followers = self.followers
        following = self.following
        html_url = self.html_url
        created_at = self.created_at.isoformat()

        type = self.type
        updated_at = self.updated_at.isoformat()

        description = self.description
        name = self.name
        company = self.company
        blog = self.blog
        location = self.location
        email = self.email
        twitter_username = self.twitter_username
        is_verified = self.is_verified
        total_private_repos = self.total_private_repos
        owned_private_repos = self.owned_private_repos
        private_gists = self.private_gists
        disk_usage = self.disk_usage
        collaborators = self.collaborators
        billing_email = self.billing_email
        plan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        default_repository_permission = self.default_repository_permission
        members_can_create_repositories = self.members_can_create_repositories
        two_factor_requirement_enabled = self.two_factor_requirement_enabled
        members_allowed_repository_creation_type = self.members_allowed_repository_creation_type
        members_can_create_public_repositories = self.members_can_create_public_repositories
        members_can_create_private_repositories = self.members_can_create_private_repositories
        members_can_create_internal_repositories = self.members_can_create_internal_repositories
        members_can_create_pages = self.members_can_create_pages
        members_can_create_public_pages = self.members_can_create_public_pages
        members_can_create_private_pages = self.members_can_create_private_pages
        members_can_fork_private_repositories = self.members_can_fork_private_repositories
        web_commit_signoff_required = self.web_commit_signoff_required

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
                "has_organization_projects": has_organization_projects,
                "has_repository_projects": has_repository_projects,
                "public_repos": public_repos,
                "public_gists": public_gists,
                "followers": followers,
                "following": following,
                "html_url": html_url,
                "created_at": created_at,
                "type": type,
                "updated_at": updated_at,
                "description": description,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if company is not UNSET:
            field_dict["company"] = company
        if blog is not UNSET:
            field_dict["blog"] = blog
        if location is not UNSET:
            field_dict["location"] = location
        if email is not UNSET:
            field_dict["email"] = email
        if twitter_username is not UNSET:
            field_dict["twitter_username"] = twitter_username
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified
        if total_private_repos is not UNSET:
            field_dict["total_private_repos"] = total_private_repos
        if owned_private_repos is not UNSET:
            field_dict["owned_private_repos"] = owned_private_repos
        if private_gists is not UNSET:
            field_dict["private_gists"] = private_gists
        if disk_usage is not UNSET:
            field_dict["disk_usage"] = disk_usage
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators
        if billing_email is not UNSET:
            field_dict["billing_email"] = billing_email
        if plan is not UNSET:
            field_dict["plan"] = plan
        if default_repository_permission is not UNSET:
            field_dict["default_repository_permission"] = default_repository_permission
        if members_can_create_repositories is not UNSET:
            field_dict["members_can_create_repositories"] = members_can_create_repositories
        if two_factor_requirement_enabled is not UNSET:
            field_dict["two_factor_requirement_enabled"] = two_factor_requirement_enabled
        if members_allowed_repository_creation_type is not UNSET:
            field_dict["members_allowed_repository_creation_type"] = members_allowed_repository_creation_type
        if members_can_create_public_repositories is not UNSET:
            field_dict["members_can_create_public_repositories"] = members_can_create_public_repositories
        if members_can_create_private_repositories is not UNSET:
            field_dict["members_can_create_private_repositories"] = members_can_create_private_repositories
        if members_can_create_internal_repositories is not UNSET:
            field_dict["members_can_create_internal_repositories"] = members_can_create_internal_repositories
        if members_can_create_pages is not UNSET:
            field_dict["members_can_create_pages"] = members_can_create_pages
        if members_can_create_public_pages is not UNSET:
            field_dict["members_can_create_public_pages"] = members_can_create_public_pages
        if members_can_create_private_pages is not UNSET:
            field_dict["members_can_create_private_pages"] = members_can_create_private_pages
        if members_can_fork_private_repositories is not UNSET:
            field_dict["members_can_fork_private_repositories"] = members_can_fork_private_repositories
        if web_commit_signoff_required is not UNSET:
            field_dict["web_commit_signoff_required"] = web_commit_signoff_required

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

        has_organization_projects = d.pop("has_organization_projects")

        has_repository_projects = d.pop("has_repository_projects")

        public_repos = d.pop("public_repos")

        public_gists = d.pop("public_gists")

        followers = d.pop("followers")

        following = d.pop("following")

        html_url = d.pop("html_url")

        created_at = isoparse(d.pop("created_at"))

        type = d.pop("type")

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description")

        name = d.pop("name", UNSET)

        company = d.pop("company", UNSET)

        blog = d.pop("blog", UNSET)

        location = d.pop("location", UNSET)

        email = d.pop("email", UNSET)

        twitter_username = d.pop("twitter_username", UNSET)

        is_verified = d.pop("is_verified", UNSET)

        total_private_repos = d.pop("total_private_repos", UNSET)

        owned_private_repos = d.pop("owned_private_repos", UNSET)

        private_gists = d.pop("private_gists", UNSET)

        disk_usage = d.pop("disk_usage", UNSET)

        collaborators = d.pop("collaborators", UNSET)

        billing_email = d.pop("billing_email", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, TeamOrganizationPlan]
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = TeamOrganizationPlan.from_dict(_plan)

        default_repository_permission = d.pop("default_repository_permission", UNSET)

        members_can_create_repositories = d.pop("members_can_create_repositories", UNSET)

        two_factor_requirement_enabled = d.pop("two_factor_requirement_enabled", UNSET)

        members_allowed_repository_creation_type = d.pop("members_allowed_repository_creation_type", UNSET)

        members_can_create_public_repositories = d.pop("members_can_create_public_repositories", UNSET)

        members_can_create_private_repositories = d.pop("members_can_create_private_repositories", UNSET)

        members_can_create_internal_repositories = d.pop("members_can_create_internal_repositories", UNSET)

        members_can_create_pages = d.pop("members_can_create_pages", UNSET)

        members_can_create_public_pages = d.pop("members_can_create_public_pages", UNSET)

        members_can_create_private_pages = d.pop("members_can_create_private_pages", UNSET)

        members_can_fork_private_repositories = d.pop("members_can_fork_private_repositories", UNSET)

        web_commit_signoff_required = d.pop("web_commit_signoff_required", UNSET)

        team_organization = cls(
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
            has_organization_projects=has_organization_projects,
            has_repository_projects=has_repository_projects,
            public_repos=public_repos,
            public_gists=public_gists,
            followers=followers,
            following=following,
            html_url=html_url,
            created_at=created_at,
            type=type,
            updated_at=updated_at,
            description=description,
            name=name,
            company=company,
            blog=blog,
            location=location,
            email=email,
            twitter_username=twitter_username,
            is_verified=is_verified,
            total_private_repos=total_private_repos,
            owned_private_repos=owned_private_repos,
            private_gists=private_gists,
            disk_usage=disk_usage,
            collaborators=collaborators,
            billing_email=billing_email,
            plan=plan,
            default_repository_permission=default_repository_permission,
            members_can_create_repositories=members_can_create_repositories,
            two_factor_requirement_enabled=two_factor_requirement_enabled,
            members_allowed_repository_creation_type=members_allowed_repository_creation_type,
            members_can_create_public_repositories=members_can_create_public_repositories,
            members_can_create_private_repositories=members_can_create_private_repositories,
            members_can_create_internal_repositories=members_can_create_internal_repositories,
            members_can_create_pages=members_can_create_pages,
            members_can_create_public_pages=members_can_create_public_pages,
            members_can_create_private_pages=members_can_create_private_pages,
            members_can_fork_private_repositories=members_can_fork_private_repositories,
            web_commit_signoff_required=web_commit_signoff_required,
        )

        team_organization.additional_properties = d
        return team_organization

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
