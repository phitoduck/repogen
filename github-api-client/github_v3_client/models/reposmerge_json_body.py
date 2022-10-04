from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposmergeJsonBody")


@attr.s(auto_attribs=True)
class ReposmergeJsonBody:
    """
    Attributes:
        base (str): The name of the base branch that the head will be merged into.
        head (str): The head to merge. This can be a branch name or a commit SHA1.
        commit_message (Union[Unset, str]): Commit message to use for the merge commit. If omitted, a default message
            will be used.
    """

    base: str
    head: str
    commit_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        base = self.base
        head = self.head
        commit_message = self.commit_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base": base,
                "head": head,
            }
        )
        if commit_message is not UNSET:
            field_dict["commit_message"] = commit_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        base = d.pop("base")

        head = d.pop("head")

        commit_message = d.pop("commit_message", UNSET)

        reposmerge_json_body = cls(
            base=base,
            head=head,
            commit_message=commit_message,
        )

        reposmerge_json_body.additional_properties = d
        return reposmerge_json_body

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
