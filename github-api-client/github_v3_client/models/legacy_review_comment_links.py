from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.link import Link

T = TypeVar("T", bound="LegacyReviewCommentLinks")


@attr.s(auto_attribs=True)
class LegacyReviewCommentLinks:
    """
    Attributes:
        self_ (Link): Hypermedia Link
        html (Link): Hypermedia Link
        pull_request (Link): Hypermedia Link
    """

    self_: Link
    html: Link
    pull_request: Link
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        html = self.html.to_dict()

        pull_request = self.pull_request.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "html": html,
                "pull_request": pull_request,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        self_ = Link.from_dict(d.pop("self"))

        html = Link.from_dict(d.pop("html"))

        pull_request = Link.from_dict(d.pop("pull_request"))

        legacy_review_comment_links = cls(
            self_=self_,
            html=html,
            pull_request=pull_request,
        )

        legacy_review_comment_links.additional_properties = d
        return legacy_review_comment_links

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
