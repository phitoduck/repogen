from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CheckssetSuitesPreferencesJsonBodyAutoTriggerChecksItem")


@attr.s(auto_attribs=True)
class CheckssetSuitesPreferencesJsonBodyAutoTriggerChecksItem:
    """
    Attributes:
        app_id (int): The `id` of the GitHub App.
        setting (bool): Set to `true` to enable automatic creation of CheckSuite events upon pushes to the repository,
            or `false` to disable them. Default: True.
    """

    app_id: int
    setting: bool = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_id = self.app_id
        setting = self.setting

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_id": app_id,
                "setting": setting,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        app_id = d.pop("app_id")

        setting = d.pop("setting")

        checksset_suites_preferences_json_body_auto_trigger_checks_item = cls(
            app_id=app_id,
            setting=setting,
        )

        checksset_suites_preferences_json_body_auto_trigger_checks_item.additional_properties = d
        return checksset_suites_preferences_json_body_auto_trigger_checks_item

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
