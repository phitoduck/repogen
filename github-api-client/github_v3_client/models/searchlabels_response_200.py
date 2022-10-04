from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.label_search_result_item import LabelSearchResultItem

T = TypeVar("T", bound="SearchlabelsResponse200")


@attr.s(auto_attribs=True)
class SearchlabelsResponse200:
    """
    Attributes:
        total_count (int):
        incomplete_results (bool):
        items (List[LabelSearchResultItem]):
    """

    total_count: int
    incomplete_results: bool
    items: List[LabelSearchResultItem]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        incomplete_results = self.incomplete_results
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_count": total_count,
                "incomplete_results": incomplete_results,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_count = d.pop("total_count")

        incomplete_results = d.pop("incomplete_results")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = LabelSearchResultItem.from_dict(items_item_data)

            items.append(items_item)

        searchlabels_response_200 = cls(
            total_count=total_count,
            incomplete_results=incomplete_results,
            items=items,
        )

        searchlabels_response_200.additional_properties = d
        return searchlabels_response_200

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
