from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.timeline_committed_event_author import TimelineCommittedEventAuthor
from ..models.timeline_committed_event_committer import TimelineCommittedEventCommitter
from ..models.timeline_committed_event_parents_item import TimelineCommittedEventParentsItem
from ..models.timeline_committed_event_tree import TimelineCommittedEventTree
from ..models.timeline_committed_event_verification import TimelineCommittedEventVerification
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimelineCommittedEvent")


@attr.s(auto_attribs=True)
class TimelineCommittedEvent:
    """Timeline Committed Event

    Attributes:
        sha (str): SHA for the commit Example: 7638417db6d59f3c431d3e1f261cc637155684cd.
        node_id (str):
        url (str):
        author (TimelineCommittedEventAuthor): Identifying information for the git-user
        committer (TimelineCommittedEventCommitter): Identifying information for the git-user
        message (str): Message describing the purpose of the commit Example: Fix #42.
        tree (TimelineCommittedEventTree):
        parents (List[TimelineCommittedEventParentsItem]):
        verification (TimelineCommittedEventVerification):
        html_url (str):
        event (Union[Unset, str]):
    """

    sha: str
    node_id: str
    url: str
    author: TimelineCommittedEventAuthor
    committer: TimelineCommittedEventCommitter
    message: str
    tree: TimelineCommittedEventTree
    parents: List[TimelineCommittedEventParentsItem]
    verification: TimelineCommittedEventVerification
    html_url: str
    event: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sha = self.sha
        node_id = self.node_id
        url = self.url
        author = self.author.to_dict()

        committer = self.committer.to_dict()

        message = self.message
        tree = self.tree.to_dict()

        parents = []
        for parents_item_data in self.parents:
            parents_item = parents_item_data.to_dict()

            parents.append(parents_item)

        verification = self.verification.to_dict()

        html_url = self.html_url
        event = self.event

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha": sha,
                "node_id": node_id,
                "url": url,
                "author": author,
                "committer": committer,
                "message": message,
                "tree": tree,
                "parents": parents,
                "verification": verification,
                "html_url": html_url,
            }
        )
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sha = d.pop("sha")

        node_id = d.pop("node_id")

        url = d.pop("url")

        author = TimelineCommittedEventAuthor.from_dict(d.pop("author"))

        committer = TimelineCommittedEventCommitter.from_dict(d.pop("committer"))

        message = d.pop("message")

        tree = TimelineCommittedEventTree.from_dict(d.pop("tree"))

        parents = []
        _parents = d.pop("parents")
        for parents_item_data in _parents:
            parents_item = TimelineCommittedEventParentsItem.from_dict(parents_item_data)

            parents.append(parents_item)

        verification = TimelineCommittedEventVerification.from_dict(d.pop("verification"))

        html_url = d.pop("html_url")

        event = d.pop("event", UNSET)

        timeline_committed_event = cls(
            sha=sha,
            node_id=node_id,
            url=url,
            author=author,
            committer=committer,
            message=message,
            tree=tree,
            parents=parents,
            verification=verification,
            html_url=html_url,
            event=event,
        )

        timeline_committed_event.additional_properties = d
        return timeline_committed_event

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
