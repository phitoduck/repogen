from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStatisticsItemGheStatsRepos")


@attr.s(auto_attribs=True)
class ServerStatisticsItemGheStatsRepos:
    """
    Attributes:
        total_repos (Union[Unset, int]):
        root_repos (Union[Unset, int]):
        fork_repos (Union[Unset, int]):
        org_repos (Union[Unset, int]):
        total_pushes (Union[Unset, int]):
        total_wikis (Union[Unset, int]):
    """

    total_repos: Union[Unset, int] = UNSET
    root_repos: Union[Unset, int] = UNSET
    fork_repos: Union[Unset, int] = UNSET
    org_repos: Union[Unset, int] = UNSET
    total_pushes: Union[Unset, int] = UNSET
    total_wikis: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_repos = self.total_repos
        root_repos = self.root_repos
        fork_repos = self.fork_repos
        org_repos = self.org_repos
        total_pushes = self.total_pushes
        total_wikis = self.total_wikis

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_repos is not UNSET:
            field_dict["total_repos"] = total_repos
        if root_repos is not UNSET:
            field_dict["root_repos"] = root_repos
        if fork_repos is not UNSET:
            field_dict["fork_repos"] = fork_repos
        if org_repos is not UNSET:
            field_dict["org_repos"] = org_repos
        if total_pushes is not UNSET:
            field_dict["total_pushes"] = total_pushes
        if total_wikis is not UNSET:
            field_dict["total_wikis"] = total_wikis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_repos = d.pop("total_repos", UNSET)

        root_repos = d.pop("root_repos", UNSET)

        fork_repos = d.pop("fork_repos", UNSET)

        org_repos = d.pop("org_repos", UNSET)

        total_pushes = d.pop("total_pushes", UNSET)

        total_wikis = d.pop("total_wikis", UNSET)

        server_statistics_item_ghe_stats_repos = cls(
            total_repos=total_repos,
            root_repos=root_repos,
            fork_repos=fork_repos,
            org_repos=org_repos,
            total_pushes=total_pushes,
            total_wikis=total_wikis,
        )

        server_statistics_item_ghe_stats_repos.additional_properties = d
        return server_statistics_item_ghe_stats_repos

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
