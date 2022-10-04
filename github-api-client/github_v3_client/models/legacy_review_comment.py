import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.author_association import AuthorAssociation
from ..models.legacy_review_comment_links import LegacyReviewCommentLinks
from ..models.legacy_review_comment_side import LegacyReviewCommentSide
from ..models.legacy_review_comment_start_side import LegacyReviewCommentStartSide
from ..models.reaction_rollup import ReactionRollup
from ..models.simple_user import SimpleUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="LegacyReviewComment")


@attr.s(auto_attribs=True)
class LegacyReviewComment:
    """Legacy Review Comment

    Attributes:
        url (str):  Example: https://api.github.com/repos/octocat/Hello-World/pulls/comments/1.
        id (int):  Example: 10.
        node_id (str):  Example: MDI0OlB1bGxSZXF1ZXN0UmV2aWV3Q29tbWVudDEw.
        diff_hunk (str):  Example: @@ -16,33 +16,40 @@ public class Connection : IConnection....
        path (str):  Example: file1.txt.
        original_position (int):  Example: 4.
        commit_id (str):  Example: 6dcb09b5b57875f334f61aebed695e2e4193db5e.
        original_commit_id (str):  Example: 9c48853fa3dc5c1c3d6f1f1cd1f2743e72652840.
        body (str):  Example: Great stuff.
        created_at (datetime.datetime):  Example: 2011-04-14T16:00:49Z.
        updated_at (datetime.datetime):  Example: 2011-04-14T16:00:49Z.
        html_url (str):  Example: https://github.com/octocat/Hello-World/pull/1#discussion-diff-1.
        pull_request_url (str):  Example: https://api.github.com/repos/octocat/Hello-World/pulls/1.
        author_association (AuthorAssociation): How the author is associated with the repository. Example: OWNER.
        links (LegacyReviewCommentLinks):
        pull_request_review_id (Optional[int]):  Example: 42.
        position (Optional[int]):  Example: 1.
        in_reply_to_id (Union[Unset, int]):  Example: 8.
        user (Optional[SimpleUser]): Simple User
        body_text (Union[Unset, str]):
        body_html (Union[Unset, str]):
        reactions (Union[Unset, ReactionRollup]):
        side (Union[Unset, LegacyReviewCommentSide]): The side of the first line of the range for a multi-line comment.
            Default: LegacyReviewCommentSide.RIGHT.
        start_side (Union[Unset, None, LegacyReviewCommentStartSide]): The side of the first line of the range for a
            multi-line comment. Default: LegacyReviewCommentStartSide.RIGHT.
        line (Union[Unset, int]): The line of the blob to which the comment applies. The last line of the range for a
            multi-line comment Example: 2.
        original_line (Union[Unset, int]): The original line of the blob to which the comment applies. The last line of
            the range for a multi-line comment Example: 2.
        start_line (Union[Unset, None, int]): The first line of the range for a multi-line comment. Example: 2.
        original_start_line (Union[Unset, None, int]): The original first line of the range for a multi-line comment.
            Example: 2.
    """

    url: str
    id: int
    node_id: str
    diff_hunk: str
    path: str
    original_position: int
    commit_id: str
    original_commit_id: str
    body: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    html_url: str
    pull_request_url: str
    author_association: AuthorAssociation
    links: LegacyReviewCommentLinks
    pull_request_review_id: Optional[int]
    position: Optional[int]
    user: Optional[SimpleUser]
    in_reply_to_id: Union[Unset, int] = UNSET
    body_text: Union[Unset, str] = UNSET
    body_html: Union[Unset, str] = UNSET
    reactions: Union[Unset, ReactionRollup] = UNSET
    side: Union[Unset, LegacyReviewCommentSide] = LegacyReviewCommentSide.RIGHT
    start_side: Union[Unset, None, LegacyReviewCommentStartSide] = LegacyReviewCommentStartSide.RIGHT
    line: Union[Unset, int] = UNSET
    original_line: Union[Unset, int] = UNSET
    start_line: Union[Unset, None, int] = UNSET
    original_start_line: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        node_id = self.node_id
        diff_hunk = self.diff_hunk
        path = self.path
        original_position = self.original_position
        commit_id = self.commit_id
        original_commit_id = self.original_commit_id
        body = self.body
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        html_url = self.html_url
        pull_request_url = self.pull_request_url
        author_association = self.author_association.value

        links = self.links.to_dict()

        pull_request_review_id = self.pull_request_review_id
        position = self.position
        in_reply_to_id = self.in_reply_to_id
        user = self.user.to_dict() if self.user else None

        body_text = self.body_text
        body_html = self.body_html
        reactions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reactions, Unset):
            reactions = self.reactions.to_dict()

        side: Union[Unset, str] = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        start_side: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_side, Unset):
            start_side = self.start_side.value if self.start_side else None

        line = self.line
        original_line = self.original_line
        start_line = self.start_line
        original_start_line = self.original_start_line

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "node_id": node_id,
                "diff_hunk": diff_hunk,
                "path": path,
                "original_position": original_position,
                "commit_id": commit_id,
                "original_commit_id": original_commit_id,
                "body": body,
                "created_at": created_at,
                "updated_at": updated_at,
                "html_url": html_url,
                "pull_request_url": pull_request_url,
                "author_association": author_association,
                "_links": links,
                "pull_request_review_id": pull_request_review_id,
                "position": position,
                "user": user,
            }
        )
        if in_reply_to_id is not UNSET:
            field_dict["in_reply_to_id"] = in_reply_to_id
        if body_text is not UNSET:
            field_dict["body_text"] = body_text
        if body_html is not UNSET:
            field_dict["body_html"] = body_html
        if reactions is not UNSET:
            field_dict["reactions"] = reactions
        if side is not UNSET:
            field_dict["side"] = side
        if start_side is not UNSET:
            field_dict["start_side"] = start_side
        if line is not UNSET:
            field_dict["line"] = line
        if original_line is not UNSET:
            field_dict["original_line"] = original_line
        if start_line is not UNSET:
            field_dict["start_line"] = start_line
        if original_start_line is not UNSET:
            field_dict["original_start_line"] = original_start_line

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        node_id = d.pop("node_id")

        diff_hunk = d.pop("diff_hunk")

        path = d.pop("path")

        original_position = d.pop("original_position")

        commit_id = d.pop("commit_id")

        original_commit_id = d.pop("original_commit_id")

        body = d.pop("body")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        html_url = d.pop("html_url")

        pull_request_url = d.pop("pull_request_url")

        author_association = AuthorAssociation(d.pop("author_association"))

        links = LegacyReviewCommentLinks.from_dict(d.pop("_links"))

        pull_request_review_id = d.pop("pull_request_review_id")

        position = d.pop("position")

        in_reply_to_id = d.pop("in_reply_to_id", UNSET)

        _user = d.pop("user")
        user: Optional[SimpleUser]
        if _user is None:
            user = None
        else:
            user = SimpleUser.from_dict(_user)

        body_text = d.pop("body_text", UNSET)

        body_html = d.pop("body_html", UNSET)

        _reactions = d.pop("reactions", UNSET)
        reactions: Union[Unset, ReactionRollup]
        if isinstance(_reactions, Unset):
            reactions = UNSET
        else:
            reactions = ReactionRollup.from_dict(_reactions)

        _side = d.pop("side", UNSET)
        side: Union[Unset, LegacyReviewCommentSide]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = LegacyReviewCommentSide(_side)

        _start_side = d.pop("start_side", UNSET)
        start_side: Union[Unset, None, LegacyReviewCommentStartSide]
        if _start_side is None:
            start_side = None
        elif isinstance(_start_side, Unset):
            start_side = UNSET
        else:
            start_side = LegacyReviewCommentStartSide(_start_side)

        line = d.pop("line", UNSET)

        original_line = d.pop("original_line", UNSET)

        start_line = d.pop("start_line", UNSET)

        original_start_line = d.pop("original_start_line", UNSET)

        legacy_review_comment = cls(
            url=url,
            id=id,
            node_id=node_id,
            diff_hunk=diff_hunk,
            path=path,
            original_position=original_position,
            commit_id=commit_id,
            original_commit_id=original_commit_id,
            body=body,
            created_at=created_at,
            updated_at=updated_at,
            html_url=html_url,
            pull_request_url=pull_request_url,
            author_association=author_association,
            links=links,
            pull_request_review_id=pull_request_review_id,
            position=position,
            in_reply_to_id=in_reply_to_id,
            user=user,
            body_text=body_text,
            body_html=body_html,
            reactions=reactions,
            side=side,
            start_side=start_side,
            line=line,
            original_line=original_line,
            start_line=start_line,
            original_start_line=original_start_line,
        )

        legacy_review_comment.additional_properties = d
        return legacy_review_comment

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
