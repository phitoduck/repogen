from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.webhook_delivery_request_headers import WebhookDeliveryRequestHeaders
from ..models.webhook_delivery_request_payload import WebhookDeliveryRequestPayload

T = TypeVar("T", bound="WebhookDeliveryRequest")


@attr.s(auto_attribs=True)
class WebhookDeliveryRequest:
    """
    Attributes:
        headers (Optional[WebhookDeliveryRequestHeaders]): The request headers sent with the webhook delivery.
        payload (Optional[WebhookDeliveryRequestPayload]): The webhook payload.
    """

    headers: Optional[WebhookDeliveryRequestHeaders]
    payload: Optional[WebhookDeliveryRequestPayload]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headers = self.headers.to_dict() if self.headers else None

        payload = self.payload.to_dict() if self.payload else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "headers": headers,
                "payload": payload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _headers = d.pop("headers")
        headers: Optional[WebhookDeliveryRequestHeaders]
        if _headers is None:
            headers = None
        else:
            headers = WebhookDeliveryRequestHeaders.from_dict(_headers)

        _payload = d.pop("payload")
        payload: Optional[WebhookDeliveryRequestPayload]
        if _payload is None:
            payload = None
        else:
            payload = WebhookDeliveryRequestPayload.from_dict(_payload)

        webhook_delivery_request = cls(
            headers=headers,
            payload=payload,
        )

        webhook_delivery_request.additional_properties = d
        return webhook_delivery_request

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
