import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.workflow_state import WorkflowState
from ..types import UNSET, Unset

T = TypeVar("T", bound="Workflow")


@attr.s(auto_attribs=True)
class Workflow:
    """A GitHub Actions workflow

    Attributes:
        id (int):  Example: 5.
        node_id (str):  Example: MDg6V29ya2Zsb3cxMg==.
        name (str):  Example: CI.
        path (str):  Example: ruby.yaml.
        state (WorkflowState):  Example: active.
        created_at (datetime.datetime):  Example: 2019-12-06T14:20:20.000Z.
        updated_at (datetime.datetime):  Example: 2019-12-06T14:20:20.000Z.
        url (str):  Example: https://api.github.com/repos/actions/setup-ruby/workflows/5.
        html_url (str):  Example: https://github.com/actions/setup-ruby/blob/master/.github/workflows/ruby.yaml.
        badge_url (str):  Example: https://github.com/actions/setup-ruby/workflows/CI/badge.svg.
        deleted_at (Union[Unset, datetime.datetime]):  Example: 2019-12-06T14:20:20.000Z.
    """

    id: int
    node_id: str
    name: str
    path: str
    state: WorkflowState
    created_at: datetime.datetime
    updated_at: datetime.datetime
    url: str
    html_url: str
    badge_url: str
    deleted_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        name = self.name
        path = self.path
        state = self.state.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        url = self.url
        html_url = self.html_url
        badge_url = self.badge_url
        deleted_at: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "node_id": node_id,
                "name": name,
                "path": path,
                "state": state,
                "created_at": created_at,
                "updated_at": updated_at,
                "url": url,
                "html_url": html_url,
                "badge_url": badge_url,
            }
        )
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        node_id = d.pop("node_id")

        name = d.pop("name")

        path = d.pop("path")

        state = WorkflowState(d.pop("state"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        url = d.pop("url")

        html_url = d.pop("html_url")

        badge_url = d.pop("badge_url")

        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: Union[Unset, datetime.datetime]
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        workflow = cls(
            id=id,
            node_id=node_id,
            name=name,
            path=path,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            url=url,
            html_url=html_url,
            badge_url=badge_url,
            deleted_at=deleted_at,
        )

        workflow.additional_properties = d
        return workflow

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
