from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.job import Job

T = TypeVar("T", bound="ActionslistJobsForWorkflowRunResponse200")


@attr.s(auto_attribs=True)
class ActionslistJobsForWorkflowRunResponse200:
    """
    Attributes:
        total_count (int):
        jobs (List[Job]):
    """

    total_count: int
    jobs: List[Job]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        jobs = []
        for jobs_item_data in self.jobs:
            jobs_item = jobs_item_data.to_dict()

            jobs.append(jobs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_count": total_count,
                "jobs": jobs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_count = d.pop("total_count")

        jobs = []
        _jobs = d.pop("jobs")
        for jobs_item_data in _jobs:
            jobs_item = Job.from_dict(jobs_item_data)

            jobs.append(jobs_item)

        actionslist_jobs_for_workflow_run_response_200 = cls(
            total_count=total_count,
            jobs=jobs,
        )

        actionslist_jobs_for_workflow_run_response_200.additional_properties = d
        return actionslist_jobs_for_workflow_run_response_200

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
