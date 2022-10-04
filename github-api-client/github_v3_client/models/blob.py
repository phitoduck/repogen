from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Blob")


@attr.s(auto_attribs=True)
class Blob:
    """Blob

    Attributes:
        content (str):
        encoding (str):
        url (str):
        sha (str):
        node_id (str):
        size (Optional[int]):
        highlighted_content (Union[Unset, str]):
    """

    content: str
    encoding: str
    url: str
    sha: str
    node_id: str
    size: Optional[int]
    highlighted_content: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content
        encoding = self.encoding
        url = self.url
        sha = self.sha
        node_id = self.node_id
        size = self.size
        highlighted_content = self.highlighted_content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "encoding": encoding,
                "url": url,
                "sha": sha,
                "node_id": node_id,
                "size": size,
            }
        )
        if highlighted_content is not UNSET:
            field_dict["highlighted_content"] = highlighted_content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content")

        encoding = d.pop("encoding")

        url = d.pop("url")

        sha = d.pop("sha")

        node_id = d.pop("node_id")

        size = d.pop("size")

        highlighted_content = d.pop("highlighted_content", UNSET)

        blob = cls(
            content=content,
            encoding=encoding,
            url=url,
            sha=sha,
            node_id=node_id,
            size=size,
            highlighted_content=highlighted_content,
        )

        blob.additional_properties = d
        return blob

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
