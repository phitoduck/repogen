from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.secret_scanning_alert_resolution import SecretScanningAlertResolution
from ..models.secret_scanning_alert_state import SecretScanningAlertState
from ..types import UNSET, Unset

T = TypeVar("T", bound="SecretScanningupdateAlertJsonBody")


@attr.s(auto_attribs=True)
class SecretScanningupdateAlertJsonBody:
    """
    Attributes:
        state (SecretScanningAlertState): Sets the state of the secret scanning alert. You must provide `resolution`
            when you set the state to `resolved`.
        resolution (Union[Unset, None, SecretScanningAlertResolution]): **Required when the `state` is `resolved`.** The
            reason for resolving the alert.
        resolution_comment (Union[Unset, None, str]): An optional comment when closing an alert. Cannot be updated or
            deleted. Must be `null` when changing `state` to `open`.
    """

    state: SecretScanningAlertState
    resolution: Union[Unset, None, SecretScanningAlertResolution] = UNSET
    resolution_comment: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state.value

        resolution: Union[Unset, None, str] = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.value if self.resolution else None

        resolution_comment = self.resolution_comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if resolution_comment is not UNSET:
            field_dict["resolution_comment"] = resolution_comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state = SecretScanningAlertState(d.pop("state"))

        _resolution = d.pop("resolution", UNSET)
        resolution: Union[Unset, None, SecretScanningAlertResolution]
        if _resolution is None:
            resolution = None
        elif isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = SecretScanningAlertResolution(_resolution)

        resolution_comment = d.pop("resolution_comment", UNSET)

        secret_scanningupdate_alert_json_body = cls(
            state=state,
            resolution=resolution,
            resolution_comment=resolution_comment,
        )

        secret_scanningupdate_alert_json_body.additional_properties = d
        return secret_scanningupdate_alert_json_body

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
