from enum import Enum


class PagesHttpsCertificateState(str, Enum):
    NEW = "new"
    AUTHORIZATION_CREATED = "authorization_created"
    AUTHORIZATION_PENDING = "authorization_pending"
    AUTHORIZED = "authorized"
    AUTHORIZATION_REVOKED = "authorization_revoked"
    ISSUED = "issued"
    UPLOADED = "uploaded"
    APPROVED = "approved"
    ERRORED = "errored"
    BAD_AUTHZ = "bad_authz"
    DESTROY_PENDING = "destroy_pending"
    DNS_CHANGED = "dns_changed"

    def __str__(self) -> str:
        return str(self.value)
