from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.security_and_analysis_advanced_security import SecurityAndAnalysisAdvancedSecurity
from ..models.security_and_analysis_secret_scanning import SecurityAndAnalysisSecretScanning
from ..models.security_and_analysis_secret_scanning_push_protection import (
    SecurityAndAnalysisSecretScanningPushProtection,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SecurityAndAnalysis")


@attr.s(auto_attribs=True)
class SecurityAndAnalysis:
    """
    Attributes:
        advanced_security (Union[Unset, SecurityAndAnalysisAdvancedSecurity]):
        secret_scanning (Union[Unset, SecurityAndAnalysisSecretScanning]):
        secret_scanning_push_protection (Union[Unset, SecurityAndAnalysisSecretScanningPushProtection]):
    """

    advanced_security: Union[Unset, SecurityAndAnalysisAdvancedSecurity] = UNSET
    secret_scanning: Union[Unset, SecurityAndAnalysisSecretScanning] = UNSET
    secret_scanning_push_protection: Union[Unset, SecurityAndAnalysisSecretScanningPushProtection] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        advanced_security: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.advanced_security, Unset):
            advanced_security = self.advanced_security.to_dict()

        secret_scanning: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.secret_scanning, Unset):
            secret_scanning = self.secret_scanning.to_dict()

        secret_scanning_push_protection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.secret_scanning_push_protection, Unset):
            secret_scanning_push_protection = self.secret_scanning_push_protection.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advanced_security is not UNSET:
            field_dict["advanced_security"] = advanced_security
        if secret_scanning is not UNSET:
            field_dict["secret_scanning"] = secret_scanning
        if secret_scanning_push_protection is not UNSET:
            field_dict["secret_scanning_push_protection"] = secret_scanning_push_protection

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _advanced_security = d.pop("advanced_security", UNSET)
        advanced_security: Union[Unset, SecurityAndAnalysisAdvancedSecurity]
        if isinstance(_advanced_security, Unset):
            advanced_security = UNSET
        else:
            advanced_security = SecurityAndAnalysisAdvancedSecurity.from_dict(_advanced_security)

        _secret_scanning = d.pop("secret_scanning", UNSET)
        secret_scanning: Union[Unset, SecurityAndAnalysisSecretScanning]
        if isinstance(_secret_scanning, Unset):
            secret_scanning = UNSET
        else:
            secret_scanning = SecurityAndAnalysisSecretScanning.from_dict(_secret_scanning)

        _secret_scanning_push_protection = d.pop("secret_scanning_push_protection", UNSET)
        secret_scanning_push_protection: Union[Unset, SecurityAndAnalysisSecretScanningPushProtection]
        if isinstance(_secret_scanning_push_protection, Unset):
            secret_scanning_push_protection = UNSET
        else:
            secret_scanning_push_protection = SecurityAndAnalysisSecretScanningPushProtection.from_dict(
                _secret_scanning_push_protection
            )

        security_and_analysis = cls(
            advanced_security=advanced_security,
            secret_scanning=secret_scanning,
            secret_scanning_push_protection=secret_scanning_push_protection,
        )

        security_and_analysis.additional_properties = d
        return security_and_analysis

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
