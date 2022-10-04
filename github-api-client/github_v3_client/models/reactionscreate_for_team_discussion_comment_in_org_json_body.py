from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.reactionscreate_for_team_discussion_comment_in_org_json_body_content import (
    ReactionscreateForTeamDiscussionCommentInOrgJsonBodyContent,
)

T = TypeVar("T", bound="ReactionscreateForTeamDiscussionCommentInOrgJsonBody")


@attr.s(auto_attribs=True)
class ReactionscreateForTeamDiscussionCommentInOrgJsonBody:
    """
    Attributes:
        content (ReactionscreateForTeamDiscussionCommentInOrgJsonBodyContent): The [reaction
            type](https://docs.github.com/rest/reference/reactions#reaction-types) to add to the team discussion comment.
    """

    content: ReactionscreateForTeamDiscussionCommentInOrgJsonBodyContent
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
        content = ReactionscreateForTeamDiscussionCommentInOrgJsonBodyContent(d.pop("content"))

        reactionscreate_for_team_discussion_comment_in_org_json_body = cls(
            content=content,
        )

        reactionscreate_for_team_discussion_comment_in_org_json_body.additional_properties = d
        return reactionscreate_for_team_discussion_comment_in_org_json_body

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
