from tempfile import TemporaryDirectory
from textwrap import dedent
from typing import List, Union
from git.repo import Repo
from pathlib import Path
from rich import print

"""
def make_remote_url
https://<access_token>:x-oauth-basic@github.com/username/your-project
"""

def create_local_git_repo(repo_dir: Path) -> Repo:
    repo = Repo.init(path=repo_dir)
    return repo

def create_readme_md(dir: Union[str, Path]):
    readme_fpath = Path(dir) / "README.md"
    readme_fpath.write_text(dedent(
        """\
        # I am a repository!

        I was created with Pulumi :)
        """
    ))

def push_new_repo_to_remote(repo: Repo, remote_git_url: str):
    stage_all_repo_files(repo=repo)
    repo.index.commit("Initial commit by Pulumi.")
    repo.create_remote("origin", url=remote_git_url)
    repo.remote("origin").push()
    

def stage_all_repo_files(repo: Repo):
    dot_git_dir = Path(repo.common_dir)
    repo_dir = (dot_git_dir / "..").resolve()
    repo_files: List[Path] = list(map(str, repo_dir.rglob("*")))
    repo.index.add(repo_files)


def main():
    THIS_DIR = Path(__file__).parent
    with TemporaryDirectory(dir=THIS_DIR) as repo_dir:
        repo: Repo = create_local_git_repo(repo_dir=Path(repo_dir))
        create_readme_md(dir=repo_dir)
        # push_new_repo_to_remote(repo=repo, remote_git_url="hi")
        while True:
            ...

if __name__ == "__main__":
    main()