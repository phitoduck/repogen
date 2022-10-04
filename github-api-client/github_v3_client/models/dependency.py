from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.dependency_relationship import DependencyRelationship
from ..models.dependency_scope import DependencyScope
from ..models.metadata import Metadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="Dependency")


@attr.s(auto_attribs=True)
class Dependency:
    """
    Attributes:
        package_url (Union[Unset, str]): Package-url (PURL) of dependency. See https://github.com/package-url/purl-spec
            for more details. Example: pkg:/npm/%40actions/http-client@1.0.11.
        metadata (Union[Unset, Metadata]): User-defined metadata to store domain-specific information limited to 8 keys
            with scalar values.
        relationship (Union[Unset, DependencyRelationship]): A notation of whether a dependency is requested directly by
            this manifest or is a dependency of another dependency. Example: direct.
        scope (Union[Unset, DependencyScope]): A notation of whether the dependency is required for the primary build
            artifact (runtime) or is only used for development. Future versions of this specification may allow for more
            granular scopes. Example: runtime.
        dependencies (Union[Unset, List[str]]): Array of package-url (PURLs) of direct child dependencies. Example:
            @actions/http-client.
    """

    package_url: Union[Unset, str] = UNSET
    metadata: Union[Unset, Metadata] = UNSET
    relationship: Union[Unset, DependencyRelationship] = UNSET
    scope: Union[Unset, DependencyScope] = UNSET
    dependencies: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        package_url = self.package_url
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        relationship: Union[Unset, str] = UNSET
        if not isinstance(self.relationship, Unset):
            relationship = self.relationship.value

        scope: Union[Unset, str] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        dependencies: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if package_url is not UNSET:
            field_dict["package_url"] = package_url
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if scope is not UNSET:
            field_dict["scope"] = scope
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        package_url = d.pop("package_url", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        _relationship = d.pop("relationship", UNSET)
        relationship: Union[Unset, DependencyRelationship]
        if isinstance(_relationship, Unset):
            relationship = UNSET
        else:
            relationship = DependencyRelationship(_relationship)

        _scope = d.pop("scope", UNSET)
        scope: Union[Unset, DependencyScope]
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = DependencyScope(_scope)

        dependencies = cast(List[str], d.pop("dependencies", UNSET))

        dependency = cls(
            package_url=package_url,
            metadata=metadata,
            relationship=relationship,
            scope=scope,
            dependencies=dependencies,
        )

        return dependency
