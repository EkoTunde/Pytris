import os
import consts
import pygame
import settings
from assets import ASSETS
from typing import List, Tuple
from utils import relocate
# , get_initial_coords, rotate_figure_i, rotate_figure_z


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
        print("Implemented as figure {}".format(self._figure_type))
        self._asset = ASSETS.get(self._figure_type)
        self._coords = None
        self._rotation = consts.DEGREES_0
        self._initial_x = 3
        if self._figure_type == consts.FIGURE_O:
            self._initial_x = 4

    @property
    def figure_type(self) -> int:
        return self._figure_type

    @property
    def coords(self) -> List[Tuple[int, int]]:
        return self._coords

    def please_get_coords(self, row) -> List[Tuple[int, int]]:
        self._coords = self.get_initial_coords(row)
        return self._coords

    def get_initial_coords(self, row):
        raise NotImplementedError(
            "Please implement this method: get_initial_coords")

    @property
    def asset(self) -> pygame.Surface:
        return self._asset

    def move_left(self) -> None:
        for i, coord in enumerate(self._coords):
            self._coords[i] = (coord[0], coord[1] - 1)

    def move_right(self) -> None:
        for i, coord in enumerate(self._coords):
            self._coords[i] = (coord[0], coord[1] + 1)

    def move_down(self) -> None:
        for i, coord in enumerate(self._coords):
            self._coords[i] = (coord[0] - 1, coord[1])

    def rotate(self) -> None:
        print("rotating figure")
        # self.perform_rotate(self._rotation)
        print("rotating figure from", self._coords, end=" ")
        if self._rotation == consts.DEGREES_0:
            self._coords = self.rotate_to_90(self._coords)
        if self._rotation == consts.DEGREES_90:
            self._coords = self.rotate_to_180(self._coords)
        if self._rotation == consts.DEGREES_180:
            self._coords = self.rotate_to_270(self._coords)
        if self._rotation == consts.DEGREES_270:
            self._coords = self.rotate_to_0(self._coords)
        # if self._figure_type == consts.FIGURE_I:
        #     print("rotating figure I")
        #     self._coords = rotate_figure_i(self._coords, self._rotation)
        # if self._figure_type == consts.FIGURE_Z:
        #     print("rotating figure Z")
        #     self._coords = rotate_figure_z(self._coords, self._rotation)
        print("to", self._coords)
        self._rotation += 1
        if self._rotation > consts.DEGREES_270:
            self._rotation = consts.DEGREES_0

    def rotate_to_90(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        raise NotImplementedError(
            "Please implement this method: rotate_90")

    def rotate_to_180(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        raise NotImplementedError(
            "Please implement this method: rotate_180")

    def rotate_to_270(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        raise NotImplementedError(
            "Please implement this method: rotate_270")

    def rotate_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        raise NotImplementedError(
            "Please implement this method: rotate")


class FigureI(Figure):

    def __init__(self) -> None:
        super(FigureI, self).__init__(consts.FIGURE_I)

    def get_initial_coords(
        self, row
    ) -> list[Tuple[int, int]]:
        #    0 1 2 3 4 5 6 7 8 9
        # 0
        # 1        o o o o
        # 2
        return [
            (row, self._initial_x),
            (row, self._initial_x + 1),
            (row, self._initial_x + 2),
            (row, self._initial_x + 3)
        ]

    def rotate_to_90(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, right=2),
                relocate(coords[1], right=1),
                relocate(coords[2], down=1),
                relocate(coords[3], down=2, left=1)]

    def rotate_to_180(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [
            relocate(coords[0], down=1, right=1),
            coords[1],
            relocate(coords[2], up=1, left=1),
            relocate(coords[3], up=2, left=2)]

    def rotate_to_270(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=2, left=2),
                relocate(coords[1], down=1, left=1),
                coords[2],
                relocate(coords[3], up=1, right=1)]

    def rotate_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=2, left=1),
                relocate(coords[1], up=1),
                relocate(coords[2], right=1),
                relocate(coords[3], right=2, down=1)]


class FigureJ(Figure):

    def __init__(self) -> None:
        super(FigureJ, self).__init__(consts.FIGURE_J)

    def get_initial_coords(
        self, row
    ) -> list[Tuple[int, int]]:
        #    0 1 2 3 4 5 6 7 8 9
        # 0        o
        # 1        o o o
        # 2
        return [
            (row + 1, self._initial_x),
            (row, self._initial_x),
            (row, self._initial_x + 1),
            (row, self._initial_x + 2),
        ]

    def rotate_to_90(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=2),
                relocate(coords[1], up=1, right=1),
                coords[2],
                relocate(coords[3], down=1, left=1)]

    def rotate_to_180(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1),
                relocate(coords[1], right=1),
                relocate(coords[2], up=1),
                relocate(coords[2], up=2, left=1)]

    def rotate_to_270(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, left=2),
                relocate(coords[1], down=2, left=1),
                relocate(coords[2], down=1),
                relocate(coords[3], right=1)]

    def rotate_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=2),
                relocate(coords[1], up=1, left=1),
                relocate(coords[2], down=2, left=2),
                relocate(coords[3], down=1, right=1)]


