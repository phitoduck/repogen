import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.gist_commit_change_status import GistCommitChangeStatus
from ..models.simple_user import SimpleUser

T = TypeVar("T", bound="GistCommit")


@attr.s(auto_attribs=True)
class GistCommit:
    """Gist Commit

    Attributes:
        url (str):  Example: https://api.github.com/gists/aa5a315d61ae9438b18d/57a7f021a713b1c5a6a199b54cc514735d2d462f.
        version (str):  Example: 57a7f021a713b1c5a6a199b54cc514735d2d462f.
        change_status (GistCommitChangeStatus):
        committed_at (datetime.datetime):  Example: 2010-04-14T02:15:15Z.
        user (Optional[SimpleUser]): Simple User
    """

    url: str
    version: str
    change_status: GistCommitChangeStatus
    committed_at: datetime.datetime
    user: Optional[SimpleUser]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        version = self.version
        change_status = self.change_status.to_dict()

        committed_at = self.committed_at.isoformat()

        user = self.user.to_dict() if self.user else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "version": version,
                "change_status": change_status,
                "committed_at": committed_at,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        version = d.pop("version")

        change_status = GistCommitChangeStatus.from_dict(d.pop("change_status"))

        committed_at = isoparse(d.pop("committed_at"))

        _user = d.pop("user")
        user: Optional[SimpleUser]
        if _user is None:
            user = None
        else:
            user = SimpleUser.from_dict(_user)

        gist_commit = cls(
            url=url,
            version=version,
            change_status=change_status,
            committed_at=committed_at,
            user=user,
        )

        gist_commit.additional_properties = d
        return gist_commit

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
