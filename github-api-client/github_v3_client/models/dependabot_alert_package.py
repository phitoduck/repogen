from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="DependabotAlertPackage")


@attr.s(auto_attribs=True)
class DependabotAlertPackage:
    """Details for the vulnerable package.

    Attributes:
        ecosystem (str): The package's language or package management ecosystem.
        name (str): The unique package name within its ecosystem.
    """

    ecosystem: str
    name: str

    def to_dict(self) -> Dict[str, Any]:
        ecosystem = self.ecosystem
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "ecosystem": ecosystem,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ecosystem = d.pop("ecosystem")

        name = d.pop("name")

        dependabot_alert_package = cls(
            ecosystem=ecosystem,
            name=name,
        )

        return dependabot_alert_package
