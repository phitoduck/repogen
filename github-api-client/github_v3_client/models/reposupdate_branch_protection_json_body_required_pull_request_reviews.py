from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reposupdate_branch_protection_json_body_required_pull_request_reviews_bypass_pull_request_allowances import (
    ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviewsBypassPullRequestAllowances,
)
from ..models.reposupdate_branch_protection_json_body_required_pull_request_reviews_dismissal_restrictions import (
    ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviewsDismissalRestrictions,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviews")


@attr.s(auto_attribs=True)
class ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviews:
    """Require at least one approving review on a pull request, before merging. Set to `null` to disable.

    Attributes:
        dismissal_restrictions (Union[Unset,
            ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviewsDismissalRestrictions]): Specify which users,
            teams, and apps can dismiss pull request reviews. Pass an empty `dismissal_restrictions` object to disable. User
            and team `dismissal_restrictions` are only available for organization-owned repositories. Omit this parameter
            for personal repositories.
        dismiss_stale_reviews (Union[Unset, bool]): Set to `true` if you want to automatically dismiss approving reviews
            when someone pushes a new commit.
        require_code_owner_reviews (Union[Unset, bool]): Blocks merging pull requests until [code
            owners](https://docs.github.com/articles/about-code-owners/) review them.
        required_approving_review_count (Union[Unset, int]): Specify the number of reviewers required to approve pull
            requests. Use a number between 1 and 6 or 0 to not require reviewers.
        bypass_pull_request_allowances (Union[Unset,
            ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviewsBypassPullRequestAllowances]): Allow specific
            users, teams, or apps to bypass pull request requirements.
    """

    dismissal_restrictions: Union[
        Unset, ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviewsDismissalRestrictions
    ] = UNSET
    dismiss_stale_reviews: Union[Unset, bool] = UNSET
    require_code_owner_reviews: Union[Unset, bool] = UNSET
    required_approving_review_count: Union[Unset, int] = UNSET
    bypass_pull_request_allowances: Union[
        Unset, ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviewsBypassPullRequestAllowances
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dismissal_restrictions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dismissal_restrictions, Unset):
            dismissal_restrictions = self.dismissal_restrictions.to_dict()

        dismiss_stale_reviews = self.dismiss_stale_reviews
        require_code_owner_reviews = self.require_code_owner_reviews
        required_approving_review_count = self.required_approving_review_count
        bypass_pull_request_allowances: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bypass_pull_request_allowances, Unset):
            bypass_pull_request_allowances = self.bypass_pull_request_allowances.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dismissal_restrictions is not UNSET:
            field_dict["dismissal_restrictions"] = dismissal_restrictions
        if dismiss_stale_reviews is not UNSET:
            field_dict["dismiss_stale_reviews"] = dismiss_stale_reviews
        if require_code_owner_reviews is not UNSET:
            field_dict["require_code_owner_reviews"] = require_code_owner_reviews
        if required_approving_review_count is not UNSET:
            field_dict["required_approving_review_count"] = required_approving_review_count
        if bypass_pull_request_allowances is not UNSET:
            field_dict["bypass_pull_request_allowances"] = bypass_pull_request_allowances

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _dismissal_restrictions = d.pop("dismissal_restrictions", UNSET)
        dismissal_restrictions: Union[
            Unset, ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviewsDismissalRestrictions
        ]
        if isinstance(_dismissal_restrictions, Unset):
            dismissal_restrictions = UNSET
        else:
            dismissal_restrictions = (
                ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviewsDismissalRestrictions.from_dict(
                    _dismissal_restrictions
                )
            )

        dismiss_stale_reviews = d.pop("dismiss_stale_reviews", UNSET)

        require_code_owner_reviews = d.pop("require_code_owner_reviews", UNSET)

        required_approving_review_count = d.pop("required_approving_review_count", UNSET)

        _bypass_pull_request_allowances = d.pop("bypass_pull_request_allowances", UNSET)
        bypass_pull_request_allowances: Union[
            Unset, ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviewsBypassPullRequestAllowances
        ]
        if isinstance(_bypass_pull_request_allowances, Unset):
            bypass_pull_request_allowances = UNSET
        else:
            bypass_pull_request_allowances = (
                ReposupdateBranchProtectionJsonBodyRequiredPullRequestReviewsBypassPullRequestAllowances.from_dict(
                    _bypass_pull_request_allowances
                )
            )

        reposupdate_branch_protection_json_body_required_pull_request_reviews = cls(
            dismissal_restrictions=dismissal_restrictions,
            dismiss_stale_reviews=dismiss_stale_reviews,
            require_code_owner_reviews=require_code_owner_reviews,
            required_approving_review_count=required_approving_review_count,
            bypass_pull_request_allowances=bypass_pull_request_allowances,
        )

        reposupdate_branch_protection_json_body_required_pull_request_reviews.additional_properties = d
        return reposupdate_branch_protection_json_body_required_pull_request_reviews

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
