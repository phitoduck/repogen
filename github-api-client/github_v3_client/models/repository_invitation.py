import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="RepositoryInvitation")


@attr.s(auto_attribs=True)
class RepositoryInvitation:
    """Repository invitations let you manage who you collaborate with.

    Attributes:
        subscribed (bool): Determines if notifications should be received from this repository. Example: True.
        ignored (bool): Determines if all notifications should be blocked from this repository.
        created_at (datetime.datetime):  Example: 2012-10-06T21:34:12Z.
        url (str):  Example: https://api.github.com/repos/octocat/example/subscription.
        repository_url (str):  Example: https://api.github.com/repos/octocat/example.
        reason (Optional[str]):
    """

    subscribed: bool
    ignored: bool
    created_at: datetime.datetime
    url: str
    repository_url: str
    reason: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subscribed = self.subscribed
        ignored = self.ignored
        created_at = self.created_at.isoformat()

        url = self.url
        repository_url = self.repository_url
        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscribed": subscribed,
                "ignored": ignored,
                "created_at": created_at,
                "url": url,
                "repository_url": repository_url,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subscribed = d.pop("subscribed")

        ignored = d.pop("ignored")

        created_at = isoparse(d.pop("created_at"))

        url = d.pop("url")

        repository_url = d.pop("repository_url")

        reason = d.pop("reason")

        repository_invitation = cls(
            subscribed=subscribed,
            ignored=ignored,
            created_at=created_at,
            url=url,
            repository_url=repository_url,
            reason=reason,
        )

        repository_invitation.additional_properties = d
        return repository_invitation

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
