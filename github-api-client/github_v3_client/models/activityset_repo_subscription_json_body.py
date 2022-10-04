from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivitysetRepoSubscriptionJsonBody")


@attr.s(auto_attribs=True)
class ActivitysetRepoSubscriptionJsonBody:
    """
    Attributes:
        subscribed (Union[Unset, bool]): Determines if notifications should be received from this repository.
        ignored (Union[Unset, bool]): Determines if all notifications should be blocked from this repository.
    """

    subscribed: Union[Unset, bool] = UNSET
    ignored: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subscribed = self.subscribed
        ignored = self.ignored

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscribed is not UNSET:
            field_dict["subscribed"] = subscribed
        if ignored is not UNSET:
            field_dict["ignored"] = ignored

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subscribed = d.pop("subscribed", UNSET)

        ignored = d.pop("ignored", UNSET)

        activityset_repo_subscription_json_body = cls(
            subscribed=subscribed,
            ignored=ignored,
        )

        activityset_repo_subscription_json_body.additional_properties = d
        return activityset_repo_subscription_json_body

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
