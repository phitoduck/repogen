from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArtifactWorkflowRun")


@attr.s(auto_attribs=True)
class ArtifactWorkflowRun:
    """
    Attributes:
        id (Union[Unset, int]):  Example: 10.
        repository_id (Union[Unset, int]):  Example: 42.
        head_repository_id (Union[Unset, int]):  Example: 42.
        head_branch (Union[Unset, str]):  Example: main.
        head_sha (Union[Unset, str]):  Example: 009b8a3a9ccbb128af87f9b1c0f4c62e8a304f6d.
    """

    id: Union[Unset, int] = UNSET
    repository_id: Union[Unset, int] = UNSET
    head_repository_id: Union[Unset, int] = UNSET
    head_branch: Union[Unset, str] = UNSET
    head_sha: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        repository_id = self.repository_id
        head_repository_id = self.head_repository_id
        head_branch = self.head_branch
        head_sha = self.head_sha

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if repository_id is not UNSET:
            field_dict["repository_id"] = repository_id
        if head_repository_id is not UNSET:
            field_dict["head_repository_id"] = head_repository_id
        if head_branch is not UNSET:
            field_dict["head_branch"] = head_branch
        if head_sha is not UNSET:
            field_dict["head_sha"] = head_sha

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        repository_id = d.pop("repository_id", UNSET)

        head_repository_id = d.pop("head_repository_id", UNSET)

        head_branch = d.pop("head_branch", UNSET)

        head_sha = d.pop("head_sha", UNSET)

        artifact_workflow_run = cls(
            id=id,
            repository_id=repository_id,
            head_repository_id=head_repository_id,
            head_branch=head_branch,
            head_sha=head_sha,
        )

        artifact_workflow_run.additional_properties = d
        return artifact_workflow_run

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
