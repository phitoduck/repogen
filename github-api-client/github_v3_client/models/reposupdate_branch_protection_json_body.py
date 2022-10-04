from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.reposupdate_branch_protection_json_body_required_pull_request_reviews import (
    ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviews,
)
from ..models.reposupdate_branch_protection_json_body_required_status_checks import (
    ReposupdateBranchProtectionJsonBodyRequiredStatusChecks,
)
from ..models.reposupdate_branch_protection_json_body_restrictions import (
    ReposupdateBranchProtectionJsonBodyRestrictions,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdateBranchProtectionJsonBody")


@attr.s(auto_attribs=True)
class ReposupdateBranchProtectionJsonBody:
    """
    Attributes:
        required_status_checks (Optional[ReposupdateBranchProtectionJsonBodyRequiredStatusChecks]): Require status
            checks to pass before merging. Set to `null` to disable.
        enforce_admins (Optional[bool]): Enforce all configured restrictions for administrators. Set to `true` to
            enforce required status checks for repository administrators. Set to `null` to disable.
        required_pull_request_reviews (Optional[ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviews]): Require
            at least one approving review on a pull request, before merging. Set to `null` to disable.
        restrictions (Optional[ReposupdateBranchProtectionJsonBodyRestrictions]): Restrict who can push to the protected
            branch. User, app, and team `restrictions` are only available for organization-owned repositories. Set to `null`
            to disable.
        required_linear_history (Union[Unset, bool]): Enforces a linear commit Git history, which prevents anyone from
            pushing merge commits to a branch. Set to `true` to enforce a linear commit history. Set to `false` to disable a
            linear commit Git history. Your repository must allow squash merging or rebase merging before you can enable a
            linear commit history. Default: `false`. For more information, see "[Requiring a linear commit
            history](https://docs.github.com/github/administering-a-repository/requiring-a-linear-commit-history)" in the
            GitHub Help documentation.
        allow_force_pushes (Union[Unset, None, bool]): Permits force pushes to the protected branch by anyone with write
            access to the repository. Set to `true` to allow force pushes. Set to `false` or `null` to block force pushes.
            Default: `false`. For more information, see "[Enabling force pushes to a protected
            branch](https://docs.github.com/en/github/administering-a-repository/enabling-force-pushes-to-a-protected-
            branch)" in the GitHub Help documentation."
        allow_deletions (Union[Unset, bool]): Allows deletion of the protected branch by anyone with write access to the
            repository. Set to `false` to prevent deletion of the protected branch. Default: `false`. For more information,
            see "[Enabling force pushes to a protected branch](https://docs.github.com/en/github/administering-a-
            repository/enabling-force-pushes-to-a-protected-branch)" in the GitHub Help documentation.
        block_creations (Union[Unset, bool]): If set to `true`, the `restrictions` branch protection settings which
            limits who can push will also block pushes which create new branches, unless the push is initiated by a user,
            team, or app which has the ability to push. Set to `true` to restrict new branch creation. Default: `false`.
        required_conversation_resolution (Union[Unset, bool]): Requires all conversations on code to be resolved before
            a pull request can be merged into a branch that matches this rule. Set to `false` to disable. Default: `false`.
    """

    required_status_checks: Optional[ReposupdateBranchProtectionJsonBodyRequiredStatusChecks]
    enforce_admins: Optional[bool]
    required_pull_request_reviews: Optional[ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviews]
    restrictions: Optional[ReposupdateBranchProtectionJsonBodyRestrictions]
    required_linear_history: Union[Unset, bool] = UNSET
    allow_force_pushes: Union[Unset, None, bool] = UNSET
    allow_deletions: Union[Unset, bool] = UNSET
    block_creations: Union[Unset, bool] = UNSET
    required_conversation_resolution: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        required_status_checks = self.required_status_checks.to_dict() if self.required_status_checks else None

        enforce_admins = self.enforce_admins
        required_pull_request_reviews = (
            self.required_pull_request_reviews.to_dict() if self.required_pull_request_reviews else None
        )

        restrictions = self.restrictions.to_dict() if self.restrictions else None

        required_linear_history = self.required_linear_history
        allow_force_pushes = self.allow_force_pushes
        allow_deletions = self.allow_deletions
        block_creations = self.block_creations
        required_conversation_resolution = self.required_conversation_resolution

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "required_status_checks": required_status_checks,
                "enforce_admins": enforce_admins,
                "required_pull_request_reviews": required_pull_request_reviews,
                "restrictions": restrictions,
            }
        )
        if required_linear_history is not UNSET:
            field_dict["required_linear_history"] = required_linear_history
        if allow_force_pushes is not UNSET:
            field_dict["allow_force_pushes"] = allow_force_pushes
        if allow_deletions is not UNSET:
            field_dict["allow_deletions"] = allow_deletions
        if block_creations is not UNSET:
            field_dict["block_creations"] = block_creations
        if required_conversation_resolution is not UNSET:
            field_dict["required_conversation_resolution"] = required_conversation_resolution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _required_status_checks = d.pop("required_status_checks")
        required_status_checks: Optional[ReposupdateBranchProtectionJsonBodyRequiredStatusChecks]
        if _required_status_checks is None:
            required_status_checks = None
        else:
            required_status_checks = ReposupdateBranchProtectionJsonBodyRequiredStatusChecks.from_dict(
                _required_status_checks
            )

        enforce_admins = d.pop("enforce_admins")

        _required_pull_request_reviews = d.pop("required_pull_request_reviews")
        required_pull_request_reviews: Optional[ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviews]
        if _required_pull_request_reviews is None:
            required_pull_request_reviews = None
        else:
            required_pull_request_reviews = ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviews.from_dict(
                _required_pull_request_reviews
            )

        _restrictions = d.pop("restrictions")
        restrictions: Optional[ReposupdateBranchProtectionJsonBodyRestrictions]
        if _restrictions is None:
            restrictions = None
        else:
            restrictions = ReposupdateBranchProtectionJsonBodyRestrictions.from_dict(_restrictions)

        required_linear_history = d.pop("required_linear_history", UNSET)

        allow_force_pushes = d.pop("allow_force_pushes", UNSET)

        allow_deletions = d.pop("allow_deletions", UNSET)

        block_creations = d.pop("block_creations", UNSET)

        required_conversation_resolution = d.pop("required_conversation_resolution", UNSET)

        reposupdate_branch_protection_json_body = cls(
            required_status_checks=required_status_checks,
            enforce_admins=enforce_admins,
            required_pull_request_reviews=required_pull_request_reviews,
            restrictions=restrictions,
            required_linear_history=required_linear_history,
            allow_force_pushes=allow_force_pushes,
            allow_deletions=allow_deletions,
            block_creations=block_creations,
            required_conversation_resolution=required_conversation_resolution,
        )

        reposupdate_branch_protection_json_body.additional_properties = d
        return reposupdate_branch_protection_json_body

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
