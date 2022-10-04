from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="AdvancedSecurityActiveCommittersUser")


@attr.s(auto_attribs=True)
class AdvancedSecurityActiveCommittersUser:
    """
    Attributes:
        user_login (str):
        last_pushed_date (str):  Example: 2021-11-03.
    """

    user_login: str
    last_pushed_date: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_login = self.user_login
        last_pushed_date = self.last_pushed_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_login": user_login,
                "last_pushed_date": last_pushed_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_login = d.pop("user_login")

        last_pushed_date = d.pop("last_pushed_date")

        advanced_security_active_committers_user = cls(
            user_login=user_login,
            last_pushed_date=last_pushed_date,
        )

        advanced_security_active_committers_user.additional_properties = d
        return advanced_security_active_committers_user

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
