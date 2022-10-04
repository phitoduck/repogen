from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reposupdate_json_body_security_and_analysis_advanced_security import (
    ReposupdateJsonBodySecurityAndAnalysisAdvancedSecurity,
)
from ..models.reposupdate_json_body_security_and_analysis_secret_scanning import (
    ReposupdateJsonBodySecurityAndAnalysisSecretScanning,
)
from ..models.reposupdate_json_body_security_and_analysis_secret_scanning_push_protection import (
    ReposupdateJsonBodySecurityAndAnalysisSecretScanningPushProtection,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdateJsonBodySecurityAndAnalysis")


@attr.s(auto_attribs=True)
class ReposupdateJsonBodySecurityAndAnalysis:
    """Specify which security and analysis features to enable or disable for the repository.

    To use this parameter, you must have admin permissions for the repository or be an owner or security manager for the
    organization that owns the repository. For more information, see "[Managing security managers in your
    organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-
    roles/managing-security-managers-in-your-organization)."

    For example, to enable GitHub Advanced Security, use this data in the body of the `PATCH` request:
    `{ "security_and_analysis": {"advanced_security": { "status": "enabled" } } }`.

    You can check which security and analysis features are currently enabled by using a `GET /repos/{owner}/{repo}`
    request.

        Attributes:
            advanced_security (Union[Unset, ReposupdateJsonBodySecurityAndAnalysisAdvancedSecurity]): Use the `status`
                property to enable or disable GitHub Advanced Security for this repository. For more information, see "[About
                GitHub Advanced Security](/github/getting-started-with-github/learning-about-github/about-github-advanced-
                security)."
            secret_scanning (Union[Unset, ReposupdateJsonBodySecurityAndAnalysisSecretScanning]): Use the `status` property
                to enable or disable secret scanning for this repository. For more information, see "[About secret
                scanning](/code-security/secret-security/about-secret-scanning)."
            secret_scanning_push_protection (Union[Unset,
                ReposupdateJsonBodySecurityAndAnalysisSecretScanningPushProtection]): Use the `status` property to enable or
                disable secret scanning push protection for this repository. For more information, see "[Protecting pushes with
                secret scanning](/code-security/secret-scanning/protecting-pushes-with-secret-scanning)."
    """

    advanced_security: Union[Unset, ReposupdateJsonBodySecurityAndAnalysisAdvancedSecurity] = UNSET
    secret_scanning: Union[Unset, ReposupdateJsonBodySecurityAndAnalysisSecretScanning] = UNSET
    secret_scanning_push_protection: Union[
        Unset, ReposupdateJsonBodySecurityAndAnalysisSecretScanningPushProtection
    ] = UNSET
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
        advanced_security: Union[Unset, ReposupdateJsonBodySecurityAndAnalysisAdvancedSecurity]
        if isinstance(_advanced_security, Unset):
            advanced_security = UNSET
        else:
            advanced_security = ReposupdateJsonBodySecurityAndAnalysisAdvancedSecurity.from_dict(_advanced_security)

        _secret_scanning = d.pop("secret_scanning", UNSET)
        secret_scanning: Union[Unset, ReposupdateJsonBodySecurityAndAnalysisSecretScanning]
        if isinstance(_secret_scanning, Unset):
            secret_scanning = UNSET
        else:
            secret_scanning = ReposupdateJsonBodySecurityAndAnalysisSecretScanning.from_dict(_secret_scanning)

        _secret_scanning_push_protection = d.pop("secret_scanning_push_protection", UNSET)
        secret_scanning_push_protection: Union[
            Unset, ReposupdateJsonBodySecurityAndAnalysisSecretScanningPushProtection
        ]
        if isinstance(_secret_scanning_push_protection, Unset):
            secret_scanning_push_protection = UNSET
        else:
            secret_scanning_push_protection = (
                ReposupdateJsonBodySecurityAndAnalysisSecretScanningPushProtection.from_dict(
                    _secret_scanning_push_protection
                )
            )

        reposupdate_json_body_security_and_analysis = cls(
            advanced_security=advanced_security,
            secret_scanning=secret_scanning,
            secret_scanning_push_protection=secret_scanning_push_protection,
        )

        reposupdate_json_body_security_and_analysis.additional_properties = d
        return reposupdate_json_body_security_and_analysis

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
