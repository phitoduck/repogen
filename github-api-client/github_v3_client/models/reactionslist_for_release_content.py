from enum import Enum


class ReactionslistForReleaseContent(str, Enum):
    VALUE_0 = "+1"
    LAUGH = "laugh"
    HEART = "heart"
    HOORAY = "hooray"
    ROCKET = "rocket"
    EYES = "eyes"

    def __str__(self) -> str:
        return str(self.value)
