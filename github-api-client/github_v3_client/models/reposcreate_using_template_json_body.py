from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateUsingTemplateJsonBody")


@attr.s(auto_attribs=True)
class ReposcreateUsingTemplateJsonBody:
    """
    Attributes:
        name (str): The name of the new repository.
        owner (Union[Unset, str]): The organization or person who will own the new repository. To create a new
            repository in an organization, the authenticated user must be a member of the specified organization.
        description (Union[Unset, str]): A short description of the new repository.
        include_all_branches (Union[Unset, bool]): Set to `true` to include the directory structure and files from all
            branches in the template repository, and not just the default branch. Default: `false`.
        private (Union[Unset, bool]): Either `true` to create a new private repository or `false` to create a new public
            one.
    """

    name: str
    owner: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    include_all_branches: Union[Unset, bool] = False
    private: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        owner = self.owner
        description = self.description
        include_all_branches = self.include_all_branches
        private = self.private

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if owner is not UNSET:
            field_dict["owner"] = owner
        if description is not UNSET:
            field_dict["description"] = description
        if include_all_branches is not UNSET:
            field_dict["include_all_branches"] = include_all_branches
        if private is not UNSET:
            field_dict["private"] = private

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        owner = d.pop("owner", UNSET)

        description = d.pop("description", UNSET)

        include_all_branches = d.pop("include_all_branches", UNSET)

        private = d.pop("private", UNSET)

        reposcreate_using_template_json_body = cls(
            name=name,
            owner=owner,
            description=description,
            include_all_branches=include_all_branches,
            private=private,
        )

        reposcreate_using_template_json_body.additional_properties = d
        return reposcreate_using_template_json_body

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
