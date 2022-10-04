from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgsconvertMemberToOutsideCollaboratorJsonBody")


@attr.s(auto_attribs=True)
class OrgsconvertMemberToOutsideCollaboratorJsonBody:
    """
    Attributes:
        async_ (Union[Unset, bool]): When set to `true`, the request will be performed asynchronously. Returns a 202
            status code when the job is successfully queued.
    """

    async_: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        async_ = self.async_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if async_ is not UNSET:
            field_dict["async"] = async_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        async_ = d.pop("async", UNSET)

        orgsconvert_member_to_outside_collaborator_json_body = cls(
            async_=async_,
        )

        orgsconvert_member_to_outside_collaborator_json_body.additional_properties = d
        return orgsconvert_member_to_outside_collaborator_json_body

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
