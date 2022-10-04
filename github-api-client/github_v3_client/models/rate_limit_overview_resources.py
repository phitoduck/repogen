from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rate_limit import RateLimit
from ..types import UNSET, Unset

T = TypeVar("T", bound="RateLimitOverviewResources")


@attr.s(auto_attribs=True)
class RateLimitOverviewResources:
    """
    Attributes:
        core (RateLimit):
        search (RateLimit):
        graphql (Union[Unset, RateLimit]):
        source_import (Union[Unset, RateLimit]):
        integration_manifest (Union[Unset, RateLimit]):
        code_scanning_upload (Union[Unset, RateLimit]):
        actions_runner_registration (Union[Unset, RateLimit]):
        scim (Union[Unset, RateLimit]):
        dependency_snapshots (Union[Unset, RateLimit]):
    """

    core: RateLimit
    search: RateLimit
    graphql: Union[Unset, RateLimit] = UNSET
    source_import: Union[Unset, RateLimit] = UNSET
    integration_manifest: Union[Unset, RateLimit] = UNSET
    code_scanning_upload: Union[Unset, RateLimit] = UNSET
    actions_runner_registration: Union[Unset, RateLimit] = UNSET
    scim: Union[Unset, RateLimit] = UNSET
    dependency_snapshots: Union[Unset, RateLimit] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        core = self.core.to_dict()

        search = self.search.to_dict()

        graphql: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.graphql, Unset):
            graphql = self.graphql.to_dict()

        source_import: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source_import, Unset):
            source_import = self.source_import.to_dict()

        integration_manifest: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.integration_manifest, Unset):
            integration_manifest = self.integration_manifest.to_dict()

        code_scanning_upload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.code_scanning_upload, Unset):
            code_scanning_upload = self.code_scanning_upload.to_dict()

        actions_runner_registration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actions_runner_registration, Unset):
            actions_runner_registration = self.actions_runner_registration.to_dict()

        scim: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scim, Unset):
            scim = self.scim.to_dict()

        dependency_snapshots: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dependency_snapshots, Unset):
            dependency_snapshots = self.dependency_snapshots.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "core": core,
                "search": search,
            }
        )
        if graphql is not UNSET:
            field_dict["graphql"] = graphql
        if source_import is not UNSET:
            field_dict["source_import"] = source_import
        if integration_manifest is not UNSET:
            field_dict["integration_manifest"] = integration_manifest
        if code_scanning_upload is not UNSET:
            field_dict["code_scanning_upload"] = code_scanning_upload
        if actions_runner_registration is not UNSET:
            field_dict["actions_runner_registration"] = actions_runner_registration
        if scim is not UNSET:
            field_dict["scim"] = scim
        if dependency_snapshots is not UNSET:
            field_dict["dependency_snapshots"] = dependency_snapshots

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        core = RateLimit.from_dict(d.pop("core"))

        search = RateLimit.from_dict(d.pop("search"))

        _graphql = d.pop("graphql", UNSET)
        graphql: Union[Unset, RateLimit]
        if isinstance(_graphql, Unset):
            graphql = UNSET
        else:
            graphql = RateLimit.from_dict(_graphql)

        _source_import = d.pop("source_import", UNSET)
        source_import: Union[Unset, RateLimit]
        if isinstance(_source_import, Unset):
            source_import = UNSET
        else:
            source_import = RateLimit.from_dict(_source_import)

        _integration_manifest = d.pop("integration_manifest", UNSET)
        integration_manifest: Union[Unset, RateLimit]
        if isinstance(_integration_manifest, Unset):
            integration_manifest = UNSET
        else:
            integration_manifest = RateLimit.from_dict(_integration_manifest)

        _code_scanning_upload = d.pop("code_scanning_upload", UNSET)
        code_scanning_upload: Union[Unset, RateLimit]
        if isinstance(_code_scanning_upload, Unset):
            code_scanning_upload = UNSET
        else:
            code_scanning_upload = RateLimit.from_dict(_code_scanning_upload)

        _actions_runner_registration = d.pop("actions_runner_registration", UNSET)
        actions_runner_registration: Union[Unset, RateLimit]
        if isinstance(_actions_runner_registration, Unset):
            actions_runner_registration = UNSET
        else:
            actions_runner_registration = RateLimit.from_dict(_actions_runner_registration)

        _scim = d.pop("scim", UNSET)
        scim: Union[Unset, RateLimit]
        if isinstance(_scim, Unset):
            scim = UNSET
        else:
            scim = RateLimit.from_dict(_scim)

        _dependency_snapshots = d.pop("dependency_snapshots", UNSET)
        dependency_snapshots: Union[Unset, RateLimit]
        if isinstance(_dependency_snapshots, Unset):
            dependency_snapshots = UNSET
        else:
            dependency_snapshots = RateLimit.from_dict(_dependency_snapshots)

        rate_limit_overview_resources = cls(
            core=core,
            search=search,
            graphql=graphql,
            source_import=source_import,
            integration_manifest=integration_manifest,
            code_scanning_upload=code_scanning_upload,
            actions_runner_registration=actions_runner_registration,
            scim=scim,
            dependency_snapshots=dependency_snapshots,
        )

        rate_limit_overview_resources.additional_properties = d
        return rate_limit_overview_resources

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
