from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Actor")


@attr.s(auto_attribs=True)
class Actor:
    """Actor

    Attributes:
        id (int):
        login (str):
        url (str):
        avatar_url (str):
        display_login (Union[Unset, str]):
        gravatar_id (Optional[str]):
    """

    id: int
    login: str
    url: str
    avatar_url: str
    gravatar_id: Optional[str]
    display_login: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        login = self.login
        url = self.url
        avatar_url = self.avatar_url
        display_login = self.display_login
        gravatar_id = self.gravatar_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "login": login,
                "url": url,
                "avatar_url": avatar_url,
                "gravatar_id": gravatar_id,
            }
        )
        if display_login is not UNSET:
            field_dict["display_login"] = display_login

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        login = d.pop("login")

        url = d.pop("url")

        avatar_url = d.pop("avatar_url")

        display_login = d.pop("display_login", UNSET)

        gravatar_id = d.pop("gravatar_id")

        actor = cls(
            id=id,
            login=login,
            url=url,
            avatar_url=avatar_url,
            display_login=display_login,
            gravatar_id=gravatar_id,
        )

        actor.additional_properties = d
        return actor

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
