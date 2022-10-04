from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.actionsupdate_self_hosted_runner_group_for_org_json_body_visibility import (
    ActionsupdateSelfHostedRunnerGroupForOrgJsonBodyVisibility,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionsupdateSelfHostedRunnerGroupForOrgJsonBody")


@attr.s(auto_attribs=True)
class ActionsupdateSelfHostedRunnerGroupForOrgJsonBody:
    """
    Attributes:
        name (str): Name of the runner group.
        visibility (Union[Unset, ActionsupdateSelfHostedRunnerGroupForOrgJsonBodyVisibility]): Visibility of a runner
            group. You can select all repositories, select individual repositories, or all private repositories.
        allows_public_repositories (Union[Unset, bool]): Whether the runner group can be used by `public` repositories.
        restricted_to_workflows (Union[Unset, bool]): If `true`, the runner group will be restricted to running only the
            workflows specified in the `selected_workflows` array.
        selected_workflows (Union[Unset, List[str]]): List of workflows the runner group should be allowed to run. This
            setting will be ignored unless `restricted_to_workflows` is set to `true`.
    """

    name: str
    visibility: Union[Unset, ActionsupdateSelfHostedRunnerGroupForOrgJsonBodyVisibility] = UNSET
    allows_public_repositories: Union[Unset, bool] = False
    restricted_to_workflows: Union[Unset, bool] = False
    selected_workflows: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        allows_public_repositories = self.allows_public_repositories
        restricted_to_workflows = self.restricted_to_workflows
        selected_workflows: Union[Unset, List[str]] = UNSET
        if not isinstance(self.selected_workflows, Unset):
            selected_workflows = self.selected_workflows

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if allows_public_repositories is not UNSET:
            field_dict["allows_public_repositories"] = allows_public_repositories
        if restricted_to_workflows is not UNSET:
            field_dict["restricted_to_workflows"] = restricted_to_workflows
        if selected_workflows is not UNSET:
            field_dict["selected_workflows"] = selected_workflows

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, ActionsupdateSelfHostedRunnerGroupForOrgJsonBodyVisibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = ActionsupdateSelfHostedRunnerGroupForOrgJsonBodyVisibility(_visibility)

        allows_public_repositories = d.pop("allows_public_repositories", UNSET)

        restricted_to_workflows = d.pop("restricted_to_workflows", UNSET)

        selected_workflows = cast(List[str], d.pop("selected_workflows", UNSET))

        actionsupdate_self_hosted_runner_group_for_org_json_body = cls(
            name=name,
            visibility=visibility,
            allows_public_repositories=allows_public_repositories,
            restricted_to_workflows=restricted_to_workflows,
            selected_workflows=selected_workflows,
        )

        actionsupdate_self_hosted_runner_group_for_org_json_body.additional_properties = d
        return actionsupdate_self_hosted_runner_group_for_org_json_body

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
