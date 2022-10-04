from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectsdeleteResponse403")


@attr.s(auto_attribs=True)
class ProjectsdeleteResponse403:
    """
    Attributes:
        message (Union[Unset, str]):
        documentation_url (Union[Unset, str]):
        errors (Union[Unset, List[str]]):
    """

    message: Union[Unset, str] = UNSET
    documentation_url: Union[Unset, str] = UNSET
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
        field_dict.update({})
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
        message = d.pop("message", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        errors = cast(List[str], d.pop("errors", UNSET))

        projectsdelete_response_403 = cls(
            message=message,
            documentation_url=documentation_url,
            errors=errors,
        )

        projectsdelete_response_403.additional_properties = d
        return projectsdelete_response_403

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
