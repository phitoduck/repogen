from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdateReleaseJsonBody")


@attr.s(auto_attribs=True)
class ReposupdateReleaseJsonBody:
    """
    Attributes:
        tag_name (Union[Unset, str]): The name of the tag.
        target_commitish (Union[Unset, str]): Specifies the commitish value that determines where the Git tag is created
            from. Can be any branch or commit SHA. Unused if the Git tag already exists. Default: the repository's default
            branch (usually `master`).
        name (Union[Unset, str]): The name of the release.
        body (Union[Unset, str]): Text describing the contents of the tag.
        draft (Union[Unset, bool]): `true` makes the release a draft, and `false` publishes the release.
        prerelease (Union[Unset, bool]): `true` to identify the release as a prerelease, `false` to identify the release
            as a full release.
        discussion_category_name (Union[Unset, str]): If specified, a discussion of the specified category is created
            and linked to the release. The value must be a category that already exists in the repository. If there is
            already a discussion linked to the release, this parameter is ignored. For more information, see "[Managing
            categories for discussions in your repository](https://docs.github.com/discussions/managing-discussions-for-
            your-community/managing-categories-for-discussions-in-your-repository)."
    """

    tag_name: Union[Unset, str] = UNSET
    target_commitish: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    draft: Union[Unset, bool] = UNSET
    prerelease: Union[Unset, bool] = UNSET
    discussion_category_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tag_name = self.tag_name
        target_commitish = self.target_commitish
        name = self.name
        body = self.body
        draft = self.draft
        prerelease = self.prerelease
        discussion_category_name = self.discussion_category_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tag_name is not UNSET:
            field_dict["tag_name"] = tag_name
        if target_commitish is not UNSET:
            field_dict["target_commitish"] = target_commitish
        if name is not UNSET:
            field_dict["name"] = name
        if body is not UNSET:
            field_dict["body"] = body
        if draft is not UNSET:
            field_dict["draft"] = draft
        if prerelease is not UNSET:
            field_dict["prerelease"] = prerelease
        if discussion_category_name is not UNSET:
            field_dict["discussion_category_name"] = discussion_category_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tag_name = d.pop("tag_name", UNSET)

        target_commitish = d.pop("target_commitish", UNSET)

        name = d.pop("name", UNSET)

        body = d.pop("body", UNSET)

        draft = d.pop("draft", UNSET)

        prerelease = d.pop("prerelease", UNSET)

        discussion_category_name = d.pop("discussion_category_name", UNSET)

        reposupdate_release_json_body = cls(
            tag_name=tag_name,
            target_commitish=target_commitish,
            name=name,
            body=body,
            draft=draft,
            prerelease=prerelease,
            discussion_category_name=discussion_category_name,
        )

        reposupdate_release_json_body.additional_properties = d
        return reposupdate_release_json_body

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
