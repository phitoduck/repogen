import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.license_simple import LicenseSimple
from ..models.repo_search_result_item_permissions import RepoSearchResultItemPermissions
from ..models.search_result_text_matches_item import SearchResultTextMatchesItem
from ..models.simple_user import SimpleUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepoSearchResultItem")


@attr.s(auto_attribs=True)
class RepoSearchResultItem:
    """Repo Search Result Item

    Attributes:
        id (int):
        node_id (str):
        name (str):
        full_name (str):
        private (bool):
        html_url (str):
        fork (bool):
        url (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        pushed_at (datetime.datetime):
        size (int):
        stargazers_count (int):
        watchers_count (int):
        forks_count (int):
        open_issues_count (int):
        default_branch (str):
        score (float):
        forks_url (str):
        keys_url (str):
        collaborators_url (str):
        teams_url (str):
        hooks_url (str):
        issue_events_url (str):
        events_url (str):
        assignees_url (str):
        branches_url (str):
        tags_url (str):
        blobs_url (str):
        git_tags_url (str):
        git_refs_url (str):
        trees_url (str):
        statuses_url (str):
        languages_url (str):
        stargazers_url (str):
        contributors_url (str):
        subscribers_url (str):
        subscription_url (str):
        commits_url (str):
        git_commits_url (str):
        comments_url (str):
        issue_comment_url (str):
        contents_url (str):
        compare_url (str):
        merges_url (str):
        archive_url (str):
        downloads_url (str):
        issues_url (str):
        pulls_url (str):
        milestones_url (str):
        notifications_url (str):
        labels_url (str):
        releases_url (str):
        deployments_url (str):
        git_url (str):
        ssh_url (str):
        clone_url (str):
        svn_url (str):
        forks (int):
        open_issues (int):
        watchers (int):
        has_issues (bool):
        has_projects (bool):
        has_pages (bool):
        has_wiki (bool):
        has_downloads (bool):
        archived (bool):
        disabled (bool): Returns whether or not this repository disabled.
        owner (Optional[SimpleUser]): Simple User
        description (Optional[str]):
        homepage (Optional[str]):
        language (Optional[str]):
        master_branch (Union[Unset, str]):
        topics (Union[Unset, List[str]]):
        mirror_url (Optional[str]):
        visibility (Union[Unset, str]): The repository visibility: public, private, or internal.
        license_ (Optional[LicenseSimple]): License Simple
        permissions (Union[Unset, RepoSearchResultItemPermissions]):
        text_matches (Union[Unset, List[SearchResultTextMatchesItem]]):
        temp_clone_token (Union[Unset, str]):
        allow_merge_commit (Union[Unset, bool]):
        allow_squash_merge (Union[Unset, bool]):
        allow_rebase_merge (Union[Unset, bool]):
        allow_auto_merge (Union[Unset, bool]):
        delete_branch_on_merge (Union[Unset, bool]):
        allow_forking (Union[Unset, bool]):
        is_template (Union[Unset, bool]):
        web_commit_signoff_required (Union[Unset, bool]):
    """

    id: int
    node_id: str
    name: str
    full_name: str
    private: bool
    html_url: str
    fork: bool
    url: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    pushed_at: datetime.datetime
    size: int
    stargazers_count: int
    watchers_count: int
    forks_count: int
    open_issues_count: int
    default_branch: str
    score: float
    forks_url: str
    keys_url: str
    collaborators_url: str
    teams_url: str
    hooks_url: str
    issue_events_url: str
    events_url: str
    assignees_url: str
    branches_url: str
    tags_url: str
    blobs_url: str
    git_tags_url: str
    git_refs_url: str
    trees_url: str
    statuses_url: str
    languages_url: str
    stargazers_url: str
    contributors_url: str
    subscribers_url: str
    subscription_url: str
    commits_url: str
    git_commits_url: str
    comments_url: str
    issue_comment_url: str
    contents_url: str
    compare_url: str
    merges_url: str
    archive_url: str
    downloads_url: str
    issues_url: str
    pulls_url: str
    milestones_url: str
    notifications_url: str
    labels_url: str
    releases_url: str
    deployments_url: str
    git_url: str
    ssh_url: str
    clone_url: str
    svn_url: str
    forks: int
    open_issues: int
    watchers: int
    has_issues: bool
    has_projects: bool
    has_pages: bool
    has_wiki: bool
    has_downloads: bool
    archived: bool
    disabled: bool
    owner: Optional[SimpleUser]
    description: Optional[str]
    homepage: Optional[str]
    language: Optional[str]
    mirror_url: Optional[str]
    license_: Optional[LicenseSimple]
    master_branch: Union[Unset, str] = UNSET
    topics: Union[Unset, List[str]] = UNSET
    visibility: Union[Unset, str] = UNSET
    permissions: Union[Unset, RepoSearchResultItemPermissions] = UNSET
    text_matches: Union[Unset, List[SearchResultTextMatchesItem]] = UNSET
    temp_clone_token: Union[Unset, str] = UNSET
    allow_merge_commit: Union[Unset, bool] = UNSET
    allow_squash_merge: Union[Unset, bool] = UNSET
    allow_rebase_merge: Union[Unset, bool] = UNSET
    allow_auto_merge: Union[Unset, bool] = UNSET
    delete_branch_on_merge: Union[Unset, bool] = UNSET
    allow_forking: Union[Unset, bool] = UNSET
    is_template: Union[Unset, bool] = UNSET
    web_commit_signoff_required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        name = self.name
        full_name = self.full_name
        private = self.private
        html_url = self.html_url
        fork = self.fork
        url = self.url
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        pushed_at = self.pushed_at.isoformat()

        size = self.size
        stargazers_count = self.stargazers_count
        watchers_count = self.watchers_count
        forks_count = self.forks_count
        open_issues_count = self.open_issues_count
        default_branch = self.default_branch
        score = self.score
        forks_url = self.forks_url
        keys_url = self.keys_url
        collaborators_url = self.collaborators_url
        teams_url = self.teams_url
        hooks_url = self.hooks_url
        issue_events_url = self.issue_events_url
        events_url = self.events_url
        assignees_url = self.assignees_url
        branches_url = self.branches_url
        tags_url = self.tags_url
        blobs_url = self.blobs_url
        git_tags_url = self.git_tags_url
        git_refs_url = self.git_refs_url
        trees_url = self.trees_url
        statuses_url = self.statuses_url
        languages_url = self.languages_url
        stargazers_url = self.stargazers_url
        contributors_url = self.contributors_url
        subscribers_url = self.subscribers_url
        subscription_url = self.subscription_url
        commits_url = self.commits_url
        git_commits_url = self.git_commits_url
        comments_url = self.comments_url
        issue_comment_url = self.issue_comment_url
        contents_url = self.contents_url
        compare_url = self.compare_url
        merges_url = self.merges_url
        archive_url = self.archive_url
        downloads_url = self.downloads_url
        issues_url = self.issues_url
        pulls_url = self.pulls_url
        milestones_url = self.milestones_url
        notifications_url = self.notifications_url
        labels_url = self.labels_url
        releases_url = self.releases_url
        deployments_url = self.deployments_url
        git_url = self.git_url
        ssh_url = self.ssh_url
        clone_url = self.clone_url
        svn_url = self.svn_url
        forks = self.forks
        open_issues = self.open_issues
        watchers = self.watchers
        has_issues = self.has_issues
        has_projects = self.has_projects
        has_pages = self.has_pages
        has_wiki = self.has_wiki
        has_downloads = self.has_downloads
        archived = self.archived
        disabled = self.disabled
        owner = self.owner.to_dict() if self.owner else None

        description = self.description
        homepage = self.homepage
        language = self.language
        master_branch = self.master_branch
        topics: Union[Unset, List[str]] = UNSET
        if not isinstance(self.topics, Unset):
            topics = self.topics

        mirror_url = self.mirror_url
        visibility = self.visibility
        license_ = self.license_.to_dict() if self.license_ else None

        permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        text_matches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.text_matches, Unset):
            text_matches = []
            for componentsschemassearch_result_text_matches_item_data in self.text_matches:
                componentsschemassearch_result_text_matches_item = (
                    componentsschemassearch_result_text_matches_item_data.to_dict()
                )

                text_matches.append(componentsschemassearch_result_text_matches_item)

        temp_clone_token = self.temp_clone_token
        allow_merge_commit = self.allow_merge_commit
        allow_squash_merge = self.allow_squash_merge
        allow_rebase_merge = self.allow_rebase_merge
        allow_auto_merge = self.allow_auto_merge
        delete_branch_on_merge = self.delete_branch_on_merge
        allow_forking = self.allow_forking
        is_template = self.is_template
        web_commit_signoff_required = self.web_commit_signoff_required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "node_id": node_id,
                "name": name,
                "full_name": full_name,
                "private": private,
                "html_url": html_url,
                "fork": fork,
                "url": url,
                "created_at": created_at,
                "updated_at": updated_at,
                "pushed_at": pushed_at,
                "size": size,
                "stargazers_count": stargazers_count,
                "watchers_count": watchers_count,
                "forks_count": forks_count,
                "open_issues_count": open_issues_count,
                "default_branch": default_branch,
                "score": score,
                "forks_url": forks_url,
                "keys_url": keys_url,
                "collaborators_url": collaborators_url,
                "teams_url": teams_url,
                "hooks_url": hooks_url,
                "issue_events_url": issue_events_url,
                "events_url": events_url,
                "assignees_url": assignees_url,
                "branches_url": branches_url,
                "tags_url": tags_url,
                "blobs_url": blobs_url,
                "git_tags_url": git_tags_url,
                "git_refs_url": git_refs_url,
                "trees_url": trees_url,
                "statuses_url": statuses_url,
                "languages_url": languages_url,
                "stargazers_url": stargazers_url,
                "contributors_url": contributors_url,
                "subscribers_url": subscribers_url,
                "subscription_url": subscription_url,
                "commits_url": commits_url,
                "git_commits_url": git_commits_url,
                "comments_url": comments_url,
                "issue_comment_url": issue_comment_url,
                "contents_url": contents_url,
                "compare_url": compare_url,
                "merges_url": merges_url,
                "archive_url": archive_url,
                "downloads_url": downloads_url,
                "issues_url": issues_url,
                "pulls_url": pulls_url,
                "milestones_url": milestones_url,
                "notifications_url": notifications_url,
                "labels_url": labels_url,
                "releases_url": releases_url,
                "deployments_url": deployments_url,
                "git_url": git_url,
                "ssh_url": ssh_url,
                "clone_url": clone_url,
                "svn_url": svn_url,
                "forks": forks,
                "open_issues": open_issues,
                "watchers": watchers,
                "has_issues": has_issues,
                "has_projects": has_projects,
                "has_pages": has_pages,
                "has_wiki": has_wiki,
                "has_downloads": has_downloads,
                "archived": archived,
                "disabled": disabled,
                "owner": owner,
                "description": description,
                "homepage": homepage,
                "language": language,
                "mirror_url": mirror_url,
                "license": license_,
            }
        )
        if master_branch is not UNSET:
            field_dict["master_branch"] = master_branch
        if topics is not UNSET:
            field_dict["topics"] = topics
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if text_matches is not UNSET:
            field_dict["text_matches"] = text_matches
        if temp_clone_token is not UNSET:
            field_dict["temp_clone_token"] = temp_clone_token
        if allow_merge_commit is not UNSET:
            field_dict["allow_merge_commit"] = allow_merge_commit
        if allow_squash_merge is not UNSET:
            field_dict["allow_squash_merge"] = allow_squash_merge
        if allow_rebase_merge is not UNSET:
            field_dict["allow_rebase_merge"] = allow_rebase_merge
        if allow_auto_merge is not UNSET:
            field_dict["allow_auto_merge"] = allow_auto_merge
        if delete_branch_on_merge is not UNSET:
            field_dict["delete_branch_on_merge"] = delete_branch_on_merge
        if allow_forking is not UNSET:
            field_dict["allow_forking"] = allow_forking
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
        if web_commit_signoff_required is not UNSET:
            field_dict["web_commit_signoff_required"] = web_commit_signoff_required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        node_id = d.pop("node_id")

        name = d.pop("name")

        full_name = d.pop("full_name")

        private = d.pop("private")

        html_url = d.pop("html_url")

        fork = d.pop("fork")

        url = d.pop("url")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        pushed_at = isoparse(d.pop("pushed_at"))

        size = d.pop("size")

        stargazers_count = d.pop("stargazers_count")

        watchers_count = d.pop("watchers_count")

        forks_count = d.pop("forks_count")

        open_issues_count = d.pop("open_issues_count")

        default_branch = d.pop("default_branch")

        score = d.pop("score")

        forks_url = d.pop("forks_url")

        keys_url = d.pop("keys_url")

        collaborators_url = d.pop("collaborators_url")

        teams_url = d.pop("teams_url")

        hooks_url = d.pop("hooks_url")

        issue_events_url = d.pop("issue_events_url")

        events_url = d.pop("events_url")

        assignees_url = d.pop("assignees_url")

        branches_url = d.pop("branches_url")

        tags_url = d.pop("tags_url")

        blobs_url = d.pop("blobs_url")

        git_tags_url = d.pop("git_tags_url")

        git_refs_url = d.pop("git_refs_url")

        trees_url = d.pop("trees_url")

        statuses_url = d.pop("statuses_url")

        languages_url = d.pop("languages_url")

        stargazers_url = d.pop("stargazers_url")

        contributors_url = d.pop("contributors_url")

        subscribers_url = d.pop("subscribers_url")

        subscription_url = d.pop("subscription_url")

        commits_url = d.pop("commits_url")

        git_commits_url = d.pop("git_commits_url")

        comments_url = d.pop("comments_url")

        issue_comment_url = d.pop("issue_comment_url")

        contents_url = d.pop("contents_url")

        compare_url = d.pop("compare_url")

        merges_url = d.pop("merges_url")

        archive_url = d.pop("archive_url")

        downloads_url = d.pop("downloads_url")

        issues_url = d.pop("issues_url")

        pulls_url = d.pop("pulls_url")

        milestones_url = d.pop("milestones_url")

        notifications_url = d.pop("notifications_url")

        labels_url = d.pop("labels_url")

        releases_url = d.pop("releases_url")

        deployments_url = d.pop("deployments_url")

        git_url = d.pop("git_url")

        ssh_url = d.pop("ssh_url")

        clone_url = d.pop("clone_url")

        svn_url = d.pop("svn_url")

        forks = d.pop("forks")

        open_issues = d.pop("open_issues")

        watchers = d.pop("watchers")

        has_issues = d.pop("has_issues")

        has_projects = d.pop("has_projects")

        has_pages = d.pop("has_pages")

        has_wiki = d.pop("has_wiki")

        has_downloads = d.pop("has_downloads")

        archived = d.pop("archived")

        disabled = d.pop("disabled")

        _owner = d.pop("owner")
        owner: Optional[SimpleUser]
        if _owner is None:
            owner = None
        else:
            owner = SimpleUser.from_dict(_owner)

        description = d.pop("description")

        homepage = d.pop("homepage")

        language = d.pop("language")

        master_branch = d.pop("master_branch", UNSET)

        topics = cast(List[str], d.pop("topics", UNSET))

        mirror_url = d.pop("mirror_url")

        visibility = d.pop("visibility", UNSET)

        _license_ = d.pop("license")
        license_: Optional[LicenseSimple]
        if _license_ is None:
            license_ = None
        else:
            license_ = LicenseSimple.from_dict(_license_)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, RepoSearchResultItemPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = RepoSearchResultItemPermissions.from_dict(_permissions)

        text_matches = []
        _text_matches = d.pop("text_matches", UNSET)
        for componentsschemassearch_result_text_matches_item_data in _text_matches or []:
            componentsschemassearch_result_text_matches_item = SearchResultTextMatchesItem.from_dict(
                componentsschemassearch_result_text_matches_item_data
            )

            text_matches.append(componentsschemassearch_result_text_matches_item)

        temp_clone_token = d.pop("temp_clone_token", UNSET)

        allow_merge_commit = d.pop("allow_merge_commit", UNSET)

        allow_squash_merge = d.pop("allow_squash_merge", UNSET)

        allow_rebase_merge = d.pop("allow_rebase_merge", UNSET)

        allow_auto_merge = d.pop("allow_auto_merge", UNSET)

        delete_branch_on_merge = d.pop("delete_branch_on_merge", UNSET)

        allow_forking = d.pop("allow_forking", UNSET)

        is_template = d.pop("is_template", UNSET)

        web_commit_signoff_required = d.pop("web_commit_signoff_required", UNSET)

        repo_search_result_item = cls(
            id=id,
            node_id=node_id,
            name=name,
            full_name=full_name,
            private=private,
            html_url=html_url,
            fork=fork,
            url=url,
            created_at=created_at,
            updated_at=updated_at,
            pushed_at=pushed_at,
            size=size,
            stargazers_count=stargazers_count,
            watchers_count=watchers_count,
            forks_count=forks_count,
            open_issues_count=open_issues_count,
            default_branch=default_branch,
            score=score,
            forks_url=forks_url,
            keys_url=keys_url,
            collaborators_url=collaborators_url,
            teams_url=teams_url,
            hooks_url=hooks_url,
            issue_events_url=issue_events_url,
            events_url=events_url,
            assignees_url=assignees_url,
            branches_url=branches_url,
            tags_url=tags_url,
            blobs_url=blobs_url,
            git_tags_url=git_tags_url,
            git_refs_url=git_refs_url,
            trees_url=trees_url,
            statuses_url=statuses_url,
            languages_url=languages_url,
            stargazers_url=stargazers_url,
            contributors_url=contributors_url,
            subscribers_url=subscribers_url,
            subscription_url=subscription_url,
            commits_url=commits_url,
            git_commits_url=git_commits_url,
            comments_url=comments_url,
            issue_comment_url=issue_comment_url,
            contents_url=contents_url,
            compare_url=compare_url,
            merges_url=merges_url,
            archive_url=archive_url,
            downloads_url=downloads_url,
            issues_url=issues_url,
            pulls_url=pulls_url,
            milestones_url=milestones_url,
            notifications_url=notifications_url,
            labels_url=labels_url,
            releases_url=releases_url,
            deployments_url=deployments_url,
            git_url=git_url,
            ssh_url=ssh_url,
            clone_url=clone_url,
            svn_url=svn_url,
            forks=forks,
            open_issues=open_issues,
            watchers=watchers,
            has_issues=has_issues,
            has_projects=has_projects,
            has_pages=has_pages,
            has_wiki=has_wiki,
            has_downloads=has_downloads,
            archived=archived,
            disabled=disabled,
            owner=owner,
            description=description,
            homepage=homepage,
            language=language,
            master_branch=master_branch,
            topics=topics,
            mirror_url=mirror_url,
            visibility=visibility,
            license_=license_,
            permissions=permissions,
            text_matches=text_matches,
            temp_clone_token=temp_clone_token,
            allow_merge_commit=allow_merge_commit,
            allow_squash_merge=allow_squash_merge,
            allow_rebase_merge=allow_rebase_merge,
            allow_auto_merge=allow_auto_merge,
            delete_branch_on_merge=delete_branch_on_merge,
            allow_forking=allow_forking,
            is_template=is_template,
            web_commit_signoff_required=web_commit_signoff_required,
        )

        repo_search_result_item.additional_properties = d
        return repo_search_result_item

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
