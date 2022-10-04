import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.reaction_rollup import ReactionRollup
from ..models.simple_user import SimpleUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamDiscussionComment")


@attr.s(auto_attribs=True)
class TeamDiscussionComment:
    """A reply to a discussion within a team.

    Attributes:
        body (str): The main text of the comment. Example: I agree with this suggestion..
        body_html (str):  Example: <p>Do you like apples?</p>.
        body_version (str): The current version of the body content. If provided, this update operation will be rejected
            if the given version does not match the latest version on the server. Example: 0307116bbf7ced493b8d8a346c650b71.
        created_at (datetime.datetime):  Example: 2018-01-15T23:53:58Z.
        discussion_url (str):  Example: https://api.github.com/organizations/1/team/2403582/discussions/1.
        html_url (str):  Example: https://github.com/orgs/github/teams/justice-league/discussions/1/comments/1.
        node_id (str):  Example: MDIxOlRlYW1EaXNjdXNzaW9uQ29tbWVudDE=.
        number (int): The unique sequence number of a team discussion comment. Example: 42.
        updated_at (datetime.datetime):  Example: 2018-01-15T23:53:58Z.
        url (str):  Example: https://api.github.com/organizations/1/team/2403582/discussions/1/comments/1.
        author (Optional[SimpleUser]): Simple User
        last_edited_at (Optional[datetime.datetime]):
        reactions (Union[Unset, ReactionRollup]):
    """

    body: str
    body_html: str
    body_version: str
    created_at: datetime.datetime
    discussion_url: str
    html_url: str
    node_id: str
    number: int
    updated_at: datetime.datetime
    url: str
    author: Optional[SimpleUser]
    last_edited_at: Optional[datetime.datetime]
    reactions: Union[Unset, ReactionRollup] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body
        body_html = self.body_html
        body_version = self.body_version
        created_at = self.created_at.isoformat()

        discussion_url = self.discussion_url
        html_url = self.html_url
        node_id = self.node_id
        number = self.number
        updated_at = self.updated_at.isoformat()

        url = self.url
        author = self.author.to_dict() if self.author else None

        last_edited_at = self.last_edited_at.isoformat() if self.last_edited_at else None

        reactions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reactions, Unset):
            reactions = self.reactions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "body_html": body_html,
                "body_version": body_version,
                "created_at": created_at,
                "discussion_url": discussion_url,
                "html_url": html_url,
                "node_id": node_id,
                "number": number,
                "updated_at": updated_at,
                "url": url,
                "author": author,
                "last_edited_at": last_edited_at,
            }
        )
        if reactions is not UNSET:
            field_dict["reactions"] = reactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        body = d.pop("body")

        body_html = d.pop("body_html")

        body_version = d.pop("body_version")

        created_at = isoparse(d.pop("created_at"))

        discussion_url = d.pop("discussion_url")

        html_url = d.pop("html_url")

        node_id = d.pop("node_id")

        number = d.pop("number")

        updated_at = isoparse(d.pop("updated_at"))

        url = d.pop("url")

        _author = d.pop("author")
        author: Optional[SimpleUser]
        if _author is None:
            author = None
        else:
            author = SimpleUser.from_dict(_author)

        _last_edited_at = d.pop("last_edited_at")
        last_edited_at: Optional[datetime.datetime]
        if _last_edited_at is None:
            last_edited_at = None
        else:
            last_edited_at = isoparse(_last_edited_at)

        _reactions = d.pop("reactions", UNSET)
        reactions: Union[Unset, ReactionRollup]
        if isinstance(_reactions, Unset):
            reactions = UNSET
        else:
            reactions = ReactionRollup.from_dict(_reactions)

        team_discussion_comment = cls(
            body=body,
            body_html=body_html,
            body_version=body_version,
            created_at=created_at,
            discussion_url=discussion_url,
            html_url=html_url,
            node_id=node_id,
            number=number,
            updated_at=updated_at,
            url=url,
            author=author,
            last_edited_at=last_edited_at,
            reactions=reactions,
        )

        team_discussion_comment.additional_properties = d
        return team_discussion_comment

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
