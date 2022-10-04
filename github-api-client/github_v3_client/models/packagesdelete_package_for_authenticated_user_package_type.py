from enum import Enum


class PackagesdeletePackageForAuthenticatedUserPackageType(str, Enum):
    NPM = "npm"
    MAVEN = "maven"
    RUBYGEMS = "rubygems"
    DOCKER = "docker"
    NUGET = "nuget"
    CONTAINER = "container"

    def __str__(self) -> str:
        return str(self.value)
