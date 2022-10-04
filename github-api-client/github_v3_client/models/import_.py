from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.import_project_choices_item import ImportProjectChoicesItem
from ..models.import_status import ImportStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Import")


@attr.s(auto_attribs=True)
class Import:
    """A repository import from an external source.

    Attributes:
        vcs_url (str): The URL of the originating repository.
        status (ImportStatus):
        url (str):
        html_url (str):
        authors_url (str):
        repository_url (str):
        vcs (Optional[str]):
        use_lfs (Union[Unset, bool]):
        svc_root (Union[Unset, str]):
        tfvc_project (Union[Unset, str]):
        status_text (Union[Unset, None, str]):
        failed_step (Union[Unset, None, str]):
        error_message (Union[Unset, None, str]):
        import_percent (Union[Unset, None, int]):
        commit_count (Union[Unset, None, int]):
        push_percent (Union[Unset, None, int]):
        has_large_files (Union[Unset, bool]):
        large_files_size (Union[Unset, int]):
        large_files_count (Union[Unset, int]):
        project_choices (Union[Unset, List[ImportProjectChoicesItem]]):
        message (Union[Unset, str]):
        authors_count (Union[Unset, None, int]):
        svn_root (Union[Unset, str]):
    """

    vcs_url: str
    status: ImportStatus
    url: str
    html_url: str
    authors_url: str
    repository_url: str
    vcs: Optional[str]
    use_lfs: Union[Unset, bool] = UNSET
    svc_root: Union[Unset, str] = UNSET
    tfvc_project: Union[Unset, str] = UNSET
    status_text: Union[Unset, None, str] = UNSET
    failed_step: Union[Unset, None, str] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    import_percent: Union[Unset, None, int] = UNSET
    commit_count: Union[Unset, None, int] = UNSET
    push_percent: Union[Unset, None, int] = UNSET
    has_large_files: Union[Unset, bool] = UNSET
    large_files_size: Union[Unset, int] = UNSET
    large_files_count: Union[Unset, int] = UNSET
    project_choices: Union[Unset, List[ImportProjectChoicesItem]] = UNSET
    message: Union[Unset, str] = UNSET
    authors_count: Union[Unset, None, int] = UNSET
    svn_root: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vcs_url = self.vcs_url
        status = self.status.value

        url = self.url
        html_url = self.html_url
        authors_url = self.authors_url
        repository_url = self.repository_url
        vcs = self.vcs
        use_lfs = self.use_lfs
        svc_root = self.svc_root
        tfvc_project = self.tfvc_project
        status_text = self.status_text
        failed_step = self.failed_step
        error_message = self.error_message
        import_percent = self.import_percent
        commit_count = self.commit_count
        push_percent = self.push_percent
        has_large_files = self.has_large_files
        large_files_size = self.large_files_size
        large_files_count = self.large_files_count
        project_choices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.project_choices, Unset):
            project_choices = []
            for project_choices_item_data in self.project_choices:
                project_choices_item = project_choices_item_data.to_dict()

                project_choices.append(project_choices_item)

        message = self.message
        authors_count = self.authors_count
        svn_root = self.svn_root

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vcs_url": vcs_url,
                "status": status,
                "url": url,
                "html_url": html_url,
                "authors_url": authors_url,
                "repository_url": repository_url,
                "vcs": vcs,
            }
        )
        if use_lfs is not UNSET:
            field_dict["use_lfs"] = use_lfs
        if svc_root is not UNSET:
            field_dict["svc_root"] = svc_root
        if tfvc_project is not UNSET:
            field_dict["tfvc_project"] = tfvc_project
        if status_text is not UNSET:
            field_dict["status_text"] = status_text
        if failed_step is not UNSET:
            field_dict["failed_step"] = failed_step
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if import_percent is not UNSET:
            field_dict["import_percent"] = import_percent
        if commit_count is not UNSET:
            field_dict["commit_count"] = commit_count
        if push_percent is not UNSET:
            field_dict["push_percent"] = push_percent
        if has_large_files is not UNSET:
            field_dict["has_large_files"] = has_large_files
        if large_files_size is not UNSET:
            field_dict["large_files_size"] = large_files_size
        if large_files_count is not UNSET:
            field_dict["large_files_count"] = large_files_count
        if project_choices is not UNSET:
            field_dict["project_choices"] = project_choices
        if message is not UNSET:
            field_dict["message"] = message
        if authors_count is not UNSET:
            field_dict["authors_count"] = authors_count
        if svn_root is not UNSET:
            field_dict["svn_root"] = svn_root

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vcs_url = d.pop("vcs_url")

        status = ImportStatus(d.pop("status"))

        url = d.pop("url")

        html_url = d.pop("html_url")

        authors_url = d.pop("authors_url")

        repository_url = d.pop("repository_url")

        vcs = d.pop("vcs")

        use_lfs = d.pop("use_lfs", UNSET)

        svc_root = d.pop("svc_root", UNSET)

        tfvc_project = d.pop("tfvc_project", UNSET)

        status_text = d.pop("status_text", UNSET)

        failed_step = d.pop("failed_step", UNSET)

        error_message = d.pop("error_message", UNSET)

        import_percent = d.pop("import_percent", UNSET)

        commit_count = d.pop("commit_count", UNSET)

        push_percent = d.pop("push_percent", UNSET)

        has_large_files = d.pop("has_large_files", UNSET)

        large_files_size = d.pop("large_files_size", UNSET)

        large_files_count = d.pop("large_files_count", UNSET)

        project_choices = []
        _project_choices = d.pop("project_choices", UNSET)
        for project_choices_item_data in _project_choices or []:
            project_choices_item = ImportProjectChoicesItem.from_dict(project_choices_item_data)

            project_choices.append(project_choices_item)

        message = d.pop("message", UNSET)

        authors_count = d.pop("authors_count", UNSET)

        svn_root = d.pop("svn_root", UNSET)

        import_ = cls(
            vcs_url=vcs_url,
            status=status,
            url=url,
            html_url=html_url,
            authors_url=authors_url,
            repository_url=repository_url,
            vcs=vcs,
            use_lfs=use_lfs,
            svc_root=svc_root,
            tfvc_project=tfvc_project,
            status_text=status_text,
            failed_step=failed_step,
            error_message=error_message,
            import_percent=import_percent,
            commit_count=commit_count,
            push_percent=push_percent,
            has_large_files=has_large_files,
            large_files_size=large_files_size,
            large_files_count=large_files_count,
            project_choices=project_choices,
            message=message,
            authors_count=authors_count,
            svn_root=svn_root,
        )

        import_.additional_properties = d
        return import_

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
