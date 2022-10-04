from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserscreatePublicSshKeyForAuthenticatedUserJsonBody")


@attr.s(auto_attribs=True)
class UserscreatePublicSshKeyForAuthenticatedUserJsonBody:
    """
    Attributes:
        key (str): The public SSH key to add to your GitHub account.
        title (Union[Unset, str]): A descriptive name for the new key. Example: Personal MacBook Air.
    """

    key: str
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        title = d.pop("title", UNSET)

        userscreate_public_ssh_key_for_authenticated_user_json_body = cls(
            key=key,
            title=title,
        )

        userscreate_public_ssh_key_for_authenticated_user_json_body.additional_properties = d
        return userscreate_public_ssh_key_for_authenticated_user_json_body

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
