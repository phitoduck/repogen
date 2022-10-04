from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.code_scanning_alert_classification import CodeScanningAlertClassification
from ..models.code_scanning_alert_instance_message import CodeScanningAlertInstanceMessage
from ..models.code_scanning_alert_location import CodeScanningAlertLocation
from ..models.code_scanning_alert_state import CodeScanningAlertState
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodeScanningAlertInstance")


@attr.s(auto_attribs=True)
class CodeScanningAlertInstance:
    """
    Attributes:
        ref (Union[Unset, str]): The full Git reference, formatted as `refs/heads/<branch name>`,
            `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.
        analysis_key (Union[Unset, str]): Identifies the configuration under which the analysis was executed. For
            example, in GitHub Actions this includes the workflow filename and job name.
        environment (Union[Unset, str]): Identifies the variable values associated with the environment in which the
            analysis that generated this alert instance was performed, such as the language that was analyzed.
        category (Union[Unset, str]): Identifies the configuration under which the analysis was executed. Used to
            distinguish between multiple analyses for the same tool and commit, but performed on different languages or
            different parts of the code.
        state (Union[Unset, CodeScanningAlertState]): State of a code scanning alert.
        commit_sha (Union[Unset, str]):
        message (Union[Unset, CodeScanningAlertInstanceMessage]):
        location (Union[Unset, CodeScanningAlertLocation]): Describe a region within a file for the alert.
        html_url (Union[Unset, str]):
        classifications (Union[Unset, List[Optional[CodeScanningAlertClassification]]]): Classifications that have been
            applied to the file that triggered the alert.
            For example identifying it as documentation, or a generated file.
    """

    ref: Union[Unset, str] = UNSET
    analysis_key: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    state: Union[Unset, CodeScanningAlertState] = UNSET
    commit_sha: Union[Unset, str] = UNSET
    message: Union[Unset, CodeScanningAlertInstanceMessage] = UNSET
    location: Union[Unset, CodeScanningAlertLocation] = UNSET
    html_url: Union[Unset, str] = UNSET
    classifications: Union[Unset, List[Optional[CodeScanningAlertClassification]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref
        analysis_key = self.analysis_key
        environment = self.environment
        category = self.category
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        commit_sha = self.commit_sha
        message: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        html_url = self.html_url
        classifications: Union[Unset, List[Optional[str]]] = UNSET
        if not isinstance(self.classifications, Unset):
            classifications = []
            for classifications_item_data in self.classifications:
                classifications_item = classifications_item_data.value if classifications_item_data else None

                classifications.append(classifications_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ref is not UNSET:
            field_dict["ref"] = ref
        if analysis_key is not UNSET:
            field_dict["analysis_key"] = analysis_key
        if environment is not UNSET:
            field_dict["environment"] = environment
        if category is not UNSET:
            field_dict["category"] = category
        if state is not UNSET:
            field_dict["state"] = state
        if commit_sha is not UNSET:
            field_dict["commit_sha"] = commit_sha
        if message is not UNSET:
            field_dict["message"] = message
        if location is not UNSET:
            field_dict["location"] = location
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if classifications is not UNSET:
            field_dict["classifications"] = classifications

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ref = d.pop("ref", UNSET)

        analysis_key = d.pop("analysis_key", UNSET)

        environment = d.pop("environment", UNSET)

        category = d.pop("category", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, CodeScanningAlertState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CodeScanningAlertState(_state)

        commit_sha = d.pop("commit_sha", UNSET)

        _message = d.pop("message", UNSET)
        message: Union[Unset, CodeScanningAlertInstanceMessage]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = CodeScanningAlertInstanceMessage.from_dict(_message)

        _location = d.pop("location", UNSET)
        location: Union[Unset, CodeScanningAlertLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = CodeScanningAlertLocation.from_dict(_location)

        html_url = d.pop("html_url", UNSET)

        classifications = []
        _classifications = d.pop("classifications", UNSET)
        for classifications_item_data in _classifications or []:
            _classifications_item = classifications_item_data
            classifications_item: Optional[CodeScanningAlertClassification]
            if _classifications_item is None:
                classifications_item = None
            else:
                classifications_item = CodeScanningAlertClassification(_classifications_item)

            classifications.append(classifications_item)

        code_scanning_alert_instance = cls(
            ref=ref,
            analysis_key=analysis_key,
            environment=environment,
            category=category,
            state=state,
            commit_sha=commit_sha,
            message=message,
            location=location,
            html_url=html_url,
            classifications=classifications,
        )

        code_scanning_alert_instance.additional_properties = d
        return code_scanning_alert_instance

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
