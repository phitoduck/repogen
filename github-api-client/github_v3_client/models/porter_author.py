from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PorterAuthor")


@attr.s(auto_attribs=True)
class PorterAuthor:
    """Porter Author

    Attributes:
        id (int):
        remote_id (str):
        remote_name (str):
        email (str):
        name (str):
        url (str):
        import_url (str):
    """

    id: int
    remote_id: str
    remote_name: str
    email: str
    name: str
    url: str
    import_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        remote_id = self.remote_id
        remote_name = self.remote_name
        email = self.email
        name = self.name
        url = self.url
        import_url = self.import_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "remote_id": remote_id,
                "remote_name": remote_name,
                "email": email,
                "name": name,
                "url": url,
                "import_url": import_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        remote_id = d.pop("remote_id")

        remote_name = d.pop("remote_name")

        email = d.pop("email")

        name = d.pop("name")

        url = d.pop("url")

        import_url = d.pop("import_url")

        porter_author = cls(
            id=id,
            remote_id=remote_id,
            remote_name=remote_name,
            email=email,
            name=name,
            url=url,
            import_url=import_url,
        )

        porter_author.additional_properties = d
        return porter_author

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
