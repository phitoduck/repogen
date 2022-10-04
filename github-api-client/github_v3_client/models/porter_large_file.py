from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PorterLargeFile")


@attr.s(auto_attribs=True)
class PorterLargeFile:
    """Porter Large File

    Attributes:
        ref_name (str):
        path (str):
        oid (str):
        size (int):
    """

    ref_name: str
    path: str
    oid: str
    size: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref_name = self.ref_name
        path = self.path
        oid = self.oid
        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ref_name": ref_name,
                "path": path,
                "oid": oid,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ref_name = d.pop("ref_name")

        path = d.pop("path")

        oid = d.pop("oid")

        size = d.pop("size")

        porter_large_file = cls(
            ref_name=ref_name,
            path=path,
            oid=oid,
            size=size,
        )

        porter_large_file.additional_properties = d
        return porter_large_file

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
