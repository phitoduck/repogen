from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reposcreate_commit_status_json_body_state import ReposcreateCommitStatusJsonBodyState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateCommitStatusJsonBody")


@attr.s(auto_attribs=True)
class ReposcreateCommitStatusJsonBody:
    """
    Attributes:
        state (ReposcreateCommitStatusJsonBodyState): The state of the status.
        target_url (Union[Unset, None, str]): The target URL to associate with this status. This URL will be linked from
            the GitHub UI to allow users to easily see the source of the status.
            For example, if your continuous integration system is posting build status, you would want to provide the deep
            link for the build output for this specific SHA:
            `http://ci.example.com/user/repo/build/sha`
        description (Union[Unset, None, str]): A short description of the status.
        context (Union[Unset, str]): A string label to differentiate this status from the status of other systems. This
            field is case-insensitive. Default: 'default'.
    """

    state: ReposcreateCommitStatusJsonBodyState
    target_url: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    context: Union[Unset, str] = "default"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state.value

        target_url = self.target_url
        description = self.description
        context = self.context

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if target_url is not UNSET:
            field_dict["target_url"] = target_url
        if description is not UNSET:
            field_dict["description"] = description
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state = ReposcreateCommitStatusJsonBodyState(d.pop("state"))

        target_url = d.pop("target_url", UNSET)

        description = d.pop("description", UNSET)

        context = d.pop("context", UNSET)

        reposcreate_commit_status_json_body = cls(
            state=state,
            target_url=target_url,
            description=description,
            context=context,
        )

        reposcreate_commit_status_json_body.additional_properties = d
        return reposcreate_commit_status_json_body

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
