from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.branch_short_commit import BranchShortCommit

T = TypeVar("T", bound="BranchShort")


@attr.s(auto_attribs=True)
class BranchShort:
    """Branch Short

    Attributes:
        name (str):
        commit (BranchShortCommit):
        protected (bool):
    """

    name: str
    commit: BranchShortCommit
    protected: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        commit = self.commit.to_dict()

        protected = self.protected

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "commit": commit,
                "protected": protected,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        commit = BranchShortCommit.from_dict(d.pop("commit"))

        protected = d.pop("protected")

        branch_short = cls(
            name=name,
            commit=commit,
            protected=protected,
        )

        branch_short.additional_properties = d
        return branch_short

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
