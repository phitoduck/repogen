from base64 import b64encode
from functools import lru_cache
from typing import Optional, Tuple
from nacl import encoding, public
from github_v3_client import AuthenticatedClient


from github_v3_client.models import (
    ActionscreateOrUpdateEnvironmentSecretJsonBody,
    ActionsPublicKey,
)
from github_v3_client.api.actions import (
    actionscreate_or_update_environment_secret,
    actionsget_environment_public_key,
    actionsdelete_environment_secret,
)
from github_v3_client.types import Response

from repogen.custom_resources.github_action_environment_secret.errors import (
    GitHubActionSecretError,
)

GITHUB_API_BASE_URL = "https://api.github.com"


def create_or_update_secret(
    github_token: str,
    repo_id: str,
    env_name: str,
    secret_name: str,
    plaintext_secret: str,
) -> Tuple[str, str]:

    encrypted_secret, encryption_key_id = encrypt_github_action_secret(
        github_token=github_token,
        repo_id=repo_id,
        env_name=env_name,
        plaintext_secret=plaintext_secret,
    )

    client = AuthenticatedClient(
        # TODO: should we set verify_ssl to True?
        base_url=GITHUB_API_BASE_URL,
        token=github_token,
        verify_ssl=False,
    )
    secret_creation_response: Response[
        ActionscreateOrUpdateEnvironmentSecretJsonBody
    ] = actionscreate_or_update_environment_secret.sync_detailed(
        client=client,
        environment_name=env_name,
        repository_id=repo_id,
        secret_name=secret_name,
        json_body=ActionscreateOrUpdateEnvironmentSecretJsonBody(
            encrypted_value=encrypted_secret,
            key_id=encryption_key_id,
        ),
    )

    raise_error_on_bad_response(secret_creation_response)

    return encrypted_secret, encryption_key_id


def delete_secret(github_token: str, repo_id: str, secret_name: str, env_name: str):
    # TODO: should we set verify_ssl to True?
    client = AuthenticatedClient(
        base_url=GITHUB_API_BASE_URL, token=github_token, verify_ssl=False
    )
    actionsdelete_environment_secret.sync_detailed(
        client=client,
        environment_name=env_name,
        repository_id=repo_id,
        secret_name=secret_name,
    )


def encrypt_github_action_secret(
    github_token: str, repo_id: str, env_name: str, plaintext_secret: str
) -> Tuple[str, str]:
    public_key = fetch_environment_public_key(
        github_token=github_token, env_name=env_name, repo_id=repo_id
    )
    encrypted_secret: str = encrypt_secret(
        public_encryption_key=public_key.key, secret_value=plaintext_secret
    )
    return encrypted_secret, public_key.key_id


@lru_cache
def fetch_environment_public_key(
    github_token: str, repo_id: str, env_name: str
) -> ActionsPublicKey:
    client = AuthenticatedClient(
        base_url=GITHUB_API_BASE_URL, token=github_token, verify_ssl=False
    )
    public_key_response: Response[
        ActionsPublicKey
    ] = actionsget_environment_public_key.sync_detailed(
        client=client, environment_name=env_name, repository_id=repo_id
    )

    raise_error_on_bad_response(public_key_response)

    return public_key_response.parsed


def encrypt_secret(public_encryption_key: str, secret_value: str) -> str:
    """
    Encrypt a Unicode string using the public key.

    The implementation for this function came from the GitHub API docs here:
    https://docs.github.com/en/rest/actions/secrets#create-or-update-an-organization-secret

    We found that by landing on this forum question on how to create GitHub Actions secrets:
    https://github.com/pulumi/pulumi/discussions/9377
    """
    public_key = public.PublicKey(
        public_encryption_key.encode("utf-8"), encoding.Base64Encoder()
    )
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")

def is_success_status_code(status_code: int) -> bool:
    return status_code // 100 == 2

def raise_error_on_bad_response(response: Response):
    if not is_success_status_code(response.status_code):
        raise GitHubActionSecretError.from_obj(response.parsed or response)