import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.pages_https_certificate_state import PagesHttpsCertificateState
from ..types import UNSET, Unset

T = TypeVar("T", bound="PagesHttpsCertificate")


@attr.s(auto_attribs=True)
class PagesHttpsCertificate:
    """
    Attributes:
        state (PagesHttpsCertificateState):  Example: approved.
        description (str):  Example: Certificate is approved.
        domains (List[str]): Array of the domain set and its alternate name (if it is configured) Example:
            ['example.com', 'www.example.com'].
        expires_at (Union[Unset, datetime.date]):
    """

    state: PagesHttpsCertificateState
    description: str
    domains: List[str]
    expires_at: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state.value

        description = self.description
        domains = self.domains

        expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "description": description,
                "domains": domains,
            }
        )
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state = PagesHttpsCertificateState(d.pop("state"))

        description = d.pop("description")

        domains = cast(List[str], d.pop("domains"))

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: Union[Unset, datetime.date]
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at).date()

        pages_https_certificate = cls(
            state=state,
            description=description,
            domains=domains,
            expires_at=expires_at,
        )

        pages_https_certificate.additional_properties = d
        return pages_https_certificate

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
