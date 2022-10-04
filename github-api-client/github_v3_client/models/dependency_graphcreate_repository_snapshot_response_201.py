from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DependencyGraphcreateRepositorySnapshotResponse201")


@attr.s(auto_attribs=True)
class DependencyGraphcreateRepositorySnapshotResponse201:
    """
    Attributes:
        id (int): ID of the created snapshot.
        created_at (str): The time at which the snapshot was created.
        result (str): Either "SUCCESS", "ACCEPTED", or "INVALID". "SUCCESS" indicates that the snapshot was successfully
            created and the repository's dependencies were updated. "ACCEPTED" indicates that the snapshot was successfully
            created, but the repository's dependencies were not updated. "INVALID" indicates that the snapshot was
            malformed.
        message (str): A message providing further details about the result, such as why the dependencies were not
            updated.
    """

    id: int
    created_at: str
    result: str
    message: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_at = self.created_at
        result = self.result
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "result": result,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        created_at = d.pop("created_at")

        result = d.pop("result")

        message = d.pop("message")

        dependency_graphcreate_repository_snapshot_response_201 = cls(
            id=id,
            created_at=created_at,
            result=result,
            message=message,
        )

        dependency_graphcreate_repository_snapshot_response_201.additional_properties = d
        return dependency_graphcreate_repository_snapshot_response_201

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
