import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="SSHSigningKey")


@attr.s(auto_attribs=True)
class SSHSigningKey:
    """A public SSH key used to sign Git commits

    Attributes:
        key (str):
        id (int):
        title (str):
        created_at (datetime.datetime):
    """

    key: str
    id: int
    title: str
    created_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        id = self.id
        title = self.title
        created_at = self.created_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "id": id,
                "title": title,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        id = d.pop("id")

        title = d.pop("title")

        created_at = isoparse(d.pop("created_at"))

        ssh_signing_key = cls(
            key=key,
            id=id,
            title=title,
            created_at=created_at,
        )

        ssh_signing_key.additional_properties = d
        return ssh_signing_key

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
