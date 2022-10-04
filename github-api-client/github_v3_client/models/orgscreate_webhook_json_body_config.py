from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgscreateWebhookJsonBodyConfig")


@attr.s(auto_attribs=True)
class OrgscreateWebhookJsonBodyConfig:
    """Key/value pairs to provide settings for this webhook. [These are defined
    below](https://docs.github.com/rest/reference/orgs#create-hook-config-params).

        Attributes:
            url (str): The URL to which the payloads will be delivered. Example: https://example.com/webhook.
            content_type (Union[Unset, str]): The media type used to serialize the payloads. Supported values include `json`
                and `form`. The default is `form`. Example: "json".
            secret (Union[Unset, str]): If provided, the `secret` will be used as the `key` to generate the HMAC hex digest
                value for [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers).
                Example: "********".
            insecure_ssl (Union[Unset, float, str]):
            username (Union[Unset, str]):  Example: "kdaigle".
            password (Union[Unset, str]):  Example: "password".
    """

    url: str
    content_type: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    insecure_ssl: Union[Unset, float, str] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        content_type = self.content_type
        secret = self.secret
        insecure_ssl: Union[Unset, float, str]
        if isinstance(self.insecure_ssl, Unset):
            insecure_ssl = UNSET

        else:
            insecure_ssl = self.insecure_ssl

        username = self.username
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if secret is not UNSET:
            field_dict["secret"] = secret
        if insecure_ssl is not UNSET:
            field_dict["insecure_ssl"] = insecure_ssl
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        content_type = d.pop("content_type", UNSET)

        secret = d.pop("secret", UNSET)

        def _parse_insecure_ssl(data: object) -> Union[Unset, float, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, str], data)

        insecure_ssl = _parse_insecure_ssl(d.pop("insecure_ssl", UNSET))

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        orgscreate_webhook_json_body_config = cls(
            url=url,
            content_type=content_type,
            secret=secret,
            insecure_ssl=insecure_ssl,
            username=username,
            password=password,
        )

        orgscreate_webhook_json_body_config.additional_properties = d
        return orgscreate_webhook_json_body_config

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
