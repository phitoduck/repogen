from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.projectsadd_collaborator_json_body_permission import ProjectsaddCollaboratorJsonBodyPermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectsaddCollaboratorJsonBody")


@attr.s(auto_attribs=True)
class ProjectsaddCollaboratorJsonBody:
    """
    Attributes:
        permission (Union[Unset, ProjectsaddCollaboratorJsonBodyPermission]): The permission to grant the collaborator.
            Default: ProjectsaddCollaboratorJsonBodyPermission.WRITE. Example: write.
    """

    permission: Union[
        Unset, ProjectsaddCollaboratorJsonBodyPermission
    ] = ProjectsaddCollaboratorJsonBodyPermission.WRITE
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permission: Union[Unset, str] = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _permission = d.pop("permission", UNSET)
        permission: Union[Unset, ProjectsaddCollaboratorJsonBodyPermission]
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = ProjectsaddCollaboratorJsonBodyPermission(_permission)

        projectsadd_collaborator_json_body = cls(
            permission=permission,
        )

        projectsadd_collaborator_json_body.additional_properties = d
        return projectsadd_collaborator_json_body

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
