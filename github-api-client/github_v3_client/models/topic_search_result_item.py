import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.search_result_text_matches_item import SearchResultTextMatchesItem
from ..models.topic_search_result_item_aliases_item import TopicSearchResultItemAliasesItem
from ..models.topic_search_result_item_related_item import TopicSearchResultItemRelatedItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="TopicSearchResultItem")


@attr.s(auto_attribs=True)
class TopicSearchResultItem:
    """Topic Search Result Item

    Attributes:
        name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        featured (bool):
        curated (bool):
        score (float):
        display_name (Optional[str]):
        short_description (Optional[str]):
        description (Optional[str]):
        created_by (Optional[str]):
        released (Optional[str]):
        repository_count (Union[Unset, None, int]):
        logo_url (Union[Unset, None, str]):
        text_matches (Union[Unset, List[SearchResultTextMatchesItem]]):
        related (Union[Unset, None, List[TopicSearchResultItemRelatedItem]]):
        aliases (Union[Unset, None, List[TopicSearchResultItemAliasesItem]]):
    """

    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    featured: bool
    curated: bool
    score: float
    display_name: Optional[str]
    short_description: Optional[str]
    description: Optional[str]
    created_by: Optional[str]
    released: Optional[str]
    repository_count: Union[Unset, None, int] = UNSET
    logo_url: Union[Unset, None, str] = UNSET
    text_matches: Union[Unset, List[SearchResultTextMatchesItem]] = UNSET
    related: Union[Unset, None, List[TopicSearchResultItemRelatedItem]] = UNSET
    aliases: Union[Unset, None, List[TopicSearchResultItemAliasesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        featured = self.featured
        curated = self.curated
        score = self.score
        display_name = self.display_name
        short_description = self.short_description
        description = self.description
        created_by = self.created_by
        released = self.released
        repository_count = self.repository_count
        logo_url = self.logo_url
        text_matches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.text_matches, Unset):
            text_matches = []
            for componentsschemassearch_result_text_matches_item_data in self.text_matches:
                componentsschemassearch_result_text_matches_item = (
                    componentsschemassearch_result_text_matches_item_data.to_dict()
                )

                text_matches.append(componentsschemassearch_result_text_matches_item)

        related: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.related, Unset):
            if self.related is None:
                related = None
            else:
                related = []
                for related_item_data in self.related:
                    related_item = related_item_data.to_dict()

                    related.append(related_item)

        aliases: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aliases, Unset):
            if self.aliases is None:
                aliases = None
            else:
                aliases = []
                for aliases_item_data in self.aliases:
                    aliases_item = aliases_item_data.to_dict()

                    aliases.append(aliases_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
                "featured": featured,
                "curated": curated,
                "score": score,
                "display_name": display_name,
                "short_description": short_description,
                "description": description,
                "created_by": created_by,
                "released": released,
            }
        )
        if repository_count is not UNSET:
            field_dict["repository_count"] = repository_count
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if text_matches is not UNSET:
            field_dict["text_matches"] = text_matches
        if related is not UNSET:
            field_dict["related"] = related
        if aliases is not UNSET:
            field_dict["aliases"] = aliases

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        featured = d.pop("featured")

        curated = d.pop("curated")

        score = d.pop("score")

        display_name = d.pop("display_name")

        short_description = d.pop("short_description")

        description = d.pop("description")

        created_by = d.pop("created_by")

        released = d.pop("released")

        repository_count = d.pop("repository_count", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        text_matches = []
        _text_matches = d.pop("text_matches", UNSET)
        for componentsschemassearch_result_text_matches_item_data in _text_matches or []:
            componentsschemassearch_result_text_matches_item = SearchResultTextMatchesItem.from_dict(
                componentsschemassearch_result_text_matches_item_data
            )

            text_matches.append(componentsschemassearch_result_text_matches_item)

        related = []
        _related = d.pop("related", UNSET)
        for related_item_data in _related or []:
            related_item = TopicSearchResultItemRelatedItem.from_dict(related_item_data)

            related.append(related_item)

        aliases = []
        _aliases = d.pop("aliases", UNSET)
        for aliases_item_data in _aliases or []:
            aliases_item = TopicSearchResultItemAliasesItem.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        topic_search_result_item = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            featured=featured,
            curated=curated,
            score=score,
            display_name=display_name,
            short_description=short_description,
            description=description,
            created_by=created_by,
            released=released,
            repository_count=repository_count,
            logo_url=logo_url,
            text_matches=text_matches,
            related=related,
            aliases=aliases,
        )

        topic_search_result_item.additional_properties = d
        return topic_search_result_item

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
