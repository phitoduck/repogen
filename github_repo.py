from tempfile import TemporaryDirectory
from textwrap import dedent
from typing import List, Union
from git.repo import Repo
from git.refs import Head
from pathlib import Path
from rich import print
import os


THIS_DIR = Path(__file__).parent

def init_and_push_new_repo(github_access_token: str, default_branch: str, repo_username_or_org: str, repo_slug: str):
    with TemporaryDirectory(dir=THIS_DIR) as repo_dir:
        repo: Repo = create_local_git_repo(repo_dir=Path(repo_dir), default_branch=default_branch)
        create_readme_md(dir=repo_dir)

        remote_url = make_remote_url(
            github_access_token=github_access_token,
            username_or_org=repo_username_or_org,
            repo_slug=repo_slug
        )
        print(f"pushing files to: {remote_url}")
        push_new_repo_to_remote(repo=repo, remote_git_url=remote_url, branch=default_branch)
        print("pushed!")

def make_remote_url(github_access_token: str, username_or_org: str, repo_slug: str):
    return f"https://{github_access_token}:x-oauth-basic@github.com/{username_or_org}/{repo_slug}.git"

def create_local_git_repo(repo_dir: Path, default_branch: str) -> Repo:
    repo = Repo.init(path=repo_dir)
    os.chdir(str(repo_dir))
    repo.git.checkout(b=default_branch)
    return repo

def create_readme_md(dir: Union[str, Path]):
    readme_fpath = Path(dir) / "README.md"
    readme_fpath.write_text(dedent(
        """\
        # I am a repository!

        I was created with Pulumi :)
        """
    ))

def push_new_repo_to_remote(repo: Repo, remote_git_url: str, branch: str):
    stage_all_repo_files(repo=repo)
    repo.index.commit("Initial commit by Pulumi.")
    repo.create_remote("origin", url=remote_git_url)
    repo.git.push("--set-upstream", "origin", "trunk")
    # repo.git.push("-u", "origin", "head")

def stage_all_repo_files(repo: Repo):
    dot_git_dir = Path(repo.common_dir)
    repo.git.add("*")



def main():
    from dotenv import load_dotenv
    from os import environ

    load_dotenv()
    GITHUB_ACCESS_TOKEN = environ.get("GITHUB_TOKEN")
    DEFAULT_BRANCH = "trunk"

    
    while True:
        ...

# if __name__ == "__main__":
#     main()

