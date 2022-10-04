import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.author_association import AuthorAssociation
from ..models.pull_request_review_links import PullRequestReviewLinks
from ..models.simple_user import SimpleUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="PullRequestReview")


@attr.s(auto_attribs=True)
class PullRequestReview:
    """Pull Request Reviews are reviews on pull requests.

    Attributes:
        id (int): Unique identifier of the review Example: 42.
        node_id (str):  Example: MDE3OlB1bGxSZXF1ZXN0UmV2aWV3ODA=.
        body (str): The text of the review. Example: This looks great..
        state (str):  Example: CHANGES_REQUESTED.
        html_url (str):  Example: https://github.com/octocat/Hello-World/pull/12#pullrequestreview-80.
        pull_request_url (str):  Example: https://api.github.com/repos/octocat/Hello-World/pulls/12.
        links (PullRequestReviewLinks):
        commit_id (str): A commit SHA for the review. Example: 54bb654c9e6025347f57900a4a5c2313a96b8035.
        author_association (AuthorAssociation): How the author is associated with the repository. Example: OWNER.
        user (Optional[SimpleUser]): Simple User
        submitted_at (Union[Unset, datetime.datetime]):
        body_html (Union[Unset, str]):
        body_text (Union[Unset, str]):
    """

    id: int
    node_id: str
    body: str
    state: str
    html_url: str
    pull_request_url: str
    links: PullRequestReviewLinks
    commit_id: str
    author_association: AuthorAssociation
    user: Optional[SimpleUser]
    submitted_at: Union[Unset, datetime.datetime] = UNSET
    body_html: Union[Unset, str] = UNSET
    body_text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        body = self.body
        state = self.state
        html_url = self.html_url
        pull_request_url = self.pull_request_url
        links = self.links.to_dict()

        commit_id = self.commit_id
        author_association = self.author_association.value

        user = self.user.to_dict() if self.user else None

        submitted_at: Union[Unset, str] = UNSET
        if not isinstance(self.submitted_at, Unset):
            submitted_at = self.submitted_at.isoformat()

        body_html = self.body_html
        body_text = self.body_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "node_id": node_id,
                "body": body,
                "state": state,
                "html_url": html_url,
                "pull_request_url": pull_request_url,
                "_links": links,
                "commit_id": commit_id,
                "author_association": author_association,
                "user": user,
            }
        )
        if submitted_at is not UNSET:
            field_dict["submitted_at"] = submitted_at
        if body_html is not UNSET:
            field_dict["body_html"] = body_html
        if body_text is not UNSET:
            field_dict["body_text"] = body_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        node_id = d.pop("node_id")

        body = d.pop("body")

        state = d.pop("state")

        html_url = d.pop("html_url")

        pull_request_url = d.pop("pull_request_url")

        links = PullRequestReviewLinks.from_dict(d.pop("_links"))

        commit_id = d.pop("commit_id")

        author_association = AuthorAssociation(d.pop("author_association"))

        _user = d.pop("user")
        user: Optional[SimpleUser]
        if _user is None:
            user = None
        else:
            user = SimpleUser.from_dict(_user)

        _submitted_at = d.pop("submitted_at", UNSET)
        submitted_at: Union[Unset, datetime.datetime]
        if isinstance(_submitted_at, Unset):
            submitted_at = UNSET
        else:
            submitted_at = isoparse(_submitted_at)

        body_html = d.pop("body_html", UNSET)

        body_text = d.pop("body_text", UNSET)

        pull_request_review = cls(
            id=id,
            node_id=node_id,
            body=body,
            state=state,
            html_url=html_url,
            pull_request_url=pull_request_url,
            links=links,
            commit_id=commit_id,
            author_association=author_association,
            user=user,
            submitted_at=submitted_at,
            body_html=body_html,
            body_text=body_text,
        )

        pull_request_review.additional_properties = d
        return pull_request_review

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
