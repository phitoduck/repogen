import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivitymarkRepoNotificationsAsReadJsonBody")


@attr.s(auto_attribs=True)
class ActivitymarkRepoNotificationsAsReadJsonBody:
    """
    Attributes:
        last_read_at (Union[Unset, datetime.datetime]): Describes the last point that notifications were checked.
            Anything updated since this time will not be marked as read. If you omit this parameter, all notifications are
            marked as read. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-
            DDTHH:MM:SSZ`. Default: The current timestamp.
    """

    last_read_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_read_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_read_at, Unset):
            last_read_at = self.last_read_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_read_at is not UNSET:
            field_dict["last_read_at"] = last_read_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _last_read_at = d.pop("last_read_at", UNSET)
        last_read_at: Union[Unset, datetime.datetime]
        if isinstance(_last_read_at, Unset):
            last_read_at = UNSET
        else:
            last_read_at = isoparse(_last_read_at)

        activitymark_repo_notifications_as_read_json_body = cls(
            last_read_at=last_read_at,
        )

        activitymark_repo_notifications_as_read_json_body.additional_properties = d
        return activitymark_repo_notifications_as_read_json_body

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
