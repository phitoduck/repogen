from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="Verification")


@attr.s(auto_attribs=True)
class Verification:
    """
    Attributes:
        verified (bool):
        reason (str):
        payload (Optional[str]):
        signature (Optional[str]):
    """

    verified: bool
    reason: str
    payload: Optional[str]
    signature: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        verified = self.verified
        reason = self.reason
        payload = self.payload
        signature = self.signature

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "verified": verified,
                "reason": reason,
                "payload": payload,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        verified = d.pop("verified")

        reason = d.pop("reason")

        payload = d.pop("payload")

        signature = d.pop("signature")

        verification = cls(
            verified=verified,
            reason=reason,
            payload=payload,
            signature=signature,
        )

        verification.additional_properties = d
        return verification

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
