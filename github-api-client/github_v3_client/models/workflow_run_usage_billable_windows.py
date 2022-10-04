from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.workflow_run_usage_billable_windows_job_runs_item import WorkflowRunUsageBillableWINDOWSJobRunsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowRunUsageBillableWINDOWS")


@attr.s(auto_attribs=True)
class WorkflowRunUsageBillableWINDOWS:
    """
    Attributes:
        total_ms (int):
        jobs (int):
        job_runs (Union[Unset, List[WorkflowRunUsageBillableWINDOWSJobRunsItem]]):
    """

    total_ms: int
    jobs: int
    job_runs: Union[Unset, List[WorkflowRunUsageBillableWINDOWSJobRunsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_ms = self.total_ms
        jobs = self.jobs
        job_runs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.job_runs, Unset):
            job_runs = []
            for job_runs_item_data in self.job_runs:
                job_runs_item = job_runs_item_data.to_dict()

                job_runs.append(job_runs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_ms": total_ms,
                "jobs": jobs,
            }
        )
        if job_runs is not UNSET:
            field_dict["job_runs"] = job_runs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_ms = d.pop("total_ms")

        jobs = d.pop("jobs")

        job_runs = []
        _job_runs = d.pop("job_runs", UNSET)
        for job_runs_item_data in _job_runs or []:
            job_runs_item = WorkflowRunUsageBillableWINDOWSJobRunsItem.from_dict(job_runs_item_data)

            job_runs.append(job_runs_item)

        workflow_run_usage_billable_windows = cls(
            total_ms=total_ms,
            jobs=jobs,
            job_runs=job_runs,
        )

        workflow_run_usage_billable_windows.additional_properties = d
        return workflow_run_usage_billable_windows

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
