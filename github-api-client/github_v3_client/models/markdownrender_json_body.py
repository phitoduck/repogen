from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.markdownrender_json_body_mode import MarkdownrenderJsonBodyMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkdownrenderJsonBody")


@attr.s(auto_attribs=True)
class MarkdownrenderJsonBody:
    """
    Attributes:
        text (str): The Markdown text to render in HTML.
        mode (Union[Unset, MarkdownrenderJsonBodyMode]): The rendering mode. Default:
            MarkdownrenderJsonBodyMode.MARKDOWN. Example: markdown.
        context (Union[Unset, str]): The repository context to use when creating references in `gfm` mode.  For example,
            setting `context` to `octo-org/octo-repo` will change the text `#42` into an HTML link to issue 42 in the `octo-
            org/octo-repo` repository.
    """

    text: str
    mode: Union[Unset, MarkdownrenderJsonBodyMode] = MarkdownrenderJsonBodyMode.MARKDOWN
    context: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        context = self.context

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, MarkdownrenderJsonBodyMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = MarkdownrenderJsonBodyMode(_mode)

        context = d.pop("context", UNSET)

        markdownrender_json_body = cls(
            text=text,
            mode=mode,
            context=context,
        )

        markdownrender_json_body.additional_properties = d
        return markdownrender_json_body

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
