
from dataclasses import dataclass
from typing import Tuple
import pygame
import settings


@dataclass
class Title:
    """
    Dataclass for storing information about a field's title.
    """
    font: pygame.font.Font
    title: str
    surface: pygame.Surface = None
    color: Tuple[int, int, int] = settings.WHITE
    _rect: pygame.Rect = None

    def __post_init__(self):
        self.surface = self.font.render(self.title, True, self.color)

    @property
    def rect(self):
        """
        Returns the title's rect.
        """
        return self._rect

    @rect.setter
    def _rect(self, rect: pygame.Rect):
        if isinstance(rect, pygame.Rect):
            self._rect = rect
        raise TypeError("rect must be a pygame.Rect")
