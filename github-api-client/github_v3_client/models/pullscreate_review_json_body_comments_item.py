from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PullscreateReviewJsonBodyCommentsItem")


@attr.s(auto_attribs=True)
class PullscreateReviewJsonBodyCommentsItem:
    """
    Attributes:
        path (str): The relative path to the file that necessitates a review comment.
        body (str): Text of the review comment.
        position (Union[Unset, int]): The position in the diff where you want to add a review comment. Note this value
            is not the same as the line number in the file. For help finding the position value, read the note below.
        line (Union[Unset, int]):  Example: 28.
        side (Union[Unset, str]):  Example: RIGHT.
        start_line (Union[Unset, int]):  Example: 26.
        start_side (Union[Unset, str]):  Example: LEFT.
    """

    path: str
    body: str
    position: Union[Unset, int] = UNSET
    line: Union[Unset, int] = UNSET
    side: Union[Unset, str] = UNSET
    start_line: Union[Unset, int] = UNSET
    start_side: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        body = self.body
        position = self.position
        line = self.line
        side = self.side
        start_line = self.start_line
        start_side = self.start_side

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "body": body,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position
        if line is not UNSET:
            field_dict["line"] = line
        if side is not UNSET:
            field_dict["side"] = side
        if start_line is not UNSET:
            field_dict["start_line"] = start_line
        if start_side is not UNSET:
            field_dict["start_side"] = start_side

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        body = d.pop("body")

        position = d.pop("position", UNSET)

        line = d.pop("line", UNSET)

        side = d.pop("side", UNSET)

        start_line = d.pop("start_line", UNSET)

        start_side = d.pop("start_side", UNSET)

        pullscreate_review_json_body_comments_item = cls(
            path=path,
            body=body,
            position=position,
            line=line,
            side=side,
            start_line=start_line,
            start_side=start_side,
        )

        pullscreate_review_json_body_comments_item.additional_properties = d
        return pullscreate_review_json_body_comments_item

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
