import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.simple_user import SimpleUser

T = TypeVar("T", bound="Stargazer")


@attr.s(auto_attribs=True)
class Stargazer:
    """Stargazer

    Attributes:
        starred_at (datetime.datetime):
        user (Optional[SimpleUser]): Simple User
    """

    starred_at: datetime.datetime
    user: Optional[SimpleUser]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        starred_at = self.starred_at.isoformat()

        user = self.user.to_dict() if self.user else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "starred_at": starred_at,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        starred_at = isoparse(d.pop("starred_at"))

        _user = d.pop("user")
        user: Optional[SimpleUser]
        if _user is None:
            user = None
        else:
            user = SimpleUser.from_dict(_user)

        stargazer = cls(
            starred_at=starred_at,
            user=user,
        )

        stargazer.additional_properties = d
        return stargazer

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
