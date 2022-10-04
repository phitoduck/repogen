from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="InteractionsgetRestrictionsForOrgResponse200Type1")


@attr.s(auto_attribs=True)
class InteractionsgetRestrictionsForOrgResponse200Type1:
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        interactionsget_restrictions_for_org_response_200_type_1 = cls()

        return interactionsget_restrictions_for_org_response_200_type_1
