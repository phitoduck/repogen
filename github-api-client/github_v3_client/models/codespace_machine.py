from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.codespace_machine_prebuild_availability import CodespaceMachinePrebuildAvailability

T = TypeVar("T", bound="CodespaceMachine")


@attr.s(auto_attribs=True)
class CodespaceMachine:
    """A description of the machine powering a codespace.

    Attributes:
        name (str): The name of the machine. Example: standardLinux.
        display_name (str): The display name of the machine includes cores, memory, and storage. Example: 4 cores, 8 GB
            RAM, 64 GB storage.
        operating_system (str): The operating system of the machine. Example: linux.
        storage_in_bytes (int): How much storage is available to the codespace. Example: 68719476736.
        memory_in_bytes (int): How much memory is available to the codespace. Example: 8589934592.
        cpus (int): How many cores are available to the codespace. Example: 4.
        prebuild_availability (Optional[CodespaceMachinePrebuildAvailability]): Whether a prebuild is currently
            available when creating a codespace for this machine and repository. If a branch was not specified as a ref, the
            default branch will be assumed. Value will be "null" if prebuilds are not supported or prebuild availability
            could not be determined. Value will be "none" if no prebuild is available. Latest values "ready" and
            "in_progress" indicate the prebuild availability status. Example: ready.
    """

    name: str
    display_name: str
    operating_system: str
    storage_in_bytes: int
    memory_in_bytes: int
    cpus: int
    prebuild_availability: Optional[CodespaceMachinePrebuildAvailability]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        display_name = self.display_name
        operating_system = self.operating_system
        storage_in_bytes = self.storage_in_bytes
        memory_in_bytes = self.memory_in_bytes
        cpus = self.cpus
        prebuild_availability = self.prebuild_availability.value if self.prebuild_availability else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "display_name": display_name,
                "operating_system": operating_system,
                "storage_in_bytes": storage_in_bytes,
                "memory_in_bytes": memory_in_bytes,
                "cpus": cpus,
                "prebuild_availability": prebuild_availability,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("display_name")

        operating_system = d.pop("operating_system")

        storage_in_bytes = d.pop("storage_in_bytes")

        memory_in_bytes = d.pop("memory_in_bytes")

        cpus = d.pop("cpus")

        _prebuild_availability = d.pop("prebuild_availability")
        prebuild_availability: Optional[CodespaceMachinePrebuildAvailability]
        if _prebuild_availability is None:
            prebuild_availability = None
        else:
            prebuild_availability = CodespaceMachinePrebuildAvailability(_prebuild_availability)

        codespace_machine = cls(
            name=name,
            display_name=display_name,
            operating_system=operating_system,
            storage_in_bytes=storage_in_bytes,
            memory_in_bytes=memory_in_bytes,
            cpus=cpus,
            prebuild_availability=prebuild_availability,
        )

        codespace_machine.additional_properties = d
        return codespace_machine

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
