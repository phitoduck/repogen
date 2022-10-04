from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GitignoreTemplate")


@attr.s(auto_attribs=True)
class GitignoreTemplate:
    """Gitignore Template

    Attributes:
        name (str):  Example: C.
        source (str):  Example: # Object files
            *.o

            # Libraries
            *.lib
            *.a

            # Shared objects (inc. Windows DLLs)
            *.dll
            *.so
            *.so.*
            *.dylib

            # Executables
            *.exe
            *.out
            *.app
            .
    """

    name: str
    source: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        source = d.pop("source")

        gitignore_template = cls(
            name=name,
            source=source,
        )

        gitignore_template.additional_properties = d
        return gitignore_template

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
