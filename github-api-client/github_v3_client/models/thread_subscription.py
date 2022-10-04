import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThreadSubscription")


@attr.s(auto_attribs=True)
class ThreadSubscription:
    """Thread Subscription

    Attributes:
        subscribed (bool):  Example: True.
        ignored (bool):
        url (str):  Example: https://api.github.com/notifications/threads/1/subscription.
        reason (Optional[str]):
        created_at (Optional[datetime.datetime]):  Example: 2012-10-06T21:34:12Z.
        thread_url (Union[Unset, str]):  Example: https://api.github.com/notifications/threads/1.
        repository_url (Union[Unset, str]):  Example: https://api.github.com/repos/1.
    """

    subscribed: bool
    ignored: bool
    url: str
    reason: Optional[str]
    created_at: Optional[datetime.datetime]
    thread_url: Union[Unset, str] = UNSET
    repository_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subscribed = self.subscribed
        ignored = self.ignored
        url = self.url
        reason = self.reason
        created_at = self.created_at.isoformat() if self.created_at else None

        thread_url = self.thread_url
        repository_url = self.repository_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscribed": subscribed,
                "ignored": ignored,
                "url": url,
                "reason": reason,
                "created_at": created_at,
            }
        )
        if thread_url is not UNSET:
            field_dict["thread_url"] = thread_url
        if repository_url is not UNSET:
            field_dict["repository_url"] = repository_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subscribed = d.pop("subscribed")

        ignored = d.pop("ignored")

        url = d.pop("url")

        reason = d.pop("reason")

        _created_at = d.pop("created_at")
        created_at: Optional[datetime.datetime]
        if _created_at is None:
            created_at = None
        else:
            created_at = isoparse(_created_at)

        thread_url = d.pop("thread_url", UNSET)

        repository_url = d.pop("repository_url", UNSET)

        thread_subscription = cls(
            subscribed=subscribed,
            ignored=ignored,
            url=url,
            reason=reason,
            created_at=created_at,
            thread_url=thread_url,
            repository_url=repository_url,
        )

        thread_subscription.additional_properties = d
        return thread_subscription

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
