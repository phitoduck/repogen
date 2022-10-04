from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="WorkflowRunUsageBillableUBUNTUJobRunsItem")


@attr.s(auto_attribs=True)
class WorkflowRunUsageBillableUBUNTUJobRunsItem:
    """
    Attributes:
        job_id (int):
        duration_ms (int):
    """

    job_id: int
    duration_ms: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        duration_ms = self.duration_ms

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "duration_ms": duration_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_id = d.pop("job_id")

        duration_ms = d.pop("duration_ms")

        workflow_run_usage_billable_ubuntu_job_runs_item = cls(
            job_id=job_id,
            duration_ms=duration_ms,
        )

        workflow_run_usage_billable_ubuntu_job_runs_item.additional_properties = d
        return workflow_run_usage_billable_ubuntu_job_runs_item

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
