import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.job_conclusion import JobConclusion
from ..models.job_status import JobStatus
from ..models.job_steps_item import JobStepsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Job")


@attr.s(auto_attribs=True)
class Job:
    """Information of a job execution in a workflow run

    Attributes:
        id (int): The id of the job. Example: 21.
        run_id (int): The id of the associated workflow run. Example: 5.
        run_url (str):  Example: https://api.github.com/repos/github/hello-world/actions/runs/5.
        node_id (str):  Example: MDg6Q2hlY2tSdW40.
        head_sha (str): The SHA of the commit that is being run. Example: 009b8a3a9ccbb128af87f9b1c0f4c62e8a304f6d.
        url (str):  Example: https://api.github.com/repos/github/hello-world/actions/jobs/21.
        status (JobStatus): The phase of the lifecycle that the job is currently in. Example: queued.
        started_at (datetime.datetime): The time that the job started, in ISO 8601 format. Example:
            2019-08-08T08:00:00-07:00.
        name (str): The name of the job. Example: test-coverage.
        check_run_url (str):  Example: https://api.github.com/repos/github/hello-world/check-runs/4.
        labels (List[str]): Labels for the workflow job. Specified by the "runs_on" attribute in the action's workflow
            file. Example: ['self-hosted', 'foo', 'bar'].
        run_attempt (Union[Unset, int]): Attempt number of the associated workflow run, 1 for first attempt and higher
            if the workflow was re-run. Example: 1.
        html_url (Optional[str]):  Example: https://github.com/github/hello-world/runs/4.
        conclusion (Optional[JobConclusion]): The outcome of the job. Example: success.
        completed_at (Optional[datetime.datetime]): The time that the job finished, in ISO 8601 format. Example:
            2019-08-08T08:00:00-07:00.
        steps (Union[Unset, List[JobStepsItem]]): Steps in this job.
        runner_id (Optional[int]): The ID of the runner to which this job has been assigned. (If a runner hasn't yet
            been assigned, this will be null.) Example: 1.
        runner_name (Optional[str]): The name of the runner to which this job has been assigned. (If a runner hasn't yet
            been assigned, this will be null.) Example: my runner.
        runner_group_id (Optional[int]): The ID of the runner group to which this job has been assigned. (If a runner
            hasn't yet been assigned, this will be null.) Example: 2.
        runner_group_name (Optional[str]): The name of the runner group to which this job has been assigned. (If a
            runner hasn't yet been assigned, this will be null.) Example: my runner group.
    """

    id: int
    run_id: int
    run_url: str
    node_id: str
    head_sha: str
    url: str
    status: JobStatus
    started_at: datetime.datetime
    name: str
    check_run_url: str
    labels: List[str]
    html_url: Optional[str]
    conclusion: Optional[JobConclusion]
    completed_at: Optional[datetime.datetime]
    runner_id: Optional[int]
    runner_name: Optional[str]
    runner_group_id: Optional[int]
    runner_group_name: Optional[str]
    run_attempt: Union[Unset, int] = UNSET
    steps: Union[Unset, List[JobStepsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        run_id = self.run_id
        run_url = self.run_url
        node_id = self.node_id
        head_sha = self.head_sha
        url = self.url
        status = self.status.value

        started_at = self.started_at.isoformat()

        name = self.name
        check_run_url = self.check_run_url
        labels = self.labels

        run_attempt = self.run_attempt
        html_url = self.html_url
        conclusion = self.conclusion.value if self.conclusion else None

        completed_at = self.completed_at.isoformat() if self.completed_at else None

        steps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()

                steps.append(steps_item)

        runner_id = self.runner_id
        runner_name = self.runner_name
        runner_group_id = self.runner_group_id
        runner_group_name = self.runner_group_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "run_id": run_id,
                "run_url": run_url,
                "node_id": node_id,
                "head_sha": head_sha,
                "url": url,
                "status": status,
                "started_at": started_at,
                "name": name,
                "check_run_url": check_run_url,
                "labels": labels,
                "html_url": html_url,
                "conclusion": conclusion,
                "completed_at": completed_at,
                "runner_id": runner_id,
                "runner_name": runner_name,
                "runner_group_id": runner_group_id,
                "runner_group_name": runner_group_name,
            }
        )
        if run_attempt is not UNSET:
            field_dict["run_attempt"] = run_attempt
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        run_id = d.pop("run_id")

        run_url = d.pop("run_url")

        node_id = d.pop("node_id")

        head_sha = d.pop("head_sha")

        url = d.pop("url")

        status = JobStatus(d.pop("status"))

        started_at = isoparse(d.pop("started_at"))

        name = d.pop("name")

        check_run_url = d.pop("check_run_url")

        labels = cast(List[str], d.pop("labels"))

        run_attempt = d.pop("run_attempt", UNSET)

        html_url = d.pop("html_url")

        _conclusion = d.pop("conclusion")
        conclusion: Optional[JobConclusion]
        if _conclusion is None:
            conclusion = None
        else:
            conclusion = JobConclusion(_conclusion)

        _completed_at = d.pop("completed_at")
        completed_at: Optional[datetime.datetime]
        if _completed_at is None:
            completed_at = None
        else:
            completed_at = isoparse(_completed_at)

        steps = []
        _steps = d.pop("steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = JobStepsItem.from_dict(steps_item_data)

            steps.append(steps_item)

        runner_id = d.pop("runner_id")

        runner_name = d.pop("runner_name")

        runner_group_id = d.pop("runner_group_id")

        runner_group_name = d.pop("runner_group_name")

        job = cls(
            id=id,
            run_id=run_id,
            run_url=run_url,
            node_id=node_id,
            head_sha=head_sha,
            url=url,
            status=status,
            started_at=started_at,
            name=name,
            check_run_url=check_run_url,
            labels=labels,
            run_attempt=run_attempt,
            html_url=html_url,
            conclusion=conclusion,
            completed_at=completed_at,
            steps=steps,
            runner_id=runner_id,
            runner_name=runner_name,
            runner_group_id=runner_group_id,
            runner_group_name=runner_group_name,
        )

        job.additional_properties = d
        return job

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
