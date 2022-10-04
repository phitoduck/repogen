from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileCommitCommitParentsItem")


@attr.s(auto_attribs=True)
class FileCommitCommitParentsItem:
    """
    Attributes:
        url (Union[Unset, str]):
        html_url (Union[Unset, str]):
        sha (Union[Unset, str]):
    """

    url: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    sha: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        html_url = self.html_url
        sha = self.sha

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if sha is not UNSET:
            field_dict["sha"] = sha

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        html_url = d.pop("html_url", UNSET)

        sha = d.pop("sha", UNSET)

        file_commit_commit_parents_item = cls(
            url=url,
            html_url=html_url,
            sha=sha,
        )

        file_commit_commit_parents_item.additional_properties = d
        return file_commit_commit_parents_item

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
