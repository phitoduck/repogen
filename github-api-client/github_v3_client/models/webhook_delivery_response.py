from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.webhook_delivery_response_headers import WebhookDeliveryResponseHeaders

T = TypeVar("T", bound="WebhookDeliveryResponse")


@attr.s(auto_attribs=True)
class WebhookDeliveryResponse:
    """
    Attributes:
        headers (Optional[WebhookDeliveryResponseHeaders]): The response headers received when the delivery was made.
        payload (Optional[str]): The response payload received.
    """

    headers: Optional[WebhookDeliveryResponseHeaders]
    payload: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headers = self.headers.to_dict() if self.headers else None

        payload = self.payload

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
        headers: Optional[WebhookDeliveryResponseHeaders]
        if _headers is None:
            headers = None
        else:
            headers = WebhookDeliveryResponseHeaders.from_dict(_headers)

        payload = d.pop("payload")

        webhook_delivery_response = cls(
            headers=headers,
            payload=payload,
        )

        webhook_delivery_response.additional_properties = d
        return webhook_delivery_response

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
