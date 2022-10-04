from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferencedWorkflow")


@attr.s(auto_attribs=True)
class ReferencedWorkflow:
    """A workflow referenced/reused by the initial caller workflow

    Attributes:
        path (str):
        sha (str):
        ref (Union[Unset, str]):
    """

    path: str
    sha: str
    ref: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        sha = self.sha
        ref = self.ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "sha": sha,
            }
        )
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        sha = d.pop("sha")

        ref = d.pop("ref", UNSET)

        referenced_workflow = cls(
            path=path,
            sha=sha,
            ref=ref,
        )

        referenced_workflow.additional_properties = d
        return referenced_workflow

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
