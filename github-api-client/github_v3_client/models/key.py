import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="Key")


@attr.s(auto_attribs=True)
class Key:
    """Key

    Attributes:
        key (str):
        id (int):
        url (str):
        title (str):
        created_at (datetime.datetime):
        verified (bool):
        read_only (bool):
    """

    key: str
    id: int
    url: str
    title: str
    created_at: datetime.datetime
    verified: bool
    read_only: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        id = self.id
        url = self.url
        title = self.title
        created_at = self.created_at.isoformat()

        verified = self.verified
        read_only = self.read_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "id": id,
                "url": url,
                "title": title,
                "created_at": created_at,
                "verified": verified,
                "read_only": read_only,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        id = d.pop("id")

        url = d.pop("url")

        title = d.pop("title")

        created_at = isoparse(d.pop("created_at"))

        verified = d.pop("verified")

        read_only = d.pop("read_only")

        key = cls(
            key=key,
            id=id,
            url=url,
            title=title,
            created_at=created_at,
            verified=verified,
            read_only=read_only,
        )

        key.additional_properties = d
        return key

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
