from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileCommitCommitVerification")


@attr.s(auto_attribs=True)
class FileCommitCommitVerification:
    """
    Attributes:
        verified (Union[Unset, bool]):
        reason (Union[Unset, str]):
        signature (Union[Unset, None, str]):
        payload (Union[Unset, None, str]):
    """

    verified: Union[Unset, bool] = UNSET
    reason: Union[Unset, str] = UNSET
    signature: Union[Unset, None, str] = UNSET
    payload: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        verified = self.verified
        reason = self.reason
        signature = self.signature
        payload = self.payload

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if verified is not UNSET:
            field_dict["verified"] = verified
        if reason is not UNSET:
            field_dict["reason"] = reason
        if signature is not UNSET:
            field_dict["signature"] = signature
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        verified = d.pop("verified", UNSET)

        reason = d.pop("reason", UNSET)

        signature = d.pop("signature", UNSET)

        payload = d.pop("payload", UNSET)

        file_commit_commit_verification = cls(
            verified=verified,
            reason=reason,
            signature=signature,
            payload=payload,
        )

        file_commit_commit_verification.additional_properties = d
        return file_commit_commit_verification

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
