from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgHookConfig")


@attr.s(auto_attribs=True)
class OrgHookConfig:
    """
    Attributes:
        url (Union[Unset, str]):  Example: "http://example.com/2".
        insecure_ssl (Union[Unset, str]):  Example: "0".
        content_type (Union[Unset, str]):  Example: "form".
        secret (Union[Unset, str]):  Example: "********".
    """

    url: Union[Unset, str] = UNSET
    insecure_ssl: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        insecure_ssl = self.insecure_ssl
        content_type = self.content_type
        secret = self.secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if insecure_ssl is not UNSET:
            field_dict["insecure_ssl"] = insecure_ssl
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        insecure_ssl = d.pop("insecure_ssl", UNSET)

        content_type = d.pop("content_type", UNSET)

        secret = d.pop("secret", UNSET)

        org_hook_config = cls(
            url=url,
            insecure_ssl=insecure_ssl,
            content_type=content_type,
            secret=secret,
        )

        org_hook_config.additional_properties = d
        return org_hook_config

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
