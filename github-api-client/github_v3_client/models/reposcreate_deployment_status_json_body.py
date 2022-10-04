from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reposcreate_deployment_status_json_body_environment import ReposcreateDeploymentStatusJsonBodyEnvironment
from ..models.reposcreate_deployment_status_json_body_state import ReposcreateDeploymentStatusJsonBodyState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateDeploymentStatusJsonBody")


@attr.s(auto_attribs=True)
class ReposcreateDeploymentStatusJsonBody:
    """
    Attributes:
        state (ReposcreateDeploymentStatusJsonBodyState): The state of the status. When you set a transient deployment
            to `inactive`, the deployment will be shown as `destroyed` in GitHub.
        target_url (Union[Unset, str]): The target URL to associate with this status. This URL should contain output to
            keep the user updated while the task is running or serve as historical information for what happened in the
            deployment. **Note:** It's recommended to use the `log_url` parameter, which replaces `target_url`. Default: ''.
        log_url (Union[Unset, str]): The full URL of the deployment's output. This parameter replaces `target_url`. We
            will continue to accept `target_url` to support legacy uses, but we recommend replacing `target_url` with
            `log_url`. Setting `log_url` will automatically set `target_url` to the same value. Default: `""` Default: ''.
        description (Union[Unset, str]): A short description of the status. The maximum description length is 140
            characters. Default: ''.
        environment (Union[Unset, ReposcreateDeploymentStatusJsonBodyEnvironment]): Name for the target deployment
            environment, which can be changed when setting a deploy status. For example, `production`, `staging`, or `qa`.
        environment_url (Union[Unset, str]): Sets the URL for accessing your environment. Default: `""` Default: ''.
        auto_inactive (Union[Unset, bool]): Adds a new `inactive` status to all prior non-transient, non-production
            environment deployments with the same repository and `environment` name as the created status's deployment. An
            `inactive` status is only added to deployments that had a `success` state. Default: `true`
    """

    state: ReposcreateDeploymentStatusJsonBodyState
    target_url: Union[Unset, str] = ""
    log_url: Union[Unset, str] = ""
    description: Union[Unset, str] = ""
    environment: Union[Unset, ReposcreateDeploymentStatusJsonBodyEnvironment] = UNSET
    environment_url: Union[Unset, str] = ""
    auto_inactive: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state.value

        target_url = self.target_url
        log_url = self.log_url
        description = self.description
        environment: Union[Unset, str] = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value

        environment_url = self.environment_url
        auto_inactive = self.auto_inactive

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if target_url is not UNSET:
            field_dict["target_url"] = target_url
        if log_url is not UNSET:
            field_dict["log_url"] = log_url
        if description is not UNSET:
            field_dict["description"] = description
        if environment is not UNSET:
            field_dict["environment"] = environment
        if environment_url is not UNSET:
            field_dict["environment_url"] = environment_url
        if auto_inactive is not UNSET:
            field_dict["auto_inactive"] = auto_inactive

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state = ReposcreateDeploymentStatusJsonBodyState(d.pop("state"))

        target_url = d.pop("target_url", UNSET)

        log_url = d.pop("log_url", UNSET)

        description = d.pop("description", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, ReposcreateDeploymentStatusJsonBodyEnvironment]
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = ReposcreateDeploymentStatusJsonBodyEnvironment(_environment)

        environment_url = d.pop("environment_url", UNSET)

        auto_inactive = d.pop("auto_inactive", UNSET)

        reposcreate_deployment_status_json_body = cls(
            state=state,
            target_url=target_url,
            log_url=log_url,
            description=description,
            environment=environment,
            environment_url=environment_url,
            auto_inactive=auto_inactive,
        )

        reposcreate_deployment_status_json_body.additional_properties = d
        return reposcreate_deployment_status_json_body

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
