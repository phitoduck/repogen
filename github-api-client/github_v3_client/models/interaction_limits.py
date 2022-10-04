import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.interaction_group import InteractionGroup

T = TypeVar("T", bound="InteractionLimits")


@attr.s(auto_attribs=True)
class InteractionLimits:
    """Interaction limit settings.

    Attributes:
        limit (InteractionGroup): The type of GitHub user that can comment, open issues, or create pull requests while
            the interaction limit is in effect. Example: collaborators_only.
        origin (str):  Example: repository.
        expires_at (datetime.datetime):  Example: 2018-08-17T04:18:39Z.
    """

    limit: InteractionGroup
    origin: str
    expires_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit.value

        origin = self.origin
        expires_at = self.expires_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
                "origin": origin,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        limit = InteractionGroup(d.pop("limit"))

        origin = d.pop("origin")

        expires_at = isoparse(d.pop("expires_at"))

        interaction_limits = cls(
            limit=limit,
            origin=origin,
            expires_at=expires_at,
        )

        interaction_limits.additional_properties = d
        return interaction_limits

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
