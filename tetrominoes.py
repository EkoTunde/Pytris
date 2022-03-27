import consts
import pygame
from assets import ASSETS
from typing import List, Tuple, Union


class Tetromino:

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
        self._rotation = consts.DEGREES_0
        self._initial_x = 3
        if self._figure_type == consts.TETROMINO_O:
            self._initial_x = 4

    @property
    def initial_x(self):
        if self._figure_type == consts.TETROMINO_O:
            return 4
        return 3

    @property
    def figure_type(self) -> int:
        return self._figure_type

    @property
    def coords(self) -> Union[List[Tuple[int, int]], None]:
        return self._coords

    @property
    def rotation(self) -> int:
        return self._rotation

    def rotate_right(self):
        self._rotation += 1
        if self._rotation > consts.DEGREES_270:
            self._rotation = consts.DEGREES_0

    def rotate_left(self):
        self._rotation -= 1
        if self._rotation < consts.DEGREES_0:
            self._rotation = consts.DEGREES_270

    @property
    def asset(self) -> pygame.Surface:
        return self._asset

    @coords.setter
    def coords(self, value):
        msg = "Coords must be a list of tuples of row and col ints"
        error = TypeError(msg)
        if not isinstance(value, list):
            raise error
        for tup in value:
            if not isinstance(tup, tuple):
                raise error
            if not isinstance(tup[0], int) or not isinstance(tup[1], int):
                raise error
        self._coords = value

    def __str__(self):
        return consts.TETROMINOES_NAMES[self._figure_type]
