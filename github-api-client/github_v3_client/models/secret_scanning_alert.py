import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.secret_scanning_alert_resolution import SecretScanningAlertResolution
from ..models.secret_scanning_alert_state import SecretScanningAlertState
from ..models.simple_user import SimpleUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="SecretScanningAlert")


@attr.s(auto_attribs=True)
class SecretScanningAlert:
    """
    Attributes:
        number (Union[Unset, int]): The security alert number.
        created_at (Union[Unset, datetime.datetime]): The time that the alert was created in ISO 8601 format: `YYYY-MM-
            DDTHH:MM:SSZ`.
        updated_at (Union[Unset, datetime.datetime]): The time that the alert was last updated in ISO 8601 format:
            `YYYY-MM-DDTHH:MM:SSZ`.
        url (Union[Unset, str]): The REST API URL of the alert resource.
        html_url (Union[Unset, str]): The GitHub URL of the alert resource.
        locations_url (Union[Unset, str]): The REST API URL of the code locations for this alert.
        state (Union[Unset, SecretScanningAlertState]): Sets the state of the secret scanning alert. You must provide
            `resolution` when you set the state to `resolved`.
        resolution (Union[Unset, None, SecretScanningAlertResolution]): **Required when the `state` is `resolved`.** The
            reason for resolving the alert.
        resolved_at (Union[Unset, None, datetime.datetime]): The time that the alert was resolved in ISO 8601 format:
            `YYYY-MM-DDTHH:MM:SSZ`.
        resolved_by (Union[Unset, None, SimpleUser]): Simple User
        secret_type (Union[Unset, str]): The type of secret that secret scanning detected.
        secret_type_display_name (Union[Unset, str]): User-friendly name for the detected secret, matching the
            `secret_type`.
            For a list of built-in patterns, see "[Secret scanning patterns](https://docs.github.com/code-security/secret-
            scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)."
        secret (Union[Unset, str]): The secret that was detected.
        push_protection_bypassed (Union[Unset, None, bool]): Whether push protection was bypassed for the detected
            secret.
        push_protection_bypassed_by (Union[Unset, None, SimpleUser]): Simple User
        push_protection_bypassed_at (Union[Unset, None, datetime.datetime]): The time that push protection was bypassed
            in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
        resolution_comment (Union[Unset, None, str]): The comment that was optionally added when this alert was closed
    """

    number: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    url: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    locations_url: Union[Unset, str] = UNSET
    state: Union[Unset, SecretScanningAlertState] = UNSET
    resolution: Union[Unset, None, SecretScanningAlertResolution] = UNSET
    resolved_at: Union[Unset, None, datetime.datetime] = UNSET
    resolved_by: Union[Unset, None, SimpleUser] = UNSET
    secret_type: Union[Unset, str] = UNSET
    secret_type_display_name: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    push_protection_bypassed: Union[Unset, None, bool] = UNSET
    push_protection_bypassed_by: Union[Unset, None, SimpleUser] = UNSET
    push_protection_bypassed_at: Union[Unset, None, datetime.datetime] = UNSET
    resolution_comment: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        url = self.url
        html_url = self.html_url
        locations_url = self.locations_url
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        resolution: Union[Unset, None, str] = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.value if self.resolution else None

        resolved_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.resolved_at, Unset):
            resolved_at = self.resolved_at.isoformat() if self.resolved_at else None

        resolved_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.resolved_by, Unset):
            resolved_by = self.resolved_by.to_dict() if self.resolved_by else None

        secret_type = self.secret_type
        secret_type_display_name = self.secret_type_display_name
        secret = self.secret
        push_protection_bypassed = self.push_protection_bypassed
        push_protection_bypassed_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.push_protection_bypassed_by, Unset):
            push_protection_bypassed_by = (
                self.push_protection_bypassed_by.to_dict() if self.push_protection_bypassed_by else None
            )

        push_protection_bypassed_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.push_protection_bypassed_at, Unset):
            push_protection_bypassed_at = (
                self.push_protection_bypassed_at.isoformat() if self.push_protection_bypassed_at else None
            )

        resolution_comment = self.resolution_comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if locations_url is not UNSET:
            field_dict["locations_url"] = locations_url
        if state is not UNSET:
            field_dict["state"] = state
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at
        if resolved_by is not UNSET:
            field_dict["resolved_by"] = resolved_by
        if secret_type is not UNSET:
            field_dict["secret_type"] = secret_type
        if secret_type_display_name is not UNSET:
            field_dict["secret_type_display_name"] = secret_type_display_name
        if secret is not UNSET:
            field_dict["secret"] = secret
        if push_protection_bypassed is not UNSET:
            field_dict["push_protection_bypassed"] = push_protection_bypassed
        if push_protection_bypassed_by is not UNSET:
            field_dict["push_protection_bypassed_by"] = push_protection_bypassed_by
        if push_protection_bypassed_at is not UNSET:
            field_dict["push_protection_bypassed_at"] = push_protection_bypassed_at
        if resolution_comment is not UNSET:
            field_dict["resolution_comment"] = resolution_comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        url = d.pop("url", UNSET)

        html_url = d.pop("html_url", UNSET)

        locations_url = d.pop("locations_url", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, SecretScanningAlertState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = SecretScanningAlertState(_state)

        _resolution = d.pop("resolution", UNSET)
        resolution: Union[Unset, None, SecretScanningAlertResolution]
        if _resolution is None:
            resolution = None
        elif isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = SecretScanningAlertResolution(_resolution)

        _resolved_at = d.pop("resolved_at", UNSET)
        resolved_at: Union[Unset, None, datetime.datetime]
        if _resolved_at is None:
            resolved_at = None
        elif isinstance(_resolved_at, Unset):
            resolved_at = UNSET
        else:
            resolved_at = isoparse(_resolved_at)

        _resolved_by = d.pop("resolved_by", UNSET)
        resolved_by: Union[Unset, None, SimpleUser]
        if _resolved_by is None:
            resolved_by = None
        elif isinstance(_resolved_by, Unset):
            resolved_by = UNSET
        else:
            resolved_by = SimpleUser.from_dict(_resolved_by)

        secret_type = d.pop("secret_type", UNSET)

        secret_type_display_name = d.pop("secret_type_display_name", UNSET)

        secret = d.pop("secret", UNSET)

        push_protection_bypassed = d.pop("push_protection_bypassed", UNSET)

        _push_protection_bypassed_by = d.pop("push_protection_bypassed_by", UNSET)
        push_protection_bypassed_by: Union[Unset, None, SimpleUser]
        if _push_protection_bypassed_by is None:
            push_protection_bypassed_by = None
        elif isinstance(_push_protection_bypassed_by, Unset):
            push_protection_bypassed_by = UNSET
        else:
            push_protection_bypassed_by = SimpleUser.from_dict(_push_protection_bypassed_by)

        _push_protection_bypassed_at = d.pop("push_protection_bypassed_at", UNSET)
        push_protection_bypassed_at: Union[Unset, None, datetime.datetime]
        if _push_protection_bypassed_at is None:
            push_protection_bypassed_at = None
        elif isinstance(_push_protection_bypassed_at, Unset):
            push_protection_bypassed_at = UNSET
        else:
            push_protection_bypassed_at = isoparse(_push_protection_bypassed_at)

        resolution_comment = d.pop("resolution_comment", UNSET)

        secret_scanning_alert = cls(
            number=number,
            created_at=created_at,
            updated_at=updated_at,
            url=url,
            html_url=html_url,
            locations_url=locations_url,
            state=state,
            resolution=resolution,
            resolved_at=resolved_at,
            resolved_by=resolved_by,
            secret_type=secret_type,
            secret_type_display_name=secret_type_display_name,
            secret=secret,
            push_protection_bypassed=push_protection_bypassed,
            push_protection_bypassed_by=push_protection_bypassed_by,
            push_protection_bypassed_at=push_protection_bypassed_at,
            resolution_comment=resolution_comment,
        )

        secret_scanning_alert.additional_properties = d
        return secret_scanning_alert

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
