from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GistCommitChangeStatus")


@attr.s(auto_attribs=True)
class GistCommitChangeStatus:
    """
    Attributes:
        total (Union[Unset, int]):
        additions (Union[Unset, int]):
        deletions (Union[Unset, int]):
    """

    total: Union[Unset, int] = UNSET
    additions: Union[Unset, int] = UNSET
    deletions: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        additions = self.additions
        deletions = self.deletions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if additions is not UNSET:
            field_dict["additions"] = additions
        if deletions is not UNSET:
            field_dict["deletions"] = deletions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total = d.pop("total", UNSET)

        additions = d.pop("additions", UNSET)

        deletions = d.pop("deletions", UNSET)

        gist_commit_change_status = cls(
            total=total,
            additions=additions,
            deletions=deletions,
        )

        gist_commit_change_status.additional_properties = d
        return gist_commit_change_status

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
