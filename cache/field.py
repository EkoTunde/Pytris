from dataclasses import dataclass
from typing import Tuple

import pygame
from cache.title import Title


@dataclass
class Field:
    """
    Dataclass for storing information about a field.
    """
    x: int
    y: int
    width: int
    height: int
    title: Title
    _rect: pygame.Rect = None
    _board: pygame.Rect = None

    @property
    def rect_value(self) -> Tuple[int, int, int, int]:
        return (self.x, self.y, self.width, self.height)

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, rect: pygame.Rect):
        if isinstance(rect, pygame.Rect):
            self._rect = rect
        raise TypeError("rect must be a pygame.Rect")
