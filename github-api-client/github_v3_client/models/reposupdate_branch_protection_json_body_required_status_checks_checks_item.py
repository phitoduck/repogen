from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdateBranchProtectionJsonBodyRequiredStatusChecksChecksItem")


@attr.s(auto_attribs=True)
class ReposupdateBranchProtectionJsonBodyRequiredStatusChecksChecksItem:
    """
    Attributes:
        context (str): The name of the required check
        app_id (Union[Unset, int]): The ID of the GitHub App that must provide this check. Omit this field to
            automatically select the GitHub App that has recently provided this check, or any app if it was not set by a
            GitHub App. Pass -1 to explicitly allow any app to set the status.
    """

    context: str
    app_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context
        app_id = self.app_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "context": context,
            }
        )
        if app_id is not UNSET:
            field_dict["app_id"] = app_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        context = d.pop("context")

        app_id = d.pop("app_id", UNSET)

        reposupdate_branch_protection_json_body_required_status_checks_checks_item = cls(
            context=context,
            app_id=app_id,
        )

        reposupdate_branch_protection_json_body_required_status_checks_checks_item.additional_properties = d
        return reposupdate_branch_protection_json_body_required_status_checks_checks_item

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
