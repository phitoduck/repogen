from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.interaction_expiry import InteractionExpiry
from ..models.interaction_group import InteractionGroup
from ..types import UNSET, Unset

T = TypeVar("T", bound="InteractionRestrictions")


@attr.s(auto_attribs=True)
class InteractionRestrictions:
    """Limit interactions to a specific type of user for a specified duration

    Attributes:
        limit (InteractionGroup): The type of GitHub user that can comment, open issues, or create pull requests while
            the interaction limit is in effect. Example: collaborators_only.
        expiry (Union[Unset, InteractionExpiry]): The duration of the interaction restriction. Default: `one_day`.
            Example: one_month.
    """

    limit: InteractionGroup
    expiry: Union[Unset, InteractionExpiry] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit.value

        expiry: Union[Unset, str] = UNSET
        if not isinstance(self.expiry, Unset):
            expiry = self.expiry.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
            }
        )
        if expiry is not UNSET:
            field_dict["expiry"] = expiry

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        limit = InteractionGroup(d.pop("limit"))

        _expiry = d.pop("expiry", UNSET)
        expiry: Union[Unset, InteractionExpiry]
        if isinstance(_expiry, Unset):
            expiry = UNSET
        else:
            expiry = InteractionExpiry(_expiry)

        interaction_restrictions = cls(
            limit=limit,
            expiry=expiry,
        )

        interaction_restrictions.additional_properties = d
        return interaction_restrictions

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
