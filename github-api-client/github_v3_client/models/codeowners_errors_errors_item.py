from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CODEOWNERSErrorsErrorsItem")


@attr.s(auto_attribs=True)
class CODEOWNERSErrorsErrorsItem:
    """
    Attributes:
        line (int): The line number where this errors occurs. Example: 7.
        column (int): The column number where this errors occurs. Example: 3.
        kind (str): The type of error. Example: Invalid owner.
        message (str): A human-readable description of the error, combining information from multiple fields, laid out
            for display in a monospaced typeface (for example, a command-line setting). Example: Invalid owner on line 7:

              * user
                ^.
        path (str): The path of the file where the error occured. Example: .github/CODEOWNERS.
        source (Union[Unset, str]): The contents of the line where the error occurs. Example: * user.
        suggestion (Union[Unset, None, str]): Suggested action to fix the error. This will usually be `null`, but is
            provided for some common errors. Example: The pattern `/` will never match anything, did you mean `*` instead?.
    """

    line: int
    column: int
    kind: str
    message: str
    path: str
    source: Union[Unset, str] = UNSET
    suggestion: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line = self.line
        column = self.column
        kind = self.kind
        message = self.message
        path = self.path
        source = self.source
        suggestion = self.suggestion

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "line": line,
                "column": column,
                "kind": kind,
                "message": message,
                "path": path,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source
        if suggestion is not UNSET:
            field_dict["suggestion"] = suggestion

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line = d.pop("line")

        column = d.pop("column")

        kind = d.pop("kind")

        message = d.pop("message")

        path = d.pop("path")

        source = d.pop("source", UNSET)

        suggestion = d.pop("suggestion", UNSET)

        codeowners_errors_errors_item = cls(
            line=line,
            column=column,
            kind=kind,
            message=message,
            path=path,
            source=source,
            suggestion=suggestion,
        )

        codeowners_errors_errors_item.additional_properties = d
        return codeowners_errors_errors_item

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
