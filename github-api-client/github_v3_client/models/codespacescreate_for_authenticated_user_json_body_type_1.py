from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.codespacescreate_for_authenticated_user_json_body_type_1_pull_request import (
    CodespacescreateForAuthenticatedUserJsonBodyType1PullRequest,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodespacescreateForAuthenticatedUserJsonBodyType1")


@attr.s(auto_attribs=True)
class CodespacescreateForAuthenticatedUserJsonBodyType1:
    """
    Attributes:
        pull_request (CodespacescreateForAuthenticatedUserJsonBodyType1PullRequest): Pull request number for this
            codespace
        location (Union[Unset, str]): Location for this codespace. Assigned by IP if not provided
        machine (Union[Unset, str]): Machine type to use for this codespace
        devcontainer_path (Union[Unset, str]): Path to devcontainer.json config to use for this codespace
        working_directory (Union[Unset, str]): Working directory for this codespace
        idle_timeout_minutes (Union[Unset, int]): Time in minutes before codespace stops from inactivity
    """

    pull_request: CodespacescreateForAuthenticatedUserJsonBodyType1PullRequest
    location: Union[Unset, str] = UNSET
    machine: Union[Unset, str] = UNSET
    devcontainer_path: Union[Unset, str] = UNSET
    working_directory: Union[Unset, str] = UNSET
    idle_timeout_minutes: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pull_request = self.pull_request.to_dict()

        location = self.location
        machine = self.machine
        devcontainer_path = self.devcontainer_path
        working_directory = self.working_directory
        idle_timeout_minutes = self.idle_timeout_minutes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pull_request": pull_request,
            }
        )
        if location is not UNSET:
            field_dict["location"] = location
        if machine is not UNSET:
            field_dict["machine"] = machine
        if devcontainer_path is not UNSET:
            field_dict["devcontainer_path"] = devcontainer_path
        if working_directory is not UNSET:
            field_dict["working_directory"] = working_directory
        if idle_timeout_minutes is not UNSET:
            field_dict["idle_timeout_minutes"] = idle_timeout_minutes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pull_request = CodespacescreateForAuthenticatedUserJsonBodyType1PullRequest.from_dict(d.pop("pull_request"))

        location = d.pop("location", UNSET)

        machine = d.pop("machine", UNSET)

        devcontainer_path = d.pop("devcontainer_path", UNSET)

        working_directory = d.pop("working_directory", UNSET)

        idle_timeout_minutes = d.pop("idle_timeout_minutes", UNSET)

        codespacescreate_for_authenticated_user_json_body_type_1 = cls(
            pull_request=pull_request,
            location=location,
            machine=machine,
            devcontainer_path=devcontainer_path,
            working_directory=working_directory,
            idle_timeout_minutes=idle_timeout_minutes,
        )

        codespacescreate_for_authenticated_user_json_body_type_1.additional_properties = d
        return codespacescreate_for_authenticated_user_json_body_type_1

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
