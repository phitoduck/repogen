from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="RepossetTeamAccessRestrictionsJsonBodyType0")


@attr.s(auto_attribs=True)
class RepossetTeamAccessRestrictionsJsonBodyType0:
    """
    Example:
        {'teams': ['justice-league']}

    Attributes:
        teams (List[str]): The slug values for teams
    """

    teams: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        teams = self.teams

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "teams": teams,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        teams = cast(List[str], d.pop("teams"))

        reposset_team_access_restrictions_json_body_type_0 = cls(
            teams=teams,
        )

        reposset_team_access_restrictions_json_body_type_0.additional_properties = d
        return reposset_team_access_restrictions_json_body_type_0

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
