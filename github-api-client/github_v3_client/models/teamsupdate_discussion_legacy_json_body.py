from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamsupdateDiscussionLegacyJsonBody")


@attr.s(auto_attribs=True)
class TeamsupdateDiscussionLegacyJsonBody:
    """
    Attributes:
        title (Union[Unset, str]): The discussion post's title.
        body (Union[Unset, str]): The discussion post's body text.
    """

    title: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        body = self.body

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        body = d.pop("body", UNSET)

        teamsupdate_discussion_legacy_json_body = cls(
            title=title,
            body=body,
        )

        teamsupdate_discussion_legacy_json_body.additional_properties = d
        return teamsupdate_discussion_legacy_json_body

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
