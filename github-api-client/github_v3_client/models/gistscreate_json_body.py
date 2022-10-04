from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.gistscreate_json_body_files import GistscreateJsonBodyFiles
from ..models.gistscreate_json_body_public_type_1 import GistscreateJsonBodyPublicType1
from ..types import UNSET, Unset

T = TypeVar("T", bound="GistscreateJsonBody")


@attr.s(auto_attribs=True)
class GistscreateJsonBody:
    """
    Attributes:
        files (GistscreateJsonBodyFiles): Names and content for the files that make up the gist Example: {'hello.rb':
            {'content': 'puts "Hello, World!"'}}.
        description (Union[Unset, str]): Description of the gist Example: Example Ruby script.
        public (Union[GistscreateJsonBodyPublicType1, Unset, bool]):
    """

    files: GistscreateJsonBodyFiles
    description: Union[Unset, str] = UNSET
    public: Union[GistscreateJsonBodyPublicType1, Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        files = self.files.to_dict()

        description = self.description
        public: Union[Unset, bool, str]
        if isinstance(self.public, Unset):
            public = UNSET

        elif isinstance(self.public, GistscreateJsonBodyPublicType1):
            public = UNSET
            if not isinstance(self.public, Unset):
                public = self.public.value

        else:
            public = self.public

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        files = GistscreateJsonBodyFiles.from_dict(d.pop("files"))

        description = d.pop("description", UNSET)

        def _parse_public(data: object) -> Union[GistscreateJsonBodyPublicType1, Unset, bool]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _public_type_1 = data
                public_type_1: Union[Unset, GistscreateJsonBodyPublicType1]
                if isinstance(_public_type_1, Unset):
                    public_type_1 = UNSET
                else:
                    public_type_1 = GistscreateJsonBodyPublicType1(_public_type_1)

                return public_type_1
            except:  # noqa: E722
                pass
            return cast(Union[GistscreateJsonBodyPublicType1, Unset, bool], data)

        public = _parse_public(d.pop("public", UNSET))

        gistscreate_json_body = cls(
            files=files,
            description=description,
            public=public,
        )

        gistscreate_json_body.additional_properties = d
        return gistscreate_json_body

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
