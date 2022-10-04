from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.search_result_text_matches_item import SearchResultTextMatchesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelSearchResultItem")


@attr.s(auto_attribs=True)
class LabelSearchResultItem:
    """Label Search Result Item

    Attributes:
        id (int):
        node_id (str):
        url (str):
        name (str):
        color (str):
        default (bool):
        score (float):
        description (Optional[str]):
        text_matches (Union[Unset, List[SearchResultTextMatchesItem]]):
    """

    id: int
    node_id: str
    url: str
    name: str
    color: str
    default: bool
    score: float
    description: Optional[str]
    text_matches: Union[Unset, List[SearchResultTextMatchesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        url = self.url
        name = self.name
        color = self.color
        default = self.default
        score = self.score
        description = self.description
        text_matches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.text_matches, Unset):
            text_matches = []
            for componentsschemassearch_result_text_matches_item_data in self.text_matches:
                componentsschemassearch_result_text_matches_item = (
                    componentsschemassearch_result_text_matches_item_data.to_dict()
                )

                text_matches.append(componentsschemassearch_result_text_matches_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "node_id": node_id,
                "url": url,
                "name": name,
                "color": color,
                "default": default,
                "score": score,
                "description": description,
            }
        )
        if text_matches is not UNSET:
            field_dict["text_matches"] = text_matches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        node_id = d.pop("node_id")

        url = d.pop("url")

        name = d.pop("name")

        color = d.pop("color")

        default = d.pop("default")

        score = d.pop("score")

        description = d.pop("description")

        text_matches = []
        _text_matches = d.pop("text_matches", UNSET)
        for componentsschemassearch_result_text_matches_item_data in _text_matches or []:
            componentsschemassearch_result_text_matches_item = SearchResultTextMatchesItem.from_dict(
                componentsschemassearch_result_text_matches_item_data
            )

            text_matches.append(componentsschemassearch_result_text_matches_item)

        label_search_result_item = cls(
            id=id,
            node_id=node_id,
            url=url,
            name=name,
            color=color,
            default=default,
            score=score,
            description=description,
            text_matches=text_matches,
        )

        label_search_result_item.additional_properties = d
        return label_search_result_item

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
