from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitcreateBlobJsonBody")


@attr.s(auto_attribs=True)
class GitcreateBlobJsonBody:
    """
    Attributes:
        content (str): The new blob's content.
        encoding (Union[Unset, str]): The encoding used for `content`. Currently, `"utf-8"` and `"base64"` are
            supported. Default: 'utf-8'.
    """

    content: str
    encoding: Union[Unset, str] = "utf-8"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content
        encoding = self.encoding

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if encoding is not UNSET:
            field_dict["encoding"] = encoding

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content")

        encoding = d.pop("encoding", UNSET)

        gitcreate_blob_json_body = cls(
            content=content,
            encoding=encoding,
        )

        gitcreate_blob_json_body.additional_properties = d
        return gitcreate_blob_json_body

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
