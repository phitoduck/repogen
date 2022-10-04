import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="TimelineCommittedEventCommitter")


@attr.s(auto_attribs=True)
class TimelineCommittedEventCommitter:
    """Identifying information for the git-user

    Attributes:
        date (datetime.datetime): Timestamp of the commit Example: 2014-08-09T08:02:04+12:00.
        email (str): Git email address of the user Example: monalisa.octocat@example.com.
        name (str): Name of the git user Example: Monalisa Octocat.
    """

    date: datetime.datetime
    email: str
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date.isoformat()

        email = self.email
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "email": email,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = isoparse(d.pop("date"))

        email = d.pop("email")

        name = d.pop("name")

        timeline_committed_event_committer = cls(
            date=date,
            email=email,
            name=name,
        )

        timeline_committed_event_committer.additional_properties = d
        return timeline_committed_event_committer

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
