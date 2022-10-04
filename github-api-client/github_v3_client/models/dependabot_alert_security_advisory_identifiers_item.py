from typing import Any, Dict, Type, TypeVar

import attr

from ..models.dependabot_alert_security_advisory_identifiers_item_type import (
    DependabotAlertSecurityAdvisoryIdentifiersItemType,
)

T = TypeVar("T", bound="DependabotAlertSecurityAdvisoryIdentifiersItem")


@attr.s(auto_attribs=True)
class DependabotAlertSecurityAdvisoryIdentifiersItem:
    """An advisory identifier.

    Attributes:
        type (DependabotAlertSecurityAdvisoryIdentifiersItemType): The type of advisory identifier.
        value (str): The value of the advisory identifer.
    """

    type: DependabotAlertSecurityAdvisoryIdentifiersItemType
    value: str

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = DependabotAlertSecurityAdvisoryIdentifiersItemType(d.pop("type"))

        value = d.pop("value")

        dependabot_alert_security_advisory_identifiers_item = cls(
            type=type,
            value=value,
        )

        return dependabot_alert_security_advisory_identifiers_item
