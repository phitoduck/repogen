import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FetchesInformationAboutAnExportOfACodespace")


@attr.s(auto_attribs=True)
class FetchesInformationAboutAnExportOfACodespace:
    """An export of a codespace. Also, latest export details for a codespace can be fetched with id = latest

    Attributes:
        state (Union[Unset, None, str]): State of the latest export Example: succeeded | failed | in_progress.
        completed_at (Union[Unset, None, datetime.datetime]): Completion time of the last export operation Example:
            2021-01-01T19:01:12Z.
        branch (Union[Unset, None, str]): Name of the exported branch Example: codespace-monalisa-octocat-hello-
            world-g4wpq6h95q.
        sha (Union[Unset, None, str]): Git commit SHA of the exported branch Example:
            fd95a81ca01e48ede9f39c799ecbcef817b8a3b2.
        id (Union[Unset, str]): Id for the export details Example: latest.
        export_url (Union[Unset, str]): Url for fetching export details Example:
            https://api.github.com/user/codespaces/:name/exports/latest.
        html_url (Union[Unset, None, str]): Web url for the exported branch Example: https://github.com/octocat/hello-
            world/tree/:branch.
    """

    state: Union[Unset, None, str] = UNSET
    completed_at: Union[Unset, None, datetime.datetime] = UNSET
    branch: Union[Unset, None, str] = UNSET
    sha: Union[Unset, None, str] = UNSET
    id: Union[Unset, str] = UNSET
    export_url: Union[Unset, str] = UNSET
    html_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state = self.state
        completed_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat() if self.completed_at else None

        branch = self.branch
        sha = self.sha
        id = self.id
        export_url = self.export_url
        html_url = self.html_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if branch is not UNSET:
            field_dict["branch"] = branch
        if sha is not UNSET:
            field_dict["sha"] = sha
        if id is not UNSET:
            field_dict["id"] = id
        if export_url is not UNSET:
            field_dict["export_url"] = export_url
        if html_url is not UNSET:
            field_dict["html_url"] = html_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state = d.pop("state", UNSET)

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, None, datetime.datetime]
        if _completed_at is None:
            completed_at = None
        elif isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        branch = d.pop("branch", UNSET)

        sha = d.pop("sha", UNSET)

        id = d.pop("id", UNSET)

        export_url = d.pop("export_url", UNSET)

        html_url = d.pop("html_url", UNSET)

        fetches_information_about_an_export_of_a_codespace = cls(
            state=state,
            completed_at=completed_at,
            branch=branch,
            sha=sha,
            id=id,
            export_url=export_url,
            html_url=html_url,
        )

        fetches_information_about_an_export_of_a_codespace.additional_properties = d
        return fetches_information_about_an_export_of_a_codespace

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
