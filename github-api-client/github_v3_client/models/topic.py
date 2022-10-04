from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="Topic")


@attr.s(auto_attribs=True)
class Topic:
    """A topic aggregates entities that are related to a subject.

    Attributes:
        names (List[str]):
    """

    names: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        names = self.names

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "names": names,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        names = cast(List[str], d.pop("names"))

        topic = cls(
            names=names,
        )

        topic.additional_properties = d
        return topic

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
