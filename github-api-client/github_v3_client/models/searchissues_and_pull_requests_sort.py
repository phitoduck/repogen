from enum import Enum


class SearchissuesAndPullRequestsSort(str, Enum):
    COMMENTS = "comments"
    REACTIONS = "reactions"
    REACTIONS_1 = "reactions--1"
    REACTIONS_SMILE = "reactions-smile"
    REACTIONS_THINKING_FACE = "reactions-thinking_face"
    REACTIONS_HEART = "reactions-heart"
    REACTIONS_TADA = "reactions-tada"
    INTERACTIONS = "interactions"
    CREATED = "created"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
