from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.api_overview_ssh_key_fingerprints import ApiOverviewSshKeyFingerprints
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiOverview")


@attr.s(auto_attribs=True)
class ApiOverview:
    """Api Overview

    Attributes:
        verifiable_password_authentication (bool):  Example: True.
        ssh_key_fingerprints (Union[Unset, ApiOverviewSshKeyFingerprints]):
        ssh_keys (Union[Unset, List[str]]):  Example: ['ssh-ed25519
            AAAAC3NzaC1lZDI1NTE5AAAAIOMqqnkVzrm0SdG6UOoqKLsabgH5C9okWi0dh2l9GKJl'].
        hooks (Union[Unset, List[str]]):  Example: ['127.0.0.1/32'].
        web (Union[Unset, List[str]]):  Example: ['127.0.0.1/32'].
        api (Union[Unset, List[str]]):  Example: ['127.0.0.1/32'].
        git (Union[Unset, List[str]]):  Example: ['127.0.0.1/32'].
        packages (Union[Unset, List[str]]):  Example: ['13.65.0.0/16', '157.55.204.33/32', '2a01:111:f403:f90c::/62'].
        pages (Union[Unset, List[str]]):  Example: ['192.30.252.153/32', '192.30.252.154/32'].
        importer (Union[Unset, List[str]]):  Example: ['54.158.161.132', '54.226.70.38'].
        actions (Union[Unset, List[str]]):  Example: ['13.64.0.0/16', '13.65.0.0/16'].
        dependabot (Union[Unset, List[str]]):  Example: ['192.168.7.15/32', '192.168.7.16/32'].
    """

    verifiable_password_authentication: bool
    ssh_key_fingerprints: Union[Unset, ApiOverviewSshKeyFingerprints] = UNSET
    ssh_keys: Union[Unset, List[str]] = UNSET
    hooks: Union[Unset, List[str]] = UNSET
    web: Union[Unset, List[str]] = UNSET
    api: Union[Unset, List[str]] = UNSET
    git: Union[Unset, List[str]] = UNSET
    packages: Union[Unset, List[str]] = UNSET
    pages: Union[Unset, List[str]] = UNSET
    importer: Union[Unset, List[str]] = UNSET
    actions: Union[Unset, List[str]] = UNSET
    dependabot: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        verifiable_password_authentication = self.verifiable_password_authentication
        ssh_key_fingerprints: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ssh_key_fingerprints, Unset):
            ssh_key_fingerprints = self.ssh_key_fingerprints.to_dict()

        ssh_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ssh_keys, Unset):
            ssh_keys = self.ssh_keys

        hooks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hooks, Unset):
            hooks = self.hooks

        web: Union[Unset, List[str]] = UNSET
        if not isinstance(self.web, Unset):
            web = self.web

        api: Union[Unset, List[str]] = UNSET
        if not isinstance(self.api, Unset):
            api = self.api

        git: Union[Unset, List[str]] = UNSET
        if not isinstance(self.git, Unset):
            git = self.git

        packages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.packages, Unset):
            packages = self.packages

        pages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.pages, Unset):
            pages = self.pages

        importer: Union[Unset, List[str]] = UNSET
        if not isinstance(self.importer, Unset):
            importer = self.importer

        actions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions

        dependabot: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dependabot, Unset):
            dependabot = self.dependabot

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "verifiable_password_authentication": verifiable_password_authentication,
            }
        )
        if ssh_key_fingerprints is not UNSET:
            field_dict["ssh_key_fingerprints"] = ssh_key_fingerprints
        if ssh_keys is not UNSET:
            field_dict["ssh_keys"] = ssh_keys
        if hooks is not UNSET:
            field_dict["hooks"] = hooks
        if web is not UNSET:
            field_dict["web"] = web
        if api is not UNSET:
            field_dict["api"] = api
        if git is not UNSET:
            field_dict["git"] = git
        if packages is not UNSET:
            field_dict["packages"] = packages
        if pages is not UNSET:
            field_dict["pages"] = pages
        if importer is not UNSET:
            field_dict["importer"] = importer
        if actions is not UNSET:
            field_dict["actions"] = actions
        if dependabot is not UNSET:
            field_dict["dependabot"] = dependabot

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        verifiable_password_authentication = d.pop("verifiable_password_authentication")

        _ssh_key_fingerprints = d.pop("ssh_key_fingerprints", UNSET)
        ssh_key_fingerprints: Union[Unset, ApiOverviewSshKeyFingerprints]
        if isinstance(_ssh_key_fingerprints, Unset):
            ssh_key_fingerprints = UNSET
        else:
            ssh_key_fingerprints = ApiOverviewSshKeyFingerprints.from_dict(_ssh_key_fingerprints)

        ssh_keys = cast(List[str], d.pop("ssh_keys", UNSET))

        hooks = cast(List[str], d.pop("hooks", UNSET))

        web = cast(List[str], d.pop("web", UNSET))

        api = cast(List[str], d.pop("api", UNSET))

        git = cast(List[str], d.pop("git", UNSET))

        packages = cast(List[str], d.pop("packages", UNSET))

        pages = cast(List[str], d.pop("pages", UNSET))

        importer = cast(List[str], d.pop("importer", UNSET))

        actions = cast(List[str], d.pop("actions", UNSET))

        dependabot = cast(List[str], d.pop("dependabot", UNSET))

        api_overview = cls(
            verifiable_password_authentication=verifiable_password_authentication,
            ssh_key_fingerprints=ssh_key_fingerprints,
            ssh_keys=ssh_keys,
            hooks=hooks,
            web=web,
            api=api,
            git=git,
            packages=packages,
            pages=pages,
            importer=importer,
            actions=actions,
            dependabot=dependabot,
        )

        api_overview.additional_properties = d
        return api_overview

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
