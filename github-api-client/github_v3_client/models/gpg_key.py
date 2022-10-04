import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.gpg_key_emails_item import GPGKeyEmailsItem
from ..models.gpg_key_subkeys_item import GPGKeySubkeysItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="GPGKey")


@attr.s(auto_attribs=True)
class GPGKey:
    """A unique encryption key

    Attributes:
        id (int):  Example: 3.
        key_id (str):  Example: 3262EFF25BA0D270.
        public_key (str):  Example: xsBNBFayYZ....
        emails (List[GPGKeyEmailsItem]):  Example: [{'email': 'octocat@users.noreply.github.com', 'verified': True}].
        subkeys (List[GPGKeySubkeysItem]):  Example: [{'id': 4, 'primary_key_id': 3, 'key_id': '4A595D4C72EE49C7',
            'public_key': 'zsBNBFayYZ...', 'emails': [], 'subkeys': [], 'can_sign': False, 'can_encrypt_comms': True,
            'can_encrypt_storage': True, 'can_certify': False, 'created_at': '2016-03-24T11:31:04-06:00', 'expires_at':
            None, 'revoked': False}].
        can_sign (bool):  Example: True.
        can_encrypt_comms (bool):
        can_encrypt_storage (bool):
        can_certify (bool):  Example: True.
        created_at (datetime.datetime):  Example: 2016-03-24T11:31:04-06:00.
        revoked (bool):  Example: True.
        name (Union[Unset, None, str]):  Example: Octocat's GPG Key.
        primary_key_id (Optional[int]):
        expires_at (Optional[datetime.datetime]):
        raw_key (Optional[str]):
    """

    id: int
    key_id: str
    public_key: str
    emails: List[GPGKeyEmailsItem]
    subkeys: List[GPGKeySubkeysItem]
    can_sign: bool
    can_encrypt_comms: bool
    can_encrypt_storage: bool
    can_certify: bool
    created_at: datetime.datetime
    revoked: bool
    primary_key_id: Optional[int]
    expires_at: Optional[datetime.datetime]
    raw_key: Optional[str]
    name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key_id = self.key_id
        public_key = self.public_key
        emails = []
        for emails_item_data in self.emails:
            emails_item = emails_item_data.to_dict()

            emails.append(emails_item)

        subkeys = []
        for subkeys_item_data in self.subkeys:
            subkeys_item = subkeys_item_data.to_dict()

            subkeys.append(subkeys_item)

        can_sign = self.can_sign
        can_encrypt_comms = self.can_encrypt_comms
        can_encrypt_storage = self.can_encrypt_storage
        can_certify = self.can_certify
        created_at = self.created_at.isoformat()

        revoked = self.revoked
        name = self.name
        primary_key_id = self.primary_key_id
        expires_at = self.expires_at.isoformat() if self.expires_at else None

        raw_key = self.raw_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "key_id": key_id,
                "public_key": public_key,
                "emails": emails,
                "subkeys": subkeys,
                "can_sign": can_sign,
                "can_encrypt_comms": can_encrypt_comms,
                "can_encrypt_storage": can_encrypt_storage,
                "can_certify": can_certify,
                "created_at": created_at,
                "revoked": revoked,
                "primary_key_id": primary_key_id,
                "expires_at": expires_at,
                "raw_key": raw_key,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        key_id = d.pop("key_id")

        public_key = d.pop("public_key")

        emails = []
        _emails = d.pop("emails")
        for emails_item_data in _emails:
            emails_item = GPGKeyEmailsItem.from_dict(emails_item_data)

            emails.append(emails_item)

        subkeys = []
        _subkeys = d.pop("subkeys")
        for subkeys_item_data in _subkeys:
            subkeys_item = GPGKeySubkeysItem.from_dict(subkeys_item_data)

            subkeys.append(subkeys_item)

        can_sign = d.pop("can_sign")

        can_encrypt_comms = d.pop("can_encrypt_comms")

        can_encrypt_storage = d.pop("can_encrypt_storage")

        can_certify = d.pop("can_certify")

        created_at = isoparse(d.pop("created_at"))

        revoked = d.pop("revoked")

        name = d.pop("name", UNSET)

        primary_key_id = d.pop("primary_key_id")

        _expires_at = d.pop("expires_at")
        expires_at: Optional[datetime.datetime]
        if _expires_at is None:
            expires_at = None
        else:
            expires_at = isoparse(_expires_at)

        raw_key = d.pop("raw_key")

        gpg_key = cls(
            id=id,
            key_id=key_id,
            public_key=public_key,
            emails=emails,
            subkeys=subkeys,
            can_sign=can_sign,
            can_encrypt_comms=can_encrypt_comms,
            can_encrypt_storage=can_encrypt_storage,
            can_certify=can_certify,
            created_at=created_at,
            revoked=revoked,
            name=name,
            primary_key_id=primary_key_id,
            expires_at=expires_at,
            raw_key=raw_key,
        )

        gpg_key.additional_properties = d
        return gpg_key

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
