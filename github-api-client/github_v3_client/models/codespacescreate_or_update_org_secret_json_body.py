from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.codespacescreate_or_update_org_secret_json_body_visibility import (
    CodespacescreateOrUpdateOrgSecretJsonBodyVisibility,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodespacescreateOrUpdateOrgSecretJsonBody")


@attr.s(auto_attribs=True)
class CodespacescreateOrUpdateOrgSecretJsonBody:
    """
    Attributes:
        visibility (CodespacescreateOrUpdateOrgSecretJsonBodyVisibility): Which type of organization repositories have
            access to the organization secret. `selected` means only the repositories specified by `selected_repository_ids`
            can access the secret.
        encrypted_value (Union[Unset, str]): The value for your secret, encrypted with
            [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from
            the [Get an organization public key](https://docs.github.com/rest/reference/codespaces#get-an-organization-
            public-key) endpoint.
        key_id (Union[Unset, str]): The ID of the key you used to encrypt the secret.
        selected_repository_ids (Union[Unset, List[int]]): An array of repository IDs that can access the organization
            secret. You can only provide a list of repository IDs when the `visibility` is set to `selected`. You can manage
            the list of selected repositories using the [List selected repositories for an organization
            secret](https://docs.github.com/rest/reference/codespaces#list-selected-repositories-for-an-organization-
            secret), [Set selected repositories for an organization
            secret](https://docs.github.com/rest/reference/codespaces#set-selected-repositories-for-an-organization-secret),
            and [Remove selected repository from an organization
            secret](https://docs.github.com/rest/reference/codespaces#remove-selected-repository-from-an-organization-
            secret) endpoints.
    """

    visibility: CodespacescreateOrUpdateOrgSecretJsonBodyVisibility
    encrypted_value: Union[Unset, str] = UNSET
    key_id: Union[Unset, str] = UNSET
    selected_repository_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        visibility = self.visibility.value

        encrypted_value = self.encrypted_value
        key_id = self.key_id
        selected_repository_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.selected_repository_ids, Unset):
            selected_repository_ids = self.selected_repository_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "visibility": visibility,
            }
        )
        if encrypted_value is not UNSET:
            field_dict["encrypted_value"] = encrypted_value
        if key_id is not UNSET:
            field_dict["key_id"] = key_id
        if selected_repository_ids is not UNSET:
            field_dict["selected_repository_ids"] = selected_repository_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        visibility = CodespacescreateOrUpdateOrgSecretJsonBodyVisibility(d.pop("visibility"))

        encrypted_value = d.pop("encrypted_value", UNSET)

        key_id = d.pop("key_id", UNSET)

        selected_repository_ids = cast(List[int], d.pop("selected_repository_ids", UNSET))

        codespacescreate_or_update_org_secret_json_body = cls(
            visibility=visibility,
            encrypted_value=encrypted_value,
            key_id=key_id,
            selected_repository_ids=selected_repository_ids,
        )

        codespacescreate_or_update_org_secret_json_body.additional_properties = d
        return codespacescreate_or_update_org_secret_json_body

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
