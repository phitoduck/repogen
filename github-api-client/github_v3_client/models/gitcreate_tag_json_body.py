from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.gitcreate_tag_json_body_tagger import GitcreateTagJsonBodyTagger
from ..models.gitcreate_tag_json_body_type import GitcreateTagJsonBodyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GitcreateTagJsonBody")


@attr.s(auto_attribs=True)
class GitcreateTagJsonBody:
    """
    Attributes:
        tag (str): The tag's name. This is typically a version (e.g., "v0.0.1").
        message (str): The tag message.
        object_ (str): The SHA of the git object this is tagging.
        type (GitcreateTagJsonBodyType): The type of the object we're tagging. Normally this is a `commit` but it can
            also be a `tree` or a `blob`.
        tagger (Union[Unset, GitcreateTagJsonBodyTagger]): An object with information about the individual creating the
            tag.
    """

    tag: str
    message: str
    object_: str
    type: GitcreateTagJsonBodyType
    tagger: Union[Unset, GitcreateTagJsonBodyTagger] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tag = self.tag
        message = self.message
        object_ = self.object_
        type = self.type.value

        tagger: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tagger, Unset):
            tagger = self.tagger.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag": tag,
                "message": message,
                "object": object_,
                "type": type,
            }
        )
        if tagger is not UNSET:
            field_dict["tagger"] = tagger

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tag = d.pop("tag")

        message = d.pop("message")

        object_ = d.pop("object")

        type = GitcreateTagJsonBodyType(d.pop("type"))

        _tagger = d.pop("tagger", UNSET)
        tagger: Union[Unset, GitcreateTagJsonBodyTagger]
        if isinstance(_tagger, Unset):
            tagger = UNSET
        else:
            tagger = GitcreateTagJsonBodyTagger.from_dict(_tagger)

        gitcreate_tag_json_body = cls(
            tag=tag,
            message=message,
            object_=object_,
            type=type,
            tagger=tagger,
        )

        gitcreate_tag_json_body.additional_properties = d
        return gitcreate_tag_json_body

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
