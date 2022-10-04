from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationErrorErrorsItem")


@attr.s(auto_attribs=True)
class ValidationErrorErrorsItem:
    """
    Attributes:
        code (str):
        resource (Union[Unset, str]):
        field (Union[Unset, str]):
        message (Union[Unset, str]):
        index (Union[Unset, int]):
        value (Union[List[str], Unset, int, str]):
    """

    code: str
    resource: Union[Unset, str] = UNSET
    field: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    index: Union[Unset, int] = UNSET
    value: Union[List[str], Unset, int, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        resource = self.resource
        field = self.field
        message = self.message
        index = self.index
        value: Union[List[str], Unset, int, str]
        if isinstance(self.value, Unset):
            value = UNSET

        elif isinstance(self.value, list):
            value = UNSET
            if not isinstance(self.value, Unset):
                if self.value is None:
                    value = None
                else:
                    value = self.value

        else:
            value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if resource is not UNSET:
            field_dict["resource"] = resource
        if field is not UNSET:
            field_dict["field"] = field
        if message is not UNSET:
            field_dict["message"] = message
        if index is not UNSET:
            field_dict["index"] = index
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        resource = d.pop("resource", UNSET)

        field = d.pop("field", UNSET)

        message = d.pop("message", UNSET)

        index = d.pop("index", UNSET)

        def _parse_value(data: object) -> Union[List[str], Unset, int, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_2 = cast(List[str], data)

                return value_type_2
            except:  # noqa: E722
                pass
            return cast(Union[List[str], Unset, int, str], data)

        value = _parse_value(d.pop("value", UNSET))

        validation_error_errors_item = cls(
            code=code,
            resource=resource,
            field=field,
            message=message,
            index=index,
            value=value,
        )

        validation_error_errors_item.additional_properties = d
        return validation_error_errors_item

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
