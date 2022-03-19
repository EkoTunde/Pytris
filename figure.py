import os
import consts
import pygame
import settings
from assets import ASSETS
from typing import Tuple
from utils import get_initial_coords, rotate_figure_i, rotate_figure_z


class Figure:

    def __init__(
        self,
        figure_type: int,
    ) -> None:
        self._figure_type = figure_type
        if (not isinstance(self._figure_type, int)
                and self._figure_type < 1
                or self._figure_type > 7):
            raise ValueError("Figure type must be an integer between 1 and 7")
        self._asset = ASSETS.get(self._figure_type)
        self._coords = None
        self._rotation = 0

    @property
    def figure_type(self) -> int:
        return self._figure_type

    @property
    def coords(self) -> list[Tuple[int, int]]:
        return self._coords

    def please_get_coords(self, row):
        self._coords = get_initial_coords(self._figure_type, row)
        return self._coords

    @property
    def asset(self):
        return self._asset

    def move_left(self):
        for i, coord in enumerate(self._coords):
            self._coords[i] = (coord[0], coord[1] - 1)

    def move_right(self):
        for i, coord in enumerate(self._coords):
            self._coords[i] = (coord[0], coord[1] + 1)

    def move_down(self):
        for i, coord in enumerate(self._coords):
            self._coords[i] = (coord[0] - 1, coord[1])

    def rotate(self):
        if self._figure_type == consts.FIGURE_I:
            print("rotating figure I")
            self._coords = rotate_figure_i(self._coords, self._rotation)
        if self._figure_type == consts.FIGURE_Z:
            print("rotating figure Z")
            self._coords = rotate_figure_z(self._coords, self._rotation)
        self._rotation += 1
        if self._rotation > 3:
            self._rotation = 0


class Figure2:

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
