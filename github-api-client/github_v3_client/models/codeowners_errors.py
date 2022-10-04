from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.codeowners_errors_errors_item import CODEOWNERSErrorsErrorsItem

T = TypeVar("T", bound="CODEOWNERSErrors")


@attr.s(auto_attribs=True)
class CODEOWNERSErrors:
    """A list of errors found in a repo's CODEOWNERS file

    Attributes:
        errors (List[CODEOWNERSErrorsErrorsItem]):
    """

    errors: List[CODEOWNERSErrorsErrorsItem]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = CODEOWNERSErrorsErrorsItem.from_dict(errors_item_data)

            errors.append(errors_item)

        codeowners_errors = cls(
            errors=errors,
        )

        codeowners_errors.additional_properties = d
        return codeowners_errors

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
