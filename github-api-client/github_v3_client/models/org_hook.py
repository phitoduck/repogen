import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.org_hook_config import OrgHookConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgHook")


@attr.s(auto_attribs=True)
class OrgHook:
    """Org Hook

    Attributes:
        id (int):  Example: 1.
        url (str):  Example: https://api.github.com/orgs/octocat/hooks/1.
        ping_url (str):  Example: https://api.github.com/orgs/octocat/hooks/1/pings.
        name (str):  Example: web.
        events (List[str]):  Example: ['push', 'pull_request'].
        active (bool):  Example: True.
        config (OrgHookConfig):
        updated_at (datetime.datetime):  Example: 2011-09-06T20:39:23Z.
        created_at (datetime.datetime):  Example: 2011-09-06T17:26:27Z.
        type (str):
        deliveries_url (Union[Unset, str]):  Example: https://api.github.com/orgs/octocat/hooks/1/deliveries.
    """

    id: int
    url: str
    ping_url: str
    name: str
    events: List[str]
    active: bool
    config: OrgHookConfig
    updated_at: datetime.datetime
    created_at: datetime.datetime
    type: str
    deliveries_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        ping_url = self.ping_url
        name = self.name
        events = self.events

        active = self.active
        config = self.config.to_dict()

        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        type = self.type
        deliveries_url = self.deliveries_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "ping_url": ping_url,
                "name": name,
                "events": events,
                "active": active,
                "config": config,
                "updated_at": updated_at,
                "created_at": created_at,
                "type": type,
            }
        )
        if deliveries_url is not UNSET:
            field_dict["deliveries_url"] = deliveries_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        ping_url = d.pop("ping_url")

        name = d.pop("name")

        events = cast(List[str], d.pop("events"))

        active = d.pop("active")

        config = OrgHookConfig.from_dict(d.pop("config"))

        updated_at = isoparse(d.pop("updated_at"))

        created_at = isoparse(d.pop("created_at"))

        type = d.pop("type")

        deliveries_url = d.pop("deliveries_url", UNSET)

        org_hook = cls(
            id=id,
            url=url,
            ping_url=ping_url,
            name=name,
            events=events,
            active=active,
            config=config,
            updated_at=updated_at,
            created_at=created_at,
            type=type,
            deliveries_url=deliveries_url,
        )

        org_hook.additional_properties = d
        return org_hook

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
