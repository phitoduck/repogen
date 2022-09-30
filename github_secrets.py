from base64 import b64encode
from nacl import encoding, public

def encrypt_github_action_secret(public_encryption_key: str, secret_value: str) -> str:
    """
    Encrypt a Unicode string using the public key.

    The implementation for this function came from the GitHub API docs here:
    https://docs.github.com/en/rest/actions/secrets#create-or-update-an-organization-secret

    We found that by landing on this forum question on how to create GitHub Actions secrets:
    https://github.com/pulumi/pulumi/discussions/9377
    """
    public_key = public.PublicKey(public_encryption_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")