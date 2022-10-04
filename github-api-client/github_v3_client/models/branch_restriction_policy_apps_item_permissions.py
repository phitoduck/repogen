from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchRestrictionPolicyAppsItemPermissions")


@attr.s(auto_attribs=True)
class BranchRestrictionPolicyAppsItemPermissions:
    """
    Attributes:
        metadata (Union[Unset, str]):
        contents (Union[Unset, str]):
        issues (Union[Unset, str]):
        single_file (Union[Unset, str]):
    """

    metadata: Union[Unset, str] = UNSET
    contents: Union[Unset, str] = UNSET
    issues: Union[Unset, str] = UNSET
    single_file: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata = self.metadata
        contents = self.contents
        issues = self.issues
        single_file = self.single_file

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if contents is not UNSET:
            field_dict["contents"] = contents
        if issues is not UNSET:
            field_dict["issues"] = issues
        if single_file is not UNSET:
            field_dict["single_file"] = single_file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metadata = d.pop("metadata", UNSET)

        contents = d.pop("contents", UNSET)

        issues = d.pop("issues", UNSET)

        single_file = d.pop("single_file", UNSET)

        branch_restriction_policy_apps_item_permissions = cls(
            metadata=metadata,
            contents=contents,
            issues=issues,
            single_file=single_file,
        )

        branch_restriction_policy_apps_item_permissions.additional_properties = d
        return branch_restriction_policy_apps_item_permissions

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
