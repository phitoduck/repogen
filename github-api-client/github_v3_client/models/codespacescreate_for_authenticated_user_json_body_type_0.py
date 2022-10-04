from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodespacescreateForAuthenticatedUserJsonBodyType0")


@attr.s(auto_attribs=True)
class CodespacescreateForAuthenticatedUserJsonBodyType0:
    """
    Attributes:
        repository_id (int): Repository id for this codespace
        ref (Union[Unset, str]): Git ref (typically a branch name) for this codespace
        location (Union[Unset, str]): Location for this codespace. Assigned by IP if not provided
        client_ip (Union[Unset, str]): IP for location auto-detection when proxying a request
        machine (Union[Unset, str]): Machine type to use for this codespace
        devcontainer_path (Union[Unset, str]): Path to devcontainer.json config to use for this codespace
        multi_repo_permissions_opt_out (Union[Unset, bool]): Whether to authorize requested permissions from
            devcontainer.json
        working_directory (Union[Unset, str]): Working directory for this codespace
        idle_timeout_minutes (Union[Unset, int]): Time in minutes before codespace stops from inactivity
        display_name (Union[Unset, str]): Display name for this codespace
        retention_period_minutes (Union[Unset, int]): Duration in minutes after codespace has gone idle in which it will
            be deleted. Must be integer minutes between 0 and 43200 (30 days).
    """

    repository_id: int
    ref: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    client_ip: Union[Unset, str] = UNSET
    machine: Union[Unset, str] = UNSET
    devcontainer_path: Union[Unset, str] = UNSET
    multi_repo_permissions_opt_out: Union[Unset, bool] = UNSET
    working_directory: Union[Unset, str] = UNSET
    idle_timeout_minutes: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    retention_period_minutes: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repository_id = self.repository_id
        ref = self.ref
        location = self.location
        client_ip = self.client_ip
        machine = self.machine
        devcontainer_path = self.devcontainer_path
        multi_repo_permissions_opt_out = self.multi_repo_permissions_opt_out
        working_directory = self.working_directory
        idle_timeout_minutes = self.idle_timeout_minutes
        display_name = self.display_name
        retention_period_minutes = self.retention_period_minutes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repository_id": repository_id,
            }
        )
        if ref is not UNSET:
            field_dict["ref"] = ref
        if location is not UNSET:
            field_dict["location"] = location
        if client_ip is not UNSET:
            field_dict["client_ip"] = client_ip
        if machine is not UNSET:
            field_dict["machine"] = machine
        if devcontainer_path is not UNSET:
            field_dict["devcontainer_path"] = devcontainer_path
        if multi_repo_permissions_opt_out is not UNSET:
            field_dict["multi_repo_permissions_opt_out"] = multi_repo_permissions_opt_out
        if working_directory is not UNSET:
            field_dict["working_directory"] = working_directory
        if idle_timeout_minutes is not UNSET:
            field_dict["idle_timeout_minutes"] = idle_timeout_minutes
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if retention_period_minutes is not UNSET:
            field_dict["retention_period_minutes"] = retention_period_minutes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        repository_id = d.pop("repository_id")

        ref = d.pop("ref", UNSET)

        location = d.pop("location", UNSET)

        client_ip = d.pop("client_ip", UNSET)

        machine = d.pop("machine", UNSET)

        devcontainer_path = d.pop("devcontainer_path", UNSET)

        multi_repo_permissions_opt_out = d.pop("multi_repo_permissions_opt_out", UNSET)

        working_directory = d.pop("working_directory", UNSET)

        idle_timeout_minutes = d.pop("idle_timeout_minutes", UNSET)

        display_name = d.pop("display_name", UNSET)

        retention_period_minutes = d.pop("retention_period_minutes", UNSET)

        codespacescreate_for_authenticated_user_json_body_type_0 = cls(
            repository_id=repository_id,
            ref=ref,
            location=location,
            client_ip=client_ip,
            machine=machine,
            devcontainer_path=devcontainer_path,
            multi_repo_permissions_opt_out=multi_repo_permissions_opt_out,
            working_directory=working_directory,
            idle_timeout_minutes=idle_timeout_minutes,
            display_name=display_name,
            retention_period_minutes=retention_period_minutes,
        )

        codespacescreate_for_authenticated_user_json_body_type_0.additional_properties = d
        return codespacescreate_for_authenticated_user_json_body_type_0

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
