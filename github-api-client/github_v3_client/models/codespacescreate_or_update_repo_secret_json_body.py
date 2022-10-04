from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodespacescreateOrUpdateRepoSecretJsonBody")


@attr.s(auto_attribs=True)
class CodespacescreateOrUpdateRepoSecretJsonBody:
    """
    Attributes:
        encrypted_value (Union[Unset, str]): Value for your secret, encrypted with
            [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from
            the [Get a repository public key](https://docs.github.com/rest/reference/codespaces#get-a-repository-public-key)
            endpoint.
        key_id (Union[Unset, str]): ID of the key you used to encrypt the secret.
    """

    encrypted_value: Union[Unset, str] = UNSET
    key_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encrypted_value = self.encrypted_value
        key_id = self.key_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encrypted_value is not UNSET:
            field_dict["encrypted_value"] = encrypted_value
        if key_id is not UNSET:
            field_dict["key_id"] = key_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        encrypted_value = d.pop("encrypted_value", UNSET)

        key_id = d.pop("key_id", UNSET)

        codespacescreate_or_update_repo_secret_json_body = cls(
            encrypted_value=encrypted_value,
            key_id=key_id,
        )

        codespacescreate_or_update_repo_secret_json_body.additional_properties = d
        return codespacescreate_or_update_repo_secret_json_body

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
