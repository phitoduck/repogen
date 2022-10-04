from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.orgsupdate_webhook_json_body_config import OrgsupdateWebhookJsonBodyConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgsupdateWebhookJsonBody")


@attr.s(auto_attribs=True)
class OrgsupdateWebhookJsonBody:
    """
    Attributes:
        config (Union[Unset, OrgsupdateWebhookJsonBodyConfig]): Key/value pairs to provide settings for this webhook.
            [These are defined below](https://docs.github.com/rest/reference/orgs#update-hook-config-params).
        events (Union[Unset, List[str]]): Determines what [events](https://docs.github.com/webhooks/event-payloads) the
            hook is triggered for.
        active (Union[Unset, bool]): Determines if notifications are sent when the webhook is triggered. Set to `true`
            to send notifications. Default: True.
        name (Union[Unset, str]):  Example: "web".
    """

    config: Union[Unset, OrgsupdateWebhookJsonBodyConfig] = UNSET
    events: Union[Unset, List[str]] = UNSET
    active: Union[Unset, bool] = True
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        active = self.active
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if events is not UNSET:
            field_dict["events"] = events
        if active is not UNSET:
            field_dict["active"] = active
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, OrgsupdateWebhookJsonBodyConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = OrgsupdateWebhookJsonBodyConfig.from_dict(_config)

        events = cast(List[str], d.pop("events", UNSET))

        active = d.pop("active", UNSET)

        name = d.pop("name", UNSET)

        orgsupdate_webhook_json_body = cls(
            config=config,
            events=events,
            active=active,
            name=name,
        )

        orgsupdate_webhook_json_body.additional_properties = d
        return orgsupdate_webhook_json_body

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
