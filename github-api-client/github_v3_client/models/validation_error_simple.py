from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationErrorSimple")


@attr.s(auto_attribs=True)
class ValidationErrorSimple:
    """Validation Error Simple

    Attributes:
        message (str):
        documentation_url (str):
        errors (Union[Unset, List[str]]):
    """

    message: str
    documentation_url: str
    errors: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        documentation_url = self.documentation_url
        errors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "documentation_url": documentation_url,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message")

        documentation_url = d.pop("documentation_url")

        errors = cast(List[str], d.pop("errors", UNSET))

        validation_error_simple = cls(
            message=message,
            documentation_url=documentation_url,
            errors=errors,
        )

        validation_error_simple.additional_properties = d
        return validation_error_simple

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
