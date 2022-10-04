from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GitTagObject")


@attr.s(auto_attribs=True)
class GitTagObject:
    """
    Attributes:
        sha (str):
        type (str):
        url (str):
    """

    sha: str
    type: str
    url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sha = self.sha
        type = self.type
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha": sha,
                "type": type,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sha = d.pop("sha")

        type = d.pop("type")

        url = d.pop("url")

        git_tag_object = cls(
            sha=sha,
            type=type,
            url=url,
        )

        git_tag_object.additional_properties = d
        return git_tag_object

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
