from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="Email")


@attr.s(auto_attribs=True)
class Email:
    """Email

    Attributes:
        email (str):  Example: octocat@github.com.
        primary (bool):  Example: True.
        verified (bool):  Example: True.
        visibility (Optional[str]):  Example: public.
    """

    email: str
    primary: bool
    verified: bool
    visibility: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        primary = self.primary
        verified = self.verified
        visibility = self.visibility

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "primary": primary,
                "verified": verified,
                "visibility": visibility,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        primary = d.pop("primary")

        verified = d.pop("verified")

        visibility = d.pop("visibility")

        email = cls(
            email=email,
            primary=primary,
            verified=verified,
            visibility=visibility,
        )

        email.additional_properties = d
        return email

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
