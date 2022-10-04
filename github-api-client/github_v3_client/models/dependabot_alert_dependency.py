from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.dependabot_alert_dependency_scope import DependabotAlertDependencyScope
from ..models.dependabot_alert_package import DependabotAlertPackage
from ..types import UNSET, Unset

T = TypeVar("T", bound="DependabotAlertDependency")


@attr.s(auto_attribs=True)
class DependabotAlertDependency:
    """Details for the vulnerable dependency.

    Attributes:
        package (Union[Unset, DependabotAlertPackage]): Details for the vulnerable package.
        manifest_path (Union[Unset, str]): The full path to the dependency manifest file, relative to the root of the
            repository.
        scope (Union[Unset, None, DependabotAlertDependencyScope]): The execution scope of the vulnerable dependency.
    """

    package: Union[Unset, DependabotAlertPackage] = UNSET
    manifest_path: Union[Unset, str] = UNSET
    scope: Union[Unset, None, DependabotAlertDependencyScope] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.package, Unset):
            package = self.package.to_dict()

        manifest_path = self.manifest_path
        scope: Union[Unset, None, str] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value if self.scope else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package is not UNSET:
            field_dict["package"] = package
        if manifest_path is not UNSET:
            field_dict["manifest_path"] = manifest_path
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _package = d.pop("package", UNSET)
        package: Union[Unset, DependabotAlertPackage]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = DependabotAlertPackage.from_dict(_package)

        manifest_path = d.pop("manifest_path", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: Union[Unset, None, DependabotAlertDependencyScope]
        if _scope is None:
            scope = None
        elif isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = DependabotAlertDependencyScope(_scope)

        dependabot_alert_dependency = cls(
            package=package,
            manifest_path=manifest_path,
            scope=scope,
        )

        dependabot_alert_dependency.additional_properties = d
        return dependabot_alert_dependency

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
