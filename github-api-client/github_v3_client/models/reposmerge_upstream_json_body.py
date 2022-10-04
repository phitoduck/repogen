from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ReposmergeUpstreamJsonBody")


@attr.s(auto_attribs=True)
class ReposmergeUpstreamJsonBody:
    """
    Attributes:
        branch (str): The name of the branch which should be updated to match upstream.
    """

    branch: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        branch = self.branch

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "branch": branch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        branch = d.pop("branch")

        reposmerge_upstream_json_body = cls(
            branch=branch,
        )

        reposmerge_upstream_json_body.additional_properties = d
        return reposmerge_upstream_json_body

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
