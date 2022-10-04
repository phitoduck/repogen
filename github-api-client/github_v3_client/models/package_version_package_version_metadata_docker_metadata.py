from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageVersionPackageVersionMetadataDockerMetadata")


@attr.s(auto_attribs=True)
class PackageVersionPackageVersionMetadataDockerMetadata:
    """
    Attributes:
        tag (Union[Unset, List[str]]):
    """

    tag: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tag: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tag = cast(List[str], d.pop("tag", UNSET))

        package_version_package_version_metadata_docker_metadata = cls(
            tag=tag,
        )

        package_version_package_version_metadata_docker_metadata.additional_properties = d
        return package_version_package_version_metadata_docker_metadata

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
