from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodespacesPublicKey")


@attr.s(auto_attribs=True)
class CodespacesPublicKey:
    """The public key used for setting Codespaces secrets.

    Attributes:
        key_id (str): The identifier for the key. Example: 1234567.
        key (str): The Base64 encoded public key. Example: hBT5WZEj8ZoOv6TYJsfWq7MxTEQopZO5/IT3ZCVQPzs=.
        id (Union[Unset, int]):  Example: 2.
        url (Union[Unset, str]):  Example: https://api.github.com/user/keys/2.
        title (Union[Unset, str]):  Example: ssh-rsa AAAAB3NzaC1yc2EAAA.
        created_at (Union[Unset, str]):  Example: 2011-01-26T19:01:12Z.
    """

    key_id: str
    key: str
    id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_id = self.key_id
        key = self.key
        id = self.id
        url = self.url
        title = self.title
        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key_id": key_id,
                "key": key,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if title is not UNSET:
            field_dict["title"] = title
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_id = d.pop("key_id")

        key = d.pop("key")

        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        title = d.pop("title", UNSET)

        created_at = d.pop("created_at", UNSET)

        codespaces_public_key = cls(
            key_id=key_id,
            key=key,
            id=id,
            url=url,
            title=title,
            created_at=created_at,
        )

        codespaces_public_key.additional_properties = d
        return codespaces_public_key

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
