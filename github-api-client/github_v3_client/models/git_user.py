from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitUser")


@attr.s(auto_attribs=True)
class GitUser:
    """Metaproperties for Git author/committer information.

    Attributes:
        name (Union[Unset, str]):  Example: "Chris Wanstrath".
        email (Union[Unset, str]):  Example: "chris@ozmm.org".
        date (Union[Unset, str]):  Example: "2007-10-29T02:42:39.000-07:00".
    """

    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        email = self.email
        date = self.date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        date = d.pop("date", UNSET)

        git_user = cls(
            name=name,
            email=email,
            date=date,
        )

        git_user.additional_properties = d
        return git_user

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
