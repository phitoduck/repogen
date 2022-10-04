from enum import Enum


class ReactionscreateForIssueJsonBodyContent(str, Enum):
    VALUE_0 = "+1"
    VALUE_1 = "-1"
    LAUGH = "laugh"
    CONFUSED = "confused"
    HEART = "heart"
    HOORAY = "hooray"
    ROCKET = "rocket"
    EYES = "eyes"

    def __str__(self) -> str:
        return str(self.value)
