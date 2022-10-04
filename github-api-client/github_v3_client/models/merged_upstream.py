from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.merged_upstream_merge_type import MergedUpstreamMergeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MergedUpstream")


@attr.s(auto_attribs=True)
class MergedUpstream:
    """Results of a successful merge upstream request

    Attributes:
        message (Union[Unset, str]):
        merge_type (Union[Unset, MergedUpstreamMergeType]):
        base_branch (Union[Unset, str]):
    """

    message: Union[Unset, str] = UNSET
    merge_type: Union[Unset, MergedUpstreamMergeType] = UNSET
    base_branch: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        merge_type: Union[Unset, str] = UNSET
        if not isinstance(self.merge_type, Unset):
            merge_type = self.merge_type.value

        base_branch = self.base_branch

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if merge_type is not UNSET:
            field_dict["merge_type"] = merge_type
        if base_branch is not UNSET:
            field_dict["base_branch"] = base_branch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        _merge_type = d.pop("merge_type", UNSET)
        merge_type: Union[Unset, MergedUpstreamMergeType]
        if isinstance(_merge_type, Unset):
            merge_type = UNSET
        else:
            merge_type = MergedUpstreamMergeType(_merge_type)

        base_branch = d.pop("base_branch", UNSET)

        merged_upstream = cls(
            message=message,
            merge_type=merge_type,
            base_branch=base_branch,
        )

        merged_upstream.additional_properties = d
        return merged_upstream

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
