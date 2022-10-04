from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.reactionscreate_for_commit_comment_json_body_content import ReactionscreateForCommitCommentJsonBodyContent

T = TypeVar("T", bound="ReactionscreateForCommitCommentJsonBody")


@attr.s(auto_attribs=True)
class ReactionscreateForCommitCommentJsonBody:
    """
    Attributes:
        content (ReactionscreateForCommitCommentJsonBodyContent): The [reaction
            type](https://docs.github.com/rest/reference/reactions#reaction-types) to add to the commit comment.
    """

    content: ReactionscreateForCommitCommentJsonBodyContent
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = ReactionscreateForCommitCommentJsonBodyContent(d.pop("content"))

        reactionscreate_for_commit_comment_json_body = cls(
            content=content,
        )

        reactionscreate_for_commit_comment_json_body.additional_properties = d
        return reactionscreate_for_commit_comment_json_body

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
