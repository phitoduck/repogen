from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pullsdismiss_review_json_body_event import PullsdismissReviewJsonBodyEvent
from ..types import UNSET, Unset

T = TypeVar("T", bound="PullsdismissReviewJsonBody")


@attr.s(auto_attribs=True)
class PullsdismissReviewJsonBody:
    """
    Attributes:
        message (str): The message for the pull request review dismissal
        event (Union[Unset, PullsdismissReviewJsonBodyEvent]):  Example: "DISMISS".
    """

    message: str
    event: Union[Unset, PullsdismissReviewJsonBodyEvent] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        event: Union[Unset, str] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message")

        _event = d.pop("event", UNSET)
        event: Union[Unset, PullsdismissReviewJsonBodyEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = PullsdismissReviewJsonBodyEvent(_event)

        pullsdismiss_review_json_body = cls(
            message=message,
            event=event,
        )

        pullsdismiss_review_json_body.additional_properties = d
        return pullsdismiss_review_json_body

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
