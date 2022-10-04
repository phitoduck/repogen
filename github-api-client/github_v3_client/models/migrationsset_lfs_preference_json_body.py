from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.migrationsset_lfs_preference_json_body_use_lfs import MigrationssetLfsPreferenceJsonBodyUseLfs

T = TypeVar("T", bound="MigrationssetLfsPreferenceJsonBody")


@attr.s(auto_attribs=True)
class MigrationssetLfsPreferenceJsonBody:
    """
    Attributes:
        use_lfs (MigrationssetLfsPreferenceJsonBodyUseLfs): Whether to store large files during the import. `opt_in`
            means large files will be stored using Git LFS. `opt_out` means large files will be removed during the import.
    """

    use_lfs: MigrationssetLfsPreferenceJsonBodyUseLfs
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        use_lfs = self.use_lfs.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "use_lfs": use_lfs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        use_lfs = MigrationssetLfsPreferenceJsonBodyUseLfs(d.pop("use_lfs"))

        migrationsset_lfs_preference_json_body = cls(
            use_lfs=use_lfs,
        )

        migrationsset_lfs_preference_json_body.additional_properties = d
        return migrationsset_lfs_preference_json_body

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
