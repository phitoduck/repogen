from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="DependabotAlertSecurityAdvisoryReferencesItem")


@attr.s(auto_attribs=True)
class DependabotAlertSecurityAdvisoryReferencesItem:
    """A link to additional advisory information.

    Attributes:
        url (str): The URL of the reference.
    """

    url: str

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        dependabot_alert_security_advisory_references_item = cls(
            url=url,
        )

        return dependabot_alert_security_advisory_references_item
