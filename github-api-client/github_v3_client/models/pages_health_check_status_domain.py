from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PagesHealthCheckStatusDomain")


@attr.s(auto_attribs=True)
class PagesHealthCheckStatusDomain:
    """
    Attributes:
        host (Union[Unset, str]):
        uri (Union[Unset, str]):
        nameservers (Union[Unset, str]):
        dns_resolves (Union[Unset, bool]):
        is_proxied (Union[Unset, None, bool]):
        is_cloudflare_ip (Union[Unset, None, bool]):
        is_fastly_ip (Union[Unset, None, bool]):
        is_old_ip_address (Union[Unset, None, bool]):
        is_a_record (Union[Unset, None, bool]):
        has_cname_record (Union[Unset, None, bool]):
        has_mx_records_present (Union[Unset, None, bool]):
        is_valid_domain (Union[Unset, bool]):
        is_apex_domain (Union[Unset, bool]):
        should_be_a_record (Union[Unset, None, bool]):
        is_cname_to_github_user_domain (Union[Unset, None, bool]):
        is_cname_to_pages_dot_github_dot_com (Union[Unset, None, bool]):
        is_cname_to_fastly (Union[Unset, None, bool]):
        is_pointed_to_github_pages_ip (Union[Unset, None, bool]):
        is_non_github_pages_ip_present (Union[Unset, None, bool]):
        is_pages_domain (Union[Unset, bool]):
        is_served_by_pages (Union[Unset, None, bool]):
        is_valid (Union[Unset, bool]):
        reason (Union[Unset, None, str]):
        responds_to_https (Union[Unset, bool]):
        enforces_https (Union[Unset, bool]):
        https_error (Union[Unset, None, str]):
        is_https_eligible (Union[Unset, None, bool]):
        caa_error (Union[Unset, None, str]):
    """

    host: Union[Unset, str] = UNSET
    uri: Union[Unset, str] = UNSET
    nameservers: Union[Unset, str] = UNSET
    dns_resolves: Union[Unset, bool] = UNSET
    is_proxied: Union[Unset, None, bool] = UNSET
    is_cloudflare_ip: Union[Unset, None, bool] = UNSET
    is_fastly_ip: Union[Unset, None, bool] = UNSET
    is_old_ip_address: Union[Unset, None, bool] = UNSET
    is_a_record: Union[Unset, None, bool] = UNSET
    has_cname_record: Union[Unset, None, bool] = UNSET
    has_mx_records_present: Union[Unset, None, bool] = UNSET
    is_valid_domain: Union[Unset, bool] = UNSET
    is_apex_domain: Union[Unset, bool] = UNSET
    should_be_a_record: Union[Unset, None, bool] = UNSET
    is_cname_to_github_user_domain: Union[Unset, None, bool] = UNSET
    is_cname_to_pages_dot_github_dot_com: Union[Unset, None, bool] = UNSET
    is_cname_to_fastly: Union[Unset, None, bool] = UNSET
    is_pointed_to_github_pages_ip: Union[Unset, None, bool] = UNSET
    is_non_github_pages_ip_present: Union[Unset, None, bool] = UNSET
    is_pages_domain: Union[Unset, bool] = UNSET
    is_served_by_pages: Union[Unset, None, bool] = UNSET
    is_valid: Union[Unset, bool] = UNSET
    reason: Union[Unset, None, str] = UNSET
    responds_to_https: Union[Unset, bool] = UNSET
    enforces_https: Union[Unset, bool] = UNSET
    https_error: Union[Unset, None, str] = UNSET
    is_https_eligible: Union[Unset, None, bool] = UNSET
    caa_error: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host
        uri = self.uri
        nameservers = self.nameservers
        dns_resolves = self.dns_resolves
        is_proxied = self.is_proxied
        is_cloudflare_ip = self.is_cloudflare_ip
        is_fastly_ip = self.is_fastly_ip
        is_old_ip_address = self.is_old_ip_address
        is_a_record = self.is_a_record
        has_cname_record = self.has_cname_record
        has_mx_records_present = self.has_mx_records_present
        is_valid_domain = self.is_valid_domain
        is_apex_domain = self.is_apex_domain
        should_be_a_record = self.should_be_a_record
        is_cname_to_github_user_domain = self.is_cname_to_github_user_domain
        is_cname_to_pages_dot_github_dot_com = self.is_cname_to_pages_dot_github_dot_com
        is_cname_to_fastly = self.is_cname_to_fastly
        is_pointed_to_github_pages_ip = self.is_pointed_to_github_pages_ip
        is_non_github_pages_ip_present = self.is_non_github_pages_ip_present
        is_pages_domain = self.is_pages_domain
        is_served_by_pages = self.is_served_by_pages
        is_valid = self.is_valid
        reason = self.reason
        responds_to_https = self.responds_to_https
        enforces_https = self.enforces_https
        https_error = self.https_error
        is_https_eligible = self.is_https_eligible
        caa_error = self.caa_error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if uri is not UNSET:
            field_dict["uri"] = uri
        if nameservers is not UNSET:
            field_dict["nameservers"] = nameservers
        if dns_resolves is not UNSET:
            field_dict["dns_resolves"] = dns_resolves
        if is_proxied is not UNSET:
            field_dict["is_proxied"] = is_proxied
        if is_cloudflare_ip is not UNSET:
            field_dict["is_cloudflare_ip"] = is_cloudflare_ip
        if is_fastly_ip is not UNSET:
            field_dict["is_fastly_ip"] = is_fastly_ip
        if is_old_ip_address is not UNSET:
            field_dict["is_old_ip_address"] = is_old_ip_address
        if is_a_record is not UNSET:
            field_dict["is_a_record"] = is_a_record
        if has_cname_record is not UNSET:
            field_dict["has_cname_record"] = has_cname_record
        if has_mx_records_present is not UNSET:
            field_dict["has_mx_records_present"] = has_mx_records_present
        if is_valid_domain is not UNSET:
            field_dict["is_valid_domain"] = is_valid_domain
        if is_apex_domain is not UNSET:
            field_dict["is_apex_domain"] = is_apex_domain
        if should_be_a_record is not UNSET:
            field_dict["should_be_a_record"] = should_be_a_record
        if is_cname_to_github_user_domain is not UNSET:
            field_dict["is_cname_to_github_user_domain"] = is_cname_to_github_user_domain
        if is_cname_to_pages_dot_github_dot_com is not UNSET:
            field_dict["is_cname_to_pages_dot_github_dot_com"] = is_cname_to_pages_dot_github_dot_com
        if is_cname_to_fastly is not UNSET:
            field_dict["is_cname_to_fastly"] = is_cname_to_fastly
        if is_pointed_to_github_pages_ip is not UNSET:
            field_dict["is_pointed_to_github_pages_ip"] = is_pointed_to_github_pages_ip
        if is_non_github_pages_ip_present is not UNSET:
            field_dict["is_non_github_pages_ip_present"] = is_non_github_pages_ip_present
        if is_pages_domain is not UNSET:
            field_dict["is_pages_domain"] = is_pages_domain
        if is_served_by_pages is not UNSET:
            field_dict["is_served_by_pages"] = is_served_by_pages
        if is_valid is not UNSET:
            field_dict["is_valid"] = is_valid
        if reason is not UNSET:
            field_dict["reason"] = reason
        if responds_to_https is not UNSET:
            field_dict["responds_to_https"] = responds_to_https
        if enforces_https is not UNSET:
            field_dict["enforces_https"] = enforces_https
        if https_error is not UNSET:
            field_dict["https_error"] = https_error
        if is_https_eligible is not UNSET:
            field_dict["is_https_eligible"] = is_https_eligible
        if caa_error is not UNSET:
            field_dict["caa_error"] = caa_error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host", UNSET)

        uri = d.pop("uri", UNSET)

        nameservers = d.pop("nameservers", UNSET)

        dns_resolves = d.pop("dns_resolves", UNSET)

        is_proxied = d.pop("is_proxied", UNSET)

        is_cloudflare_ip = d.pop("is_cloudflare_ip", UNSET)

        is_fastly_ip = d.pop("is_fastly_ip", UNSET)

        is_old_ip_address = d.pop("is_old_ip_address", UNSET)

        is_a_record = d.pop("is_a_record", UNSET)

        has_cname_record = d.pop("has_cname_record", UNSET)

        has_mx_records_present = d.pop("has_mx_records_present", UNSET)

        is_valid_domain = d.pop("is_valid_domain", UNSET)

        is_apex_domain = d.pop("is_apex_domain", UNSET)

        should_be_a_record = d.pop("should_be_a_record", UNSET)

        is_cname_to_github_user_domain = d.pop("is_cname_to_github_user_domain", UNSET)

        is_cname_to_pages_dot_github_dot_com = d.pop("is_cname_to_pages_dot_github_dot_com", UNSET)

        is_cname_to_fastly = d.pop("is_cname_to_fastly", UNSET)

        is_pointed_to_github_pages_ip = d.pop("is_pointed_to_github_pages_ip", UNSET)

        is_non_github_pages_ip_present = d.pop("is_non_github_pages_ip_present", UNSET)

        is_pages_domain = d.pop("is_pages_domain", UNSET)

        is_served_by_pages = d.pop("is_served_by_pages", UNSET)

        is_valid = d.pop("is_valid", UNSET)

        reason = d.pop("reason", UNSET)

        responds_to_https = d.pop("responds_to_https", UNSET)

        enforces_https = d.pop("enforces_https", UNSET)

        https_error = d.pop("https_error", UNSET)

        is_https_eligible = d.pop("is_https_eligible", UNSET)

        caa_error = d.pop("caa_error", UNSET)

        pages_health_check_status_domain = cls(
            host=host,
            uri=uri,
            nameservers=nameservers,
            dns_resolves=dns_resolves,
            is_proxied=is_proxied,
            is_cloudflare_ip=is_cloudflare_ip,
            is_fastly_ip=is_fastly_ip,
            is_old_ip_address=is_old_ip_address,
            is_a_record=is_a_record,
            has_cname_record=has_cname_record,
            has_mx_records_present=has_mx_records_present,
            is_valid_domain=is_valid_domain,
            is_apex_domain=is_apex_domain,
            should_be_a_record=should_be_a_record,
            is_cname_to_github_user_domain=is_cname_to_github_user_domain,
            is_cname_to_pages_dot_github_dot_com=is_cname_to_pages_dot_github_dot_com,
            is_cname_to_fastly=is_cname_to_fastly,
            is_pointed_to_github_pages_ip=is_pointed_to_github_pages_ip,
            is_non_github_pages_ip_present=is_non_github_pages_ip_present,
            is_pages_domain=is_pages_domain,
            is_served_by_pages=is_served_by_pages,
            is_valid=is_valid,
            reason=reason,
            responds_to_https=responds_to_https,
            enforces_https=enforces_https,
            https_error=https_error,
            is_https_eligible=is_https_eligible,
            caa_error=caa_error,
        )

        pages_health_check_status_domain.additional_properties = d
        return pages_health_check_status_domain

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
