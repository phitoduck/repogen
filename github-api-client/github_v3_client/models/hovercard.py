from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.hovercard_contexts_item import HovercardContextsItem

T = TypeVar("T", bound="Hovercard")


@attr.s(auto_attribs=True)
class Hovercard:
    """Hovercard

    Attributes:
        contexts (List[HovercardContextsItem]):
    """

    contexts: List[HovercardContextsItem]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contexts = []
        for contexts_item_data in self.contexts:
            contexts_item = contexts_item_data.to_dict()

            contexts.append(contexts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contexts": contexts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contexts = []
        _contexts = d.pop("contexts")
        for contexts_item_data in _contexts:
            contexts_item = HovercardContextsItem.from_dict(contexts_item_data)

            contexts.append(contexts_item)

        hovercard = cls(
            contexts=contexts,
        )

        hovercard.additional_properties = d
        return hovercard

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
