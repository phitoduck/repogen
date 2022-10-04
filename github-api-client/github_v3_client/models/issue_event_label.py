from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="IssueEventLabel")


@attr.s(auto_attribs=True)
class IssueEventLabel:
    """Issue Event Label

    Attributes:
        name (Optional[str]):
        color (Optional[str]):
    """

    name: Optional[str]
    color: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        color = self.color

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "color": color,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        color = d.pop("color")

        issue_event_label = cls(
            name=name,
            color=color,
        )

        issue_event_label.additional_properties = d
        return issue_event_label

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
