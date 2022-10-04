import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.hook_response import HookResponse
from ..models.webhook_config import WebhookConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="Webhook")


@attr.s(auto_attribs=True)
class Webhook:
    """Webhooks for repositories.

    Attributes:
        type (str):
        id (int): Unique identifier of the webhook. Example: 42.
        name (str): The name of a valid service, use 'web' for a webhook. Example: web.
        active (bool): Determines whether the hook is actually triggered on pushes. Example: True.
        events (List[str]): Determines what events the hook is triggered for. Default: ['push']. Example: ['push',
            'pull_request'].
        config (WebhookConfig):
        updated_at (datetime.datetime):  Example: 2011-09-06T20:39:23Z.
        created_at (datetime.datetime):  Example: 2011-09-06T17:26:27Z.
        url (str):  Example: https://api.github.com/repos/octocat/Hello-World/hooks/1.
        test_url (str):  Example: https://api.github.com/repos/octocat/Hello-World/hooks/1/test.
        ping_url (str):  Example: https://api.github.com/repos/octocat/Hello-World/hooks/1/pings.
        last_response (HookResponse):
        deliveries_url (Union[Unset, str]):  Example: https://api.github.com/repos/octocat/Hello-
            World/hooks/1/deliveries.
    """

    type: str
    id: int
    name: str
    active: bool
    events: List[str]
    config: WebhookConfig
    updated_at: datetime.datetime
    created_at: datetime.datetime
    url: str
    test_url: str
    ping_url: str
    last_response: HookResponse
    deliveries_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        id = self.id
        name = self.name
        active = self.active
        events = self.events

        config = self.config.to_dict()

        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        url = self.url
        test_url = self.test_url
        ping_url = self.ping_url
        last_response = self.last_response.to_dict()

        deliveries_url = self.deliveries_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
                "name": name,
                "active": active,
                "events": events,
                "config": config,
                "updated_at": updated_at,
                "created_at": created_at,
                "url": url,
                "test_url": test_url,
                "ping_url": ping_url,
                "last_response": last_response,
            }
        )
        if deliveries_url is not UNSET:
            field_dict["deliveries_url"] = deliveries_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        id = d.pop("id")

        name = d.pop("name")

        active = d.pop("active")

        events = cast(List[str], d.pop("events"))

        config = WebhookConfig.from_dict(d.pop("config"))

        updated_at = isoparse(d.pop("updated_at"))

        created_at = isoparse(d.pop("created_at"))

        url = d.pop("url")

        test_url = d.pop("test_url")

        ping_url = d.pop("ping_url")

        last_response = HookResponse.from_dict(d.pop("last_response"))

        deliveries_url = d.pop("deliveries_url", UNSET)

        webhook = cls(
            type=type,
            id=id,
            name=name,
            active=active,
            events=events,
            config=config,
            updated_at=updated_at,
            created_at=created_at,
            url=url,
            test_url=test_url,
            ping_url=ping_url,
            last_response=last_response,
            deliveries_url=deliveries_url,
        )

        webhook.additional_properties = d
        return webhook

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
