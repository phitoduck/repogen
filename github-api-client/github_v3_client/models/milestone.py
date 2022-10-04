import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.milestone_state import MilestoneState
from ..models.simple_user import SimpleUser

T = TypeVar("T", bound="Milestone")


@attr.s(auto_attribs=True)
class Milestone:
    """A collection of related issues and pull requests.

    Attributes:
        url (str):  Example: https://api.github.com/repos/octocat/Hello-World/milestones/1.
        html_url (str):  Example: https://github.com/octocat/Hello-World/milestones/v1.0.
        labels_url (str):  Example: https://api.github.com/repos/octocat/Hello-World/milestones/1/labels.
        id (int):  Example: 1002604.
        node_id (str):  Example: MDk6TWlsZXN0b25lMTAwMjYwNA==.
        number (int): The number of the milestone. Example: 42.
        state (MilestoneState): The state of the milestone. Default: MilestoneState.OPEN. Example: open.
        title (str): The title of the milestone. Example: v1.0.
        open_issues (int):  Example: 4.
        closed_issues (int):  Example: 8.
        created_at (datetime.datetime):  Example: 2011-04-10T20:09:31Z.
        updated_at (datetime.datetime):  Example: 2014-03-03T18:58:10Z.
        description (Optional[str]):  Example: Tracking milestone for version 1.0.
        creator (Optional[SimpleUser]): Simple User
        closed_at (Optional[datetime.datetime]):  Example: 2013-02-12T13:22:01Z.
        due_on (Optional[datetime.datetime]):  Example: 2012-10-09T23:39:01Z.
    """

    url: str
    html_url: str
    labels_url: str
    id: int
    node_id: str
    number: int
    title: str
    open_issues: int
    closed_issues: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: Optional[str]
    creator: Optional[SimpleUser]
    closed_at: Optional[datetime.datetime]
    due_on: Optional[datetime.datetime]
    state: MilestoneState = MilestoneState.OPEN
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        html_url = self.html_url
        labels_url = self.labels_url
        id = self.id
        node_id = self.node_id
        number = self.number
        state = self.state.value

        title = self.title
        open_issues = self.open_issues
        closed_issues = self.closed_issues
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description
        creator = self.creator.to_dict() if self.creator else None

        closed_at = self.closed_at.isoformat() if self.closed_at else None

        due_on = self.due_on.isoformat() if self.due_on else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "html_url": html_url,
                "labels_url": labels_url,
                "id": id,
                "node_id": node_id,
                "number": number,
                "state": state,
                "title": title,
                "open_issues": open_issues,
                "closed_issues": closed_issues,
                "created_at": created_at,
                "updated_at": updated_at,
                "description": description,
                "creator": creator,
                "closed_at": closed_at,
                "due_on": due_on,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        html_url = d.pop("html_url")

        labels_url = d.pop("labels_url")

        id = d.pop("id")

        node_id = d.pop("node_id")

        number = d.pop("number")

        state = MilestoneState(d.pop("state"))

        title = d.pop("title")

        open_issues = d.pop("open_issues")

        closed_issues = d.pop("closed_issues")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description")

        _creator = d.pop("creator")
        creator: Optional[SimpleUser]
        if _creator is None:
            creator = None
        else:
            creator = SimpleUser.from_dict(_creator)

        _closed_at = d.pop("closed_at")
        closed_at: Optional[datetime.datetime]
        if _closed_at is None:
            closed_at = None
        else:
            closed_at = isoparse(_closed_at)

        _due_on = d.pop("due_on")
        due_on: Optional[datetime.datetime]
        if _due_on is None:
            due_on = None
        else:
            due_on = isoparse(_due_on)

        milestone = cls(
            url=url,
            html_url=html_url,
            labels_url=labels_url,
            id=id,
            node_id=node_id,
            number=number,
            state=state,
            title=title,
            open_issues=open_issues,
            closed_issues=closed_issues,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            creator=creator,
            closed_at=closed_at,
            due_on=due_on,
        )

        milestone.additional_properties = d
        return milestone

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
