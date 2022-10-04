from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopicSearchResultItemAliasesItemTopicRelation")


@attr.s(auto_attribs=True)
class TopicSearchResultItemAliasesItemTopicRelation:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        topic_id (Union[Unset, int]):
        relation_type (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    topic_id: Union[Unset, int] = UNSET
    relation_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        topic_id = self.topic_id
        relation_type = self.relation_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if topic_id is not UNSET:
            field_dict["topic_id"] = topic_id
        if relation_type is not UNSET:
            field_dict["relation_type"] = relation_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        topic_id = d.pop("topic_id", UNSET)

        relation_type = d.pop("relation_type", UNSET)

        topic_search_result_item_aliases_item_topic_relation = cls(
            id=id,
            name=name,
            topic_id=topic_id,
            relation_type=relation_type,
        )

        topic_search_result_item_aliases_item_topic_relation.additional_properties = d
        return topic_search_result_item_aliases_item_topic_relation

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
