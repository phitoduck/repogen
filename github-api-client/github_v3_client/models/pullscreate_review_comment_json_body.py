from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pullscreate_review_comment_json_body_side import PullscreateReviewCommentJsonBodySide
from ..models.pullscreate_review_comment_json_body_start_side import PullscreateReviewCommentJsonBodyStartSide
from ..types import UNSET, Unset

T = TypeVar("T", bound="PullscreateReviewCommentJsonBody")


@attr.s(auto_attribs=True)
class PullscreateReviewCommentJsonBody:
    """
    Attributes:
        body (str): The text of the review comment.
        commit_id (str): The SHA of the commit needing a comment. Not using the latest commit SHA may render your
            comment outdated if a subsequent commit modifies the line you specify as the `position`.
        path (str): The relative path to the file that necessitates a comment.
        line (int): The line of the blob in the pull request diff that the comment applies to. For a multi-line comment,
            the last line of the range that your comment applies to.
        position (Union[Unset, int]): **This parameter is deprecated. Use `line` instead**. The position in the diff
            where you want to add a review comment. Note this value is not the same as the line number in the file. For help
            finding the position value, read the note above.
        side (Union[Unset, PullscreateReviewCommentJsonBodySide]): In a split diff view, the side of the diff that the
            pull request's changes appear on. Can be `LEFT` or `RIGHT`. Use `LEFT` for deletions that appear in red. Use
            `RIGHT` for additions that appear in green or unchanged lines that appear in white and are shown for context.
            For a multi-line comment, side represents whether the last line of the comment range is a deletion or addition.
            For more information, see "[Diff view options](https://docs.github.com/en/articles/about-comparing-branches-in-
            pull-requests#diff-view-options)" in the GitHub Help documentation.
        start_line (Union[Unset, int]): **Required when using multi-line comments unless using `in_reply_to`**. The
            `start_line` is the first line in the pull request diff that your multi-line comment applies to. To learn more
            about multi-line comments, see "[Commenting on a pull request](https://docs.github.com/en/articles/commenting-
            on-a-pull-request#adding-line-comments-to-a-pull-request)" in the GitHub Help documentation.
        start_side (Union[Unset, PullscreateReviewCommentJsonBodyStartSide]): **Required when using multi-line comments
            unless using `in_reply_to`**. The `start_side` is the starting side of the diff that the comment applies to. Can
            be `LEFT` or `RIGHT`. To learn more about multi-line comments, see "[Commenting on a pull
            request](https://docs.github.com/en/articles/commenting-on-a-pull-request#adding-line-comments-to-a-pull-
            request)" in the GitHub Help documentation. See `side` in this table for additional context.
        in_reply_to (Union[Unset, int]): The ID of the review comment to reply to. To find the ID of a review comment
            with ["List review comments on a pull request"](#list-review-comments-on-a-pull-request). When specified, all
            parameters other than `body` in the request body are ignored. Example: 2.
    """

    body: str
    commit_id: str
    path: str
    line: int
    position: Union[Unset, int] = UNSET
    side: Union[Unset, PullscreateReviewCommentJsonBodySide] = UNSET
    start_line: Union[Unset, int] = UNSET
    start_side: Union[Unset, PullscreateReviewCommentJsonBodyStartSide] = UNSET
    in_reply_to: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body
        commit_id = self.commit_id
        path = self.path
        line = self.line
        position = self.position
        side: Union[Unset, str] = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        start_line = self.start_line
        start_side: Union[Unset, str] = UNSET
        if not isinstance(self.start_side, Unset):
            start_side = self.start_side.value

        in_reply_to = self.in_reply_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "commit_id": commit_id,
                "path": path,
                "line": line,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position
        if side is not UNSET:
            field_dict["side"] = side
        if start_line is not UNSET:
            field_dict["start_line"] = start_line
        if start_side is not UNSET:
            field_dict["start_side"] = start_side
        if in_reply_to is not UNSET:
            field_dict["in_reply_to"] = in_reply_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        body = d.pop("body")

        commit_id = d.pop("commit_id")

        path = d.pop("path")

        line = d.pop("line")

        position = d.pop("position", UNSET)

        _side = d.pop("side", UNSET)
        side: Union[Unset, PullscreateReviewCommentJsonBodySide]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = PullscreateReviewCommentJsonBodySide(_side)

        start_line = d.pop("start_line", UNSET)

        _start_side = d.pop("start_side", UNSET)
        start_side: Union[Unset, PullscreateReviewCommentJsonBodyStartSide]
        if isinstance(_start_side, Unset):
            start_side = UNSET
        else:
            start_side = PullscreateReviewCommentJsonBodyStartSide(_start_side)

        in_reply_to = d.pop("in_reply_to", UNSET)

        pullscreate_review_comment_json_body = cls(
            body=body,
            commit_id=commit_id,
            path=path,
            line=line,
            position=position,
            side=side,
            start_line=start_line,
            start_side=start_side,
            in_reply_to=in_reply_to,
        )

        pullscreate_review_comment_json_body.additional_properties = d
        return pullscreate_review_comment_json_body

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
