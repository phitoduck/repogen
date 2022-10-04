from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.simple_user import SimpleUser

T = TypeVar("T", bound="ProjectCollaboratorPermission")


@attr.s(auto_attribs=True)
class ProjectCollaboratorPermission:
    """Project Collaborator Permission

    Attributes:
        permission (str):
        user (Optional[SimpleUser]): Simple User
    """

    permission: str
    user: Optional[SimpleUser]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permission = self.permission
        user = self.user.to_dict() if self.user else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "permission": permission,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        permission = d.pop("permission")

        _user = d.pop("user")
        user: Optional[SimpleUser]
        if _user is None:
            user = None
        else:
            user = SimpleUser.from_dict(_user)

        project_collaborator_permission = cls(
            permission=permission,
            user=user,
        )

        project_collaborator_permission.additional_properties = d
        return project_collaborator_permission

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
