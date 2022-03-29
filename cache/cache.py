from dataclasses import dataclass
from cache.field import Field
from cache.title import Title
import consts
import pygame
import settings


@dataclass
class Cache:
    """
    Dataclass for storing information about a cache.
    """
    font: pygame.font.Font
    bold: pygame.font.Font

    lines: Field = None
    level: Field = None
    score: Field = None

    def __post_init__(self):
        self.lines = Field(
            x=settings.DEFAULT_INFO_FIELD_X,
            y=settings.LINES_FIELD_Y,
            width=settings.DEFAULT_INFO_FIELD_WIDTH,
            height=settings.DEFAULT_INFO_FIELD_HEIGHT,
            title=Title(font=self.font, title=consts.LINES_FIELD_TITLE)
        )
