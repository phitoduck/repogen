from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateOrUpdateFileContentsJsonBodyAuthor")


@attr.s(auto_attribs=True)
class ReposcreateOrUpdateFileContentsJsonBodyAuthor:
    """The author of the file. Default: The `committer` or the authenticated user if you omit `committer`.

    Attributes:
        name (str): The name of the author or committer of the commit. You'll receive a `422` status code if `name` is
            omitted.
        email (str): The email of the author or committer of the commit. You'll receive a `422` status code if `email`
            is omitted.
        date (Union[Unset, str]):  Example: "2013-01-15T17:13:22+05:00".
    """

    name: str
    email: str
    date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        email = self.email
        date = self.date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "email": email,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        email = d.pop("email")

        date = d.pop("date", UNSET)

        reposcreate_or_update_file_contents_json_body_author = cls(
            name=name,
            email=email,
            date=date,
        )

        reposcreate_or_update_file_contents_json_body_author.additional_properties = d
        return reposcreate_or_update_file_contents_json_body_author

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
