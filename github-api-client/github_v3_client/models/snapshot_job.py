from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnapshotJob")


@attr.s(auto_attribs=True)
class SnapshotJob:
    """
    Attributes:
        id (str): The external ID of the job. Example: 5622a2b0-63f6-4732-8c34-a1ab27e102a11.
        correlator (str): Correlator provides a key that is used to group snapshots submitted over time. Only the
            "latest" submitted snapshot for a given combination of `job.correlator` and `detector.name` will be considered
            when calculating a repository's current dependencies. Correlator should be as unique as it takes to distinguish
            all detection runs for a given "wave" of CI workflow you run. If you're using GitHub Actions, a good default
            value for this could be the environment variables GITHUB_WORKFLOW and GITHUB_JOB concatenated together. If
            you're using a build matrix, then you'll also need to add additional key(s) to distinguish between each
            submission inside a matrix variation. Example: yourworkflowname_yourjobname.
        html_url (Union[Unset, str]): The url for the job. Example: http://example.com/build.
    """

    id: str
    correlator: str
    html_url: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        correlator = self.correlator
        html_url = self.html_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "correlator": correlator,
            }
        )
        if html_url is not UNSET:
            field_dict["html_url"] = html_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        correlator = d.pop("correlator")

        html_url = d.pop("html_url", UNSET)

        snapshot_job = cls(
            id=id,
            correlator=correlator,
            html_url=html_url,
        )

        return snapshot_job
