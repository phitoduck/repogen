from enum import Enum


class MigrationsstartImportJsonBodyVcs(str, Enum):
    SUBVERSION = "subversion"
    GIT = "git"
    MERCURIAL = "mercurial"
    TFVC = "tfvc"

    def __str__(self) -> str:
        return str(self.value)
