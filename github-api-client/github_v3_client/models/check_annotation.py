from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="CheckAnnotation")


@attr.s(auto_attribs=True)
class CheckAnnotation:
    """Check Annotation

    Attributes:
        path (str):  Example: README.md.
        start_line (int):  Example: 2.
        end_line (int):  Example: 2.
        blob_href (str):
        start_column (Optional[int]):  Example: 5.
        end_column (Optional[int]):  Example: 10.
        annotation_level (Optional[str]):  Example: warning.
        title (Optional[str]):  Example: Spell Checker.
        message (Optional[str]):  Example: Check your spelling for 'banaas'..
        raw_details (Optional[str]):  Example: Do you mean 'bananas' or 'banana'?.
    """

    path: str
    start_line: int
    end_line: int
    blob_href: str
    start_column: Optional[int]
    end_column: Optional[int]
    annotation_level: Optional[str]
    title: Optional[str]
    message: Optional[str]
    raw_details: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        start_line = self.start_line
        end_line = self.end_line
        blob_href = self.blob_href
        start_column = self.start_column
        end_column = self.end_column
        annotation_level = self.annotation_level
        title = self.title
        message = self.message
        raw_details = self.raw_details

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "start_line": start_line,
                "end_line": end_line,
                "blob_href": blob_href,
                "start_column": start_column,
                "end_column": end_column,
                "annotation_level": annotation_level,
                "title": title,
                "message": message,
                "raw_details": raw_details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        start_line = d.pop("start_line")

        end_line = d.pop("end_line")

        blob_href = d.pop("blob_href")

        start_column = d.pop("start_column")

        end_column = d.pop("end_column")

        annotation_level = d.pop("annotation_level")

        title = d.pop("title")

        message = d.pop("message")

        raw_details = d.pop("raw_details")

        check_annotation = cls(
            path=path,
            start_line=start_line,
            end_line=end_line,
            blob_href=blob_href,
            start_column=start_column,
            end_column=end_column,
            annotation_level=annotation_level,
            title=title,
            message=message,
            raw_details=raw_details,
        )

        check_annotation.additional_properties = d
        return check_annotation

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
