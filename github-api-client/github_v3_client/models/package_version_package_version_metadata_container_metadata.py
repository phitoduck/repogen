from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="PackageVersionPackageVersionMetadataContainerMetadata")


@attr.s(auto_attribs=True)
class PackageVersionPackageVersionMetadataContainerMetadata:
    """
    Attributes:
        tags (List[str]):
    """

    tags: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tags = cast(List[str], d.pop("tags"))

        package_version_package_version_metadata_container_metadata = cls(
            tags=tags,
        )

        package_version_package_version_metadata_container_metadata.additional_properties = d
        return package_version_package_version_metadata_container_metadata

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
