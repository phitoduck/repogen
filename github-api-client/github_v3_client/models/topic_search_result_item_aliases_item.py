from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.topic_search_result_item_aliases_item_topic_relation import TopicSearchResultItemAliasesItemTopicRelation
from ..types import UNSET, Unset

T = TypeVar("T", bound="TopicSearchResultItemAliasesItem")


@attr.s(auto_attribs=True)
class TopicSearchResultItemAliasesItem:
    """
    Attributes:
        topic_relation (Union[Unset, TopicSearchResultItemAliasesItemTopicRelation]):
    """

    topic_relation: Union[Unset, TopicSearchResultItemAliasesItemTopicRelation] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        topic_relation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.topic_relation, Unset):
            topic_relation = self.topic_relation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if topic_relation is not UNSET:
            field_dict["topic_relation"] = topic_relation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _topic_relation = d.pop("topic_relation", UNSET)
        topic_relation: Union[Unset, TopicSearchResultItemAliasesItemTopicRelation]
        if isinstance(_topic_relation, Unset):
            topic_relation = UNSET
        else:
            topic_relation = TopicSearchResultItemAliasesItemTopicRelation.from_dict(_topic_relation)

        topic_search_result_item_aliases_item = cls(
            topic_relation=topic_relation,
        )

        topic_search_result_item_aliases_item.additional_properties = d
        return topic_search_result_item_aliases_item

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
