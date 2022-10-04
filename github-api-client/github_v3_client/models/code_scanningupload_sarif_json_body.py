import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodeScanninguploadSarifJsonBody")


@attr.s(auto_attribs=True)
class CodeScanninguploadSarifJsonBody:
    """
    Attributes:
        commit_sha (str): The SHA of the commit to which the analysis you are uploading relates.
        ref (str): The full Git reference, formatted as `refs/heads/<branch name>`,
            `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.
        sarif (str): A Base64 string representing the SARIF file to upload. You must first compress your SARIF file
            using [`gzip`](http://www.gnu.org/software/gzip/manual/gzip.html) and then translate the contents of the file
            into a Base64 encoding string. For more information, see "[SARIF support for code
            scanning](https://docs.github.com/code-security/secure-coding/sarif-support-for-code-scanning)."
        checkout_uri (Union[Unset, str]): The base directory used in the analysis, as it appears in the SARIF file.
            This property is used to convert file paths from absolute to relative, so that alerts can be mapped to their
            correct location in the repository. Example: file:///github/workspace/.
        started_at (Union[Unset, datetime.datetime]): The time that the analysis run began. This is a timestamp in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
        tool_name (Union[Unset, str]): The name of the tool used to generate the code scanning analysis. If this
            parameter is not used, the tool name defaults to "API". If the uploaded SARIF contains a tool GUID, this will be
            available for filtering using the `tool_guid` parameter of operations such as `GET /repos/{owner}/{repo}/code-
            scanning/alerts`.
    """

    commit_sha: str
    ref: str
    sarif: str
    checkout_uri: Union[Unset, str] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    tool_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commit_sha = self.commit_sha
        ref = self.ref
        sarif = self.sarif
        checkout_uri = self.checkout_uri
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        tool_name = self.tool_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commit_sha": commit_sha,
                "ref": ref,
                "sarif": sarif,
            }
        )
        if checkout_uri is not UNSET:
            field_dict["checkout_uri"] = checkout_uri
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if tool_name is not UNSET:
            field_dict["tool_name"] = tool_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        commit_sha = d.pop("commit_sha")

        ref = d.pop("ref")

        sarif = d.pop("sarif")

        checkout_uri = d.pop("checkout_uri", UNSET)

        _started_at = d.pop("started_at", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        tool_name = d.pop("tool_name", UNSET)

        code_scanningupload_sarif_json_body = cls(
            commit_sha=commit_sha,
            ref=ref,
            sarif=sarif,
            checkout_uri=checkout_uri,
            started_at=started_at,
            tool_name=tool_name,
        )

        code_scanningupload_sarif_json_body.additional_properties = d
        return code_scanningupload_sarif_json_body

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
