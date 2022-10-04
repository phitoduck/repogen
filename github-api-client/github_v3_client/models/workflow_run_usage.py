from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.workflow_run_usage_billable import WorkflowRunUsageBillable
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowRunUsage")


@attr.s(auto_attribs=True)
class WorkflowRunUsage:
    """Workflow Run Usage

    Attributes:
        billable (WorkflowRunUsageBillable):
        run_duration_ms (Union[Unset, int]):
    """

    billable: WorkflowRunUsageBillable
    run_duration_ms: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billable = self.billable.to_dict()

        run_duration_ms = self.run_duration_ms

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billable": billable,
            }
        )
        if run_duration_ms is not UNSET:
            field_dict["run_duration_ms"] = run_duration_ms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        billable = WorkflowRunUsageBillable.from_dict(d.pop("billable"))

        run_duration_ms = d.pop("run_duration_ms", UNSET)

        workflow_run_usage = cls(
            billable=billable,
            run_duration_ms=run_duration_ms,
        )

        workflow_run_usage.additional_properties = d
        return workflow_run_usage

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
