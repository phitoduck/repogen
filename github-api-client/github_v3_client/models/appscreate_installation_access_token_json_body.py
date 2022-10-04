from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.app_permissions import AppPermissions
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppscreateInstallationAccessTokenJsonBody")


@attr.s(auto_attribs=True)
class AppscreateInstallationAccessTokenJsonBody:
    """
    Attributes:
        repositories (Union[Unset, List[str]]): List of repository names that the token should have access to
        repository_ids (Union[Unset, List[int]]): List of repository IDs that the token should have access to Example:
            [1].
        permissions (Union[Unset, AppPermissions]): The permissions granted to the user-to-server access token. Example:
            {'contents': 'read', 'issues': 'read', 'deployments': 'write', 'single_file': 'read'}.
    """

    repositories: Union[Unset, List[str]] = UNSET
    repository_ids: Union[Unset, List[int]] = UNSET
    permissions: Union[Unset, AppPermissions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repositories: Union[Unset, List[str]] = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = self.repositories

        repository_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.repository_ids, Unset):
            repository_ids = self.repository_ids

        permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repositories is not UNSET:
            field_dict["repositories"] = repositories
        if repository_ids is not UNSET:
            field_dict["repository_ids"] = repository_ids
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        repositories = cast(List[str], d.pop("repositories", UNSET))

        repository_ids = cast(List[int], d.pop("repository_ids", UNSET))

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, AppPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = AppPermissions.from_dict(_permissions)

        appscreate_installation_access_token_json_body = cls(
            repositories=repositories,
            repository_ids=repository_ids,
            permissions=permissions,
        )

        appscreate_installation_access_token_json_body.additional_properties = d
        return appscreate_installation_access_token_json_body

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
