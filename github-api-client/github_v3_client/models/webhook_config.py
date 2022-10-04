from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookConfig")


@attr.s(auto_attribs=True)
class WebhookConfig:
    """
    Attributes:
        email (Union[Unset, str]):  Example: "foo@bar.com".
        password (Union[Unset, str]):  Example: "foo".
        room (Union[Unset, str]):  Example: "roomer".
        subdomain (Union[Unset, str]):  Example: "foo".
        url (Union[Unset, str]): The URL to which the payloads will be delivered. Example: https://example.com/webhook.
        insecure_ssl (Union[Unset, float, str]):
        content_type (Union[Unset, str]): The media type used to serialize the payloads. Supported values include `json`
            and `form`. The default is `form`. Example: "json".
        digest (Union[Unset, str]):  Example: "sha256".
        secret (Union[Unset, str]): If provided, the `secret` will be used as the `key` to generate the HMAC hex digest
            value for [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers).
            Example: "********".
        token (Union[Unset, str]):  Example: "abc".
    """

    email: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    room: Union[Unset, str] = UNSET
    subdomain: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    insecure_ssl: Union[Unset, float, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    digest: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        password = self.password
        room = self.room
        subdomain = self.subdomain
        url = self.url
        insecure_ssl: Union[Unset, float, str]
        if isinstance(self.insecure_ssl, Unset):
            insecure_ssl = UNSET

        else:
            insecure_ssl = self.insecure_ssl

        content_type = self.content_type
        digest = self.digest
        secret = self.secret
        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if password is not UNSET:
            field_dict["password"] = password
        if room is not UNSET:
            field_dict["room"] = room
        if subdomain is not UNSET:
            field_dict["subdomain"] = subdomain
        if url is not UNSET:
            field_dict["url"] = url
        if insecure_ssl is not UNSET:
            field_dict["insecure_ssl"] = insecure_ssl
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if digest is not UNSET:
            field_dict["digest"] = digest
        if secret is not UNSET:
            field_dict["secret"] = secret
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        password = d.pop("password", UNSET)

        room = d.pop("room", UNSET)

        subdomain = d.pop("subdomain", UNSET)

        url = d.pop("url", UNSET)

        def _parse_insecure_ssl(data: object) -> Union[Unset, float, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, str], data)

        insecure_ssl = _parse_insecure_ssl(d.pop("insecure_ssl", UNSET))

        content_type = d.pop("content_type", UNSET)

        digest = d.pop("digest", UNSET)

        secret = d.pop("secret", UNSET)

        token = d.pop("token", UNSET)

        webhook_config = cls(
            email=email,
            password=password,
            room=room,
            subdomain=subdomain,
            url=url,
            insecure_ssl=insecure_ssl,
            content_type=content_type,
            digest=digest,
            secret=secret,
            token=token,
        )

        webhook_config.additional_properties = d
        return webhook_config

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
