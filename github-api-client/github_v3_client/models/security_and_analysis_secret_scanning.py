from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.security_and_analysis_secret_scanning_status import SecurityAndAnalysisSecretScanningStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SecurityAndAnalysisSecretScanning")


@attr.s(auto_attribs=True)
class SecurityAndAnalysisSecretScanning:
    """
    Attributes:
        status (Union[Unset, SecurityAndAnalysisSecretScanningStatus]):
    """

    status: Union[Unset, SecurityAndAnalysisSecretScanningStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, SecurityAndAnalysisSecretScanningStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SecurityAndAnalysisSecretScanningStatus(_status)

        security_and_analysis_secret_scanning = cls(
            status=status,
        )

        security_and_analysis_secret_scanning.additional_properties = d
        return security_and_analysis_secret_scanning

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
