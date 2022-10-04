from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionsreRunWorkflowJsonBody")


@attr.s(auto_attribs=True)
class ActionsreRunWorkflowJsonBody:
    """
    Attributes:
        enable_debug_logging (Union[Unset, bool]): Whether to enable debug logging for the re-run.
    """

    enable_debug_logging: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable_debug_logging = self.enable_debug_logging

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_debug_logging is not UNSET:
            field_dict["enable_debug_logging"] = enable_debug_logging

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable_debug_logging = d.pop("enable_debug_logging", UNSET)

        actionsre_run_workflow_json_body = cls(
            enable_debug_logging=enable_debug_logging,
        )

        actionsre_run_workflow_json_body.additional_properties = d
        return actionsre_run_workflow_json_body

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
