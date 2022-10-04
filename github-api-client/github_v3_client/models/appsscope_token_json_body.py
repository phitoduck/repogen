from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.app_permissions import AppPermissions
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppsscopeTokenJsonBody")


@attr.s(auto_attribs=True)
class AppsscopeTokenJsonBody:
    """
    Attributes:
        access_token (str): The OAuth access token used to authenticate to the GitHub API. Example:
            e72e16c7e42f292c6912e7710c838347ae178b4a.
        target (Union[Unset, str]): The name of the user or organization to scope the user-to-server access token to.
            **Required** unless `target_id` is specified. Example: octocat.
        target_id (Union[Unset, int]): The ID of the user or organization to scope the user-to-server access token to.
            **Required** unless `target` is specified. Example: 1.
        repositories (Union[Unset, List[str]]): The list of repository names to scope the user-to-server access token
            to. `repositories` may not be specified if `repository_ids` is specified.
        repository_ids (Union[Unset, List[int]]): The list of repository IDs to scope the user-to-server access token
            to. `repository_ids` may not be specified if `repositories` is specified. Example: [1].
        permissions (Union[Unset, AppPermissions]): The permissions granted to the user-to-server access token. Example:
            {'contents': 'read', 'issues': 'read', 'deployments': 'write', 'single_file': 'read'}.
    """

    access_token: str
    target: Union[Unset, str] = UNSET
    target_id: Union[Unset, int] = UNSET
    repositories: Union[Unset, List[str]] = UNSET
    repository_ids: Union[Unset, List[int]] = UNSET
    permissions: Union[Unset, AppPermissions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token
        target = self.target
        target_id = self.target_id
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
        field_dict.update(
            {
                "access_token": access_token,
            }
        )
        if target is not UNSET:
            field_dict["target"] = target
        if target_id is not UNSET:
            field_dict["target_id"] = target_id
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
        access_token = d.pop("access_token")

        target = d.pop("target", UNSET)

        target_id = d.pop("target_id", UNSET)

        repositories = cast(List[str], d.pop("repositories", UNSET))

        repository_ids = cast(List[int], d.pop("repository_ids", UNSET))

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, AppPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = AppPermissions.from_dict(_permissions)

        appsscope_token_json_body = cls(
            access_token=access_token,
            target=target,
            target_id=target_id,
            repositories=repositories,
            repository_ids=repository_ids,
            permissions=permissions,
        )

        appsscope_token_json_body.additional_properties = d
        return appsscope_token_json_body

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
