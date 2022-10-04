from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PagesSourceHash")


@attr.s(auto_attribs=True)
class PagesSourceHash:
    """
    Attributes:
        branch (str):
        path (str):
    """

    branch: str
    path: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        branch = self.branch
        path = self.path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "branch": branch,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        branch = d.pop("branch")

        path = d.pop("path")

        pages_source_hash = cls(
            branch=branch,
            path=path,
        )

        pages_source_hash.additional_properties = d
        return pages_source_hash

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
