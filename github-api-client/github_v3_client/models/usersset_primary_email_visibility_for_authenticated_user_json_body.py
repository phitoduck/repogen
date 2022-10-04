from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.usersset_primary_email_visibility_for_authenticated_user_json_body_visibility import (
    UserssetPrimaryEmailVisibilityForAuthenticatedUserJsonBodyVisibility,
)

T = TypeVar("T", bound="UserssetPrimaryEmailVisibilityForAuthenticatedUserJsonBody")


@attr.s(auto_attribs=True)
class UserssetPrimaryEmailVisibilityForAuthenticatedUserJsonBody:
    """
    Attributes:
        visibility (UserssetPrimaryEmailVisibilityForAuthenticatedUserJsonBodyVisibility): Denotes whether an email is
            publicly visible.
    """

    visibility: UserssetPrimaryEmailVisibilityForAuthenticatedUserJsonBodyVisibility
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        visibility = self.visibility.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "visibility": visibility,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        visibility = UserssetPrimaryEmailVisibilityForAuthenticatedUserJsonBodyVisibility(d.pop("visibility"))

        usersset_primary_email_visibility_for_authenticated_user_json_body = cls(
            visibility=visibility,
        )

        usersset_primary_email_visibility_for_authenticated_user_json_body.additional_properties = d
        return usersset_primary_email_visibility_for_authenticated_user_json_body

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
