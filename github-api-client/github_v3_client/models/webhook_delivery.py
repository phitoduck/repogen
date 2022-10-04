import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.webhook_delivery_request import WebhookDeliveryRequest
from ..models.webhook_delivery_response import WebhookDeliveryResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookDelivery")


@attr.s(auto_attribs=True)
class WebhookDelivery:
    """Delivery made by a webhook.

    Attributes:
        id (int): Unique identifier of the delivery. Example: 42.
        guid (str): Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this
            event). Example: 58474f00-b361-11eb-836d-0e4f3503ccbe.
        delivered_at (datetime.datetime): Time when the delivery was delivered. Example: 2021-05-12T20:33:44Z.
        redelivery (bool): Whether the delivery is a redelivery.
        duration (float): Time spent delivering. Example: 0.03.
        status (str): Description of the status of the attempted delivery Example: failed to connect.
        status_code (int): Status code received when delivery was made. Example: 502.
        event (str): The event that triggered the delivery. Example: issues.
        request (WebhookDeliveryRequest):
        response (WebhookDeliveryResponse):
        action (Optional[str]): The type of activity for the event that triggered the delivery. Example: opened.
        installation_id (Optional[int]): The id of the GitHub App installation associated with this event. Example: 123.
        repository_id (Optional[int]): The id of the repository associated with this event. Example: 123.
        url (Union[Unset, str]): The URL target of the delivery. Example: https://www.example.com.
    """

    id: int
    guid: str
    delivered_at: datetime.datetime
    redelivery: bool
    duration: float
    status: str
    status_code: int
    event: str
    request: WebhookDeliveryRequest
    response: WebhookDeliveryResponse
    action: Optional[str]
    installation_id: Optional[int]
    repository_id: Optional[int]
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        guid = self.guid
        delivered_at = self.delivered_at.isoformat()

        redelivery = self.redelivery
        duration = self.duration
        status = self.status
        status_code = self.status_code
        event = self.event
        request = self.request.to_dict()

        response = self.response.to_dict()

        action = self.action
        installation_id = self.installation_id
        repository_id = self.repository_id
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "guid": guid,
                "delivered_at": delivered_at,
                "redelivery": redelivery,
                "duration": duration,
                "status": status,
                "status_code": status_code,
                "event": event,
                "request": request,
                "response": response,
                "action": action,
                "installation_id": installation_id,
                "repository_id": repository_id,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        guid = d.pop("guid")

        delivered_at = isoparse(d.pop("delivered_at"))

        redelivery = d.pop("redelivery")

        duration = d.pop("duration")

        status = d.pop("status")

        status_code = d.pop("status_code")

        event = d.pop("event")

        request = WebhookDeliveryRequest.from_dict(d.pop("request"))

        response = WebhookDeliveryResponse.from_dict(d.pop("response"))

        action = d.pop("action")

        installation_id = d.pop("installation_id")

        repository_id = d.pop("repository_id")

        url = d.pop("url", UNSET)

        webhook_delivery = cls(
            id=id,
            guid=guid,
            delivered_at=delivered_at,
            redelivery=redelivery,
            duration=duration,
            status=status,
            status_code=status_code,
            event=event,
            request=request,
            response=response,
            action=action,
            installation_id=installation_id,
            repository_id=repository_id,
            url=url,
        )

        webhook_delivery.additional_properties = d
        return webhook_delivery

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
