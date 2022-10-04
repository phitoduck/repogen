from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManifestFile")


@attr.s(auto_attribs=True)
class ManifestFile:
    """
    Attributes:
        source_location (Union[Unset, str]): The path of the manifest file relative to the root of the Git repository.
            Example: /src/build/package-lock.json.
    """

    source_location: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        source_location = self.source_location

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if source_location is not UNSET:
            field_dict["source_location"] = source_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_location = d.pop("source_location", UNSET)

        manifest_file = cls(
            source_location=source_location,
        )

        return manifest_file
