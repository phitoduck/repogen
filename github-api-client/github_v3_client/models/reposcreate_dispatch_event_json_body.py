from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reposcreate_dispatch_event_json_body_client_payload import ReposcreateDispatchEventJsonBodyClientPayload
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateDispatchEventJsonBody")


@attr.s(auto_attribs=True)
class ReposcreateDispatchEventJsonBody:
    """
    Attributes:
        event_type (str): A custom webhook event name. Must be 100 characters or fewer.
        client_payload (Union[Unset, ReposcreateDispatchEventJsonBodyClientPayload]): JSON payload with extra
            information about the webhook event that your action or workflow may use. The maximum number of top-level
            properties is 10.
    """

    event_type: str
    client_payload: Union[Unset, ReposcreateDispatchEventJsonBodyClientPayload] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type = self.event_type
        client_payload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client_payload, Unset):
            client_payload = self.client_payload.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
            }
        )
        if client_payload is not UNSET:
            field_dict["client_payload"] = client_payload

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_type = d.pop("event_type")

        _client_payload = d.pop("client_payload", UNSET)
        client_payload: Union[Unset, ReposcreateDispatchEventJsonBodyClientPayload]
        if isinstance(_client_payload, Unset):
            client_payload = UNSET
        else:
            client_payload = ReposcreateDispatchEventJsonBodyClientPayload.from_dict(_client_payload)

        reposcreate_dispatch_event_json_body = cls(
            event_type=event_type,
            client_payload=client_payload,
        )

        reposcreate_dispatch_event_json_body.additional_properties = d
        return reposcreate_dispatch_event_json_body

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
