from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="HovercardContextsItem")


@attr.s(auto_attribs=True)
class HovercardContextsItem:
    """
    Attributes:
        message (str):
        octicon (str):
    """

    message: str
    octicon: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        octicon = self.octicon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "octicon": octicon,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message")

        octicon = d.pop("octicon")

        hovercard_contexts_item = cls(
            message=message,
            octicon=octicon,
        )

        hovercard_contexts_item.additional_properties = d
        return hovercard_contexts_item

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
