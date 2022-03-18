import os
from typing import Tuple
import pygame
import settings
import consts


class Figure:

    def __init__(
        self,
        figure_type: int
    ) -> None:
        # self.figure_type = figure_type
        self.figure_type = consts.FIGURE_I
        if (not isinstance(self.figure_type, int)
                and self.figure_type < 1
                or self.figure_type > 7):
            raise ValueError("Figure type must be an integer between 1 and 7")
        self._image = pygame.image.load(os.path.join(
            'assets', f'figure_{self.figure_type}.png'))
        self.size = settings.FIGURES_SIZES[self.figure_type]
        self.figure = pygame.transform.scale(self._image, self.size)
        self.rotation = 0
        self.moving = True
        self.col = 5
        self.coords = (0, 0)

    def rotate(self):
        self.rotation += 1
        if self.rotation > 3:
            self.rotation = 0
        self.figure = pygame.transform.rotate(self.figure, 90)

    def draw(self, win, coordinates: Tuple[int, int]):
        self.coords = coordinates
        win.blit(self.figure, self.coords)

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    @property
    def x(self):
        return self.coords[0]

    @property
    def y(self):
        return self.coords[1]
