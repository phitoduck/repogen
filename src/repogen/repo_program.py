"""A Python Pulumi program"""

from functools import lru_cache
import pulumi_github as github
from repogen.custom_resources.github_action_environment_secret.resource import GithubActionsSecret, GithubActionsSecretArgs
from repogen.custom_resources.scaffolded_project.github_repo import init_and_push_new_repo

from dotenv import load_dotenv
from os import environ
from pulumi import Output, ResourceOptions
import pulumi
from pulumi import automation as auto
from rich import print

from repogen.custom_resources.scaffolded_project.resource import ScaffoldedProjectFiles, ScaffoldedProjectFilesArgs

load_dotenv()
GITHUB_ACCESS_TOKEN = environ["GITHUB_TOKEN"]
"""
I wanted to avoid using Pulumi.yaml to manage this token so that these resources could be imported/created in a CLI tool.
Relying on Pulumi.yaml and pulumi.Config() allows pulumi to manage/encrypt secrets, but would require end users to do
some pulumi-specific setup if they were to use a CLI tool that wraps this file (or any other interface over the pulumi automation API)
"""

def run(repo_name: str, destroy: bool = False):
    stack = auto.create_or_select_stack(
        project_name="repogen",
        stack_name=repo_name,
        program=create_repo,
    )
    stack.set_config(key="repo-name", value=auto.ConfigValue(repo_name))

    if destroy:
        stack.destroy(on_output=print)
        return

    stack.up(on_output=print)

def create_repo():
    cfg = pulumi.Config()
    repo_name: str = cfg.get("repo-name")

    repo = github.Repository(
        resource_name=repo_name,
        # resource_name="sample-repo",
        name=repo_name,
        # name="sample-repo",
        archive_on_destroy=False,
    )

    scaffolded_project_files = ScaffoldedProjectFiles(
        "scaffolded-project-files",
        args=ScaffoldedProjectFilesArgs(
            default_branch="trunk", 
            repo_name=repo._name, 
            owner_user_or_org_name="rootski-ci"
        ),
        opts=ResourceOptions(depends_on=repo)
    )

    trunk_branch = github.BranchDefault(
        resource_name=f"{repo._name}--default-branch",
        branch="trunk",
        repository=repo,
        opts=ResourceOptions(depends_on=scaffolded_project_files)
    )

    create_environment("Sandbox", repo=repo)
    create_environment("Development", repo=repo)
    create_environment("Production", repo=repo)


def create_environment(env_name: str, repo: github.Repository):
    env = github.RepositoryEnvironment(
        resource_name=f"{env_name}-environment",
        repository=repo,
        environment=env_name,
    )

    secret_name = "TEST_SECRET"
    args = GithubActionsSecretArgs(
        repo_id=repo.repo_id, 
        env_name=env.environment, 
        secret_name="TEST_SECRET",
        # pulumi handles plaintext values differently (internally) if you
        # call Output.secret(). It makes Pulumi encrypt them in the state.
        # https://www.pulumi.com/docs/intro/concepts/secrets/#programmatically-creating-secrets
        plaintext_secret=Output.secret("dummy"), 
    )
    GithubActionsSecret(f"{repo._name}/{env_name}/{secret_name}", args=args)

if __name__ == "__main__":
    run(repo_name="sample-repo", destroy=True)