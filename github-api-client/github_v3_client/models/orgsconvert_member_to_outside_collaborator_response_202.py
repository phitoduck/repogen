from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="OrgsconvertMemberToOutsideCollaboratorResponse202")


@attr.s(auto_attribs=True)
class OrgsconvertMemberToOutsideCollaboratorResponse202:
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        orgsconvert_member_to_outside_collaborator_response_202 = cls()

        return orgsconvert_member_to_outside_collaborator_response_202
