from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateForkJsonBody")


@attr.s(auto_attribs=True)
class ReposcreateForkJsonBody:
    """
    Attributes:
        organization (Union[Unset, str]): Optional parameter to specify the organization name if forking into an
            organization.
        name (Union[Unset, str]): When forking from an existing repository, a new name for the fork.
        default_branch_only (Union[Unset, bool]): When forking from an existing repository, fork with only the default
            branch.
    """

    organization: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    default_branch_only: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization = self.organization
        name = self.name
        default_branch_only = self.default_branch_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization is not UNSET:
            field_dict["organization"] = organization
        if name is not UNSET:
            field_dict["name"] = name
        if default_branch_only is not UNSET:
            field_dict["default_branch_only"] = default_branch_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        organization = d.pop("organization", UNSET)

        name = d.pop("name", UNSET)

        default_branch_only = d.pop("default_branch_only", UNSET)

        reposcreate_fork_json_body = cls(
            organization=organization,
            name=name,
            default_branch_only=default_branch_only,
        )

        reposcreate_fork_json_body.additional_properties = d
        return reposcreate_fork_json_body

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
