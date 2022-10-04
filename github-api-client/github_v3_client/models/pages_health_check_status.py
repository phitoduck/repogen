from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pages_health_check_status_alt_domain import PagesHealthCheckStatusAltDomain
from ..models.pages_health_check_status_domain import PagesHealthCheckStatusDomain
from ..types import UNSET, Unset

T = TypeVar("T", bound="PagesHealthCheckStatus")


@attr.s(auto_attribs=True)
class PagesHealthCheckStatus:
    """Pages Health Check Status

    Attributes:
        domain (Union[Unset, PagesHealthCheckStatusDomain]):
        alt_domain (Union[Unset, None, PagesHealthCheckStatusAltDomain]):
    """

    domain: Union[Unset, PagesHealthCheckStatusDomain] = UNSET
    alt_domain: Union[Unset, None, PagesHealthCheckStatusAltDomain] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.domain, Unset):
            domain = self.domain.to_dict()

        alt_domain: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.alt_domain, Unset):
            alt_domain = self.alt_domain.to_dict() if self.alt_domain else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if alt_domain is not UNSET:
            field_dict["alt_domain"] = alt_domain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _domain = d.pop("domain", UNSET)
        domain: Union[Unset, PagesHealthCheckStatusDomain]
        if isinstance(_domain, Unset):
            domain = UNSET
        else:
            domain = PagesHealthCheckStatusDomain.from_dict(_domain)

        _alt_domain = d.pop("alt_domain", UNSET)
        alt_domain: Union[Unset, None, PagesHealthCheckStatusAltDomain]
        if _alt_domain is None:
            alt_domain = None
        elif isinstance(_alt_domain, Unset):
            alt_domain = UNSET
        else:
            alt_domain = PagesHealthCheckStatusAltDomain.from_dict(_alt_domain)

        pages_health_check_status = cls(
            domain=domain,
            alt_domain=alt_domain,
        )

        pages_health_check_status.additional_properties = d
        return pages_health_check_status

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
