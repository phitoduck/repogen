import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.page_build_error import PageBuildError
from ..models.simple_user import SimpleUser

T = TypeVar("T", bound="PageBuild")


@attr.s(auto_attribs=True)
class PageBuild:
    """Page Build

    Attributes:
        url (str):
        status (str):
        error (PageBuildError):
        commit (str):
        duration (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        pusher (Optional[SimpleUser]): Simple User
    """

    url: str
    status: str
    error: PageBuildError
    commit: str
    duration: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    pusher: Optional[SimpleUser]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        status = self.status
        error = self.error.to_dict()

        commit = self.commit
        duration = self.duration
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        pusher = self.pusher.to_dict() if self.pusher else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "status": status,
                "error": error,
                "commit": commit,
                "duration": duration,
                "created_at": created_at,
                "updated_at": updated_at,
                "pusher": pusher,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        status = d.pop("status")

        error = PageBuildError.from_dict(d.pop("error"))

        commit = d.pop("commit")

        duration = d.pop("duration")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        _pusher = d.pop("pusher")
        pusher: Optional[SimpleUser]
        if _pusher is None:
            pusher = None
        else:
            pusher = SimpleUser.from_dict(_pusher)

        page_build = cls(
            url=url,
            status=status,
            error=error,
            commit=commit,
            duration=duration,
            created_at=created_at,
            updated_at=updated_at,
            pusher=pusher,
        )

        page_build.additional_properties = d
        return page_build

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
