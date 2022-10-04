from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reposcreate_for_authenticated_user_json_body_merge_commit_message import (
    ReposcreateForAuthenticatedUserJsonBodyMergeCommitMessage,
)
from ..models.reposcreate_for_authenticated_user_json_body_merge_commit_title import (
    ReposcreateForAuthenticatedUserJsonBodyMergeCommitTitle,
)
from ..models.reposcreate_for_authenticated_user_json_body_squash_merge_commit_message import (
    ReposcreateForAuthenticatedUserJsonBodySquashMergeCommitMessage,
)
from ..models.reposcreate_for_authenticated_user_json_body_squash_merge_commit_title import (
    ReposcreateForAuthenticatedUserJsonBodySquashMergeCommitTitle,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateForAuthenticatedUserJsonBody")


@attr.s(auto_attribs=True)
class ReposcreateForAuthenticatedUserJsonBody:
    """
    Attributes:
        name (str): The name of the repository. Example: Team Environment.
        description (Union[Unset, str]): A short description of the repository.
        homepage (Union[Unset, str]): A URL with more information about the repository.
        private (Union[Unset, bool]): Whether the repository is private.
        has_issues (Union[Unset, bool]): Whether issues are enabled. Default: True. Example: True.
        has_projects (Union[Unset, bool]): Whether projects are enabled. Default: True. Example: True.
        has_wiki (Union[Unset, bool]): Whether the wiki is enabled. Default: True. Example: True.
        team_id (Union[Unset, int]): The id of the team that will be granted access to this repository. This is only
            valid when creating a repository in an organization.
        auto_init (Union[Unset, bool]): Whether the repository is initialized with a minimal README.
        gitignore_template (Union[Unset, str]): The desired language or platform to apply to the .gitignore. Example:
            Haskell.
        license_template (Union[Unset, str]): The license keyword of the open source license for this repository.
            Example: mit.
        allow_squash_merge (Union[Unset, bool]): Whether to allow squash merges for pull requests. Default: True.
            Example: True.
        allow_merge_commit (Union[Unset, bool]): Whether to allow merge commits for pull requests. Default: True.
            Example: True.
        allow_rebase_merge (Union[Unset, bool]): Whether to allow rebase merges for pull requests. Default: True.
            Example: True.
        allow_auto_merge (Union[Unset, bool]): Whether to allow Auto-merge to be used on pull requests.
        delete_branch_on_merge (Union[Unset, bool]): Whether to delete head branches when pull requests are merged
        squash_merge_commit_title (Union[Unset, ReposcreateForAuthenticatedUserJsonBodySquashMergeCommitTitle]): The
            default value for a squash merge commit title:

            - `PR_TITLE` - default to the pull request's title.
            - `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when
            more than one commit).
        squash_merge_commit_message (Union[Unset, ReposcreateForAuthenticatedUserJsonBodySquashMergeCommitMessage]): The
            default value for a squash merge commit message:

            - `PR_BODY` - default to the pull request's body.
            - `COMMIT_MESSAGES` - default to the branch's commit messages.
            - `BLANK` - default to a blank commit message.
        merge_commit_title (Union[Unset, ReposcreateForAuthenticatedUserJsonBodyMergeCommitTitle]): The default value
            for a merge commit title.

            - `PR_TITLE` - default to the pull request's title.
            - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-
            name).
        merge_commit_message (Union[Unset, ReposcreateForAuthenticatedUserJsonBodyMergeCommitMessage]): The default
            value for a merge commit message.

            - `PR_TITLE` - default to the pull request's title.
            - `PR_BODY` - default to the pull request's body.
            - `BLANK` - default to a blank commit message.
        has_downloads (Union[Unset, bool]): Whether downloads are enabled. Default: True. Example: True.
        is_template (Union[Unset, bool]): Whether this repository acts as a template that can be used to generate new
            repositories. Example: True.
    """

    name: str
    description: Union[Unset, str] = UNSET
    homepage: Union[Unset, str] = UNSET
    private: Union[Unset, bool] = False
    has_issues: Union[Unset, bool] = True
    has_projects: Union[Unset, bool] = True
    has_wiki: Union[Unset, bool] = True
    team_id: Union[Unset, int] = UNSET
    auto_init: Union[Unset, bool] = False
    gitignore_template: Union[Unset, str] = UNSET
    license_template: Union[Unset, str] = UNSET
    allow_squash_merge: Union[Unset, bool] = True
    allow_merge_commit: Union[Unset, bool] = True
    allow_rebase_merge: Union[Unset, bool] = True
    allow_auto_merge: Union[Unset, bool] = False
    delete_branch_on_merge: Union[Unset, bool] = False
    squash_merge_commit_title: Union[Unset, ReposcreateForAuthenticatedUserJsonBodySquashMergeCommitTitle] = UNSET
    squash_merge_commit_message: Union[Unset, ReposcreateForAuthenticatedUserJsonBodySquashMergeCommitMessage] = UNSET
    merge_commit_title: Union[Unset, ReposcreateForAuthenticatedUserJsonBodyMergeCommitTitle] = UNSET
    merge_commit_message: Union[Unset, ReposcreateForAuthenticatedUserJsonBodyMergeCommitMessage] = UNSET
    has_downloads: Union[Unset, bool] = True
    is_template: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        homepage = self.homepage
        private = self.private
        has_issues = self.has_issues
        has_projects = self.has_projects
        has_wiki = self.has_wiki
        team_id = self.team_id
        auto_init = self.auto_init
        gitignore_template = self.gitignore_template
        license_template = self.license_template
        allow_squash_merge = self.allow_squash_merge
        allow_merge_commit = self.allow_merge_commit
        allow_rebase_merge = self.allow_rebase_merge
        allow_auto_merge = self.allow_auto_merge
        delete_branch_on_merge = self.delete_branch_on_merge
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

        has_downloads = self.has_downloads
        is_template = self.is_template

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if private is not UNSET:
            field_dict["private"] = private
        if has_issues is not UNSET:
            field_dict["has_issues"] = has_issues
        if has_projects is not UNSET:
            field_dict["has_projects"] = has_projects
        if has_wiki is not UNSET:
            field_dict["has_wiki"] = has_wiki
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if auto_init is not UNSET:
            field_dict["auto_init"] = auto_init
        if gitignore_template is not UNSET:
            field_dict["gitignore_template"] = gitignore_template
        if license_template is not UNSET:
            field_dict["license_template"] = license_template
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
        if squash_merge_commit_title is not UNSET:
            field_dict["squash_merge_commit_title"] = squash_merge_commit_title
        if squash_merge_commit_message is not UNSET:
            field_dict["squash_merge_commit_message"] = squash_merge_commit_message
        if merge_commit_title is not UNSET:
            field_dict["merge_commit_title"] = merge_commit_title
        if merge_commit_message is not UNSET:
            field_dict["merge_commit_message"] = merge_commit_message
        if has_downloads is not UNSET:
            field_dict["has_downloads"] = has_downloads
        if is_template is not UNSET:
            field_dict["is_template"] = is_template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        homepage = d.pop("homepage", UNSET)

        private = d.pop("private", UNSET)

        has_issues = d.pop("has_issues", UNSET)

        has_projects = d.pop("has_projects", UNSET)

        has_wiki = d.pop("has_wiki", UNSET)

        team_id = d.pop("team_id", UNSET)

        auto_init = d.pop("auto_init", UNSET)

        gitignore_template = d.pop("gitignore_template", UNSET)

        license_template = d.pop("license_template", UNSET)

        allow_squash_merge = d.pop("allow_squash_merge", UNSET)

        allow_merge_commit = d.pop("allow_merge_commit", UNSET)

        allow_rebase_merge = d.pop("allow_rebase_merge", UNSET)

        allow_auto_merge = d.pop("allow_auto_merge", UNSET)

        delete_branch_on_merge = d.pop("delete_branch_on_merge", UNSET)

        _squash_merge_commit_title = d.pop("squash_merge_commit_title", UNSET)
        squash_merge_commit_title: Union[Unset, ReposcreateForAuthenticatedUserJsonBodySquashMergeCommitTitle]
        if isinstance(_squash_merge_commit_title, Unset):
            squash_merge_commit_title = UNSET
        else:
            squash_merge_commit_title = ReposcreateForAuthenticatedUserJsonBodySquashMergeCommitTitle(
                _squash_merge_commit_title
            )

        _squash_merge_commit_message = d.pop("squash_merge_commit_message", UNSET)
        squash_merge_commit_message: Union[Unset, ReposcreateForAuthenticatedUserJsonBodySquashMergeCommitMessage]
        if isinstance(_squash_merge_commit_message, Unset):
            squash_merge_commit_message = UNSET
        else:
            squash_merge_commit_message = ReposcreateForAuthenticatedUserJsonBodySquashMergeCommitMessage(
                _squash_merge_commit_message
            )

        _merge_commit_title = d.pop("merge_commit_title", UNSET)
        merge_commit_title: Union[Unset, ReposcreateForAuthenticatedUserJsonBodyMergeCommitTitle]
        if isinstance(_merge_commit_title, Unset):
            merge_commit_title = UNSET
        else:
            merge_commit_title = ReposcreateForAuthenticatedUserJsonBodyMergeCommitTitle(_merge_commit_title)

        _merge_commit_message = d.pop("merge_commit_message", UNSET)
        merge_commit_message: Union[Unset, ReposcreateForAuthenticatedUserJsonBodyMergeCommitMessage]
        if isinstance(_merge_commit_message, Unset):
            merge_commit_message = UNSET
        else:
            merge_commit_message = ReposcreateForAuthenticatedUserJsonBodyMergeCommitMessage(_merge_commit_message)

        has_downloads = d.pop("has_downloads", UNSET)

        is_template = d.pop("is_template", UNSET)

        reposcreate_for_authenticated_user_json_body = cls(
            name=name,
            description=description,
            homepage=homepage,
            private=private,
            has_issues=has_issues,
            has_projects=has_projects,
            has_wiki=has_wiki,
            team_id=team_id,
            auto_init=auto_init,
            gitignore_template=gitignore_template,
            license_template=license_template,
            allow_squash_merge=allow_squash_merge,
            allow_merge_commit=allow_merge_commit,
            allow_rebase_merge=allow_rebase_merge,
            allow_auto_merge=allow_auto_merge,
            delete_branch_on_merge=delete_branch_on_merge,
            squash_merge_commit_title=squash_merge_commit_title,
            squash_merge_commit_message=squash_merge_commit_message,
            merge_commit_title=merge_commit_title,
            merge_commit_message=merge_commit_message,
            has_downloads=has_downloads,
            is_template=is_template,
        )

        reposcreate_for_authenticated_user_json_body.additional_properties = d
        return reposcreate_for_authenticated_user_json_body

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
