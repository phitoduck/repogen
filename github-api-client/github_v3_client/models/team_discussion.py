import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.reaction_rollup import ReactionRollup
from ..models.simple_user import SimpleUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamDiscussion")


@attr.s(auto_attribs=True)
class TeamDiscussion:
    """A team discussion is a persistent record of a free-form conversation within a team.

    Attributes:
        body (str): The main text of the discussion. Example: Please suggest improvements to our workflow in comments..
        body_html (str):  Example: <p>Hi! This is an area for us to collaborate as a team</p>.
        body_version (str): The current version of the body content. If provided, this update operation will be rejected
            if the given version does not match the latest version on the server. Example: 0307116bbf7ced493b8d8a346c650b71.
        comments_count (int):
        comments_url (str):  Example: https://api.github.com/organizations/1/team/2343027/discussions/1/comments.
        created_at (datetime.datetime):  Example: 2018-01-25T18:56:31Z.
        html_url (str):  Example: https://github.com/orgs/github/teams/justice-league/discussions/1.
        node_id (str):  Example: MDE0OlRlYW1EaXNjdXNzaW9uMQ==.
        number (int): The unique sequence number of a team discussion. Example: 42.
        pinned (bool): Whether or not this discussion should be pinned for easy retrieval. Example: True.
        private (bool): Whether or not this discussion should be restricted to team members and organization
            administrators. Example: True.
        team_url (str):  Example: https://api.github.com/organizations/1/team/2343027.
        title (str): The title of the discussion. Example: How can we improve our workflow?.
        updated_at (datetime.datetime):  Example: 2018-01-25T18:56:31Z.
        url (str):  Example: https://api.github.com/organizations/1/team/2343027/discussions/1.
        author (Optional[SimpleUser]): Simple User
        last_edited_at (Optional[datetime.datetime]):
        reactions (Union[Unset, ReactionRollup]):
    """

    body: str
    body_html: str
    body_version: str
    comments_count: int
    comments_url: str
    created_at: datetime.datetime
    html_url: str
    node_id: str
    number: int
    pinned: bool
    private: bool
    team_url: str
    title: str
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
        comments_count = self.comments_count
        comments_url = self.comments_url
        created_at = self.created_at.isoformat()

        html_url = self.html_url
        node_id = self.node_id
        number = self.number
        pinned = self.pinned
        private = self.private
        team_url = self.team_url
        title = self.title
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
                "comments_count": comments_count,
                "comments_url": comments_url,
                "created_at": created_at,
                "html_url": html_url,
                "node_id": node_id,
                "number": number,
                "pinned": pinned,
                "private": private,
                "team_url": team_url,
                "title": title,
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

        comments_count = d.pop("comments_count")

        comments_url = d.pop("comments_url")

        created_at = isoparse(d.pop("created_at"))

        html_url = d.pop("html_url")

        node_id = d.pop("node_id")

        number = d.pop("number")

        pinned = d.pop("pinned")

        private = d.pop("private")

        team_url = d.pop("team_url")

        title = d.pop("title")

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

        team_discussion = cls(
            body=body,
            body_html=body_html,
            body_version=body_version,
            comments_count=comments_count,
            comments_url=comments_url,
            created_at=created_at,
            html_url=html_url,
            node_id=node_id,
            number=number,
            pinned=pinned,
            private=private,
            team_url=team_url,
            title=title,
            updated_at=updated_at,
            url=url,
            author=author,
            last_edited_at=last_edited_at,
            reactions=reactions,
        )

        team_discussion.additional_properties = d
        return team_discussion

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
