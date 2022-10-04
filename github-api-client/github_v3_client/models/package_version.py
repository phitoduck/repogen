import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.package_version_package_version_metadata import PackageVersionPackageVersionMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageVersion")


@attr.s(auto_attribs=True)
class PackageVersion:
    """A version of a software package

    Attributes:
        id (int): Unique identifier of the package version. Example: 1.
        name (str): The name of the package version. Example: latest.
        url (str):  Example: https://api.github.com/orgs/github/packages/container/super-linter/versions/786068.
        package_html_url (str):  Example: https://github.com/orgs/github/packages/container/package/super-linter.
        created_at (datetime.datetime):  Example: 2011-04-10T20:09:31Z.
        updated_at (datetime.datetime):  Example: 2014-03-03T18:58:10Z.
        html_url (Union[Unset, str]):  Example: https://github.com/orgs/github/packages/container/super-linter/786068.
        license_ (Union[Unset, str]):  Example: MIT.
        description (Union[Unset, str]):
        deleted_at (Union[Unset, datetime.datetime]):  Example: 2014-03-03T18:58:10Z.
        metadata (Union[Unset, PackageVersionPackageVersionMetadata]):
    """

    id: int
    name: str
    url: str
    package_html_url: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    html_url: Union[Unset, str] = UNSET
    license_: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    deleted_at: Union[Unset, datetime.datetime] = UNSET
    metadata: Union[Unset, PackageVersionPackageVersionMetadata] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        url = self.url
        package_html_url = self.package_html_url
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        html_url = self.html_url
        license_ = self.license_
        description = self.description
        deleted_at: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "url": url,
                "package_html_url": package_html_url,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if license_ is not UNSET:
            field_dict["license"] = license_
        if description is not UNSET:
            field_dict["description"] = description
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        url = d.pop("url")

        package_html_url = d.pop("package_html_url")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        html_url = d.pop("html_url", UNSET)

        license_ = d.pop("license", UNSET)

        description = d.pop("description", UNSET)

        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: Union[Unset, datetime.datetime]
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PackageVersionPackageVersionMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PackageVersionPackageVersionMetadata.from_dict(_metadata)

        package_version = cls(
            id=id,
            name=name,
            url=url,
            package_html_url=package_html_url,
            created_at=created_at,
            updated_at=updated_at,
            html_url=html_url,
            license_=license_,
            description=description,
            deleted_at=deleted_at,
            metadata=metadata,
        )

        package_version.additional_properties = d
        return package_version

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
