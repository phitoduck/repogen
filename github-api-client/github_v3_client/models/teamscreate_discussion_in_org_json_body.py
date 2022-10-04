from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamscreateDiscussionInOrgJsonBody")


@attr.s(auto_attribs=True)
class TeamscreateDiscussionInOrgJsonBody:
    """
    Attributes:
        title (str): The discussion post's title.
        body (str): The discussion post's body text.
        private (Union[Unset, bool]): Private posts are only visible to team members, organization owners, and team
            maintainers. Public posts are visible to all members of the organization. Set to `true` to create a private
            post.
    """

    title: str
    body: str
    private: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        body = self.body
        private = self.private

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "body": body,
            }
        )
        if private is not UNSET:
            field_dict["private"] = private

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        body = d.pop("body")

        private = d.pop("private", UNSET)

        teamscreate_discussion_in_org_json_body = cls(
            title=title,
            body=body,
            private=private,
        )

        teamscreate_discussion_in_org_json_body.additional_properties = d
        return teamscreate_discussion_in_org_json_body

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
