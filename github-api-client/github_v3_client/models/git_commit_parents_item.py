from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GitCommitParentsItem")


@attr.s(auto_attribs=True)
class GitCommitParentsItem:
    """
    Attributes:
        sha (str): SHA for the commit Example: 7638417db6d59f3c431d3e1f261cc637155684cd.
        url (str):
        html_url (str):
    """

    sha: str
    url: str
    html_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sha = self.sha
        url = self.url
        html_url = self.html_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha": sha,
                "url": url,
                "html_url": html_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sha = d.pop("sha")

        url = d.pop("url")

        html_url = d.pop("html_url")

        git_commit_parents_item = cls(
            sha=sha,
            url=url,
            html_url=html_url,
        )

        git_commit_parents_item.additional_properties = d
        return git_commit_parents_item

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