class FigureL(Figure):

    def __init__(self) -> None:
        super(FigureL, self).__init__(consts.FIGURE_L)

    def perform_rotate(self, rotation) -> None:
        pass

    def get_initial_coords(
        self, row
    ) -> list[Tuple[int, int]]:
        #    0 1 2 3 4 5 6 7 8 9
        # 0            o
        # 1        o o o
        # 2
        return [
            (row, self._initial_x),
            (row, self._initial_x + 1),
            (row, self._initial_x + 2),
            (row+1, self._initial_x + 2)
        ]

    def rotate_to_90(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=2),
                relocate(coords[1], up=1, right=1),
                coords[2],
                relocate(coords[3], down=1, left=1)]

    def rotate_to_180(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, right=1),
                relocate(coords[1], down=1, left=1),
                relocate(coords[2], down=2, left=2),
                relocate(coords[2], down=2, left=2)]

    def rotate_to_270(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, right=1),
                relocate(coords[1], up=1, left=1),
                relocate(coords[2], up=2, left=1),
                relocate(coords[3], right=1)]

    def rotate_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=1),
                relocate(coords[1], down=1, left=1),
                relocate(coords[2], down=2, left=2),
                relocate(coords[3], up=1, right=1)]


class FigureO(Figure):

    def __init__(self) -> None:
        super(FigureO, self).__init__(consts.FIGURE_O)

    def get_initial_coords(
        self, row
    ) -> list[Tuple[int, int]]:
        #    0 1 2 3 4 5 6 7 8 9
        # 0          o o
        # 1          o o
        # 2
        return [
            (row, self._initial_x),
            (row, self._initial_x + 1),
            (row+1, self._initial_x),
            (row+1, self._initial_x + 1)
        ]

    def rotate_to_90(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=2),
                relocate(coords[1], up=1, right=1),
                coords[2],
                relocate(coords[3], down=1, left=1)]

    def rotate_to_180(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, right=1),
                relocate(coords[1], down=1, left=1),
                relocate(coords[2], down=2, left=2),
                relocate(coords[2], down=2, left=2)]

    def rotate_to_270(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, right=1),
                relocate(coords[1], up=1, left=1),
                relocate(coords[2], up=2, left=1),
                relocate(coords[3], right=1)]

    def rotate_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=1),
                relocate(coords[1], down=1, left=1),
                relocate(coords[2], down=2, left=2),
                relocate(coords[3], up=1, right=1)]


class FigureS(Figure):

    def __init__(self) -> None:
        super(FigureS, self).__init__(consts.FIGURE_S)

    def perform_rotate(self, rotation) -> None:
        pass

    def get_initial_coords(
        self, row
    ) -> list[Tuple[int, int]]:
        #    0 1 2 3 4 5 6 7 8 9
        # 0          o o
        # 1        o o
        # 2
        return [
            (row, self._initial_x),
            (row, self._initial_x + 1),
            (row+1, self._initial_x + 1),
            (row+1, self._initial_x + 2)
        ]

    def rotate_to_90(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=2),
                relocate(coords[1], up=1, right=1),
                coords[2],
                relocate(coords[3], down=1, left=1)]

    def rotate_to_180(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, right=1),
                relocate(coords[1], down=1, left=1),
                relocate(coords[2], down=2, left=2),
                relocate(coords[2], down=2, left=2)]

    def rotate_to_270(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, right=1),
                relocate(coords[1], up=1, left=1),
                relocate(coords[2], up=2, left=1),
                relocate(coords[3], right=1)]

    def rotate_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=1),
                relocate(coords[1], down=1, left=1),
                relocate(coords[2], down=2, left=2),
                relocate(coords[3], up=1, right=1)]


class FigureZ(Figure):

    def __init__(self) -> None:
        super(FigureZ, self).__init__(consts.FIGURE_Z)

    def perform_rotate(self, rotation) -> None:
        pass

    def get_initial_coords(
        self, row
    ) -> list[Tuple[int, int]]:
        #    0 1 2 3 4 5 6 7 8 9
        # 0        o o
        # 1          o o
        # 2
        return [
            (row+1, self._initial_x),
            (row+1, self._initial_x + 1),
            (row, self._initial_x + 1),
            (row, self._initial_x + 2),
        ]

    def rotate_to_90(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=2),
                relocate(coords[1], up=1, right=1),
                coords[2],
                relocate(coords[3], down=1, left=1)]

    def rotate_to_180(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, right=1),
                relocate(coords[1], down=1, left=1),
                relocate(coords[2], down=2, left=2),
                relocate(coords[2], down=2, left=2)]

    def rotate_to_270(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, right=1),
                relocate(coords[1], up=1, left=1),
                relocate(coords[2], up=2, left=1),
                relocate(coords[3], right=1)]

    def rotate_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=1),
                relocate(coords[1], down=1, left=1),
                relocate(coords[2], down=2, left=2),
                relocate(coords[3], up=1, right=1)]


class FigureT(Figure):

    def __init__(self) -> None:
        super(FigureT, self).__init__(consts.FIGURE_T)

    def perform_rotate(self, rotation) -> None:
        pass

    def get_initial_coords(
        self, row
    ) -> list[Tuple[int, int]]:
        #    0 1 2 3 4 5 6 7 8 9
        # 0          o
        # 1        o o o
        # 2
        return [
            (row, self._initial_x),
            (row, self._initial_x + 1),
            (row, self._initial_x + 2),
            (row + 1, self._initial_x + 1)
        ]

    def rotate_to_90(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=2),
                relocate(coords[1], up=1, right=1),
                coords[2],
                relocate(coords[3], down=1, left=1)]

    def rotate_to_180(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, right=1),
                relocate(coords[1], down=1, left=1),
                relocate(coords[2], down=2, left=2),
                relocate(coords[2], down=2, left=2)]

    def rotate_to_270(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, right=1),
                relocate(coords[1], up=1, left=1),
                relocate(coords[2], up=2, left=1),
                relocate(coords[3], right=1)]

    def rotate_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=1),
                relocate(coords[1], down=1, left=1),
                relocate(coords[2], down=2, left=2),
                relocate(coords[3], up=1, right=1)]


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

    @ property
    def width(self):
        return self.size[0]

    @ property
    def height(self):
        return self.size[1]

    @ property
    def x(self):
        return self.coords[0]

    @ property
    def y(self):
        return self.coords[1]
