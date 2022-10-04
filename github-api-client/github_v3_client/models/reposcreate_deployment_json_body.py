from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.reposcreate_deployment_json_body_payload_type_0 import ReposcreateDeploymentJsonBodyPayloadType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateDeploymentJsonBody")


@attr.s(auto_attribs=True)
class ReposcreateDeploymentJsonBody:
    """
    Attributes:
        ref (str): The ref to deploy. This can be a branch, tag, or SHA.
        task (Union[Unset, str]): Specifies a task to execute (e.g., `deploy` or `deploy:migrations`). Default:
            'deploy'.
        auto_merge (Union[Unset, bool]): Attempts to automatically merge the default branch into the requested ref, if
            it's behind the default branch. Default: True.
        required_contexts (Union[Unset, List[str]]): The [status](https://docs.github.com/rest/commits/statuses)
            contexts to verify against commit status checks. If you omit this parameter, GitHub verifies all unique contexts
            before creating a deployment. To bypass checking entirely, pass an empty array. Defaults to all unique contexts.
        payload (Union[ReposcreateDeploymentJsonBodyPayloadType0, Unset, str]):
        environment (Union[Unset, str]): Name for the target deployment environment (e.g., `production`, `staging`,
            `qa`). Default: 'production'.
        description (Union[Unset, None, str]): Short description of the deployment. Default: ''.
        transient_environment (Union[Unset, bool]): Specifies if the given environment is specific to the deployment and
            will no longer exist at some point in the future. Default: `false`
        production_environment (Union[Unset, bool]): Specifies if the given environment is one that end-users directly
            interact with. Default: `true` when `environment` is `production` and `false` otherwise.
    """

    ref: str
    task: Union[Unset, str] = "deploy"
    auto_merge: Union[Unset, bool] = True
    required_contexts: Union[Unset, List[str]] = UNSET
    payload: Union[ReposcreateDeploymentJsonBodyPayloadType0, Unset, str] = UNSET
    environment: Union[Unset, str] = "production"
    description: Union[Unset, None, str] = ""
    transient_environment: Union[Unset, bool] = False
    production_environment: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref
        task = self.task
        auto_merge = self.auto_merge
        required_contexts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.required_contexts, Unset):
            required_contexts = self.required_contexts

        payload: Union[Dict[str, Any], Unset, str]
        if isinstance(self.payload, Unset):
            payload = UNSET

        elif isinstance(self.payload, ReposcreateDeploymentJsonBodyPayloadType0):
            payload = UNSET
            if not isinstance(self.payload, Unset):
                payload = self.payload.to_dict()

        else:
            payload = self.payload

        environment = self.environment
        description = self.description
        transient_environment = self.transient_environment
        production_environment = self.production_environment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ref": ref,
            }
        )
        if task is not UNSET:
            field_dict["task"] = task
        if auto_merge is not UNSET:
            field_dict["auto_merge"] = auto_merge
        if required_contexts is not UNSET:
            field_dict["required_contexts"] = required_contexts
        if payload is not UNSET:
            field_dict["payload"] = payload
        if environment is not UNSET:
            field_dict["environment"] = environment
        if description is not UNSET:
            field_dict["description"] = description
        if transient_environment is not UNSET:
            field_dict["transient_environment"] = transient_environment
        if production_environment is not UNSET:
            field_dict["production_environment"] = production_environment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ref = d.pop("ref")

        task = d.pop("task", UNSET)

        auto_merge = d.pop("auto_merge", UNSET)

        required_contexts = cast(List[str], d.pop("required_contexts", UNSET))

        def _parse_payload(data: object) -> Union[ReposcreateDeploymentJsonBodyPayloadType0, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _payload_type_0 = data
                payload_type_0: Union[Unset, ReposcreateDeploymentJsonBodyPayloadType0]
                if isinstance(_payload_type_0, Unset):
                    payload_type_0 = UNSET
                else:
                    payload_type_0 = ReposcreateDeploymentJsonBodyPayloadType0.from_dict(_payload_type_0)

                return payload_type_0
            except:  # noqa: E722
                pass
            return cast(Union[ReposcreateDeploymentJsonBodyPayloadType0, Unset, str], data)

        payload = _parse_payload(d.pop("payload", UNSET))

        environment = d.pop("environment", UNSET)

        description = d.pop("description", UNSET)

        transient_environment = d.pop("transient_environment", UNSET)

        production_environment = d.pop("production_environment", UNSET)

        reposcreate_deployment_json_body = cls(
            ref=ref,
            task=task,
            auto_merge=auto_merge,
            required_contexts=required_contexts,
            payload=payload,
            environment=environment,
            description=description,
            transient_environment=transient_environment,
            production_environment=production_environment,
        )

        reposcreate_deployment_json_body.additional_properties = d
        return reposcreate_deployment_json_body

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
