from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="ReposremoveAppAccessRestrictionsJsonBodyType0")


@attr.s(auto_attribs=True)
class ReposremoveAppAccessRestrictionsJsonBodyType0:
    """
    Example:
        {'apps': ['my-app']}

    Attributes:
        apps (List[str]): apps parameter
    """

    apps: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        apps = self.apps

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apps": apps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        apps = cast(List[str], d.pop("apps"))

        reposremove_app_access_restrictions_json_body_type_0 = cls(
            apps=apps,
        )

        reposremove_app_access_restrictions_json_body_type_0.additional_properties = d
        return reposremove_app_access_restrictions_json_body_type_0

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
