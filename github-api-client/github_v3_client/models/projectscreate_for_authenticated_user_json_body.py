from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectscreateForAuthenticatedUserJsonBody")


@attr.s(auto_attribs=True)
class ProjectscreateForAuthenticatedUserJsonBody:
    """
    Attributes:
        name (str): Name of the project Example: Week One Sprint.
        body (Union[Unset, None, str]): Body of the project Example: This project represents the sprint of the first
            week in January.
    """

    name: str
    body: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        body = self.body

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        body = d.pop("body", UNSET)

        projectscreate_for_authenticated_user_json_body = cls(
            name=name,
            body=body,
        )

        projectscreate_for_authenticated_user_json_body.additional_properties = d
        return projectscreate_for_authenticated_user_json_body

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
