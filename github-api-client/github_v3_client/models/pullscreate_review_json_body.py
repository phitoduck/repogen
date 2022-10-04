from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pullscreate_review_json_body_comments_item import PullscreateReviewJsonBodyCommentsItem
from ..models.pullscreate_review_json_body_event import PullscreateReviewJsonBodyEvent
from ..types import UNSET, Unset

T = TypeVar("T", bound="PullscreateReviewJsonBody")


@attr.s(auto_attribs=True)
class PullscreateReviewJsonBody:
    """
    Attributes:
        commit_id (Union[Unset, str]): The SHA of the commit that needs a review. Not using the latest commit SHA may
            render your review comment outdated if a subsequent commit modifies the line you specify as the `position`.
            Defaults to the most recent commit in the pull request when you do not specify a value.
        body (Union[Unset, str]): **Required** when using `REQUEST_CHANGES` or `COMMENT` for the `event` parameter. The
            body text of the pull request review.
        event (Union[Unset, PullscreateReviewJsonBodyEvent]): The review action you want to perform. The review actions
            include: `APPROVE`, `REQUEST_CHANGES`, or `COMMENT`. By leaving this blank, you set the review action state to
            `PENDING`, which means you will need to [submit the pull request
            review](https://docs.github.com/rest/pulls#submit-a-review-for-a-pull-request) when you are ready.
        comments (Union[Unset, List[PullscreateReviewJsonBodyCommentsItem]]): Use the following table to specify the
            location, destination, and contents of the draft review comment.
    """

    commit_id: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    event: Union[Unset, PullscreateReviewJsonBodyEvent] = UNSET
    comments: Union[Unset, List[PullscreateReviewJsonBodyCommentsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commit_id = self.commit_id
        body = self.body
        event: Union[Unset, str] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.value

        comments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()

                comments.append(comments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit_id is not UNSET:
            field_dict["commit_id"] = commit_id
        if body is not UNSET:
            field_dict["body"] = body
        if event is not UNSET:
            field_dict["event"] = event
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        commit_id = d.pop("commit_id", UNSET)

        body = d.pop("body", UNSET)

        _event = d.pop("event", UNSET)
        event: Union[Unset, PullscreateReviewJsonBodyEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = PullscreateReviewJsonBodyEvent(_event)

        comments = []
        _comments = d.pop("comments", UNSET)
        for comments_item_data in _comments or []:
            comments_item = PullscreateReviewJsonBodyCommentsItem.from_dict(comments_item_data)

            comments.append(comments_item)

        pullscreate_review_json_body = cls(
            commit_id=commit_id,
            body=body,
            event=event,
            comments=comments,
        )

        pullscreate_review_json_body.additional_properties = d
        return pullscreate_review_json_body

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
