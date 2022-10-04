from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiOverviewSshKeyFingerprints")


@attr.s(auto_attribs=True)
class ApiOverviewSshKeyFingerprints:
    """
    Attributes:
        sha256_rsa (Union[Unset, str]):
        sha256_dsa (Union[Unset, str]):
        sha256_ecdsa (Union[Unset, str]):
        sha256_ed25519 (Union[Unset, str]):
    """

    sha256_rsa: Union[Unset, str] = UNSET
    sha256_dsa: Union[Unset, str] = UNSET
    sha256_ecdsa: Union[Unset, str] = UNSET
    sha256_ed25519: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sha256_rsa = self.sha256_rsa
        sha256_dsa = self.sha256_dsa
        sha256_ecdsa = self.sha256_ecdsa
        sha256_ed25519 = self.sha256_ed25519

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sha256_rsa is not UNSET:
            field_dict["SHA256_RSA"] = sha256_rsa
        if sha256_dsa is not UNSET:
            field_dict["SHA256_DSA"] = sha256_dsa
        if sha256_ecdsa is not UNSET:
            field_dict["SHA256_ECDSA"] = sha256_ecdsa
        if sha256_ed25519 is not UNSET:
            field_dict["SHA256_ED25519"] = sha256_ed25519

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sha256_rsa = d.pop("SHA256_RSA", UNSET)

        sha256_dsa = d.pop("SHA256_DSA", UNSET)

        sha256_ecdsa = d.pop("SHA256_ECDSA", UNSET)

        sha256_ed25519 = d.pop("SHA256_ED25519", UNSET)

        api_overview_ssh_key_fingerprints = cls(
            sha256_rsa=sha256_rsa,
            sha256_dsa=sha256_dsa,
            sha256_ecdsa=sha256_ecdsa,
            sha256_ed25519=sha256_ed25519,
        )

        api_overview_ssh_key_fingerprints.additional_properties = d
        return api_overview_ssh_key_fingerprints

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
