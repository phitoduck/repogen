from __future__ import annotations
from typing import Type
from pprint import pformat

class GitHubActionSecretError(Exception):
    """Raised when an error occurs while doing CRUD operations creating a github actions environment secret."""

    @classmethod
    def from_obj(cls: Type[GitHubActionSecretError], obj: object) -> GitHubActionSecretError:
        intro = "Error: thrown when accessing the GitHub API\n"
        pretty_obj_str: str = pformat(obj.__dict__)
        return cls(intro + pretty_obj_str)
