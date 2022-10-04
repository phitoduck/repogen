from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStatisticsItemGheStatsOrgs")


@attr.s(auto_attribs=True)
class ServerStatisticsItemGheStatsOrgs:
    """
    Attributes:
        total_orgs (Union[Unset, int]):
        disabled_orgs (Union[Unset, int]):
        total_teams (Union[Unset, int]):
        total_team_members (Union[Unset, int]):
    """

    total_orgs: Union[Unset, int] = UNSET
    disabled_orgs: Union[Unset, int] = UNSET
    total_teams: Union[Unset, int] = UNSET
    total_team_members: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_orgs = self.total_orgs
        disabled_orgs = self.disabled_orgs
        total_teams = self.total_teams
        total_team_members = self.total_team_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_orgs is not UNSET:
            field_dict["total_orgs"] = total_orgs
        if disabled_orgs is not UNSET:
            field_dict["disabled_orgs"] = disabled_orgs
        if total_teams is not UNSET:
            field_dict["total_teams"] = total_teams
        if total_team_members is not UNSET:
            field_dict["total_team_members"] = total_team_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_orgs = d.pop("total_orgs", UNSET)

        disabled_orgs = d.pop("disabled_orgs", UNSET)

        total_teams = d.pop("total_teams", UNSET)

        total_team_members = d.pop("total_team_members", UNSET)

        server_statistics_item_ghe_stats_orgs = cls(
            total_orgs=total_orgs,
            disabled_orgs=disabled_orgs,
            total_teams=total_teams,
            total_team_members=total_team_members,
        )

        server_statistics_item_ghe_stats_orgs.additional_properties = d
        return server_statistics_item_ghe_stats_orgs

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
