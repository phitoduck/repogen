import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitcreateCommitJsonBodyCommitter")


@attr.s(auto_attribs=True)
class GitcreateCommitJsonBodyCommitter:
    """Information about the person who is making the commit. By default, `committer` will use the information set in
    `author`. See the `author` and `committer` object below for details.

        Attributes:
            name (Union[Unset, str]): The name of the author (or committer) of the commit
            email (Union[Unset, str]): The email of the author (or committer) of the commit
            date (Union[Unset, datetime.datetime]): Indicates when this commit was authored (or committed). This is a
                timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        email = self.email
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

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

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        gitcreate_commit_json_body_committer = cls(
            name=name,
            email=email,
            date=date,
        )

        gitcreate_commit_json_body_committer.additional_properties = d
        return gitcreate_commit_json_body_committer

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
