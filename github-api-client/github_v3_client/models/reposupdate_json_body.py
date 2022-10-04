from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reposupdate_json_body_merge_commit_message import ReposupdateJsonBodyMergeCommitMessage
from ..models.reposupdate_json_body_merge_commit_title import ReposupdateJsonBodyMergeCommitTitle
from ..models.reposupdate_json_body_security_and_analysis import ReposupdateJsonBodySecurityAndAnalysis
from ..models.reposupdate_json_body_squash_merge_commit_message import ReposupdateJsonBodySquashMergeCommitMessage
from ..models.reposupdate_json_body_squash_merge_commit_title import ReposupdateJsonBodySquashMergeCommitTitle
from ..models.reposupdate_json_body_visibility import ReposupdateJsonBodyVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdateJsonBody")


@attr.s(auto_attribs=True)
class ReposupdateJsonBody:
    """
    Attributes:
        name (Union[Unset, str]): The name of the repository.
        description (Union[Unset, str]): A short description of the repository.
        homepage (Union[Unset, str]): A URL with more information about the repository.
        private (Union[Unset, bool]): Either `true` to make the repository private or `false` to make it public.
            Default: `false`.
            **Note**: You will get a `422` error if the organization restricts [changing repository
            visibility](https://docs.github.com/articles/repository-permission-levels-for-an-organization#changing-the-
            visibility-of-repositories) to organization owners and a non-owner tries to change the value of private.
        visibility (Union[Unset, ReposupdateJsonBodyVisibility]): Can be `public` or `private`. If your organization is
            associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+,
            `visibility` can also be `internal`."
        security_and_analysis (Union[Unset, None, ReposupdateJsonBodySecurityAndAnalysis]): Specify which security and
            analysis features to enable or disable for the repository.

            To use this parameter, you must have admin permissions for the repository or be an owner or security manager for
            the organization that owns the repository. For more information, see "[Managing security managers in your
            organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-
            roles/managing-security-managers-in-your-organization)."

            For example, to enable GitHub Advanced Security, use this data in the body of the `PATCH` request:
            `{ "security_and_analysis": {"advanced_security": { "status": "enabled" } } }`.

            You can check which security and analysis features are currently enabled by using a `GET /repos/{owner}/{repo}`
            request.
        has_issues (Union[Unset, bool]): Either `true` to enable issues for this repository or `false` to disable them.
            Default: True.
        has_projects (Union[Unset, bool]): Either `true` to enable projects for this repository or `false` to disable
            them. **Note:** If you're creating a repository in an organization that has disabled repository projects, the
            default is `false`, and if you pass `true`, the API returns an error. Default: True.
        has_wiki (Union[Unset, bool]): Either `true` to enable the wiki for this repository or `false` to disable it.
            Default: True.
        is_template (Union[Unset, bool]): Either `true` to make this repo available as a template repository or `false`
            to prevent it.
        default_branch (Union[Unset, str]): Updates the default branch for this repository.
        allow_squash_merge (Union[Unset, bool]): Either `true` to allow squash-merging pull requests, or `false` to
            prevent squash-merging. Default: True.
        allow_merge_commit (Union[Unset, bool]): Either `true` to allow merging pull requests with a merge commit, or
            `false` to prevent merging pull requests with merge commits. Default: True.
        allow_rebase_merge (Union[Unset, bool]): Either `true` to allow rebase-merging pull requests, or `false` to
            prevent rebase-merging. Default: True.
        allow_auto_merge (Union[Unset, bool]): Either `true` to allow auto-merge on pull requests, or `false` to
            disallow auto-merge.
        delete_branch_on_merge (Union[Unset, bool]): Either `true` to allow automatically deleting head branches when
            pull requests are merged, or `false` to prevent automatic deletion.
        allow_update_branch (Union[Unset, bool]): Either `true` to always allow a pull request head branch that is
            behind its base branch to be updated even if it is not required to be up to date before merging, or false
            otherwise.
        use_squash_pr_title_as_default (Union[Unset, bool]): Either `true` to allow squash-merge commits to use pull
            request title, or `false` to use commit message. **This property has been deprecated. Please use
            `squash_merge_commit_title` instead.
        squash_merge_commit_title (Union[Unset, ReposupdateJsonBodySquashMergeCommitTitle]): The default value for a
            squash merge commit title:

            - `PR_TITLE` - default to the pull request's title.
            - `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when
            more than one commit).
        squash_merge_commit_message (Union[Unset, ReposupdateJsonBodySquashMergeCommitMessage]): The default value for a
            squash merge commit message:

            - `PR_BODY` - default to the pull request's body.
            - `COMMIT_MESSAGES` - default to the branch's commit messages.
            - `BLANK` - default to a blank commit message.
        merge_commit_title (Union[Unset, ReposupdateJsonBodyMergeCommitTitle]): The default value for a merge commit
            title.

            - `PR_TITLE` - default to the pull request's title.
            - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-
            name).
        merge_commit_message (Union[Unset, ReposupdateJsonBodyMergeCommitMessage]): The default value for a merge commit
            message.

            - `PR_TITLE` - default to the pull request's title.
            - `PR_BODY` - default to the pull request's body.
            - `BLANK` - default to a blank commit message.
        archived (Union[Unset, bool]): `true` to archive this repository. **Note**: You cannot unarchive repositories
            through the API.
        allow_forking (Union[Unset, bool]): Either `true` to allow private forks, or `false` to prevent private forks.
        web_commit_signoff_required (Union[Unset, bool]): Either `true` to require contributors to sign off on web-based
            commits, or `false` to not require contributors to sign off on web-based commits.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    homepage: Union[Unset, str] = UNSET
    private: Union[Unset, bool] = False
    visibility: Union[Unset, ReposupdateJsonBodyVisibility] = UNSET
    security_and_analysis: Union[Unset, None, ReposupdateJsonBodySecurityAndAnalysis] = UNSET
    has_issues: Union[Unset, bool] = True
    has_projects: Union[Unset, bool] = True
    has_wiki: Union[Unset, bool] = True
    is_template: Union[Unset, bool] = False
    default_branch: Union[Unset, str] = UNSET
    allow_squash_merge: Union[Unset, bool] = True
    allow_merge_commit: Union[Unset, bool] = True
    allow_rebase_merge: Union[Unset, bool] = True
    allow_auto_merge: Union[Unset, bool] = False
    delete_branch_on_merge: Union[Unset, bool] = False
    allow_update_branch: Union[Unset, bool] = False
    use_squash_pr_title_as_default: Union[Unset, bool] = False
    squash_merge_commit_title: Union[Unset, ReposupdateJsonBodySquashMergeCommitTitle] = UNSET
    squash_merge_commit_message: Union[Unset, ReposupdateJsonBodySquashMergeCommitMessage] = UNSET
    merge_commit_title: Union[Unset, ReposupdateJsonBodyMergeCommitTitle] = UNSET
    merge_commit_message: Union[Unset, ReposupdateJsonBodyMergeCommitMessage] = UNSET
    archived: Union[Unset, bool] = False
    allow_forking: Union[Unset, bool] = False
    web_commit_signoff_required: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        homepage = self.homepage
        private = self.private
        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        security_and_analysis: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.security_and_analysis, Unset):
            security_and_analysis = self.security_and_analysis.to_dict() if self.security_and_analysis else None

        has_issues = self.has_issues
        has_projects = self.has_projects
        has_wiki = self.has_wiki
        is_template = self.is_template
        default_branch = self.default_branch
        allow_squash_merge = self.allow_squash_merge
        allow_merge_commit = self.allow_merge_commit
        allow_rebase_merge = self.allow_rebase_merge
        allow_auto_merge = self.allow_auto_merge
        delete_branch_on_merge = self.delete_branch_on_merge
        allow_update_branch = self.allow_update_branch
        use_squash_pr_title_as_default = self.use_squash_pr_title_as_default
        squash_merge_commit_title: Union[Unset, str] = UNSET
        if not isinstance(self.squash_merge_commit_title, Unset):
            squash_merge_commit_title = self.squash_merge_commit_title.value

        squash_merge_commit_message: Union[Unset, str] = UNSET
        if not isinstance(self.squash_merge_commit_message, Unset):
            squash_merge_commit_message = self.squash_merge_commit_message.value

        merge_commit_title: Union[Unset, str] = UNSET
        if not isinstance(self.merge_commit_title, Unset):
            merge_commit_title = self.merge_commit_title.value

        merge_commit_message: Union[Unset, str] = UNSET
        if not isinstance(self.merge_commit_message, Unset):
            merge_commit_message = self.merge_commit_message.value

        archived = self.archived
        allow_forking = self.allow_forking
        web_commit_signoff_required = self.web_commit_signoff_required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if private is not UNSET:
            field_dict["private"] = private
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if security_and_analysis is not UNSET:
            field_dict["security_and_analysis"] = security_and_analysis
        if has_issues is not UNSET:
            field_dict["has_issues"] = has_issues
        if has_projects is not UNSET:
            field_dict["has_projects"] = has_projects
        if has_wiki is not UNSET:
            field_dict["has_wiki"] = has_wiki
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
        if default_branch is not UNSET:
            field_dict["default_branch"] = default_branch
        if allow_squash_merge is not UNSET:
            field_dict["allow_squash_merge"] = allow_squash_merge
        if allow_merge_commit is not UNSET:
            field_dict["allow_merge_commit"] = allow_merge_commit
        if allow_rebase_merge is not UNSET:
            field_dict["allow_rebase_merge"] = allow_rebase_merge
        if allow_auto_merge is not UNSET:
            field_dict["allow_auto_merge"] = allow_auto_merge
        if delete_branch_on_merge is not UNSET:
            field_dict["delete_branch_on_merge"] = delete_branch_on_merge
        if allow_update_branch is not UNSET:
            field_dict["allow_update_branch"] = allow_update_branch
        if use_squash_pr_title_as_default is not UNSET:
            field_dict["use_squash_pr_title_as_default"] = use_squash_pr_title_as_default
        if squash_merge_commit_title is not UNSET:
            field_dict["squash_merge_commit_title"] = squash_merge_commit_title
        if squash_merge_commit_message is not UNSET:
            field_dict["squash_merge_commit_message"] = squash_merge_commit_message
        if merge_commit_title is not UNSET:
            field_dict["merge_commit_title"] = merge_commit_title
        if merge_commit_message is not UNSET:
            field_dict["merge_commit_message"] = merge_commit_message
        if archived is not UNSET:
            field_dict["archived"] = archived
        if allow_forking is not UNSET:
            field_dict["allow_forking"] = allow_forking
        if web_commit_signoff_required is not UNSET:
            field_dict["web_commit_signoff_required"] = web_commit_signoff_required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        homepage = d.pop("homepage", UNSET)

        private = d.pop("private", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, ReposupdateJsonBodyVisibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = ReposupdateJsonBodyVisibility(_visibility)

        _security_and_analysis = d.pop("security_and_analysis", UNSET)
        security_and_analysis: Union[Unset, None, ReposupdateJsonBodySecurityAndAnalysis]
        if _security_and_analysis is None:
            security_and_analysis = None
        elif isinstance(_security_and_analysis, Unset):
            security_and_analysis = UNSET
        else:
            security_and_analysis = ReposupdateJsonBodySecurityAndAnalysis.from_dict(_security_and_analysis)

        has_issues = d.pop("has_issues", UNSET)

        has_projects = d.pop("has_projects", UNSET)

        has_wiki = d.pop("has_wiki", UNSET)

        is_template = d.pop("is_template", UNSET)

        default_branch = d.pop("default_branch", UNSET)

        allow_squash_merge = d.pop("allow_squash_merge", UNSET)

        allow_merge_commit = d.pop("allow_merge_commit", UNSET)

        allow_rebase_merge = d.pop("allow_rebase_merge", UNSET)

        allow_auto_merge = d.pop("allow_auto_merge", UNSET)

        delete_branch_on_merge = d.pop("delete_branch_on_merge", UNSET)

        allow_update_branch = d.pop("allow_update_branch", UNSET)

        use_squash_pr_title_as_default = d.pop("use_squash_pr_title_as_default", UNSET)

        _squash_merge_commit_title = d.pop("squash_merge_commit_title", UNSET)
        squash_merge_commit_title: Union[Unset, ReposupdateJsonBodySquashMergeCommitTitle]
        if isinstance(_squash_merge_commit_title, Unset):
            squash_merge_commit_title = UNSET
        else:
            squash_merge_commit_title = ReposupdateJsonBodySquashMergeCommitTitle(_squash_merge_commit_title)

        _squash_merge_commit_message = d.pop("squash_merge_commit_message", UNSET)
        squash_merge_commit_message: Union[Unset, ReposupdateJsonBodySquashMergeCommitMessage]
        if isinstance(_squash_merge_commit_message, Unset):
            squash_merge_commit_message = UNSET
        else:
            squash_merge_commit_message = ReposupdateJsonBodySquashMergeCommitMessage(_squash_merge_commit_message)

        _merge_commit_title = d.pop("merge_commit_title", UNSET)
        merge_commit_title: Union[Unset, ReposupdateJsonBodyMergeCommitTitle]
        if isinstance(_merge_commit_title, Unset):
            merge_commit_title = UNSET
        else:
            merge_commit_title = ReposupdateJsonBodyMergeCommitTitle(_merge_commit_title)

        _merge_commit_message = d.pop("merge_commit_message", UNSET)
        merge_commit_message: Union[Unset, ReposupdateJsonBodyMergeCommitMessage]
        if isinstance(_merge_commit_message, Unset):
            merge_commit_message = UNSET
        else:
            merge_commit_message = ReposupdateJsonBodyMergeCommitMessage(_merge_commit_message)

        archived = d.pop("archived", UNSET)

        allow_forking = d.pop("allow_forking", UNSET)

        web_commit_signoff_required = d.pop("web_commit_signoff_required", UNSET)

        reposupdate_json_body = cls(
            name=name,
            description=description,
            homepage=homepage,
            private=private,
            visibility=visibility,
            security_and_analysis=security_and_analysis,
            has_issues=has_issues,
            has_projects=has_projects,
            has_wiki=has_wiki,
            is_template=is_template,
            default_branch=default_branch,
            allow_squash_merge=allow_squash_merge,
            allow_merge_commit=allow_merge_commit,
            allow_rebase_merge=allow_rebase_merge,
            allow_auto_merge=allow_auto_merge,
            delete_branch_on_merge=delete_branch_on_merge,
            allow_update_branch=allow_update_branch,
            use_squash_pr_title_as_default=use_squash_pr_title_as_default,
            squash_merge_commit_title=squash_merge_commit_title,
            squash_merge_commit_message=squash_merge_commit_message,
            merge_commit_title=merge_commit_title,
            merge_commit_message=merge_commit_message,
            archived=archived,
            allow_forking=allow_forking,
            web_commit_signoff_required=web_commit_signoff_required,
        )

        reposupdate_json_body.additional_properties = d
        return reposupdate_json_body

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
