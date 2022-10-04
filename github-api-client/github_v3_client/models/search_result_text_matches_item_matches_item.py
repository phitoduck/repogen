from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchResultTextMatchesItemMatchesItem")


@attr.s(auto_attribs=True)
class SearchResultTextMatchesItemMatchesItem:
    """
    Attributes:
        text (Union[Unset, str]):
        indices (Union[Unset, List[int]]):
    """

    text: Union[Unset, str] = UNSET
    indices: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        indices: Union[Unset, List[int]] = UNSET
        if not isinstance(self.indices, Unset):
            indices = self.indices

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if indices is not UNSET:
            field_dict["indices"] = indices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text", UNSET)

        indices = cast(List[int], d.pop("indices", UNSET))

        search_result_text_matches_item_matches_item = cls(
            text=text,
            indices=indices,
        )

        search_result_text_matches_item_matches_item.additional_properties = d
        return search_result_text_matches_item_matches_item

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
