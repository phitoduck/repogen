from __future__ import annotations

from dataclasses import dataclass
from typing import Type
from pulumi import Input, Output
from pulumi.dynamic import Resource, ResourceProvider, CreateResult
from os import environ
from dotenv import load_dotenv

from repogen.custom_resources.github_action_environment_secret.secrets_utils import (
    create_or_update_secret,
    delete_secret,
)

load_dotenv()
GITHUB_TOKEN = environ["GITHUB_TOKEN"]


@dataclass
class GithubActionsSecretArgs:

    repo_id: Input[str]
    env_name: Input[str]
    secret_name: Input[str]
    plaintext_secret: Input[str]

    @property
    def id(self) -> str:
        return f"{self.repo_id}/{self.env_name}/{self.secret_name}"

    @property
    def clean_repo_id(self) -> str:
        return str(int(self.repo_id))

    @classmethod
    def from_props(cls: Type[GithubActionsSecretArgs], props: dict) -> GithubActionsSecretArgs:
        return cls(
            repo_id=str(int(props["repo_id"])),
            env_name=props["env_name"],
            secret_name=props["secret_name"],
            plaintext_secret=props["plaintext_secret"],
        )


class GithubActionsSecretProvider(ResourceProvider):
    def create(self, props: dict):
        props_obj = GithubActionsSecretArgs.from_props(props)
        encrypted_secret, encryption_key_id = create_or_update_secret(
            # NOTE: we could take the github token from the pulumi config yaml file as well
            github_token=GITHUB_TOKEN,
            repo_id=props_obj.clean_repo_id,
            env_name=props_obj.env_name,
            secret_name=props_obj.secret_name,
            plaintext_secret=props_obj.plaintext_secret,
        )
        return CreateResult(
            id_=props_obj.id, outs={**props, "encryption_key_id": encryption_key_id, "encrypted_secret": encrypted_secret}
        )

    def delete(self, id: str, props: dict):
        try:
            props_obj = GithubActionsSecretArgs.from_props(props)
            delete_secret(
                github_token=GITHUB_TOKEN,
                repo_id=props_obj.repo_id,
                env_name=props_obj.env_name,
                secret_name=props_obj.secret_name,
            )
        except KeyError as e:
            print("Key error", str(e))


class GithubActionsSecret(Resource):

    # these annotations are unnecessary, but allow autocompletion for properties
    # that are provided with the magic "get attribute" method. These values come
    # from populating the "outs" dict
    repo_id: Output[str]
    env_name: Output[str]
    secret_name: Output[str]
    encrypted_secret: Output[str]
    encryption_key_id: Output[str]

    def __init__(self, name, args: GithubActionsSecretArgs, opts=None):
        super().__init__(GithubActionsSecretProvider(), name, args.__dict__, opts)
