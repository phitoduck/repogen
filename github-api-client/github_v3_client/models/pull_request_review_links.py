from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.pull_request_review_links_html import PullRequestReviewLinksHtml
from ..models.pull_request_review_links_pull_request import PullRequestReviewLinksPullRequest

T = TypeVar("T", bound="PullRequestReviewLinks")


@attr.s(auto_attribs=True)
class PullRequestReviewLinks:
    """
    Attributes:
        html (PullRequestReviewLinksHtml):
        pull_request (PullRequestReviewLinksPullRequest):
    """

    html: PullRequestReviewLinksHtml
    pull_request: PullRequestReviewLinksPullRequest
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        html = self.html.to_dict()

        pull_request = self.pull_request.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "html": html,
                "pull_request": pull_request,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        html = PullRequestReviewLinksHtml.from_dict(d.pop("html"))

        pull_request = PullRequestReviewLinksPullRequest.from_dict(d.pop("pull_request"))

        pull_request_review_links = cls(
            html=html,
            pull_request=pull_request,
        )

        pull_request_review_links.additional_properties = d
        return pull_request_review_links

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
