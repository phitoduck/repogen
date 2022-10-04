from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepoSearchResultItemPermissions")


@attr.s(auto_attribs=True)
class RepoSearchResultItemPermissions:
    """
    Attributes:
        admin (bool):
        push (bool):
        pull (bool):
        maintain (Union[Unset, bool]):
        triage (Union[Unset, bool]):
    """

    admin: bool
    push: bool
    pull: bool
    maintain: Union[Unset, bool] = UNSET
    triage: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        admin = self.admin
        push = self.push
        pull = self.pull
        maintain = self.maintain
        triage = self.triage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "admin": admin,
                "push": push,
                "pull": pull,
            }
        )
        if maintain is not UNSET:
            field_dict["maintain"] = maintain
        if triage is not UNSET:
            field_dict["triage"] = triage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        admin = d.pop("admin")

        push = d.pop("push")

        pull = d.pop("pull")

        maintain = d.pop("maintain", UNSET)

        triage = d.pop("triage", UNSET)

        repo_search_result_item_permissions = cls(
            admin=admin,
            push=push,
            pull=pull,
            maintain=maintain,
            triage=triage,
        )

        repo_search_result_item_permissions.additional_properties = d
        return repo_search_result_item_permissions

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
