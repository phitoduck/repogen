from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="SnapshotDetector")


@attr.s(auto_attribs=True)
class SnapshotDetector:
    """A description of the detector used.

    Attributes:
        name (str): The name of the detector used. Example: docker buildtime detector.
        version (str): The version of the detector used. Example: 1.0.0.
        url (str): The url of the detector used. Example: http://example.com/docker-buildtimer-detector.
    """

    name: str
    version: str
    url: str

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        version = self.version
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "version": version,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        version = d.pop("version")

        url = d.pop("url")

        snapshot_detector = cls(
            name=name,
            version=version,
            url=url,
        )

        return snapshot_detector
