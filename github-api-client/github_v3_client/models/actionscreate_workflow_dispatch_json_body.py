from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.actionscreate_workflow_dispatch_json_body_inputs import ActionscreateWorkflowDispatchJsonBodyInputs
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionscreateWorkflowDispatchJsonBody")


@attr.s(auto_attribs=True)
class ActionscreateWorkflowDispatchJsonBody:
    """
    Attributes:
        ref (str): The git reference for the workflow. The reference can be a branch or tag name.
        inputs (Union[Unset, ActionscreateWorkflowDispatchJsonBodyInputs]): Input keys and values configured in the
            workflow file. The maximum number of properties is 10. Any default properties configured in the workflow file
            will be used when `inputs` are omitted.
    """

    ref: str
    inputs: Union[Unset, ActionscreateWorkflowDispatchJsonBodyInputs] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref
        inputs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ref": ref,
            }
        )
        if inputs is not UNSET:
            field_dict["inputs"] = inputs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ref = d.pop("ref")

        _inputs = d.pop("inputs", UNSET)
        inputs: Union[Unset, ActionscreateWorkflowDispatchJsonBodyInputs]
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = ActionscreateWorkflowDispatchJsonBodyInputs.from_dict(_inputs)

        actionscreate_workflow_dispatch_json_body = cls(
            ref=ref,
            inputs=inputs,
        )

        actionscreate_workflow_dispatch_json_body.additional_properties = d
        return actionscreate_workflow_dispatch_json_body

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
