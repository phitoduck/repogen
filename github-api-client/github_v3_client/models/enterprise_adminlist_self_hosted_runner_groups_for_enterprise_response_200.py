from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.runner_groups_enterprise import RunnerGroupsEnterprise

T = TypeVar("T", bound="EnterpriseAdminlistSelfHostedRunnerGroupsForEnterpriseResponse200")


@attr.s(auto_attribs=True)
class EnterpriseAdminlistSelfHostedRunnerGroupsForEnterpriseResponse200:
    """
    Attributes:
        total_count (float):
        runner_groups (List[RunnerGroupsEnterprise]):
    """

    total_count: float
    runner_groups: List[RunnerGroupsEnterprise]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        runner_groups = []
        for runner_groups_item_data in self.runner_groups:
            runner_groups_item = runner_groups_item_data.to_dict()

            runner_groups.append(runner_groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_count": total_count,
                "runner_groups": runner_groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_count = d.pop("total_count")

        runner_groups = []
        _runner_groups = d.pop("runner_groups")
        for runner_groups_item_data in _runner_groups:
            runner_groups_item = RunnerGroupsEnterprise.from_dict(runner_groups_item_data)

            runner_groups.append(runner_groups_item)

        enterprise_adminlist_self_hosted_runner_groups_for_enterprise_response_200 = cls(
            total_count=total_count,
            runner_groups=runner_groups,
        )

        enterprise_adminlist_self_hosted_runner_groups_for_enterprise_response_200.additional_properties = d
        return enterprise_adminlist_self_hosted_runner_groups_for_enterprise_response_200

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
