from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.dependency_graph_diff_item_change_type import DependencyGraphDiffItemChangeType
from ..models.dependency_graph_diff_item_scope import DependencyGraphDiffItemScope
from ..models.dependency_graph_diff_item_vulnerabilities_item import DependencyGraphDiffItemVulnerabilitiesItem

T = TypeVar("T", bound="DependencyGraphDiffItem")


@attr.s(auto_attribs=True)
class DependencyGraphDiffItem:
    """
    Attributes:
        change_type (DependencyGraphDiffItemChangeType):
        manifest (str):  Example: path/to/package-lock.json.
        ecosystem (str):  Example: npm.
        name (str):  Example: @actions/core.
        version (str):  Example: 1.0.0.
        vulnerabilities (List[DependencyGraphDiffItemVulnerabilitiesItem]):
        scope (DependencyGraphDiffItemScope): Where the dependency is utilized. `development` means that the dependency
            is only utilized in the development environment. `runtime` means that the dependency is utilized at runtime and
            in the development environment.
        package_url (Optional[str]):  Example: pkg:/npm/%40actions/core@1.1.0.
        license_ (Optional[str]):  Example: MIT.
        source_repository_url (Optional[str]):  Example: https://github.com/github/actions.
    """

    change_type: DependencyGraphDiffItemChangeType
    manifest: str
    ecosystem: str
    name: str
    version: str
    vulnerabilities: List[DependencyGraphDiffItemVulnerabilitiesItem]
    scope: DependencyGraphDiffItemScope
    package_url: Optional[str]
    license_: Optional[str]
    source_repository_url: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        change_type = self.change_type.value

        manifest = self.manifest
        ecosystem = self.ecosystem
        name = self.name
        version = self.version
        vulnerabilities = []
        for vulnerabilities_item_data in self.vulnerabilities:
            vulnerabilities_item = vulnerabilities_item_data.to_dict()

            vulnerabilities.append(vulnerabilities_item)

        scope = self.scope.value

        package_url = self.package_url
        license_ = self.license_
        source_repository_url = self.source_repository_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "change_type": change_type,
                "manifest": manifest,
                "ecosystem": ecosystem,
                "name": name,
                "version": version,
                "vulnerabilities": vulnerabilities,
                "scope": scope,
                "package_url": package_url,
                "license": license_,
                "source_repository_url": source_repository_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        change_type = DependencyGraphDiffItemChangeType(d.pop("change_type"))

        manifest = d.pop("manifest")

        ecosystem = d.pop("ecosystem")

        name = d.pop("name")

        version = d.pop("version")

        vulnerabilities = []
        _vulnerabilities = d.pop("vulnerabilities")
        for vulnerabilities_item_data in _vulnerabilities:
            vulnerabilities_item = DependencyGraphDiffItemVulnerabilitiesItem.from_dict(vulnerabilities_item_data)

            vulnerabilities.append(vulnerabilities_item)

        scope = DependencyGraphDiffItemScope(d.pop("scope"))

        package_url = d.pop("package_url")

        license_ = d.pop("license")

        source_repository_url = d.pop("source_repository_url")

        dependency_graph_diff_item = cls(
            change_type=change_type,
            manifest=manifest,
            ecosystem=ecosystem,
            name=name,
            version=version,
            vulnerabilities=vulnerabilities,
            scope=scope,
            package_url=package_url,
            license_=license_,
            source_repository_url=source_repository_url,
        )

        dependency_graph_diff_item.additional_properties = d
        return dependency_graph_diff_item

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
