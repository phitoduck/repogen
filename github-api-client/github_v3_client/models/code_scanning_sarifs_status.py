from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.code_scanning_sarifs_status_processing_status import CodeScanningSarifsStatusProcessingStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodeScanningSarifsStatus")


@attr.s(auto_attribs=True)
class CodeScanningSarifsStatus:
    """
    Attributes:
        processing_status (Union[Unset, CodeScanningSarifsStatusProcessingStatus]): `pending` files have not yet been
            processed, while `complete` means results from the SARIF have been stored. `failed` files have either not been
            processed at all, or could only be partially processed.
        analyses_url (Union[Unset, None, str]): The REST API URL for getting the analyses associated with the upload.
        errors (Union[Unset, None, List[str]]): Any errors that ocurred during processing of the delivery.
    """

    processing_status: Union[Unset, CodeScanningSarifsStatusProcessingStatus] = UNSET
    analyses_url: Union[Unset, None, str] = UNSET
    errors: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        processing_status: Union[Unset, str] = UNSET
        if not isinstance(self.processing_status, Unset):
            processing_status = self.processing_status.value

        analyses_url = self.analyses_url
        errors: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.errors, Unset):
            if self.errors is None:
                errors = None
            else:
                errors = self.errors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if processing_status is not UNSET:
            field_dict["processing_status"] = processing_status
        if analyses_url is not UNSET:
            field_dict["analyses_url"] = analyses_url
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _processing_status = d.pop("processing_status", UNSET)
        processing_status: Union[Unset, CodeScanningSarifsStatusProcessingStatus]
        if isinstance(_processing_status, Unset):
            processing_status = UNSET
        else:
            processing_status = CodeScanningSarifsStatusProcessingStatus(_processing_status)

        analyses_url = d.pop("analyses_url", UNSET)

        errors = cast(List[str], d.pop("errors", UNSET))

        code_scanning_sarifs_status = cls(
            processing_status=processing_status,
            analyses_url=analyses_url,
            errors=errors,
        )

        code_scanning_sarifs_status.additional_properties = d
        return code_scanning_sarifs_status

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
