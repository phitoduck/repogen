from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RunnerGroupsEnterprise")


@attr.s(auto_attribs=True)
class RunnerGroupsEnterprise:
    """
    Attributes:
        id (float):
        name (str):
        visibility (str):
        default (bool):
        runners_url (str):
        allows_public_repositories (bool):
        selected_organizations_url (Union[Unset, str]):
        workflow_restrictions_read_only (Union[Unset, bool]): If `true`, the `restricted_to_workflows` and
            `selected_workflows` fields cannot be modified.
        restricted_to_workflows (Union[Unset, bool]): If `true`, the runner group will be restricted to running only the
            workflows specified in the `selected_workflows` array.
        selected_workflows (Union[Unset, List[str]]): List of workflows the runner group should be allowed to run. This
            setting will be ignored unless `restricted_to_workflows` is set to `true`.
    """

    id: float
    name: str
    visibility: str
    default: bool
    runners_url: str
    allows_public_repositories: bool
    selected_organizations_url: Union[Unset, str] = UNSET
    workflow_restrictions_read_only: Union[Unset, bool] = False
    restricted_to_workflows: Union[Unset, bool] = False
    selected_workflows: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        visibility = self.visibility
        default = self.default
        runners_url = self.runners_url
        allows_public_repositories = self.allows_public_repositories
        selected_organizations_url = self.selected_organizations_url
        workflow_restrictions_read_only = self.workflow_restrictions_read_only
        restricted_to_workflows = self.restricted_to_workflows
        selected_workflows: Union[Unset, List[str]] = UNSET
        if not isinstance(self.selected_workflows, Unset):
            selected_workflows = self.selected_workflows

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "visibility": visibility,
                "default": default,
                "runners_url": runners_url,
                "allows_public_repositories": allows_public_repositories,
            }
        )
        if selected_organizations_url is not UNSET:
            field_dict["selected_organizations_url"] = selected_organizations_url
        if workflow_restrictions_read_only is not UNSET:
            field_dict["workflow_restrictions_read_only"] = workflow_restrictions_read_only
        if restricted_to_workflows is not UNSET:
            field_dict["restricted_to_workflows"] = restricted_to_workflows
        if selected_workflows is not UNSET:
            field_dict["selected_workflows"] = selected_workflows

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        visibility = d.pop("visibility")

        default = d.pop("default")

        runners_url = d.pop("runners_url")

        allows_public_repositories = d.pop("allows_public_repositories")

        selected_organizations_url = d.pop("selected_organizations_url", UNSET)

        workflow_restrictions_read_only = d.pop("workflow_restrictions_read_only", UNSET)

        restricted_to_workflows = d.pop("restricted_to_workflows", UNSET)

        selected_workflows = cast(List[str], d.pop("selected_workflows", UNSET))

        runner_groups_enterprise = cls(
            id=id,
            name=name,
            visibility=visibility,
            default=default,
            runners_url=runners_url,
            allows_public_repositories=allows_public_repositories,
            selected_organizations_url=selected_organizations_url,
            workflow_restrictions_read_only=workflow_restrictions_read_only,
            restricted_to_workflows=restricted_to_workflows,
            selected_workflows=selected_workflows,
        )

        runner_groups_enterprise.additional_properties = d
        return runner_groups_enterprise

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
