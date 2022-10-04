import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.job_steps_item_status import JobStepsItemStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobStepsItem")


@attr.s(auto_attribs=True)
class JobStepsItem:
    """
    Attributes:
        status (JobStepsItemStatus): The phase of the lifecycle that the job is currently in. Example: queued.
        name (str): The name of the job. Example: test-coverage.
        number (int):  Example: 1.
        conclusion (Optional[str]): The outcome of the job. Example: success.
        started_at (Union[Unset, None, datetime.datetime]): The time that the step started, in ISO 8601 format. Example:
            2019-08-08T08:00:00-07:00.
        completed_at (Union[Unset, None, datetime.datetime]): The time that the job finished, in ISO 8601 format.
            Example: 2019-08-08T08:00:00-07:00.
    """

    status: JobStepsItemStatus
    name: str
    number: int
    conclusion: Optional[str]
    started_at: Union[Unset, None, datetime.datetime] = UNSET
    completed_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        name = self.name
        number = self.number
        conclusion = self.conclusion
        started_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat() if self.started_at else None

        completed_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat() if self.completed_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "name": name,
                "number": number,
                "conclusion": conclusion,
            }
        )
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = JobStepsItemStatus(d.pop("status"))

        name = d.pop("name")

        number = d.pop("number")

        conclusion = d.pop("conclusion")

        _started_at = d.pop("started_at", UNSET)
        started_at: Union[Unset, None, datetime.datetime]
        if _started_at is None:
            started_at = None
        elif isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, None, datetime.datetime]
        if _completed_at is None:
            completed_at = None
        elif isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        job_steps_item = cls(
            status=status,
            name=name,
            number=number,
            conclusion=conclusion,
            started_at=started_at,
            completed_at=completed_at,
        )

        job_steps_item.additional_properties = d
        return job_steps_item

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
