from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.deployment_branch_policy import DeploymentBranchPolicy

T = TypeVar("T", bound="ReposlistDeploymentBranchPoliciesResponse200")


@attr.s(auto_attribs=True)
class ReposlistDeploymentBranchPoliciesResponse200:
    """
    Attributes:
        total_count (int): The number of deployment branch policies for the environment. Example: 2.
        branch_policies (List[DeploymentBranchPolicy]):
    """

    total_count: int
    branch_policies: List[DeploymentBranchPolicy]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        branch_policies = []
        for branch_policies_item_data in self.branch_policies:
            branch_policies_item = branch_policies_item_data.to_dict()

            branch_policies.append(branch_policies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_count": total_count,
                "branch_policies": branch_policies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_count = d.pop("total_count")

        branch_policies = []
        _branch_policies = d.pop("branch_policies")
        for branch_policies_item_data in _branch_policies:
            branch_policies_item = DeploymentBranchPolicy.from_dict(branch_policies_item_data)

            branch_policies.append(branch_policies_item)

        reposlist_deployment_branch_policies_response_200 = cls(
            total_count=total_count,
            branch_policies=branch_policies,
        )

        reposlist_deployment_branch_policies_response_200.additional_properties = d
        return reposlist_deployment_branch_policies_response_200

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
