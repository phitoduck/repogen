from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.diff_entry_status import DiffEntryStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiffEntry")


@attr.s(auto_attribs=True)
class DiffEntry:
    """Diff Entry

    Attributes:
        sha (str):  Example: bbcd538c8e72b8c175046e27cc8f907076331401.
        filename (str):  Example: file1.txt.
        status (DiffEntryStatus):  Example: added.
        additions (int):  Example: 103.
        deletions (int):  Example: 21.
        changes (int):  Example: 124.
        blob_url (str):  Example: https://github.com/octocat/Hello-
            World/blob/6dcb09b5b57875f334f61aebed695e2e4193db5e/file1.txt.
        raw_url (str):  Example: https://github.com/octocat/Hello-
            World/raw/6dcb09b5b57875f334f61aebed695e2e4193db5e/file1.txt.
        contents_url (str):  Example: https://api.github.com/repos/octocat/Hello-
            World/contents/file1.txt?ref=6dcb09b5b57875f334f61aebed695e2e4193db5e.
        patch (Union[Unset, str]):  Example: @@ -132,7 +132,7 @@ module Test @@ -1000,7 +1000,7 @@ module Test.
        previous_filename (Union[Unset, str]):  Example: file.txt.
    """

    sha: str
    filename: str
    status: DiffEntryStatus
    additions: int
    deletions: int
    changes: int
    blob_url: str
    raw_url: str
    contents_url: str
    patch: Union[Unset, str] = UNSET
    previous_filename: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sha = self.sha
        filename = self.filename
        status = self.status.value

        additions = self.additions
        deletions = self.deletions
        changes = self.changes
        blob_url = self.blob_url
        raw_url = self.raw_url
        contents_url = self.contents_url
        patch = self.patch
        previous_filename = self.previous_filename

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha": sha,
                "filename": filename,
                "status": status,
                "additions": additions,
                "deletions": deletions,
                "changes": changes,
                "blob_url": blob_url,
                "raw_url": raw_url,
                "contents_url": contents_url,
            }
        )
        if patch is not UNSET:
            field_dict["patch"] = patch
        if previous_filename is not UNSET:
            field_dict["previous_filename"] = previous_filename

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sha = d.pop("sha")

        filename = d.pop("filename")

        status = DiffEntryStatus(d.pop("status"))

        additions = d.pop("additions")

        deletions = d.pop("deletions")

        changes = d.pop("changes")

        blob_url = d.pop("blob_url")

        raw_url = d.pop("raw_url")

        contents_url = d.pop("contents_url")

        patch = d.pop("patch", UNSET)

        previous_filename = d.pop("previous_filename", UNSET)

        diff_entry = cls(
            sha=sha,
            filename=filename,
            status=status,
            additions=additions,
            deletions=deletions,
            changes=changes,
            blob_url=blob_url,
            raw_url=raw_url,
            contents_url=contents_url,
            patch=patch,
            previous_filename=previous_filename,
        )

        diff_entry.additional_properties = d
        return diff_entry

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
