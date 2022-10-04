from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.server_statistics_item_dormant_users import ServerStatisticsItemDormantUsers
from ..models.server_statistics_item_ghe_stats import ServerStatisticsItemGheStats
from ..models.server_statistics_item_github_connect import ServerStatisticsItemGithubConnect
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStatisticsItem")


@attr.s(auto_attribs=True)
class ServerStatisticsItem:
    """
    Attributes:
        server_id (Union[Unset, str]):
        collection_date (Union[Unset, str]):
        schema_version (Union[Unset, str]):
        ghes_version (Union[Unset, str]):
        host_name (Union[Unset, str]):
        github_connect (Union[Unset, ServerStatisticsItemGithubConnect]):
        ghe_stats (Union[Unset, ServerStatisticsItemGheStats]):
        dormant_users (Union[Unset, ServerStatisticsItemDormantUsers]):
    """

    server_id: Union[Unset, str] = UNSET
    collection_date: Union[Unset, str] = UNSET
    schema_version: Union[Unset, str] = UNSET
    ghes_version: Union[Unset, str] = UNSET
    host_name: Union[Unset, str] = UNSET
    github_connect: Union[Unset, ServerStatisticsItemGithubConnect] = UNSET
    ghe_stats: Union[Unset, ServerStatisticsItemGheStats] = UNSET
    dormant_users: Union[Unset, ServerStatisticsItemDormantUsers] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_id = self.server_id
        collection_date = self.collection_date
        schema_version = self.schema_version
        ghes_version = self.ghes_version
        host_name = self.host_name
        github_connect: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.github_connect, Unset):
            github_connect = self.github_connect.to_dict()

        ghe_stats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ghe_stats, Unset):
            ghe_stats = self.ghe_stats.to_dict()

        dormant_users: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dormant_users, Unset):
            dormant_users = self.dormant_users.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server_id is not UNSET:
            field_dict["server_id"] = server_id
        if collection_date is not UNSET:
            field_dict["collection_date"] = collection_date
        if schema_version is not UNSET:
            field_dict["schema_version"] = schema_version
        if ghes_version is not UNSET:
            field_dict["ghes_version"] = ghes_version
        if host_name is not UNSET:
            field_dict["host_name"] = host_name
        if github_connect is not UNSET:
            field_dict["github_connect"] = github_connect
        if ghe_stats is not UNSET:
            field_dict["ghe_stats"] = ghe_stats
        if dormant_users is not UNSET:
            field_dict["dormant_users"] = dormant_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server_id = d.pop("server_id", UNSET)

        collection_date = d.pop("collection_date", UNSET)

        schema_version = d.pop("schema_version", UNSET)

        ghes_version = d.pop("ghes_version", UNSET)

        host_name = d.pop("host_name", UNSET)

        _github_connect = d.pop("github_connect", UNSET)
        github_connect: Union[Unset, ServerStatisticsItemGithubConnect]
        if isinstance(_github_connect, Unset):
            github_connect = UNSET
        else:
            github_connect = ServerStatisticsItemGithubConnect.from_dict(_github_connect)

        _ghe_stats = d.pop("ghe_stats", UNSET)
        ghe_stats: Union[Unset, ServerStatisticsItemGheStats]
        if isinstance(_ghe_stats, Unset):
            ghe_stats = UNSET
        else:
            ghe_stats = ServerStatisticsItemGheStats.from_dict(_ghe_stats)

        _dormant_users = d.pop("dormant_users", UNSET)
        dormant_users: Union[Unset, ServerStatisticsItemDormantUsers]
        if isinstance(_dormant_users, Unset):
            dormant_users = UNSET
        else:
            dormant_users = ServerStatisticsItemDormantUsers.from_dict(_dormant_users)

        server_statistics_item = cls(
            server_id=server_id,
            collection_date=collection_date,
            schema_version=schema_version,
            ghes_version=ghes_version,
            host_name=host_name,
            github_connect=github_connect,
            ghe_stats=ghe_stats,
            dormant_users=dormant_users,
        )

        server_statistics_item.additional_properties = d
        return server_statistics_item

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
