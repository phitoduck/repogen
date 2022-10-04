from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserscreateGpgKeyForAuthenticatedUserJsonBody")


@attr.s(auto_attribs=True)
class UserscreateGpgKeyForAuthenticatedUserJsonBody:
    """
    Attributes:
        armored_public_key (str): A GPG key in ASCII-armored format.
        name (Union[Unset, str]): A descriptive name for the new key.
    """

    armored_public_key: str
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        armored_public_key = self.armored_public_key
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "armored_public_key": armored_public_key,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        armored_public_key = d.pop("armored_public_key")

        name = d.pop("name", UNSET)

        userscreate_gpg_key_for_authenticated_user_json_body = cls(
            armored_public_key=armored_public_key,
            name=name,
        )

        userscreate_gpg_key_for_authenticated_user_json_body.additional_properties = d
        return userscreate_gpg_key_for_authenticated_user_json_body

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
