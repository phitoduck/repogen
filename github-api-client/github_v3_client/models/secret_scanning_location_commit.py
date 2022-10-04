from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SecretScanningLocationCommit")


@attr.s(auto_attribs=True)
class SecretScanningLocationCommit:
    """Represents a 'commit' secret scanning location type. This location type shows that a secret was detected inside a
    commit to a repository.

        Attributes:
            path (str): The file path in the repository Example: /example/secrets.txt.
            start_line (float): Line number at which the secret starts in the file
            end_line (float): Line number at which the secret ends in the file
            start_column (float): The column at which the secret starts within the start line when the file is interpreted
                as 8BIT ASCII
            end_column (float): The column at which the secret ends within the end line when the file is interpreted as 8BIT
                ASCII
            blob_sha (str): SHA-1 hash ID of the associated blob Example: af5626b4a114abcb82d63db7c8082c3c4756e51b.
            blob_url (str): The API URL to get the associated blob resource
            commit_sha (str): SHA-1 hash ID of the associated commit Example: af5626b4a114abcb82d63db7c8082c3c4756e51b.
            commit_url (str): The API URL to get the associated commit resource
    """

    path: str
    start_line: float
    end_line: float
    start_column: float
    end_column: float
    blob_sha: str
    blob_url: str
    commit_sha: str
    commit_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        start_line = self.start_line
        end_line = self.end_line
        start_column = self.start_column
        end_column = self.end_column
        blob_sha = self.blob_sha
        blob_url = self.blob_url
        commit_sha = self.commit_sha
        commit_url = self.commit_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "start_line": start_line,
                "end_line": end_line,
                "start_column": start_column,
                "end_column": end_column,
                "blob_sha": blob_sha,
                "blob_url": blob_url,
                "commit_sha": commit_sha,
                "commit_url": commit_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        start_line = d.pop("start_line")

        end_line = d.pop("end_line")

        start_column = d.pop("start_column")

        end_column = d.pop("end_column")

        blob_sha = d.pop("blob_sha")

        blob_url = d.pop("blob_url")

        commit_sha = d.pop("commit_sha")

        commit_url = d.pop("commit_url")

        secret_scanning_location_commit = cls(
            path=path,
            start_line=start_line,
            end_line=end_line,
            start_column=start_column,
            end_column=end_column,
            blob_sha=blob_sha,
            blob_url=blob_url,
            commit_sha=commit_sha,
            commit_url=commit_url,
        )

        secret_scanning_location_commit.additional_properties = d
        return secret_scanning_location_commit

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
