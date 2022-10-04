from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.workflow import Workflow

T = TypeVar("T", bound="ActionslistRepoWorkflowsResponse200")


@attr.s(auto_attribs=True)
class ActionslistRepoWorkflowsResponse200:
    """
    Attributes:
        total_count (int):
        workflows (List[Workflow]):
    """

    total_count: int
    workflows: List[Workflow]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        workflows = []
        for workflows_item_data in self.workflows:
            workflows_item = workflows_item_data.to_dict()

            workflows.append(workflows_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_count": total_count,
                "workflows": workflows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_count = d.pop("total_count")

        workflows = []
        _workflows = d.pop("workflows")
        for workflows_item_data in _workflows:
            workflows_item = Workflow.from_dict(workflows_item_data)

            workflows.append(workflows_item)

        actionslist_repo_workflows_response_200 = cls(
            total_count=total_count,
            workflows=workflows,
        )

        actionslist_repo_workflows_response_200.additional_properties = d
        return actionslist_repo_workflows_response_200

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
