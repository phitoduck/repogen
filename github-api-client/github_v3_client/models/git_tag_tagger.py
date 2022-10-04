from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GitTagTagger")


@attr.s(auto_attribs=True)
class GitTagTagger:
    """
    Attributes:
        date (str):
        email (str):
        name (str):
    """

    date: str
    email: str
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date
        email = self.email
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "email": email,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date")

        email = d.pop("email")

        name = d.pop("name")

        git_tag_tagger = cls(
            date=date,
            email=email,
            name=name,
        )

        git_tag_tagger.additional_properties = d
        return git_tag_tagger

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
