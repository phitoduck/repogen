from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="ActionssetRepoAccessToSelfHostedRunnerGroupInOrgJsonBody")


@attr.s(auto_attribs=True)
class ActionssetRepoAccessToSelfHostedRunnerGroupInOrgJsonBody:
    """
    Attributes:
        selected_repository_ids (List[int]): List of repository IDs that can access the runner group.
    """

    selected_repository_ids: List[int]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        selected_repository_ids = self.selected_repository_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selected_repository_ids": selected_repository_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        selected_repository_ids = cast(List[int], d.pop("selected_repository_ids"))

        actionsset_repo_access_to_self_hosted_runner_group_in_org_json_body = cls(
            selected_repository_ids=selected_repository_ids,
        )

        actionsset_repo_access_to_self_hosted_runner_group_in_org_json_body.additional_properties = d
        return actionsset_repo_access_to_self_hosted_runner_group_in_org_json_body

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
