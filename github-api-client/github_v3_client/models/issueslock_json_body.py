from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.issueslock_json_body_lock_reason import IssueslockJsonBodyLockReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueslockJsonBody")


@attr.s(auto_attribs=True)
class IssueslockJsonBody:
    """
    Attributes:
        lock_reason (Union[Unset, IssueslockJsonBodyLockReason]): The reason for locking the issue or pull request
            conversation. Lock will fail if you don't use one of these reasons:
            \* `off-topic`
            \* `too heated`
            \* `resolved`
            \* `spam`
    """

    lock_reason: Union[Unset, IssueslockJsonBodyLockReason] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lock_reason: Union[Unset, str] = UNSET
        if not isinstance(self.lock_reason, Unset):
            lock_reason = self.lock_reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lock_reason is not UNSET:
            field_dict["lock_reason"] = lock_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _lock_reason = d.pop("lock_reason", UNSET)
        lock_reason: Union[Unset, IssueslockJsonBodyLockReason]
        if isinstance(_lock_reason, Unset):
            lock_reason = UNSET
        else:
            lock_reason = IssueslockJsonBodyLockReason(_lock_reason)

        issueslock_json_body = cls(
            lock_reason=lock_reason,
        )

        issueslock_json_body.additional_properties = d
        return issueslock_json_body

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
