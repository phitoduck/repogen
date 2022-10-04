from enum import Enum


class MarkdownrenderJsonBodyMode(str, Enum):
    MARKDOWN = "markdown"
    GFM = "gfm"

    def __str__(self) -> str:
        return str(self.value)
