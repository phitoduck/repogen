from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.secret_scanning_location_commit import SecretScanningLocationCommit
from ..models.secret_scanning_location_type import SecretScanningLocationType

T = TypeVar("T", bound="SecretScanningLocation")


@attr.s(auto_attribs=True)
class SecretScanningLocation:
    """
    Attributes:
        type (SecretScanningLocationType): The location type. Because secrets may be found in different types of
            resources (ie. code, comments, issues), this field identifies the type of resource where the secret was found.
            Example: commit.
        details (SecretScanningLocationCommit): Represents a 'commit' secret scanning location type. This location type
            shows that a secret was detected inside a commit to a repository.
    """

    type: SecretScanningLocationType
    details: SecretScanningLocationCommit
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        details = self.details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "details": details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = SecretScanningLocationType(d.pop("type"))

        details = SecretScanningLocationCommit.from_dict(d.pop("details"))

        secret_scanning_location = cls(
            type=type,
            details=details,
        )

        secret_scanning_location.additional_properties = d
        return secret_scanning_location

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
