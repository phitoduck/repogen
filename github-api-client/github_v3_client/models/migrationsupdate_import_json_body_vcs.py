from enum import Enum


class MigrationsupdateImportJsonBodyVcs(str, Enum):
    SUBVERSION = "subversion"
    TFVC = "tfvc"
    GIT = "git"
    MERCURIAL = "mercurial"

    def __str__(self) -> str:
        return str(self.value)
