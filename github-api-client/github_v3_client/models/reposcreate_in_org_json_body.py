from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reposcreate_in_org_json_body_merge_commit_message import ReposcreateInOrgJsonBodyMergeCommitMessage
from ..models.reposcreate_in_org_json_body_merge_commit_title import ReposcreateInOrgJsonBodyMergeCommitTitle
from ..models.reposcreate_in_org_json_body_squash_merge_commit_message import (
    ReposcreateInOrgJsonBodySquashMergeCommitMessage,
)
from ..models.reposcreate_in_org_json_body_squash_merge_commit_title import (
    ReposcreateInOrgJsonBodySquashMergeCommitTitle,
)
from ..models.reposcreate_in_org_json_body_visibility import ReposcreateInOrgJsonBodyVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateInOrgJsonBody")


@attr.s(auto_attribs=True)
class ReposcreateInOrgJsonBody:
    """
    Attributes:
        name (str): The name of the repository.
        description (Union[Unset, str]): A short description of the repository.
        homepage (Union[Unset, str]): A URL with more information about the repository.
        private (Union[Unset, bool]): Whether the repository is private.
        visibility (Union[Unset, ReposcreateInOrgJsonBodyVisibility]): Can be `public` or `private`. If your
            organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server
            2.20+, `visibility` can also be `internal`. Note: For GitHub Enterprise Server and GitHub AE, this endpoint will
            only list repositories available to all users on the enterprise. For more information, see "[Creating an
            internal repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-
            repository-visibility#about-internal-repositories)" in the GitHub Help documentation.
        has_issues (Union[Unset, bool]): Either `true` to enable issues for this repository or `false` to disable them.
            Default: True.
        has_projects (Union[Unset, bool]): Either `true` to enable projects for this repository or `false` to disable
            them. **Note:** If you're creating a repository in an organization that has disabled repository projects, the
            default is `false`, and if you pass `true`, the API returns an error. Default: True.
        has_wiki (Union[Unset, bool]): Either `true` to enable the wiki for this repository or `false` to disable it.
            Default: True.
        is_template (Union[Unset, bool]): Either `true` to make this repo available as a template repository or `false`
            to prevent it.
        team_id (Union[Unset, int]): The id of the team that will be granted access to this repository. This is only
            valid when creating a repository in an organization.
        auto_init (Union[Unset, bool]): Pass `true` to create an initial commit with empty README.
        gitignore_template (Union[Unset, str]): Desired language or platform [.gitignore
            template](https://github.com/github/gitignore) to apply. Use the name of the template without the extension. For
            example, "Haskell".
        license_template (Union[Unset, str]): Choose an [open source license template](https://choosealicense.com/) that
            best suits your needs, and then use the [license keyword](https://docs.github.com/articles/licensing-a-
            repository/#searching-github-by-license-type) as the `license_template` string. For example, "mit" or "mpl-2.0".
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
        use_squash_pr_title_as_default (Union[Unset, bool]): Either `true` to allow squash-merge commits to use pull
            request title, or `false` to use commit message. **This property has been deprecated. Please use
            `squash_merge_commit_title` instead.
        squash_merge_commit_title (Union[Unset, ReposcreateInOrgJsonBodySquashMergeCommitTitle]): The default value for
            a squash merge commit title:

            - `PR_TITLE` - default to the pull request's title.
            - `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when
            more than one commit).
        squash_merge_commit_message (Union[Unset, ReposcreateInOrgJsonBodySquashMergeCommitMessage]): The default value
            for a squash merge commit message:

            - `PR_BODY` - default to the pull request's body.
            - `COMMIT_MESSAGES` - default to the branch's commit messages.
            - `BLANK` - default to a blank commit message.
        merge_commit_title (Union[Unset, ReposcreateInOrgJsonBodyMergeCommitTitle]): The default value for a merge
            commit title.

            - `PR_TITLE` - default to the pull request's title.
            - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-
            name).
        merge_commit_message (Union[Unset, ReposcreateInOrgJsonBodyMergeCommitMessage]): The default value for a merge
            commit message.

            - `PR_TITLE` - default to the pull request's title.
            - `PR_BODY` - default to the pull request's body.
            - `BLANK` - default to a blank commit message.
    """

    name: str
    description: Union[Unset, str] = UNSET
    homepage: Union[Unset, str] = UNSET
    private: Union[Unset, bool] = False
    visibility: Union[Unset, ReposcreateInOrgJsonBodyVisibility] = UNSET
    has_issues: Union[Unset, bool] = True
    has_projects: Union[Unset, bool] = True
    has_wiki: Union[Unset, bool] = True
    is_template: Union[Unset, bool] = False
    team_id: Union[Unset, int] = UNSET
    auto_init: Union[Unset, bool] = False
    gitignore_template: Union[Unset, str] = UNSET
    license_template: Union[Unset, str] = UNSET
    allow_squash_merge: Union[Unset, bool] = True
    allow_merge_commit: Union[Unset, bool] = True
    allow_rebase_merge: Union[Unset, bool] = True
    allow_auto_merge: Union[Unset, bool] = False
    delete_branch_on_merge: Union[Unset, bool] = False
    use_squash_pr_title_as_default: Union[Unset, bool] = False
    squash_merge_commit_title: Union[Unset, ReposcreateInOrgJsonBodySquashMergeCommitTitle] = UNSET
    squash_merge_commit_message: Union[Unset, ReposcreateInOrgJsonBodySquashMergeCommitMessage] = UNSET
    merge_commit_title: Union[Unset, ReposcreateInOrgJsonBodyMergeCommitTitle] = UNSET
    merge_commit_message: Union[Unset, ReposcreateInOrgJsonBodyMergeCommitMessage] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        homepage = self.homepage
        private = self.private
        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        has_issues = self.has_issues
        has_projects = self.has_projects
        has_wiki = self.has_wiki
        is_template = self.is_template
        team_id = self.team_id
        auto_init = self.auto_init
        gitignore_template = self.gitignore_template
        license_template = self.license_template
        allow_squash_merge = self.allow_squash_merge
        allow_merge_commit = self.allow_merge_commit
        allow_rebase_merge = self.allow_rebase_merge
        allow_auto_merge = self.allow_auto_merge
        delete_branch_on_merge = self.delete_branch_on_merge
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
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if has_issues is not UNSET:
            field_dict["has_issues"] = has_issues
        if has_projects is not UNSET:
            field_dict["has_projects"] = has_projects
        if has_wiki is not UNSET:
            field_dict["has_wiki"] = has_wiki
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        homepage = d.pop("homepage", UNSET)

        private = d.pop("private", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, ReposcreateInOrgJsonBodyVisibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = ReposcreateInOrgJsonBodyVisibility(_visibility)

        has_issues = d.pop("has_issues", UNSET)

        has_projects = d.pop("has_projects", UNSET)

        has_wiki = d.pop("has_wiki", UNSET)

        is_template = d.pop("is_template", UNSET)

        team_id = d.pop("team_id", UNSET)

        auto_init = d.pop("auto_init", UNSET)

        gitignore_template = d.pop("gitignore_template", UNSET)

        license_template = d.pop("license_template", UNSET)

        allow_squash_merge = d.pop("allow_squash_merge", UNSET)

        allow_merge_commit = d.pop("allow_merge_commit", UNSET)

        allow_rebase_merge = d.pop("allow_rebase_merge", UNSET)

        allow_auto_merge = d.pop("allow_auto_merge", UNSET)

        delete_branch_on_merge = d.pop("delete_branch_on_merge", UNSET)

        use_squash_pr_title_as_default = d.pop("use_squash_pr_title_as_default", UNSET)

        _squash_merge_commit_title = d.pop("squash_merge_commit_title", UNSET)
        squash_merge_commit_title: Union[Unset, ReposcreateInOrgJsonBodySquashMergeCommitTitle]
        if isinstance(_squash_merge_commit_title, Unset):
            squash_merge_commit_title = UNSET
        else:
            squash_merge_commit_title = ReposcreateInOrgJsonBodySquashMergeCommitTitle(_squash_merge_commit_title)

        _squash_merge_commit_message = d.pop("squash_merge_commit_message", UNSET)
        squash_merge_commit_message: Union[Unset, ReposcreateInOrgJsonBodySquashMergeCommitMessage]
        if isinstance(_squash_merge_commit_message, Unset):
            squash_merge_commit_message = UNSET
        else:
            squash_merge_commit_message = ReposcreateInOrgJsonBodySquashMergeCommitMessage(_squash_merge_commit_message)

        _merge_commit_title = d.pop("merge_commit_title", UNSET)
        merge_commit_title: Union[Unset, ReposcreateInOrgJsonBodyMergeCommitTitle]
        if isinstance(_merge_commit_title, Unset):
            merge_commit_title = UNSET
        else:
            merge_commit_title = ReposcreateInOrgJsonBodyMergeCommitTitle(_merge_commit_title)

        _merge_commit_message = d.pop("merge_commit_message", UNSET)
        merge_commit_message: Union[Unset, ReposcreateInOrgJsonBodyMergeCommitMessage]
        if isinstance(_merge_commit_message, Unset):
            merge_commit_message = UNSET
        else:
            merge_commit_message = ReposcreateInOrgJsonBodyMergeCommitMessage(_merge_commit_message)

        reposcreate_in_org_json_body = cls(
            name=name,
            description=description,
            homepage=homepage,
            private=private,
            visibility=visibility,
            has_issues=has_issues,
            has_projects=has_projects,
            has_wiki=has_wiki,
            is_template=is_template,
            team_id=team_id,
            auto_init=auto_init,
            gitignore_template=gitignore_template,
            license_template=license_template,
            allow_squash_merge=allow_squash_merge,
            allow_merge_commit=allow_merge_commit,
            allow_rebase_merge=allow_rebase_merge,
            allow_auto_merge=allow_auto_merge,
            delete_branch_on_merge=delete_branch_on_merge,
            use_squash_pr_title_as_default=use_squash_pr_title_as_default,
            squash_merge_commit_title=squash_merge_commit_title,
            squash_merge_commit_message=squash_merge_commit_message,
            merge_commit_title=merge_commit_title,
            merge_commit_message=merge_commit_message,
        )

        reposcreate_in_org_json_body.additional_properties = d
        return reposcreate_in_org_json_body

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
