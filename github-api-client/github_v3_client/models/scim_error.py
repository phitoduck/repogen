from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScimError")


@attr.s(auto_attribs=True)
class ScimError:
    """Scim Error

    Attributes:
        message (Union[Unset, None, str]):
        documentation_url (Union[Unset, None, str]):
        detail (Union[Unset, None, str]):
        status (Union[Unset, int]):
        scim_type (Union[Unset, None, str]):
        schemas (Union[Unset, List[str]]):
    """

    message: Union[Unset, None, str] = UNSET
    documentation_url: Union[Unset, None, str] = UNSET
    detail: Union[Unset, None, str] = UNSET
    status: Union[Unset, int] = UNSET
    scim_type: Union[Unset, None, str] = UNSET
    schemas: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        documentation_url = self.documentation_url
        detail = self.detail
        status = self.status
        scim_type = self.scim_type
        schemas: Union[Unset, List[str]] = UNSET
        if not isinstance(self.schemas, Unset):
            schemas = self.schemas

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if detail is not UNSET:
            field_dict["detail"] = detail
        if status is not UNSET:
            field_dict["status"] = status
        if scim_type is not UNSET:
            field_dict["scimType"] = scim_type
        if schemas is not UNSET:
            field_dict["schemas"] = schemas

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        detail = d.pop("detail", UNSET)

        status = d.pop("status", UNSET)

        scim_type = d.pop("scimType", UNSET)

        schemas = cast(List[str], d.pop("schemas", UNSET))

        scim_error = cls(
            message=message,
            documentation_url=documentation_url,
            detail=detail,
            status=status,
            scim_type=scim_type,
            schemas=schemas,
        )

        scim_error.additional_properties = d
        return scim_error

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
