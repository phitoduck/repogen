from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodespacescreateOrUpdateSecretForAuthenticatedUserJsonBody")


@attr.s(auto_attribs=True)
class CodespacescreateOrUpdateSecretForAuthenticatedUserJsonBody:
    """
    Attributes:
        key_id (str): ID of the key you used to encrypt the secret.
        encrypted_value (Union[Unset, str]): Value for your secret, encrypted with
            [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from
            the [Get the public key for the authenticated user](https://docs.github.com/rest/reference/codespaces#get-the-
            public-key-for-the-authenticated-user) endpoint.
        selected_repository_ids (Union[Unset, List[str]]): An array of repository ids that can access the user secret.
            You can manage the list of selected repositories using the [List selected repositories for a user
            secret](https://docs.github.com/rest/reference/codespaces#list-selected-repositories-for-a-user-secret), [Set
            selected repositories for a user secret](https://docs.github.com/rest/reference/codespaces#set-selected-
            repositories-for-a-user-secret), and [Remove a selected repository from a user
            secret](https://docs.github.com/rest/reference/codespaces#remove-a-selected-repository-from-a-user-secret)
            endpoints.
    """

    key_id: str
    encrypted_value: Union[Unset, str] = UNSET
    selected_repository_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_id = self.key_id
        encrypted_value = self.encrypted_value
        selected_repository_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.selected_repository_ids, Unset):
            selected_repository_ids = self.selected_repository_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key_id": key_id,
            }
        )
        if encrypted_value is not UNSET:
            field_dict["encrypted_value"] = encrypted_value
        if selected_repository_ids is not UNSET:
            field_dict["selected_repository_ids"] = selected_repository_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_id = d.pop("key_id")

        encrypted_value = d.pop("encrypted_value", UNSET)

        selected_repository_ids = cast(List[str], d.pop("selected_repository_ids", UNSET))

        codespacescreate_or_update_secret_for_authenticated_user_json_body = cls(
            key_id=key_id,
            encrypted_value=encrypted_value,
            selected_repository_ids=selected_repository_ids,
        )

        codespacescreate_or_update_secret_for_authenticated_user_json_body.additional_properties = d
        return codespacescreate_or_update_secret_for_authenticated_user_json_body

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
