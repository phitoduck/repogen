from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.package_version_package_version_metadata_container_metadata import (
    PackageVersionPackageVersionMetadataContainerMetadata,
)
from ..models.package_version_package_version_metadata_docker_metadata import (
    PackageVersionPackageVersionMetadataDockerMetadata,
)
from ..models.package_version_package_version_metadata_package_type import (
    PackageVersionPackageVersionMetadataPackageType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageVersionPackageVersionMetadata")


@attr.s(auto_attribs=True)
class PackageVersionPackageVersionMetadata:
    """
    Attributes:
        package_type (PackageVersionPackageVersionMetadataPackageType):  Example: docker.
        container (Union[Unset, PackageVersionPackageVersionMetadataContainerMetadata]):
        docker (Union[Unset, PackageVersionPackageVersionMetadataDockerMetadata]):
    """

    package_type: PackageVersionPackageVersionMetadataPackageType
    container: Union[Unset, PackageVersionPackageVersionMetadataContainerMetadata] = UNSET
    docker: Union[Unset, PackageVersionPackageVersionMetadataDockerMetadata] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_type = self.package_type.value

        container: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.container, Unset):
            container = self.container.to_dict()

        docker: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.docker, Unset):
            docker = self.docker.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package_type": package_type,
            }
        )
        if container is not UNSET:
            field_dict["container"] = container
        if docker is not UNSET:
            field_dict["docker"] = docker

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        package_type = PackageVersionPackageVersionMetadataPackageType(d.pop("package_type"))

        _container = d.pop("container", UNSET)
        container: Union[Unset, PackageVersionPackageVersionMetadataContainerMetadata]
        if isinstance(_container, Unset):
            container = UNSET
        else:
            container = PackageVersionPackageVersionMetadataContainerMetadata.from_dict(_container)

        _docker = d.pop("docker", UNSET)
        docker: Union[Unset, PackageVersionPackageVersionMetadataDockerMetadata]
        if isinstance(_docker, Unset):
            docker = UNSET
        else:
            docker = PackageVersionPackageVersionMetadataDockerMetadata.from_dict(_docker)

        package_version_package_version_metadata = cls(
            package_type=package_type,
            container=container,
            docker=docker,
        )

        package_version_package_version_metadata.additional_properties = d
        return package_version_package_version_metadata

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
