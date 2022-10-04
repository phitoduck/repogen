from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.codespacesset_codespaces_billing_json_body_visibility import (
    CodespacessetCodespacesBillingJsonBodyVisibility,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodespacessetCodespacesBillingJsonBody")


@attr.s(auto_attribs=True)
class CodespacessetCodespacesBillingJsonBody:
    """
    Attributes:
        visibility (CodespacessetCodespacesBillingJsonBodyVisibility): Which users can access codespaces in the
            organization. `disabled` means that no users can access codespaces in the organization.
        selected_usernames (Union[Unset, List[str]]): The usernames of the organization members who should be granted
            access to codespaces in the organization. Required when `visibility` is `selected_members`.
    """

    visibility: CodespacessetCodespacesBillingJsonBodyVisibility
    selected_usernames: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        visibility = self.visibility.value

        selected_usernames: Union[Unset, List[str]] = UNSET
        if not isinstance(self.selected_usernames, Unset):
            selected_usernames = self.selected_usernames

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "visibility": visibility,
            }
        )
        if selected_usernames is not UNSET:
            field_dict["selected_usernames"] = selected_usernames

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        visibility = CodespacessetCodespacesBillingJsonBodyVisibility(d.pop("visibility"))

        selected_usernames = cast(List[str], d.pop("selected_usernames", UNSET))

        codespacesset_codespaces_billing_json_body = cls(
            visibility=visibility,
            selected_usernames=selected_usernames,
        )

        codespacesset_codespaces_billing_json_body.additional_properties = d
        return codespacesset_codespaces_billing_json_body

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
