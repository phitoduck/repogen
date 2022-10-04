from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdateJsonBodySecurityAndAnalysisSecretScanningPushProtection")


@attr.s(auto_attribs=True)
class ReposupdateJsonBodySecurityAndAnalysisSecretScanningPushProtection:
    """Use the `status` property to enable or disable secret scanning push protection for this repository. For more
    information, see "[Protecting pushes with secret scanning](/code-security/secret-scanning/protecting-pushes-with-
    secret-scanning)."

        Attributes:
            status (Union[Unset, str]): Can be `enabled` or `disabled`.
    """

    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status", UNSET)

        reposupdate_json_body_security_and_analysis_secret_scanning_push_protection = cls(
            status=status,
        )

        reposupdate_json_body_security_and_analysis_secret_scanning_push_protection.additional_properties = d
        return reposupdate_json_body_security_and_analysis_secret_scanning_push_protection

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
