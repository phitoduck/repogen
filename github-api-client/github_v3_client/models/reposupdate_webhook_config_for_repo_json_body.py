from typing import Any, Dict, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdateWebhookConfigForRepoJsonBody")


@attr.s(auto_attribs=True)
class ReposupdateWebhookConfigForRepoJsonBody:
    """
    Example:
        {'content_type': 'json', 'insecure_ssl': '0', 'secret': '********', 'url': 'https://example.com/webhook'}

    Attributes:
        url (Union[Unset, str]): The URL to which the payloads will be delivered. Example: https://example.com/webhook.
        content_type (Union[Unset, str]): The media type used to serialize the payloads. Supported values include `json`
            and `form`. The default is `form`. Example: "json".
        secret (Union[Unset, str]): If provided, the `secret` will be used as the `key` to generate the HMAC hex digest
            value for [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers).
            Example: "********".
        insecure_ssl (Union[Unset, float, str]):
    """

    url: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    insecure_ssl: Union[Unset, float, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        content_type = self.content_type
        secret = self.secret
        insecure_ssl: Union[Unset, float, str]
        if isinstance(self.insecure_ssl, Unset):
            insecure_ssl = UNSET

        else:
            insecure_ssl = self.insecure_ssl

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if secret is not UNSET:
            field_dict["secret"] = secret
        if insecure_ssl is not UNSET:
            field_dict["insecure_ssl"] = insecure_ssl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        content_type = d.pop("content_type", UNSET)

        secret = d.pop("secret", UNSET)

        def _parse_insecure_ssl(data: object) -> Union[Unset, float, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, str], data)

        insecure_ssl = _parse_insecure_ssl(d.pop("insecure_ssl", UNSET))

        reposupdate_webhook_config_for_repo_json_body = cls(
            url=url,
            content_type=content_type,
            secret=secret,
            insecure_ssl=insecure_ssl,
        )

        return reposupdate_webhook_config_for_repo_json_body
