from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectsmoveCardResponse403ErrorsItem")


@attr.s(auto_attribs=True)
class ProjectsmoveCardResponse403ErrorsItem:
    """
    Attributes:
        code (Union[Unset, str]):
        message (Union[Unset, str]):
        resource (Union[Unset, str]):
        field (Union[Unset, str]):
    """

    code: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    resource: Union[Unset, str] = UNSET
    field: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        message = self.message
        resource = self.resource
        field = self.field

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if resource is not UNSET:
            field_dict["resource"] = resource
        if field is not UNSET:
            field_dict["field"] = field

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        resource = d.pop("resource", UNSET)

        field = d.pop("field", UNSET)

        projectsmove_card_response_403_errors_item = cls(
            code=code,
            message=message,
            resource=resource,
            field=field,
        )

        projectsmove_card_response_403_errors_item.additional_properties = d
        return projectsmove_card_response_403_errors_item

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
