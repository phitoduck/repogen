from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GPGKeySubkeysItem")


@attr.s(auto_attribs=True)
class GPGKeySubkeysItem:
    """
    Attributes:
        id (Union[Unset, int]):
        primary_key_id (Union[Unset, int]):
        key_id (Union[Unset, str]):
        public_key (Union[Unset, str]):
        emails (Union[Unset, List[Any]]):
        subkeys (Union[Unset, List[Any]]):
        can_sign (Union[Unset, bool]):
        can_encrypt_comms (Union[Unset, bool]):
        can_encrypt_storage (Union[Unset, bool]):
        can_certify (Union[Unset, bool]):
        created_at (Union[Unset, str]):
        expires_at (Union[Unset, None, str]):
        raw_key (Union[Unset, None, str]):
        revoked (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    primary_key_id: Union[Unset, int] = UNSET
    key_id: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    emails: Union[Unset, List[Any]] = UNSET
    subkeys: Union[Unset, List[Any]] = UNSET
    can_sign: Union[Unset, bool] = UNSET
    can_encrypt_comms: Union[Unset, bool] = UNSET
    can_encrypt_storage: Union[Unset, bool] = UNSET
    can_certify: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    expires_at: Union[Unset, None, str] = UNSET
    raw_key: Union[Unset, None, str] = UNSET
    revoked: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        primary_key_id = self.primary_key_id
        key_id = self.key_id
        public_key = self.public_key
        emails: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        subkeys: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.subkeys, Unset):
            subkeys = self.subkeys

        can_sign = self.can_sign
        can_encrypt_comms = self.can_encrypt_comms
        can_encrypt_storage = self.can_encrypt_storage
        can_certify = self.can_certify
        created_at = self.created_at
        expires_at = self.expires_at
        raw_key = self.raw_key
        revoked = self.revoked

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if primary_key_id is not UNSET:
            field_dict["primary_key_id"] = primary_key_id
        if key_id is not UNSET:
            field_dict["key_id"] = key_id
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if emails is not UNSET:
            field_dict["emails"] = emails
        if subkeys is not UNSET:
            field_dict["subkeys"] = subkeys
        if can_sign is not UNSET:
            field_dict["can_sign"] = can_sign
        if can_encrypt_comms is not UNSET:
            field_dict["can_encrypt_comms"] = can_encrypt_comms
        if can_encrypt_storage is not UNSET:
            field_dict["can_encrypt_storage"] = can_encrypt_storage
        if can_certify is not UNSET:
            field_dict["can_certify"] = can_certify
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if raw_key is not UNSET:
            field_dict["raw_key"] = raw_key
        if revoked is not UNSET:
            field_dict["revoked"] = revoked

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        primary_key_id = d.pop("primary_key_id", UNSET)

        key_id = d.pop("key_id", UNSET)

        public_key = d.pop("public_key", UNSET)

        emails = cast(List[Any], d.pop("emails", UNSET))

        subkeys = cast(List[Any], d.pop("subkeys", UNSET))

        can_sign = d.pop("can_sign", UNSET)

        can_encrypt_comms = d.pop("can_encrypt_comms", UNSET)

        can_encrypt_storage = d.pop("can_encrypt_storage", UNSET)

        can_certify = d.pop("can_certify", UNSET)

        created_at = d.pop("created_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        raw_key = d.pop("raw_key", UNSET)

        revoked = d.pop("revoked", UNSET)

        gpg_key_subkeys_item = cls(
            id=id,
            primary_key_id=primary_key_id,
            key_id=key_id,
            public_key=public_key,
            emails=emails,
            subkeys=subkeys,
            can_sign=can_sign,
            can_encrypt_comms=can_encrypt_comms,
            can_encrypt_storage=can_encrypt_storage,
            can_certify=can_certify,
            created_at=created_at,
            expires_at=expires_at,
            raw_key=raw_key,
            revoked=revoked,
        )

        gpg_key_subkeys_item.additional_properties = d
        return gpg_key_subkeys_item

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
