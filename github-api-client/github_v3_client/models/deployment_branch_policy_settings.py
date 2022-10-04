from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DeploymentBranchPolicySettings")


@attr.s(auto_attribs=True)
class DeploymentBranchPolicySettings:
    """The type of deployment branch policy for this environment. To allow all branches to deploy, set to `null`.

    Attributes:
        protected_branches (bool): Whether only branches with branch protection rules can deploy to this environment. If
            `protected_branches` is `true`, `custom_branch_policies` must be `false`; if `protected_branches` is `false`,
            `custom_branch_policies` must be `true`.
        custom_branch_policies (bool): Whether only branches that match the specified name patterns can deploy to this
            environment.  If `custom_branch_policies` is `true`, `protected_branches` must be `false`; if
            `custom_branch_policies` is `false`, `protected_branches` must be `true`.
    """

    protected_branches: bool
    custom_branch_policies: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        protected_branches = self.protected_branches
        custom_branch_policies = self.custom_branch_policies

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "protected_branches": protected_branches,
                "custom_branch_policies": custom_branch_policies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        protected_branches = d.pop("protected_branches")

        custom_branch_policies = d.pop("custom_branch_policies")

        deployment_branch_policy_settings = cls(
            protected_branches=protected_branches,
            custom_branch_policies=custom_branch_policies,
        )

        deployment_branch_policy_settings.additional_properties = d
        return deployment_branch_policy_settings

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
