from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.projectsmove_card_response_503_errors_item import ProjectsmoveCardResponse503ErrorsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectsmoveCardResponse503")


@attr.s(auto_attribs=True)
class ProjectsmoveCardResponse503:
    """
    Attributes:
        code (Union[Unset, str]):
        message (Union[Unset, str]):
        documentation_url (Union[Unset, str]):
        errors (Union[Unset, List[ProjectsmoveCardResponse503ErrorsItem]]):
    """

    code: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    documentation_url: Union[Unset, str] = UNSET
    errors: Union[Unset, List[ProjectsmoveCardResponse503ErrorsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        message = self.message
        documentation_url = self.documentation_url
        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ProjectsmoveCardResponse503ErrorsItem.from_dict(errors_item_data)

            errors.append(errors_item)

        projectsmove_card_response_503 = cls(
            code=code,
            message=message,
            documentation_url=documentation_url,
            errors=errors,
        )

        projectsmove_card_response_503.additional_properties = d
        return projectsmove_card_response_503

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
