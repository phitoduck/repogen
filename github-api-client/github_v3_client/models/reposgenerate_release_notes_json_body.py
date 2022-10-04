from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposgenerateReleaseNotesJsonBody")


@attr.s(auto_attribs=True)
class ReposgenerateReleaseNotesJsonBody:
    """
    Attributes:
        tag_name (str): The tag name for the release. This can be an existing tag or a new one.
        target_commitish (Union[Unset, str]): Specifies the commitish value that will be the target for the release's
            tag. Required if the supplied tag_name does not reference an existing tag. Ignored if the tag_name already
            exists.
        previous_tag_name (Union[Unset, str]): The name of the previous tag to use as the starting point for the release
            notes. Use to manually specify the range for the set of changes considered as part this release.
        configuration_file_path (Union[Unset, str]): Specifies a path to a file in the repository containing
            configuration settings used for generating the release notes. If unspecified, the configuration file located in
            the repository at '.github/release.yml' or '.github/release.yaml' will be used. If that is not present, the
            default configuration will be used.
    """

    tag_name: str
    target_commitish: Union[Unset, str] = UNSET
    previous_tag_name: Union[Unset, str] = UNSET
    configuration_file_path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tag_name = self.tag_name
        target_commitish = self.target_commitish
        previous_tag_name = self.previous_tag_name
        configuration_file_path = self.configuration_file_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag_name": tag_name,
            }
        )
        if target_commitish is not UNSET:
            field_dict["target_commitish"] = target_commitish
        if previous_tag_name is not UNSET:
            field_dict["previous_tag_name"] = previous_tag_name
        if configuration_file_path is not UNSET:
            field_dict["configuration_file_path"] = configuration_file_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tag_name = d.pop("tag_name")

        target_commitish = d.pop("target_commitish", UNSET)

        previous_tag_name = d.pop("previous_tag_name", UNSET)

        configuration_file_path = d.pop("configuration_file_path", UNSET)

        reposgenerate_release_notes_json_body = cls(
            tag_name=tag_name,
            target_commitish=target_commitish,
            previous_tag_name=previous_tag_name,
            configuration_file_path=configuration_file_path,
        )

        reposgenerate_release_notes_json_body.additional_properties = d
        return reposgenerate_release_notes_json_body

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
