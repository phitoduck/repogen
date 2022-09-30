"""A Python Pulumi program"""

from functools import lru_cache
import pulumi
import pulumi_github as github
from github_secrets import encrypt_github_action_secret

from dotenv import load_dotenv
from os import environ
from github_repo import init_and_push_new_repo

load_dotenv()
GITHUB_ACCESS_TOKEN = environ.get("GITHUB_TOKEN")

def create_environment(env_name: str, repo: github.Repository):
    env = github.RepositoryEnvironment(
        resource_name=f"{env_name}-environment",
        repository=repo,
        environment=env_name,
    )
    # create_env_secret(env=env, secret_name="ENVIRONMENT", secret_value=env_name.lower())
    

def create_env_secret(env: github.RepositoryEnvironment, secret_name: str, secret_value: str) -> github.ActionsEnvironmentSecret:
    github_public_key = get_github_actions_public_encryption_key(repo=env.repository)
    encrypted_secret = encrypt_github_action_secret(public_encryption_key=github_public_key.key, secret_value=secret_value)
    return github.actions_environment_secret.ActionsEnvironmentSecret(
        resource_name=f"{env._name}--{secret_name.lower()}--env-secret",
        secret_name=secret_name,
        encrypted_value=encrypted_secret,
        environment=env,
        repository=env.repository,
    )

@lru_cache
def get_github_actions_public_encryption_key(repo: github.Repository) -> github.AwaitableGetActionsPublicKeyResult:
    public_key = github.get_actions_public_key(repository=repo)
    return public_key


repo = github.Repository(
    resource_name="sample-repo",
    name="sample-repo",
    archive_on_destroy=False,
)

pulumi.Output.apply(
    repo.git_clone_url,
    # run git push origin trunk as a subprocess/bash command
    lambda git_clone_url: init_and_push_new_repo(
        github_access_token=GITHUB_ACCESS_TOKEN, 
        default_branch="trunk", 
        repo_username_or_org="rootski-ci", 
        repo_slug="sample-repo")
)


trunk_branch = github.BranchDefault(
    resource_name=f"{repo.name}--default-branch",
    branch="trunk",
    repository=repo,
)

create_environment("Sandbox", repo=repo)
create_environment("Development", repo=repo)
create_environment("Production", repo=repo)

"""
1. upload some boilerplate code to the repo
2. configue CI/CD for repo (with GitHub actions)--creating environments and settings env secrets in those
"""