from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.reposcreate_webhook_json_body_config import ReposcreateWebhookJsonBodyConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateWebhookJsonBody")


@attr.s(auto_attribs=True)
class ReposcreateWebhookJsonBody:
    """
    Attributes:
        name (Union[Unset, str]): Use `web` to create a webhook. Default: `web`. This parameter only accepts the value
            `web`.
        config (Union[Unset, ReposcreateWebhookJsonBodyConfig]): Key/value pairs to provide settings for this webhook.
            [These are defined below](https://docs.github.com/rest/reference/repos#create-hook-config-params).
        events (Union[Unset, List[str]]): Determines what [events](https://docs.github.com/webhooks/event-payloads) the
            hook is triggered for.
        active (Union[Unset, bool]): Determines if notifications are sent when the webhook is triggered. Set to `true`
            to send notifications. Default: True.
    """

    name: Union[Unset, str] = UNSET
    config: Union[Unset, ReposcreateWebhookJsonBodyConfig] = UNSET
    events: Union[Unset, List[str]] = UNSET
    active: Union[Unset, bool] = True

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if config is not UNSET:
            field_dict["config"] = config
        if events is not UNSET:
            field_dict["events"] = events
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, ReposcreateWebhookJsonBodyConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ReposcreateWebhookJsonBodyConfig.from_dict(_config)

        events = cast(List[str], d.pop("events", UNSET))

        active = d.pop("active", UNSET)

        reposcreate_webhook_json_body = cls(
            name=name,
            config=config,
            events=events,
            active=active,
        )

        return reposcreate_webhook_json_body
