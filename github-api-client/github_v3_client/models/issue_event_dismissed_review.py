from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueEventDismissedReview")


@attr.s(auto_attribs=True)
class IssueEventDismissedReview:
    """
    Attributes:
        state (str):
        review_id (int):
        dismissal_message (Optional[str]):
        dismissal_commit_id (Union[Unset, None, str]):
    """

    state: str
    review_id: int
    dismissal_message: Optional[str]
    dismissal_commit_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state
        review_id = self.review_id
        dismissal_message = self.dismissal_message
        dismissal_commit_id = self.dismissal_commit_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "review_id": review_id,
                "dismissal_message": dismissal_message,
            }
        )
        if dismissal_commit_id is not UNSET:
            field_dict["dismissal_commit_id"] = dismissal_commit_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state = d.pop("state")

        review_id = d.pop("review_id")

        dismissal_message = d.pop("dismissal_message")

        dismissal_commit_id = d.pop("dismissal_commit_id", UNSET)

        issue_event_dismissed_review = cls(
            state=state,
            review_id=review_id,
            dismissal_message=dismissal_message,
            dismissal_commit_id=dismissal_commit_id,
        )

        issue_event_dismissed_review.additional_properties = d
        return issue_event_dismissed_review

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
