from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivitysetThreadSubscriptionJsonBody")


@attr.s(auto_attribs=True)
class ActivitysetThreadSubscriptionJsonBody:
    """
    Attributes:
        ignored (Union[Unset, bool]): Whether to block all notifications from a thread.
    """

    ignored: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ignored = self.ignored

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ignored is not UNSET:
            field_dict["ignored"] = ignored

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ignored = d.pop("ignored", UNSET)

        activityset_thread_subscription_json_body = cls(
            ignored=ignored,
        )

        activityset_thread_subscription_json_body.additional_properties = d
        return activityset_thread_subscription_json_body

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
