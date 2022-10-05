from __future__ import annotations

from dataclasses import dataclass
from typing import Type
from pulumi import Input, Output
from pulumi.dynamic import Resource, ResourceProvider, CreateResult
from os import environ
from dotenv import load_dotenv

from repogen.custom_resources.scaffolded_project.github_repo import init_and_push_new_repo

load_dotenv()
GITHUB_TOKEN = environ["GITHUB_TOKEN"]


@dataclass
class ScaffoldedProjectFilesArgs:

    default_branch: Input[str]
    repo_name: Input[str]
    owner_user_or_org_name: Input[str]

    @classmethod
    def from_props(cls: Type[ScaffoldedProjectFilesArgs], props: dict) -> ScaffoldedProjectFilesArgs:
        return cls(
            default_branch=props["default_branch"],
            repo_name=props["repo_name"],
            owner_user_or_org_name=props["owner_user_or_org_name"],
        )

    @property
    def id(self) -> str:
        return f"{self.owner_user_or_org_name}/{self.repo_name}-files"


class ScaffolededProjectFilesProvider(ResourceProvider):
    def create(self, props: dict):
        # TODO: make this function smarter by raising an error if the repo is non-empty
        props_obj = ScaffoldedProjectFilesArgs.from_props(props)
        init_and_push_new_repo(
            default_branch=props_obj.default_branch,
            dry_run=False,
            repo_slug=props_obj.repo_name,
            repo_username_or_org=props_obj.owner_user_or_org_name,
            github_access_token=GITHUB_TOKEN,
        )
        return CreateResult(
            id_=props_obj.id, outs={**props}
        )

    def delete(self, id: str, props: dict):
        """Delete the resource by forgetting about it."""
        # props_obj = ScaffoldedProjectFilesArgs.from_props(props)
        ...


class ScaffoldedProjectFiles(Resource):

    default_branch: Input[str]
    repo_name: Input[str]
    owner_user_or_org_name: Input[str]

    def __init__(self, name, args: ScaffoldedProjectFilesArgs, opts=None):
        super().__init__(ScaffolededProjectFilesProvider(), name, {**args.__dict__, "id": name}, opts)
