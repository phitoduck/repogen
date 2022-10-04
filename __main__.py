"""A Python Pulumi program"""

from functools import lru_cache
import pulumi_github as github
from repogen.dynamic_providers.github_action_environment_secret.resource import GithubActionsSecret, GithubActionsSecretArgs

from dotenv import load_dotenv
from os import environ
from pulumi import Output

load_dotenv()
GITHUB_ACCESS_TOKEN = environ["GITHUB_TOKEN"]
"""
I wanted to avoid using Pulumi.yaml to manage this token so that these resources could be imported/created in a CLI tool.
Relying on Pulumi.yaml and pulumi.Config() allows pulumi to manage/encrypt secrets, but would require end users to do
some pulumi-specific setup if they were to use a CLI tool that wraps this file (or any other interface over the pulumi automation API)
"""

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
create_environment("Production", repo=repo)