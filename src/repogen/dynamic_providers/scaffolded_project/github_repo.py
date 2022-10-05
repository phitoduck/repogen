from tempfile import TemporaryDirectory
from textwrap import dedent
from typing import List, Optional, Union
from git.repo import Repo
from git.refs import Head
from pathlib import Path
from rich import print
from phito_projen import PythonPackage
from projen import SampleFile
import os


THIS_DIR = Path(__file__).parent
        


def init_and_push_new_repo(github_access_token: str, default_branch: str, repo_username_or_org: str, repo_slug: str, dry_run: bool = False):
    TMP_DIR = Path.home() / ".repogen"
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    with TemporaryDirectory(dir=TMP_DIR) as repo_dir:
        repo: Repo = create_local_git_repo(repo_dir=Path(repo_dir), default_branch=default_branch)
        create_python_package(
            outdir=Path(repo_dir), package_name=repo_slug, module_name="sample_pkg", install_requires=["rich"], package_version="1.0.0"
        )

        remote_url = make_remote_url(
            github_access_token=github_access_token,
            username_or_org=repo_username_or_org,
            repo_slug=repo_slug
        )
        # print(f"pushing files to: {remote_url}")
        if not dry_run:
            push_new_repo_to_remote(repo=repo, remote_git_url=remote_url, branch=default_branch)

        if dry_run:
            print("Dry run. Press CTRL + C to kill this process.")
            while True:
                ...

        print("pushed!")

def create_python_package(outdir: Path, package_name: str, module_name: str, package_version: str, install_requires: Optional[List] = None):
    package = PythonPackage(
        outdir=str(outdir),
        name=package_name,
        module_name=module_name,
        version=package_version,
        install_requires=install_requires
    )
    SampleFile(package, file_path="README.md", contents=dedent(
        f"""\
        # I am a repository!

        I was created with Pulumi :)
        """
    ))
    package.synth()


def make_remote_url(github_access_token: str, username_or_org: str, repo_slug: str):
    return f"https://{github_access_token}:x-oauth-basic@github.com/{username_or_org}/{repo_slug}.git"

def create_local_git_repo(repo_dir: Path, default_branch: str) -> Repo:
    repo = Repo.init(path=repo_dir)

    # os.chdir(str(repo_dir))
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
    repo.git.add("--all")
    repo.git.commit(m="Initial commit by Pulumi.")
    repo.git.remote("add", "origin", remote_git_url)
    repo.git.push("origin", branch)



def main():
    from dotenv import load_dotenv
    from os import environ

    load_dotenv()
    GITHUB_ACCESS_TOKEN = environ.get("GITHUB_TOKEN")

    init_and_push_new_repo(github_access_token=GITHUB_ACCESS_TOKEN, default_branch="trunk", dry_run=False, repo_slug="sample-repo", repo_username_or_org="rootski-ci")


if __name__ == "__main__":
    main()

