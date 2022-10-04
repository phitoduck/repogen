from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodeScanningAnalysisTool")


@attr.s(auto_attribs=True)
class CodeScanningAnalysisTool:
    """
    Attributes:
        name (Union[Unset, str]): The name of the tool used to generate the code scanning analysis.
        version (Union[Unset, None, str]): The version of the tool used to generate the code scanning analysis.
        guid (Union[Unset, None, str]): The GUID of the tool used to generate the code scanning analysis, if provided in
            the uploaded SARIF data.
    """

    name: Union[Unset, str] = UNSET
    version: Union[Unset, None, str] = UNSET
    guid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        version = self.version
        guid = self.guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if guid is not UNSET:
            field_dict["guid"] = guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        guid = d.pop("guid", UNSET)

        code_scanning_analysis_tool = cls(
            name=name,
            version=version,
            guid=guid,
        )

        code_scanning_analysis_tool.additional_properties = d
        return code_scanning_analysis_tool

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
