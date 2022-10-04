"""
This file is for historical purposes. It shows how we used to require that the secret
be encrypted *before* being passed to the GitHubActionsSecret custom resource.

The thinking here was that all inputs/outputs are stored in the pulumi state.
We've since learned we can register certin inputs/outputs as secrets which causes
pulumi to encrypt them.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type
from pulumi import Input, Output
from pulumi.dynamic import Resource, ResourceProvider, CreateResult
from os import environ
from dotenv import load_dotenv

from repogen.dynamic_providers.github_action_environment_secret.secrets_utils import (
    create_or_update_secret,
    delete_secret,
    encrypt_github_action_secret,
)

load_dotenv()
GITHUB_TOKEN = environ.get("GITHUB_TOKEN")


@dataclass
class GithubActionsSecretArgs:

    repo_id: Input[str]
    env_name: Input[str]
    secret_name: Input[str]
    encrypted_secret: Input[str]
    encryption_key_id: Input[str]

    @property
    def id(self) -> str:
        return f"{self.repo_id}/{self.env_name}/{self.secret_name}"


class GithubActionsSecretProvider(ResourceProvider):
    def create(self, props: dict):
        props_obj = GithubActionsSecretArgs(**props)
        create_or_update_secret(
            # NOTE: we could take the github token from the pulumi config yaml file as well
            github_token=GITHUB_TOKEN,
            env_name=props_obj.env_name,
            repo_id=props_obj.repo_id,
            encrypted_secret=props_obj.encrypted_secret,
            encryption_key_id=props_obj.encryption_key_id,
        )
        return CreateResult(id_=props_obj.id, outs={**props})

    def delete(self, id: str, props: dict):
        props_obj = GithubActionsSecretArgs(**props)
        delete_secret(
            github_token=GITHUB_TOKEN,
            repo_id=props_obj.repo_id,
            env_name=props_obj.env_name,
            secret_name=props_obj.secret_name,
        )


class GithubActionsSecret(Resource):

    # these annotations are unnecessary, but allow autocompletion for properties
    # that are provided with the magic "get attribute" method. These values come 
    # from populating the "outs" dict 
    repo_id: Output[str]
    env_name: Output[str]
    secret_name: Output[str]
    encrypted_secret: Output[str]
    secret_encryption_key_id: Output[str]

    def __init__(self, name, args: GithubActionsSecretArgs, opts=None):
        super().__init__(GithubActionsSecretProvider(), name, args.__dict__, opts)

    @classmethod
    def from_plaintext_secret(
        cls: Type[GithubActionsSecret],
        repo_id: Output[str],
        env_name: Output[str],
        secret_name: Output[str],
        plaintext_secret: Output[str],
    ) -> Output[GithubActionsSecret]:
        def create_secret(args: list):
            encrypted_secret, encryption_key_id = encrypt_github_action_secret(
                github_token=GITHUB_TOKEN,
                repo_id=args[0],
                env_name=args[1],
                plaintext_secret=args[2],
            )
            return cls(
                args=GithubActionsSecretArgs(
                    repo_id=repo_id,
                    encrypted_secret=encrypted_secret,
                    env_name=env_name,
                    secret_name=secret_name,
                    encryption_key_id=encryption_key_id,
                )
            ) 
        # t = Output.all(repo_id, env_name, plaintext_secret).apply(
        #     lambda args: encrypt_github_action_secret(
        #         github_token=GITHUB_TOKEN,
        #         repo_id=args[0],
        #         env_name=args[1],
        #         plaintext_secret=args[2],
        #     )
        # )
        
        return Output.all(repo_id, env_name, plaintext_secret).apply(
            create_secret
            # lambda args: create_secret(
            #     # github_token=GITHUB_TOKEN,
            #     repo_id=args[0],
            #     env_name=args[1],
            #     plaintext_secret=args[2],
            # )
        )
        
