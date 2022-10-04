from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BasicError")


@attr.s(auto_attribs=True)
class BasicError:
    """Basic Error

    Attributes:
        message (Union[Unset, str]):
        documentation_url (Union[Unset, str]):
        url (Union[Unset, str]):
        status (Union[Unset, str]):
    """

    message: Union[Unset, str] = UNSET
    documentation_url: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        documentation_url = self.documentation_url
        url = self.url
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if url is not UNSET:
            field_dict["url"] = url
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        url = d.pop("url", UNSET)

        status = d.pop("status", UNSET)

        basic_error = cls(
            message=message,
            documentation_url=documentation_url,
            url=url,
            status=status,
        )

        basic_error.additional_properties = d
        return basic_error

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
