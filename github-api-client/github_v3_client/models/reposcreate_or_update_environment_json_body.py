from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.deployment_branch_policy_settings import DeploymentBranchPolicySettings
from ..models.reposcreate_or_update_environment_json_body_reviewers_item import (
    ReposcreateOrUpdateEnvironmentJsonBodyReviewersItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateOrUpdateEnvironmentJsonBody")


@attr.s(auto_attribs=True)
class ReposcreateOrUpdateEnvironmentJsonBody:
    """
    Attributes:
        wait_timer (Union[Unset, int]): The amount of time to delay a job after the job is initially triggered. The time
            (in minutes) must be an integer between 0 and 43,200 (30 days). Example: 30.
        reviewers (Union[Unset, None, List[ReposcreateOrUpdateEnvironmentJsonBodyReviewersItem]]): The people or teams
            that may review jobs that reference the environment. You can list up to six users or teams as reviewers. The
            reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve
            the job for it to proceed.
        deployment_branch_policy (Union[Unset, None, DeploymentBranchPolicySettings]): The type of deployment branch
            policy for this environment. To allow all branches to deploy, set to `null`.
    """

    wait_timer: Union[Unset, int] = UNSET
    reviewers: Union[Unset, None, List[ReposcreateOrUpdateEnvironmentJsonBodyReviewersItem]] = UNSET
    deployment_branch_policy: Union[Unset, None, DeploymentBranchPolicySettings] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        wait_timer = self.wait_timer
        reviewers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.reviewers, Unset):
            if self.reviewers is None:
                reviewers = None
            else:
                reviewers = []
                for reviewers_item_data in self.reviewers:
                    reviewers_item = reviewers_item_data.to_dict()

                    reviewers.append(reviewers_item)

        deployment_branch_policy: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.deployment_branch_policy, Unset):
            deployment_branch_policy = (
                self.deployment_branch_policy.to_dict() if self.deployment_branch_policy else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if wait_timer is not UNSET:
            field_dict["wait_timer"] = wait_timer
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers
        if deployment_branch_policy is not UNSET:
            field_dict["deployment_branch_policy"] = deployment_branch_policy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        wait_timer = d.pop("wait_timer", UNSET)

        reviewers = []
        _reviewers = d.pop("reviewers", UNSET)
        for reviewers_item_data in _reviewers or []:
            reviewers_item = ReposcreateOrUpdateEnvironmentJsonBodyReviewersItem.from_dict(reviewers_item_data)

            reviewers.append(reviewers_item)

        _deployment_branch_policy = d.pop("deployment_branch_policy", UNSET)
        deployment_branch_policy: Union[Unset, None, DeploymentBranchPolicySettings]
        if _deployment_branch_policy is None:
            deployment_branch_policy = None
        elif isinstance(_deployment_branch_policy, Unset):
            deployment_branch_policy = UNSET
        else:
            deployment_branch_policy = DeploymentBranchPolicySettings.from_dict(_deployment_branch_policy)

        reposcreate_or_update_environment_json_body = cls(
            wait_timer=wait_timer,
            reviewers=reviewers,
            deployment_branch_policy=deployment_branch_policy,
        )

        return reposcreate_or_update_environment_json_body
