from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.migrationsstart_for_org_json_body_exclude_item import MigrationsstartForOrgJsonBodyExcludeItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="MigrationsstartForOrgJsonBody")


@attr.s(auto_attribs=True)
class MigrationsstartForOrgJsonBody:
    """
    Attributes:
        repositories (List[str]): A list of arrays indicating which repositories should be migrated.
        lock_repositories (Union[Unset, bool]): Indicates whether repositories should be locked (to prevent
            manipulation) while migrating data. Example: True.
        exclude_metadata (Union[Unset, bool]): Indicates whether metadata should be excluded and only git source should
            be included for the migration.
        exclude_git_data (Union[Unset, bool]): Indicates whether the repository git data should be excluded from the
            migration.
        exclude_attachments (Union[Unset, bool]): Indicates whether attachments should be excluded from the migration
            (to reduce migration archive file size). Example: True.
        exclude_releases (Union[Unset, bool]): Indicates whether releases should be excluded from the migration (to
            reduce migration archive file size). Example: True.
        exclude_owner_projects (Union[Unset, bool]): Indicates whether projects owned by the organization or users
            should be excluded. from the migration. Example: True.
        org_metadata_only (Union[Unset, bool]): Indicates whether this should only include organization metadata
            (repositories array should be empty and will ignore other flags). Example: True.
        exclude (Union[Unset, List[MigrationsstartForOrgJsonBodyExcludeItem]]): Exclude related items from being
            returned in the response in order to improve performance of the request. The array can include any of:
            `"repositories"`.
    """

    repositories: List[str]
    lock_repositories: Union[Unset, bool] = False
    exclude_metadata: Union[Unset, bool] = False
    exclude_git_data: Union[Unset, bool] = False
    exclude_attachments: Union[Unset, bool] = False
    exclude_releases: Union[Unset, bool] = False
    exclude_owner_projects: Union[Unset, bool] = False
    org_metadata_only: Union[Unset, bool] = False
    exclude: Union[Unset, List[MigrationsstartForOrgJsonBodyExcludeItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repositories = self.repositories

        lock_repositories = self.lock_repositories
        exclude_metadata = self.exclude_metadata
        exclude_git_data = self.exclude_git_data
        exclude_attachments = self.exclude_attachments
        exclude_releases = self.exclude_releases
        exclude_owner_projects = self.exclude_owner_projects
        org_metadata_only = self.org_metadata_only
        exclude: Union[Unset, List[str]] = UNSET
        if not isinstance(self.exclude, Unset):
            exclude = []
            for exclude_item_data in self.exclude:
                exclude_item = exclude_item_data.value

                exclude.append(exclude_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repositories": repositories,
            }
        )
        if lock_repositories is not UNSET:
            field_dict["lock_repositories"] = lock_repositories
        if exclude_metadata is not UNSET:
            field_dict["exclude_metadata"] = exclude_metadata
        if exclude_git_data is not UNSET:
            field_dict["exclude_git_data"] = exclude_git_data
        if exclude_attachments is not UNSET:
            field_dict["exclude_attachments"] = exclude_attachments
        if exclude_releases is not UNSET:
            field_dict["exclude_releases"] = exclude_releases
        if exclude_owner_projects is not UNSET:
            field_dict["exclude_owner_projects"] = exclude_owner_projects
        if org_metadata_only is not UNSET:
            field_dict["org_metadata_only"] = org_metadata_only
        if exclude is not UNSET:
            field_dict["exclude"] = exclude

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        repositories = cast(List[str], d.pop("repositories"))

        lock_repositories = d.pop("lock_repositories", UNSET)

        exclude_metadata = d.pop("exclude_metadata", UNSET)

        exclude_git_data = d.pop("exclude_git_data", UNSET)

        exclude_attachments = d.pop("exclude_attachments", UNSET)

        exclude_releases = d.pop("exclude_releases", UNSET)

        exclude_owner_projects = d.pop("exclude_owner_projects", UNSET)

        org_metadata_only = d.pop("org_metadata_only", UNSET)

        exclude = []
        _exclude = d.pop("exclude", UNSET)
        for exclude_item_data in _exclude or []:
            exclude_item = MigrationsstartForOrgJsonBodyExcludeItem(exclude_item_data)

            exclude.append(exclude_item)

        migrationsstart_for_org_json_body = cls(
            repositories=repositories,
            lock_repositories=lock_repositories,
            exclude_metadata=exclude_metadata,
            exclude_git_data=exclude_git_data,
            exclude_attachments=exclude_attachments,
            exclude_releases=exclude_releases,
            exclude_owner_projects=exclude_owner_projects,
            org_metadata_only=org_metadata_only,
            exclude=exclude,
        )

        migrationsstart_for_org_json_body.additional_properties = d
        return migrationsstart_for_org_json_body

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
