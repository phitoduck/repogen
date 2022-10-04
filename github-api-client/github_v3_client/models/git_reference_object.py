from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GitReferenceObject")


@attr.s(auto_attribs=True)
class GitReferenceObject:
    """
    Attributes:
        type (str):
        sha (str): SHA for the reference Example: 7638417db6d59f3c431d3e1f261cc637155684cd.
        url (str):
    """

    type: str
    sha: str
    url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        sha = self.sha
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "sha": sha,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        sha = d.pop("sha")

        url = d.pop("url")

        git_reference_object = cls(
            type=type,
            sha=sha,
            url=url,
        )

        git_reference_object.additional_properties = d
        return git_reference_object

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
