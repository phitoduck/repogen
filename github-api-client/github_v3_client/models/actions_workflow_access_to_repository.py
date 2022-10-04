from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.actions_workflow_access_to_repository_access_level import ActionsWorkflowAccessToRepositoryAccessLevel

T = TypeVar("T", bound="ActionsWorkflowAccessToRepository")


@attr.s(auto_attribs=True)
class ActionsWorkflowAccessToRepository:
    """
    Attributes:
        access_level (ActionsWorkflowAccessToRepositoryAccessLevel): Defines the level of access that workflows outside
            of the repository have to actions and reusable workflows within the
            repository. `none` means access is only possible from workflows in this repository.
    """

    access_level: ActionsWorkflowAccessToRepositoryAccessLevel
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_level = self.access_level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_level": access_level,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_level = ActionsWorkflowAccessToRepositoryAccessLevel(d.pop("access_level"))

        actions_workflow_access_to_repository = cls(
            access_level=access_level,
        )

        actions_workflow_access_to_repository.additional_properties = d
        return actions_workflow_access_to_repository

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
