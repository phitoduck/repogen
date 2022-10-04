from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionsBillingUsageMinutesUsedBreakdown")


@attr.s(auto_attribs=True)
class ActionsBillingUsageMinutesUsedBreakdown:
    """
    Attributes:
        ubuntu (Union[Unset, int]): Total minutes used on Ubuntu runner machines.
        macos (Union[Unset, int]): Total minutes used on macOS runner machines.
        windows (Union[Unset, int]): Total minutes used on Windows runner machines.
        ubuntu_4_core (Union[Unset, int]): Total minutes used on Ubuntu 4 core runner machines.
        ubuntu_8_core (Union[Unset, int]): Total minutes used on Ubuntu 8 core runner machines.
        ubuntu_16_core (Union[Unset, int]): Total minutes used on Ubuntu 16 core runner machines.
        ubuntu_32_core (Union[Unset, int]): Total minutes used on Ubuntu 32 core runner machines.
        ubuntu_64_core (Union[Unset, int]): Total minutes used on Ubuntu 64 core runner machines.
        windows_4_core (Union[Unset, int]): Total minutes used on Windows 4 core runner machines.
        windows_8_core (Union[Unset, int]): Total minutes used on Windows 8 core runner machines.
        windows_16_core (Union[Unset, int]): Total minutes used on Windows 16 core runner machines.
        windows_32_core (Union[Unset, int]): Total minutes used on Windows 32 core runner machines.
        windows_64_core (Union[Unset, int]): Total minutes used on Windows 64 core runner machines.
        total (Union[Unset, int]): Total minutes used on all runner machines.
    """

    ubuntu: Union[Unset, int] = UNSET
    macos: Union[Unset, int] = UNSET
    windows: Union[Unset, int] = UNSET
    ubuntu_4_core: Union[Unset, int] = UNSET
    ubuntu_8_core: Union[Unset, int] = UNSET
    ubuntu_16_core: Union[Unset, int] = UNSET
    ubuntu_32_core: Union[Unset, int] = UNSET
    ubuntu_64_core: Union[Unset, int] = UNSET
    windows_4_core: Union[Unset, int] = UNSET
    windows_8_core: Union[Unset, int] = UNSET
    windows_16_core: Union[Unset, int] = UNSET
    windows_32_core: Union[Unset, int] = UNSET
    windows_64_core: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ubuntu = self.ubuntu
        macos = self.macos
        windows = self.windows
        ubuntu_4_core = self.ubuntu_4_core
        ubuntu_8_core = self.ubuntu_8_core
        ubuntu_16_core = self.ubuntu_16_core
        ubuntu_32_core = self.ubuntu_32_core
        ubuntu_64_core = self.ubuntu_64_core
        windows_4_core = self.windows_4_core
        windows_8_core = self.windows_8_core
        windows_16_core = self.windows_16_core
        windows_32_core = self.windows_32_core
        windows_64_core = self.windows_64_core
        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ubuntu is not UNSET:
            field_dict["UBUNTU"] = ubuntu
        if macos is not UNSET:
            field_dict["MACOS"] = macos
        if windows is not UNSET:
            field_dict["WINDOWS"] = windows
        if ubuntu_4_core is not UNSET:
            field_dict["ubuntu_4_core"] = ubuntu_4_core
        if ubuntu_8_core is not UNSET:
            field_dict["ubuntu_8_core"] = ubuntu_8_core
        if ubuntu_16_core is not UNSET:
            field_dict["ubuntu_16_core"] = ubuntu_16_core
        if ubuntu_32_core is not UNSET:
            field_dict["ubuntu_32_core"] = ubuntu_32_core
        if ubuntu_64_core is not UNSET:
            field_dict["ubuntu_64_core"] = ubuntu_64_core
        if windows_4_core is not UNSET:
            field_dict["windows_4_core"] = windows_4_core
        if windows_8_core is not UNSET:
            field_dict["windows_8_core"] = windows_8_core
        if windows_16_core is not UNSET:
            field_dict["windows_16_core"] = windows_16_core
        if windows_32_core is not UNSET:
            field_dict["windows_32_core"] = windows_32_core
        if windows_64_core is not UNSET:
            field_dict["windows_64_core"] = windows_64_core
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ubuntu = d.pop("UBUNTU", UNSET)

        macos = d.pop("MACOS", UNSET)

        windows = d.pop("WINDOWS", UNSET)

        ubuntu_4_core = d.pop("ubuntu_4_core", UNSET)

        ubuntu_8_core = d.pop("ubuntu_8_core", UNSET)

        ubuntu_16_core = d.pop("ubuntu_16_core", UNSET)

        ubuntu_32_core = d.pop("ubuntu_32_core", UNSET)

        ubuntu_64_core = d.pop("ubuntu_64_core", UNSET)

        windows_4_core = d.pop("windows_4_core", UNSET)

        windows_8_core = d.pop("windows_8_core", UNSET)

        windows_16_core = d.pop("windows_16_core", UNSET)

        windows_32_core = d.pop("windows_32_core", UNSET)

        windows_64_core = d.pop("windows_64_core", UNSET)

        total = d.pop("total", UNSET)

        actions_billing_usage_minutes_used_breakdown = cls(
            ubuntu=ubuntu,
            macos=macos,
            windows=windows,
            ubuntu_4_core=ubuntu_4_core,
            ubuntu_8_core=ubuntu_8_core,
            ubuntu_16_core=ubuntu_16_core,
            ubuntu_32_core=ubuntu_32_core,
            ubuntu_64_core=ubuntu_64_core,
            windows_4_core=windows_4_core,
            windows_8_core=windows_8_core,
            windows_16_core=windows_16_core,
            windows_32_core=windows_32_core,
            windows_64_core=windows_64_core,
            total=total,
        )

        actions_billing_usage_minutes_used_breakdown.additional_properties = d
        return actions_billing_usage_minutes_used_breakdown

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
