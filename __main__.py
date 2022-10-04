"""A Python Pulumi program"""

from functools import lru_cache
from pathlib import Path
import pulumi
import pulumi_github as github
from repogen.dynamic_providers.github_action_environment_secret.resource import GithubActionsSecret, GithubActionsSecretArgs

from dotenv import load_dotenv
from os import environ
from pulumi import Output

load_dotenv()
GITHUB_ACCESS_TOKEN = environ.get("GITHUB_TOKEN")

def create_environment(env_name: str, repo: github.Repository):
    env = github.RepositoryEnvironment(
        resource_name=f"{env_name}-environment",
        repository=repo,
        environment=env_name,
    )

    # create_env_secret(repo_id=repo.repo_id, env=env, secret_name="ENVIRONMENT", secret_value=env_name.lower())
    if env_name=="Sandbox":
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
    

# def create_env_secret(repo_id: str, env: github.RepositoryEnvironment, secret_name: str, secret_value: str) -> github.ActionsEnvironmentSecret:
#     env_name: Output[str] = Output.apply(env.environment, lambda name: name.split(":")[-1])
#     encrypted_secret: Output[str] = encrypt_github_action_secret_async(
#         token=GITHUB_ACCESS_TOKEN,
#         repo_id=repo_id,
#         secret_value=secret_value,
#         env_name=env_name,
#     )
#     return github.actions_environment_secret.ActionsEnvironmentSecret(
#         resource_name=f"{env._name}/{secret_name.lower()}/env-secret",
#         secret_name=secret_name,
#         encrypted_value=encrypted_secret,
#         # plaintext_value=encrypted_secret,
#         environment=env,
#         repository=env.repository,
#     )

@lru_cache
def get_github_actions_public_encryption_key(repo: github.Repository) -> github.AwaitableGetActionsPublicKeyResult:
    public_key = github.get_actions_public_key(repository=repo)
    return public_key


repo = github.Repository(
    resource_name="sample-repo",
    name="sample-repo",
    archive_on_destroy=False,
)

# pulumi.Output.apply(
#     repo.git_clone_url,
#     # run git push origin trunk as a subprocess/bash command
#     lambda git_clone_url: init_and_push_new_repo(
#         github_access_token=GITHUB_ACCESS_TOKEN, 
#         default_branch="trunk", 
#         repo_username_or_org="rootski-ci", 
#         repo_slug="sample-repo")
# )


# trunk_branch = github.BranchDefault(
#     resource_name=f"{repo._name}--default-branch",
#     branch="trunk",
#     repository=repo,
# )

create_environment("Sandbox", repo=repo)
create_environment("Development", repo=repo)
# create_environment("Production", repo=repo)

"""
1. upload some boilerplate code to the repo
2. configue CI/CD for repo (with GitHub actions)--creating environments and settings env secrets in those
"""