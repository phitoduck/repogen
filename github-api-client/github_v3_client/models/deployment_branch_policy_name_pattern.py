from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DeploymentBranchPolicyNamePattern")


@attr.s(auto_attribs=True)
class DeploymentBranchPolicyNamePattern:
    """
    Attributes:
        name (str): The name pattern that branches must match in order to deploy to the environment.

            Wildcard characters will not match `/`. For example, to match branches that begin with `release/` and contain an
            additional single slash, use `release/*/*`.
            For more information about pattern matching syntax, see the [Ruby File.fnmatch documentation](https://ruby-
            doc.org/core-2.5.1/File.html#method-c-fnmatch). Example: release/*.
    """

    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        deployment_branch_policy_name_pattern = cls(
            name=name,
        )

        deployment_branch_policy_name_pattern.additional_properties = d
        return deployment_branch_policy_name_pattern

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
