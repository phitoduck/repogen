import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.metadata import Metadata
from ..models.snapshot_detector import SnapshotDetector
from ..models.snapshot_job import SnapshotJob
from ..models.snapshot_manifests import SnapshotManifests
from ..types import UNSET, Unset

T = TypeVar("T", bound="Snapshot")


@attr.s(auto_attribs=True)
class Snapshot:
    """Create a new snapshot of a repository's dependencies.

    Attributes:
        version (int): The version of the repository snapshot submission.
        job (SnapshotJob):
        sha (str): The commit SHA associated with this dependency snapshot. Example:
            ddc951f4b1293222421f2c8df679786153acf689.
        ref (str): The repository branch that triggered this snapshot. Example: refs/heads/main.
        detector (SnapshotDetector): A description of the detector used.
        scanned (datetime.datetime): The time at which the snapshot was scanned. Example: 2020-06-13T14:52:50-05:00.
        metadata (Union[Unset, Metadata]): User-defined metadata to store domain-specific information limited to 8 keys
            with scalar values.
        manifests (Union[Unset, SnapshotManifests]): A collection of package manifests, which are a collection of
            related dependencies declared in a file or representing a logical group of dependencies.
    """

    version: int
    job: SnapshotJob
    sha: str
    ref: str
    detector: SnapshotDetector
    scanned: datetime.datetime
    metadata: Union[Unset, Metadata] = UNSET
    manifests: Union[Unset, SnapshotManifests] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        job = self.job.to_dict()

        sha = self.sha
        ref = self.ref
        detector = self.detector.to_dict()

        scanned = self.scanned.isoformat()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        manifests: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.manifests, Unset):
            manifests = self.manifests.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "version": version,
                "job": job,
                "sha": sha,
                "ref": ref,
                "detector": detector,
                "scanned": scanned,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if manifests is not UNSET:
            field_dict["manifests"] = manifests

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version")

        job = SnapshotJob.from_dict(d.pop("job"))

        sha = d.pop("sha")

        ref = d.pop("ref")

        detector = SnapshotDetector.from_dict(d.pop("detector"))

        scanned = isoparse(d.pop("scanned"))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        _manifests = d.pop("manifests", UNSET)
        manifests: Union[Unset, SnapshotManifests]
        if isinstance(_manifests, Unset):
            manifests = UNSET
        else:
            manifests = SnapshotManifests.from_dict(_manifests)

        snapshot = cls(
            version=version,
            job=job,
            sha=sha,
            ref=ref,
            detector=detector,
            scanned=scanned,
            metadata=metadata,
            manifests=manifests,
        )

        return snapshot
