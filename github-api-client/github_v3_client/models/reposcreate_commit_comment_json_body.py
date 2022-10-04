from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateCommitCommentJsonBody")


@attr.s(auto_attribs=True)
class ReposcreateCommitCommentJsonBody:
    """
    Attributes:
        body (str): The contents of the comment.
        path (Union[Unset, str]): Relative path of the file to comment on.
        position (Union[Unset, int]): Line index in the diff to comment on.
        line (Union[Unset, int]): **Deprecated**. Use **position** parameter instead. Line number in the file to comment
            on.
    """

    body: str
    path: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    line: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body
        path = self.path
        position = self.position
        line = self.line

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path
        if position is not UNSET:
            field_dict["position"] = position
        if line is not UNSET:
            field_dict["line"] = line

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        body = d.pop("body")

        path = d.pop("path", UNSET)

        position = d.pop("position", UNSET)

        line = d.pop("line", UNSET)

        reposcreate_commit_comment_json_body = cls(
            body=body,
            path=path,
            position=position,
            line=line,
        )

        reposcreate_commit_comment_json_body.additional_properties = d
        return reposcreate_commit_comment_json_body

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
