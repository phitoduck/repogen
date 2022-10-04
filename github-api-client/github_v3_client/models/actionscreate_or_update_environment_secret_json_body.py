from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ActionscreateOrUpdateEnvironmentSecretJsonBody")


@attr.s(auto_attribs=True)
class ActionscreateOrUpdateEnvironmentSecretJsonBody:
    """
    Attributes:
        encrypted_value (str): Value for your secret, encrypted with
            [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from
            the [Get an environment public key](https://docs.github.com/rest/reference/actions#get-an-environment-public-
            key) endpoint.
        key_id (str): ID of the key you used to encrypt the secret.
    """

    encrypted_value: str
    key_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encrypted_value = self.encrypted_value
        key_id = self.key_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "encrypted_value": encrypted_value,
                "key_id": key_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        encrypted_value = d.pop("encrypted_value")

        key_id = d.pop("key_id")

        actionscreate_or_update_environment_secret_json_body = cls(
            encrypted_value=encrypted_value,
            key_id=key_id,
        )

        actionscreate_or_update_environment_secret_json_body.additional_properties = d
        return actionscreate_or_update_environment_secret_json_body

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
