from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.reposupdate_webhook_json_body_config import ReposupdateWebhookJsonBodyConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdateWebhookJsonBody")


@attr.s(auto_attribs=True)
class ReposupdateWebhookJsonBody:
    """
    Attributes:
        config (Union[Unset, ReposupdateWebhookJsonBodyConfig]): Key/value pairs to provide settings for this webhook.
            [These are defined below](https://docs.github.com/rest/reference/repos#create-hook-config-params).
        events (Union[Unset, List[str]]): Determines what [events](https://docs.github.com/webhooks/event-payloads) the
            hook is triggered for. This replaces the entire array of events.
        add_events (Union[Unset, List[str]]): Determines a list of events to be added to the list of events that the
            Hook triggers for.
        remove_events (Union[Unset, List[str]]): Determines a list of events to be removed from the list of events that
            the Hook triggers for.
        active (Union[Unset, bool]): Determines if notifications are sent when the webhook is triggered. Set to `true`
            to send notifications. Default: True.
    """

    config: Union[Unset, ReposupdateWebhookJsonBodyConfig] = UNSET
    events: Union[Unset, List[str]] = UNSET
    add_events: Union[Unset, List[str]] = UNSET
    remove_events: Union[Unset, List[str]] = UNSET
    active: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        add_events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.add_events, Unset):
            add_events = self.add_events

        remove_events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.remove_events, Unset):
            remove_events = self.remove_events

        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if events is not UNSET:
            field_dict["events"] = events
        if add_events is not UNSET:
            field_dict["add_events"] = add_events
        if remove_events is not UNSET:
            field_dict["remove_events"] = remove_events
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, ReposupdateWebhookJsonBodyConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ReposupdateWebhookJsonBodyConfig.from_dict(_config)

        events = cast(List[str], d.pop("events", UNSET))

        add_events = cast(List[str], d.pop("add_events", UNSET))

        remove_events = cast(List[str], d.pop("remove_events", UNSET))

        active = d.pop("active", UNSET)

        reposupdate_webhook_json_body = cls(
            config=config,
            events=events,
            add_events=add_events,
            remove_events=remove_events,
            active=active,
        )

        reposupdate_webhook_json_body.additional_properties = d
        return reposupdate_webhook_json_body

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
