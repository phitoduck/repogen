from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pullssubmit_review_json_body_event import PullssubmitReviewJsonBodyEvent
from ..types import UNSET, Unset

T = TypeVar("T", bound="PullssubmitReviewJsonBody")


@attr.s(auto_attribs=True)
class PullssubmitReviewJsonBody:
    """
    Attributes:
        event (PullssubmitReviewJsonBodyEvent): The review action you want to perform. The review actions include:
            `APPROVE`, `REQUEST_CHANGES`, or `COMMENT`. When you leave this blank, the API returns _HTTP 422 (Unrecognizable
            entity)_ and sets the review action state to `PENDING`, which means you will need to re-submit the pull request
            review using a review action.
        body (Union[Unset, str]): The body text of the pull request review
    """

    event: PullssubmitReviewJsonBodyEvent
    body: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event = self.event.value

        body = self.body

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event = PullssubmitReviewJsonBodyEvent(d.pop("event"))

        body = d.pop("body", UNSET)

        pullssubmit_review_json_body = cls(
            event=event,
            body=body,
        )

        pullssubmit_review_json_body.additional_properties = d
        return pullssubmit_review_json_body

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
