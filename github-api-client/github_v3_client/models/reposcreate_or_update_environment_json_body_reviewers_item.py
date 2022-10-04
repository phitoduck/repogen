from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.deployment_reviewer_type import DeploymentReviewerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateOrUpdateEnvironmentJsonBodyReviewersItem")


@attr.s(auto_attribs=True)
class ReposcreateOrUpdateEnvironmentJsonBodyReviewersItem:
    """
    Attributes:
        type (Union[Unset, DeploymentReviewerType]): The type of reviewer. Example: User.
        id (Union[Unset, int]): The id of the user or team who can review the deployment Example: 4532992.
    """

    type: Union[Unset, DeploymentReviewerType] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, DeploymentReviewerType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DeploymentReviewerType(_type)

        id = d.pop("id", UNSET)

        reposcreate_or_update_environment_json_body_reviewers_item = cls(
            type=type,
            id=id,
        )

        reposcreate_or_update_environment_json_body_reviewers_item.additional_properties = d
        return reposcreate_or_update_environment_json_body_reviewers_item

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
