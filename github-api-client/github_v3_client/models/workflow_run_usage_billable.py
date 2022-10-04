from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.workflow_run_usage_billable_macos import WorkflowRunUsageBillableMACOS
from ..models.workflow_run_usage_billable_ubuntu import WorkflowRunUsageBillableUBUNTU
from ..models.workflow_run_usage_billable_windows import WorkflowRunUsageBillableWINDOWS
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowRunUsageBillable")


@attr.s(auto_attribs=True)
class WorkflowRunUsageBillable:
    """
    Attributes:
        ubuntu (Union[Unset, WorkflowRunUsageBillableUBUNTU]):
        macos (Union[Unset, WorkflowRunUsageBillableMACOS]):
        windows (Union[Unset, WorkflowRunUsageBillableWINDOWS]):
    """

    ubuntu: Union[Unset, WorkflowRunUsageBillableUBUNTU] = UNSET
    macos: Union[Unset, WorkflowRunUsageBillableMACOS] = UNSET
    windows: Union[Unset, WorkflowRunUsageBillableWINDOWS] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ubuntu: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ubuntu, Unset):
            ubuntu = self.ubuntu.to_dict()

        macos: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.macos, Unset):
            macos = self.macos.to_dict()

        windows: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.windows, Unset):
            windows = self.windows.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ubuntu is not UNSET:
            field_dict["UBUNTU"] = ubuntu
        if macos is not UNSET:
            field_dict["MACOS"] = macos
        if windows is not UNSET:
            field_dict["WINDOWS"] = windows

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _ubuntu = d.pop("UBUNTU", UNSET)
        ubuntu: Union[Unset, WorkflowRunUsageBillableUBUNTU]
        if isinstance(_ubuntu, Unset):
            ubuntu = UNSET
        else:
            ubuntu = WorkflowRunUsageBillableUBUNTU.from_dict(_ubuntu)

        _macos = d.pop("MACOS", UNSET)
        macos: Union[Unset, WorkflowRunUsageBillableMACOS]
        if isinstance(_macos, Unset):
            macos = UNSET
        else:
            macos = WorkflowRunUsageBillableMACOS.from_dict(_macos)

        _windows = d.pop("WINDOWS", UNSET)
        windows: Union[Unset, WorkflowRunUsageBillableWINDOWS]
        if isinstance(_windows, Unset):
            windows = UNSET
        else:
            windows = WorkflowRunUsageBillableWINDOWS.from_dict(_windows)

        workflow_run_usage_billable = cls(
            ubuntu=ubuntu,
            macos=macos,
            windows=windows,
        )

        workflow_run_usage_billable.additional_properties = d
        return workflow_run_usage_billable

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
