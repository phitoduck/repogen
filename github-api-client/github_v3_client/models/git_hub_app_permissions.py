from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitHubAppPermissions")


@attr.s(auto_attribs=True)
class GitHubAppPermissions:
    """The set of permissions for the GitHub app

    Example:
        {'issues': 'read', 'deployments': 'write'}

    Attributes:
        issues (Union[Unset, str]):
        checks (Union[Unset, str]):
        metadata (Union[Unset, str]):
        contents (Union[Unset, str]):
        deployments (Union[Unset, str]):
    """

    issues: Union[Unset, str] = UNSET
    checks: Union[Unset, str] = UNSET
    metadata: Union[Unset, str] = UNSET
    contents: Union[Unset, str] = UNSET
    deployments: Union[Unset, str] = UNSET
    additional_properties: Dict[str, str] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issues = self.issues
        checks = self.checks
        metadata = self.metadata
        contents = self.contents
        deployments = self.deployments

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issues is not UNSET:
            field_dict["issues"] = issues
        if checks is not UNSET:
            field_dict["checks"] = checks
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if contents is not UNSET:
            field_dict["contents"] = contents
        if deployments is not UNSET:
            field_dict["deployments"] = deployments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        issues = d.pop("issues", UNSET)

        checks = d.pop("checks", UNSET)

        metadata = d.pop("metadata", UNSET)

        contents = d.pop("contents", UNSET)

        deployments = d.pop("deployments", UNSET)

        git_hub_app_permissions = cls(
            issues=issues,
            checks=checks,
            metadata=metadata,
            contents=contents,
            deployments=deployments,
        )

        git_hub_app_permissions.additional_properties = d
        return git_hub_app_permissions

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
