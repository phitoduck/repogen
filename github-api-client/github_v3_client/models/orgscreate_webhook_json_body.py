from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.orgscreate_webhook_json_body_config import OrgscreateWebhookJsonBodyConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgscreateWebhookJsonBody")


@attr.s(auto_attribs=True)
class OrgscreateWebhookJsonBody:
    """
    Attributes:
        name (str): Must be passed as "web".
        config (OrgscreateWebhookJsonBodyConfig): Key/value pairs to provide settings for this webhook. [These are
            defined below](https://docs.github.com/rest/reference/orgs#create-hook-config-params).
        events (Union[Unset, List[str]]): Determines what [events](https://docs.github.com/webhooks/event-payloads) the
            hook is triggered for.
        active (Union[Unset, bool]): Determines if notifications are sent when the webhook is triggered. Set to `true`
            to send notifications. Default: True.
    """

    name: str
    config: OrgscreateWebhookJsonBodyConfig
    events: Union[Unset, List[str]] = UNSET
    active: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        config = self.config.to_dict()

        events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "config": config,
            }
        )
        if events is not UNSET:
            field_dict["events"] = events
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        config = OrgscreateWebhookJsonBodyConfig.from_dict(d.pop("config"))

        events = cast(List[str], d.pop("events", UNSET))

        active = d.pop("active", UNSET)

        orgscreate_webhook_json_body = cls(
            name=name,
            config=config,
            events=events,
            active=active,
        )

        orgscreate_webhook_json_body.additional_properties = d
        return orgscreate_webhook_json_body

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
