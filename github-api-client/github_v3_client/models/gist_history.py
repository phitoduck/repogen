import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.gist_history_change_status import GistHistoryChangeStatus
from ..models.simple_user import SimpleUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="GistHistory")


@attr.s(auto_attribs=True)
class GistHistory:
    """Gist History

    Attributes:
        user (Union[Unset, None, SimpleUser]): Simple User
        version (Union[Unset, str]):
        committed_at (Union[Unset, datetime.datetime]):
        change_status (Union[Unset, GistHistoryChangeStatus]):
        url (Union[Unset, str]):
    """

    user: Union[Unset, None, SimpleUser] = UNSET
    version: Union[Unset, str] = UNSET
    committed_at: Union[Unset, datetime.datetime] = UNSET
    change_status: Union[Unset, GistHistoryChangeStatus] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict() if self.user else None

        version = self.version
        committed_at: Union[Unset, str] = UNSET
        if not isinstance(self.committed_at, Unset):
            committed_at = self.committed_at.isoformat()

        change_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.change_status, Unset):
            change_status = self.change_status.to_dict()

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if version is not UNSET:
            field_dict["version"] = version
        if committed_at is not UNSET:
            field_dict["committed_at"] = committed_at
        if change_status is not UNSET:
            field_dict["change_status"] = change_status
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _user = d.pop("user", UNSET)
        user: Union[Unset, None, SimpleUser]
        if _user is None:
            user = None
        elif isinstance(_user, Unset):
            user = UNSET
        else:
            user = SimpleUser.from_dict(_user)

        version = d.pop("version", UNSET)

        _committed_at = d.pop("committed_at", UNSET)
        committed_at: Union[Unset, datetime.datetime]
        if isinstance(_committed_at, Unset):
            committed_at = UNSET
        else:
            committed_at = isoparse(_committed_at)

        _change_status = d.pop("change_status", UNSET)
        change_status: Union[Unset, GistHistoryChangeStatus]
        if isinstance(_change_status, Unset):
            change_status = UNSET
        else:
            change_status = GistHistoryChangeStatus.from_dict(_change_status)

        url = d.pop("url", UNSET)

        gist_history = cls(
            user=user,
            version=version,
            committed_at=committed_at,
            change_status=change_status,
            url=url,
        )

        gist_history.additional_properties = d
        return gist_history

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
