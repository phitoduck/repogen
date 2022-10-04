from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.manifest_file import ManifestFile
from ..models.manifest_resolved import ManifestResolved
from ..models.metadata import Metadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="Manifest")


@attr.s(auto_attribs=True)
class Manifest:
    """
    Attributes:
        name (str): The name of the manifest. Example: package-lock.json.
        file (Union[Unset, ManifestFile]):
        metadata (Union[Unset, Metadata]): User-defined metadata to store domain-specific information limited to 8 keys
            with scalar values.
        resolved (Union[Unset, ManifestResolved]): A collection of resolved package dependencies.
    """

    name: str
    file: Union[Unset, ManifestFile] = UNSET
    metadata: Union[Unset, Metadata] = UNSET
    resolved: Union[Unset, ManifestResolved] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        resolved: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resolved, Unset):
            resolved = self.resolved.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if file is not UNSET:
            field_dict["file"] = file
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if resolved is not UNSET:
            field_dict["resolved"] = resolved

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        _file = d.pop("file", UNSET)
        file: Union[Unset, ManifestFile]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = ManifestFile.from_dict(_file)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        _resolved = d.pop("resolved", UNSET)
        resolved: Union[Unset, ManifestResolved]
        if isinstance(_resolved, Unset):
            resolved = UNSET
        else:
            resolved = ManifestResolved.from_dict(_resolved)

        manifest = cls(
            name=name,
            file=file,
            metadata=metadata,
            resolved=resolved,
        )

        return manifest
