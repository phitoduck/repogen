from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.search_result_text_matches_item_matches_item import SearchResultTextMatchesItemMatchesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchResultTextMatchesItem")


@attr.s(auto_attribs=True)
class SearchResultTextMatchesItem:
    """
    Attributes:
        object_url (Union[Unset, str]):
        object_type (Union[Unset, None, str]):
        property_ (Union[Unset, str]):
        fragment (Union[Unset, str]):
        matches (Union[Unset, List[SearchResultTextMatchesItemMatchesItem]]):
    """

    object_url: Union[Unset, str] = UNSET
    object_type: Union[Unset, None, str] = UNSET
    property_: Union[Unset, str] = UNSET
    fragment: Union[Unset, str] = UNSET
    matches: Union[Unset, List[SearchResultTextMatchesItemMatchesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_url = self.object_url
        object_type = self.object_type
        property_ = self.property_
        fragment = self.fragment
        matches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.matches, Unset):
            matches = []
            for matches_item_data in self.matches:
                matches_item = matches_item_data.to_dict()

                matches.append(matches_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_url is not UNSET:
            field_dict["object_url"] = object_url
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if property_ is not UNSET:
            field_dict["property"] = property_
        if fragment is not UNSET:
            field_dict["fragment"] = fragment
        if matches is not UNSET:
            field_dict["matches"] = matches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_url = d.pop("object_url", UNSET)

        object_type = d.pop("object_type", UNSET)

        property_ = d.pop("property", UNSET)

        fragment = d.pop("fragment", UNSET)

        matches = []
        _matches = d.pop("matches", UNSET)
        for matches_item_data in _matches or []:
            matches_item = SearchResultTextMatchesItemMatchesItem.from_dict(matches_item_data)

            matches.append(matches_item)

        search_result_text_matches_item = cls(
            object_url=object_url,
            object_type=object_type,
            property_=property_,
            fragment=fragment,
            matches=matches,
        )

        search_result_text_matches_item.additional_properties = d
        return search_result_text_matches_item

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
