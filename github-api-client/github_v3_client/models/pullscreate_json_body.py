from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PullscreateJsonBody")


@attr.s(auto_attribs=True)
class PullscreateJsonBody:
    """
    Attributes:
        head (str): The name of the branch where your changes are implemented. For cross-repository pull requests in the
            same network, namespace `head` with a user like this: `username:branch`.
        base (str): The name of the branch you want the changes pulled into. This should be an existing branch on the
            current repository. You cannot submit a pull request to one repository that requests a merge to a base of
            another repository.
        title (Union[Unset, str]): The title of the new pull request. Required unless `issue` is specified.
        body (Union[Unset, str]): The contents of the pull request.
        maintainer_can_modify (Union[Unset, bool]): Indicates whether [maintainers can
            modify](https://docs.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) the
            pull request.
        draft (Union[Unset, bool]): Indicates whether the pull request is a draft. See "[Draft Pull
            Requests](https://docs.github.com/en/articles/about-pull-requests#draft-pull-requests)" in the GitHub Help
            documentation to learn more.
        issue (Union[Unset, int]): An issue in the repository to convert to a pull request. The issue title, body, and
            comments will become the title, body, and comments on the new pull request. Required unless `title` is
            specified. Example: 1.
    """

    head: str
    base: str
    title: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    maintainer_can_modify: Union[Unset, bool] = UNSET
    draft: Union[Unset, bool] = UNSET
    issue: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        head = self.head
        base = self.base
        title = self.title
        body = self.body
        maintainer_can_modify = self.maintainer_can_modify
        draft = self.draft
        issue = self.issue

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "head": head,
                "base": base,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body
        if maintainer_can_modify is not UNSET:
            field_dict["maintainer_can_modify"] = maintainer_can_modify
        if draft is not UNSET:
            field_dict["draft"] = draft
        if issue is not UNSET:
            field_dict["issue"] = issue

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        head = d.pop("head")

        base = d.pop("base")

        title = d.pop("title", UNSET)

        body = d.pop("body", UNSET)

        maintainer_can_modify = d.pop("maintainer_can_modify", UNSET)

        draft = d.pop("draft", UNSET)

        issue = d.pop("issue", UNSET)

        pullscreate_json_body = cls(
            head=head,
            base=base,
            title=title,
            body=body,
            maintainer_can_modify=maintainer_can_modify,
            draft=draft,
            issue=issue,
        )

        pullscreate_json_body.additional_properties = d
        return pullscreate_json_body

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
