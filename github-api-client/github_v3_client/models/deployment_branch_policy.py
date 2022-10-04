from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentBranchPolicy")


@attr.s(auto_attribs=True)
class DeploymentBranchPolicy:
    """Details of a deployment branch policy.

    Attributes:
        id (Union[Unset, int]): The unique identifier of the branch policy. Example: 361471.
        node_id (Union[Unset, str]):  Example: MDE2OkdhdGVCcmFuY2hQb2xpY3kzNjE0NzE=.
        name (Union[Unset, str]): The name pattern that branches must match in order to deploy to the environment.
            Example: release/*.
    """

    id: Union[Unset, int] = UNSET
    node_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        node_id = d.pop("node_id", UNSET)

        name = d.pop("name", UNSET)

        deployment_branch_policy = cls(
            id=id,
            node_id=node_id,
            name=name,
        )

        deployment_branch_policy.additional_properties = d
        return deployment_branch_policy

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
