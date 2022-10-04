from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pullsupdate_json_body_state import PullsupdateJsonBodyState
from ..types import UNSET, Unset

T = TypeVar("T", bound="PullsupdateJsonBody")


@attr.s(auto_attribs=True)
class PullsupdateJsonBody:
    """
    Attributes:
        title (Union[Unset, str]): The title of the pull request.
        body (Union[Unset, str]): The contents of the pull request.
        state (Union[Unset, PullsupdateJsonBodyState]): State of this Pull Request. Either `open` or `closed`.
        base (Union[Unset, str]): The name of the branch you want your changes pulled into. This should be an existing
            branch on the current repository. You cannot update the base branch on a pull request to point to another
            repository.
        maintainer_can_modify (Union[Unset, bool]): Indicates whether [maintainers can
            modify](https://docs.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) the
            pull request.
    """

    title: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    state: Union[Unset, PullsupdateJsonBodyState] = UNSET
    base: Union[Unset, str] = UNSET
    maintainer_can_modify: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        body = self.body
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        base = self.base
        maintainer_can_modify = self.maintainer_can_modify

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body
        if state is not UNSET:
            field_dict["state"] = state
        if base is not UNSET:
            field_dict["base"] = base
        if maintainer_can_modify is not UNSET:
            field_dict["maintainer_can_modify"] = maintainer_can_modify

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        body = d.pop("body", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, PullsupdateJsonBodyState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PullsupdateJsonBodyState(_state)

        base = d.pop("base", UNSET)

        maintainer_can_modify = d.pop("maintainer_can_modify", UNSET)

        pullsupdate_json_body = cls(
            title=title,
            body=body,
            state=state,
            base=base,
            maintainer_can_modify=maintainer_can_modify,
        )

        pullsupdate_json_body.additional_properties = d
        return pullsupdate_json_body

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
