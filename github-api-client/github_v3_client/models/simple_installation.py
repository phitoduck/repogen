from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SimpleInstallation")


@attr.s(auto_attribs=True)
class SimpleInstallation:
    """Simple Installation

    Attributes:
        id (int): The ID of the installation. Example: 1.
        node_id (str): The global node ID of the installation. Example: MDQ6VXNlcjU4MzIzMQ==.
    """

    id: int
    node_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "node_id": node_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        node_id = d.pop("node_id")

        simple_installation = cls(
            id=id,
            node_id=node_id,
        )

        simple_installation.additional_properties = d
        return simple_installation

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
