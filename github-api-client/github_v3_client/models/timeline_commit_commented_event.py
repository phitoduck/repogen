from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.commit_comment import CommitComment
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimelineCommitCommentedEvent")


@attr.s(auto_attribs=True)
class TimelineCommitCommentedEvent:
    """Timeline Commit Commented Event

    Attributes:
        event (Union[Unset, str]):
        node_id (Union[Unset, str]):
        commit_id (Union[Unset, str]):
        comments (Union[Unset, List[CommitComment]]):
    """

    event: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    commit_id: Union[Unset, str] = UNSET
    comments: Union[Unset, List[CommitComment]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event = self.event
        node_id = self.node_id
        commit_id = self.commit_id
        comments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()

                comments.append(comments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if commit_id is not UNSET:
            field_dict["commit_id"] = commit_id
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event = d.pop("event", UNSET)

        node_id = d.pop("node_id", UNSET)

        commit_id = d.pop("commit_id", UNSET)

        comments = []
        _comments = d.pop("comments", UNSET)
        for comments_item_data in _comments or []:
            comments_item = CommitComment.from_dict(comments_item_data)

            comments.append(comments_item)

        timeline_commit_commented_event = cls(
            event=event,
            node_id=node_id,
            commit_id=commit_id,
            comments=comments,
        )

        timeline_commit_commented_event.additional_properties = d
        return timeline_commit_commented_event

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
