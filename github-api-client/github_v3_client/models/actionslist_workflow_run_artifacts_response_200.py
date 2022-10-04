from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.artifact import Artifact

T = TypeVar("T", bound="ActionslistWorkflowRunArtifactsResponse200")


@attr.s(auto_attribs=True)
class ActionslistWorkflowRunArtifactsResponse200:
    """
    Attributes:
        total_count (int):
        artifacts (List[Artifact]):
    """

    total_count: int
    artifacts: List[Artifact]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        artifacts = []
        for artifacts_item_data in self.artifacts:
            artifacts_item = artifacts_item_data.to_dict()

            artifacts.append(artifacts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_count": total_count,
                "artifacts": artifacts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_count = d.pop("total_count")

        artifacts = []
        _artifacts = d.pop("artifacts")
        for artifacts_item_data in _artifacts:
            artifacts_item = Artifact.from_dict(artifacts_item_data)

            artifacts.append(artifacts_item)

        actionslist_workflow_run_artifacts_response_200 = cls(
            total_count=total_count,
            artifacts=artifacts,
        )

        actionslist_workflow_run_artifacts_response_200.additional_properties = d
        return actionslist_workflow_run_artifacts_response_200

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
