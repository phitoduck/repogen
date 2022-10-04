import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.code_scanning_analysis_tool import CodeScanningAnalysisTool
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodeScanningAnalysis")


@attr.s(auto_attribs=True)
class CodeScanningAnalysis:
    """
    Attributes:
        ref (str): The full Git reference, formatted as `refs/heads/<branch name>`,
            `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.
        commit_sha (str): The SHA of the commit to which the analysis you are uploading relates.
        analysis_key (str): Identifies the configuration under which the analysis was executed. For example, in GitHub
            Actions this includes the workflow filename and job name.
        environment (str): Identifies the variable values associated with the environment in which this analysis was
            performed.
        error (str):  Example: error reading field xyz.
        created_at (datetime.datetime): The time that the analysis was created in ISO 8601 format: `YYYY-MM-
            DDTHH:MM:SSZ`.
        results_count (int): The total number of results in the analysis.
        rules_count (int): The total number of rules used in the analysis.
        id (int): Unique identifier for this analysis.
        url (str): The REST API URL of the analysis resource.
        sarif_id (str): An identifier for the upload. Example: 6c81cd8e-b078-4ac3-a3be-1dad7dbd0b53.
        tool (CodeScanningAnalysisTool):
        deletable (bool):
        warning (str): Warning generated when processing the analysis Example: 123 results were ignored.
        category (Union[Unset, str]): Identifies the configuration under which the analysis was executed. Used to
            distinguish between multiple analyses for the same tool and commit, but performed on different languages or
            different parts of the code.
    """

    ref: str
    commit_sha: str
    analysis_key: str
    environment: str
    error: str
    created_at: datetime.datetime
    results_count: int
    rules_count: int
    id: int
    url: str
    sarif_id: str
    tool: CodeScanningAnalysisTool
    deletable: bool
    warning: str
    category: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref
        commit_sha = self.commit_sha
        analysis_key = self.analysis_key
        environment = self.environment
        error = self.error
        created_at = self.created_at.isoformat()

        results_count = self.results_count
        rules_count = self.rules_count
        id = self.id
        url = self.url
        sarif_id = self.sarif_id
        tool = self.tool.to_dict()

        deletable = self.deletable
        warning = self.warning
        category = self.category

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ref": ref,
                "commit_sha": commit_sha,
                "analysis_key": analysis_key,
                "environment": environment,
                "error": error,
                "created_at": created_at,
                "results_count": results_count,
                "rules_count": rules_count,
                "id": id,
                "url": url,
                "sarif_id": sarif_id,
                "tool": tool,
                "deletable": deletable,
                "warning": warning,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ref = d.pop("ref")

        commit_sha = d.pop("commit_sha")

        analysis_key = d.pop("analysis_key")

        environment = d.pop("environment")

        error = d.pop("error")

        created_at = isoparse(d.pop("created_at"))

        results_count = d.pop("results_count")

        rules_count = d.pop("rules_count")

        id = d.pop("id")

        url = d.pop("url")

        sarif_id = d.pop("sarif_id")

        tool = CodeScanningAnalysisTool.from_dict(d.pop("tool"))

        deletable = d.pop("deletable")

        warning = d.pop("warning")

        category = d.pop("category", UNSET)

        code_scanning_analysis = cls(
            ref=ref,
            commit_sha=commit_sha,
            analysis_key=analysis_key,
            environment=environment,
            error=error,
            created_at=created_at,
            results_count=results_count,
            rules_count=rules_count,
            id=id,
            url=url,
            sarif_id=sarif_id,
            tool=tool,
            deletable=deletable,
            warning=warning,
            category=category,
        )

        code_scanning_analysis.additional_properties = d
        return code_scanning_analysis

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
