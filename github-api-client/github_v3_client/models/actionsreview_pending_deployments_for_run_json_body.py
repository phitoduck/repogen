from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.actionsreview_pending_deployments_for_run_json_body_state import (
    ActionsreviewPendingDeploymentsForRunJsonBodyState,
)

T = TypeVar("T", bound="ActionsreviewPendingDeploymentsForRunJsonBody")


@attr.s(auto_attribs=True)
class ActionsreviewPendingDeploymentsForRunJsonBody:
    """
    Attributes:
        environment_ids (List[int]): The list of environment ids to approve or reject Example: [161171787, 161171795].
        state (ActionsreviewPendingDeploymentsForRunJsonBodyState): Whether to approve or reject deployment to the
            specified environments. Example: approved.
        comment (str): A comment to accompany the deployment review Example: Ship it!.
    """

    environment_ids: List[int]
    state: ActionsreviewPendingDeploymentsForRunJsonBodyState
    comment: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        environment_ids = self.environment_ids

        state = self.state.value

        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environment_ids": environment_ids,
                "state": state,
                "comment": comment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        environment_ids = cast(List[int], d.pop("environment_ids"))

        state = ActionsreviewPendingDeploymentsForRunJsonBodyState(d.pop("state"))

        comment = d.pop("comment")

        actionsreview_pending_deployments_for_run_json_body = cls(
            environment_ids=environment_ids,
            state=state,
            comment=comment,
        )

        actionsreview_pending_deployments_for_run_json_body.additional_properties = d
        return actionsreview_pending_deployments_for_run_json_body

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
