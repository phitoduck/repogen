from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.self_hosted_runners import SelfHostedRunners
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnterpriseAdminlistSelfHostedRunnersForEnterpriseResponse200")


@attr.s(auto_attribs=True)
class EnterpriseAdminlistSelfHostedRunnersForEnterpriseResponse200:
    """
    Attributes:
        total_count (Union[Unset, float]):
        runners (Union[Unset, List[SelfHostedRunners]]):
    """

    total_count: Union[Unset, float] = UNSET
    runners: Union[Unset, List[SelfHostedRunners]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        runners: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.runners, Unset):
            runners = []
            for runners_item_data in self.runners:
                runners_item = runners_item_data.to_dict()

                runners.append(runners_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if runners is not UNSET:
            field_dict["runners"] = runners

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_count = d.pop("total_count", UNSET)

        runners = []
        _runners = d.pop("runners", UNSET)
        for runners_item_data in _runners or []:
            runners_item = SelfHostedRunners.from_dict(runners_item_data)

            runners.append(runners_item)

        enterprise_adminlist_self_hosted_runners_for_enterprise_response_200 = cls(
            total_count=total_count,
            runners=runners,
        )

        enterprise_adminlist_self_hosted_runners_for_enterprise_response_200.additional_properties = d
        return enterprise_adminlist_self_hosted_runners_for_enterprise_response_200

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
