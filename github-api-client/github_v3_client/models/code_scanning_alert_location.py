from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodeScanningAlertLocation")


@attr.s(auto_attribs=True)
class CodeScanningAlertLocation:
    """Describe a region within a file for the alert.

    Attributes:
        path (Union[Unset, str]):
        start_line (Union[Unset, int]):
        end_line (Union[Unset, int]):
        start_column (Union[Unset, int]):
        end_column (Union[Unset, int]):
    """

    path: Union[Unset, str] = UNSET
    start_line: Union[Unset, int] = UNSET
    end_line: Union[Unset, int] = UNSET
    start_column: Union[Unset, int] = UNSET
    end_column: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        start_line = self.start_line
        end_line = self.end_line
        start_column = self.start_column
        end_column = self.end_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if start_line is not UNSET:
            field_dict["start_line"] = start_line
        if end_line is not UNSET:
            field_dict["end_line"] = end_line
        if start_column is not UNSET:
            field_dict["start_column"] = start_column
        if end_column is not UNSET:
            field_dict["end_column"] = end_column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path", UNSET)

        start_line = d.pop("start_line", UNSET)

        end_line = d.pop("end_line", UNSET)

        start_column = d.pop("start_column", UNSET)

        end_column = d.pop("end_column", UNSET)

        code_scanning_alert_location = cls(
            path=path,
            start_line=start_line,
            end_line=end_line,
            start_column=start_column,
            end_column=end_column,
        )

        code_scanning_alert_location.additional_properties = d
        return code_scanning_alert_location

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
