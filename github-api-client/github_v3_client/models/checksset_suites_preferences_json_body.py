from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.checksset_suites_preferences_json_body_auto_trigger_checks_item import (
    CheckssetSuitesPreferencesJsonBodyAutoTriggerChecksItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckssetSuitesPreferencesJsonBody")


@attr.s(auto_attribs=True)
class CheckssetSuitesPreferencesJsonBody:
    """
    Attributes:
        auto_trigger_checks (Union[Unset, List[CheckssetSuitesPreferencesJsonBodyAutoTriggerChecksItem]]): Enables or
            disables automatic creation of CheckSuite events upon pushes to the repository. Enabled by default. See the
            [`auto_trigger_checks` object](https://docs.github.com/rest/reference/checks#auto_trigger_checks-object)
            description for details.
    """

    auto_trigger_checks: Union[Unset, List[CheckssetSuitesPreferencesJsonBodyAutoTriggerChecksItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auto_trigger_checks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.auto_trigger_checks, Unset):
            auto_trigger_checks = []
            for auto_trigger_checks_item_data in self.auto_trigger_checks:
                auto_trigger_checks_item = auto_trigger_checks_item_data.to_dict()

                auto_trigger_checks.append(auto_trigger_checks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_trigger_checks is not UNSET:
            field_dict["auto_trigger_checks"] = auto_trigger_checks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auto_trigger_checks = []
        _auto_trigger_checks = d.pop("auto_trigger_checks", UNSET)
        for auto_trigger_checks_item_data in _auto_trigger_checks or []:
            auto_trigger_checks_item = CheckssetSuitesPreferencesJsonBodyAutoTriggerChecksItem.from_dict(
                auto_trigger_checks_item_data
            )

            auto_trigger_checks.append(auto_trigger_checks_item)

        checksset_suites_preferences_json_body = cls(
            auto_trigger_checks=auto_trigger_checks,
        )

        checksset_suites_preferences_json_body.additional_properties = d
        return checksset_suites_preferences_json_body

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
