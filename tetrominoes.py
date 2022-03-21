import os
import consts
import pygame
import settings
from assets import ASSETS
from typing import List, Tuple
from utils import relocate
# , get_initial_coords, rotate_figure_i, rotate_figure_z


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
        print("Implemented as figure {}".format(self._figure_type))
        self._asset = ASSETS.get(self._figure_type)
        self._coords = None
        self._rotation = consts.DEGREES_0
        self._initial_x = 3
        if self._figure_type == consts.TETROMINO_O:
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

    def __update_rotation(self, decrease: bool = False) -> None:
        if decrease:
            self._rotation -= 1
            if self._rotation < consts.DEGREES_0:
                self._rotation = consts.DEGREES_270
        else:
            self._rotation += 1
            if self._rotation > consts.DEGREES_270:
                self._rotation = consts.DEGREES_0

    def rotate_counterclockwise(self):
        if self._rotation == consts.DEGREES_0:
            self._coords = self.rotate_0_to_3(self._coords)
        if self._rotation == consts.DEGREES_90:
            self._coords = self.rotate_1_to_0(self._coords)
        if self._rotation == consts.DEGREES_180:
            self._coords = self.rotate_2_to_1(self._coords)
        if self._rotation == consts.DEGREES_270:
            self._coords = self.rotate_3_to_2(self._coords)
        self.__update_rotation(decrease=True)

    def rotate_clockwise(self) -> None:
        if self._rotation == consts.DEGREES_0:
            self._coords = self.rotate_0_to_1(self._coords)
        if self._rotation == consts.DEGREES_90:
            self._coords = self.rotate_1_to_2(self._coords)
        if self._rotation == consts.DEGREES_180:
            self._coords = self.rotate_2_to_3(self._coords)
        if self._rotation == consts.DEGREES_270:
            self._coords = self.rotate_3_to_0(self._coords)
        self.__update_rotation()

    def rotate_0_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        raise NotImplementedError(
            "Please implement this method: rotate_90")

    def rotate_1_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        raise NotImplementedError(
            "Please implement this method: rotate_180")

    def rotate_2_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        raise NotImplementedError(
            "Please implement this method: rotate_270")

    def rotate_3_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        raise NotImplementedError(
            "Please implement this method: rotate")

    def rotate_0_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        raise NotImplementedError(
            "Please implement this method: rotate_90")

    def rotate_1_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        raise NotImplementedError(
            "Please implement this method: rotate_180")

    def rotate_2_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        raise NotImplementedError(
            "Please implement this method: rotate_270")

    def rotate_3_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        raise NotImplementedError(
            "Please implement this method: rotate")


class TetrominoI(Tetromino):

    def __init__(self) -> None:
        super(TetrominoI, self).__init__(consts.TETROMINO_I)

    def get_initial_coords(
        self, row
    ) -> list[Tuple[int, int]]:
        #    0 1 2 3 4 5 6 7 8 9
        # 0
        # 1        A B C D
        # 2
        return [
            (row, self._initial_x),         # A
            (row, self._initial_x + 1),     # B
            (row, self._initial_x + 2),     # C
            (row, self._initial_x + 3)      # D
        ]

    def rotate_0_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, right=2),
                relocate(coords[1], right=1),
                relocate(coords[2], down=1),
                relocate(coords[3], down=2, left=1)]

    def rotate_1_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [
            relocate(coords[0], right=1, down=2),
            relocate(coords[1], down=1),
            relocate(coords[2], left=1),
            relocate(coords[3], left=2, up=1)]

    def rotate_2_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, left=2),
                relocate(coords[1], left=1),
                relocate(coords[2], up=1),
                relocate(coords[3], up=2, right=1)]

    def rotate_3_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], left=1, up=2),
                relocate(coords[1], up=1),
                relocate(coords[2], right=1),
                relocate(coords[3], right=2, down=1)]

    def rotate_0_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=1, down=2),
                relocate(coords[1], down=1),
                relocate(coords[2], left=1),
                relocate(coords[3], left=2, up=1)]

    def rotate_1_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, left=2),
                relocate(coords[1], left=1),
                relocate(coords[2], up=1),
                relocate(coords[3], up=2, right=1)]

    def rotate_2_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [
            relocate(coords[0], left=1, up=2),
            relocate(coords[1], up=1),
            relocate(coords[2], right=1),
            relocate(coords[3], right=2, down=1)]

    def rotate_3_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, right=2),
                relocate(coords[1], right=1),
                relocate(coords[2], down=1),
                relocate(coords[3], down=2, left=1)]


class TetrominoJ(Tetromino):

    def __init__(self) -> None:
        super(TetrominoJ, self).__init__(consts.TETROMINO_J)

    def get_initial_coords(
        self, row
    ) -> list[Tuple[int, int]]:
        #    0 1 2 3 4 5 6 7 8 9
        # 0        A
        # 1        B C D
        # 2
        return [
            (row + 1, self._initial_x),
            (row, self._initial_x),
            (row, self._initial_x + 1),
            (row, self._initial_x + 2),
        ]

    def rotate_0_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=2),
                relocate(coords[1], up=1, right=1),
                coords[2],
                relocate(coords[3], down=1, left=1)]

    def rotate_1_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=2),
                relocate(coords[1], down=1, right=1),
                coords[2],
                relocate(coords[3], up=1, left=1)]

    def rotate_2_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], left=2),
                relocate(coords[1], down=1, left=1),
                coords[2],
                relocate(coords[3], up=1, right=1)]

    def rotate_3_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=2),
                relocate(coords[1], up=1, left=1),
                coords[2],
                relocate(coords[3], down=1, right=1)]

    def rotate_0_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=2),
                relocate(coords[1], down=1, right=1),
                coords[2],
                relocate(coords[3], up=1, left=1)]

    def rotate_1_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], left=2),
                relocate(coords[1], down=1, left=1),
                coords[2],
                relocate(coords[3], up=1, right=1)]

    def rotate_2_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=2),
                relocate(coords[1], up=1, left=1),
                coords[2],
                relocate(coords[3], down=1, right=1)]

    def rotate_3_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=2),
                relocate(coords[1], up=1, right=1),
                coords[2],
                relocate(coords[3], down=1, left=1)]


class TetrominoL(Tetromino):

    def __init__(self) -> None:
        super(TetrominoL, self).__init__(consts.TETROMINO_L)

    def get_initial_coords(
        self, row
    ) -> list[Tuple[int, int]]:
        #    0 1 2 3 4 5 6 7 8 9
        # 0            D
        # 1        A B C
        # 2
        return [
            (row, self._initial_x),
            (row, self._initial_x + 1),
            (row, self._initial_x + 2),
            (row+1, self._initial_x + 2)
        ]

    def rotate_0_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, right=1),
                coords[1],
                relocate(coords[2], down=1, left=1),
                relocate(coords[3], down=2)]

    def rotate_1_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, right=1),
                coords[1],
                relocate(coords[2], up=1, left=1),
                relocate(coords[3], left=2)]

    def rotate_2_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, left=1),
                coords[1],
                relocate(coords[2], up=1, right=1),
                relocate(coords[3], up=2)]

    def rotate_3_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, left=1),
                coords[1],
                relocate(coords[2], down=1, right=1),
                relocate(coords[3], right=2)]

    def rotate_0_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, right=1),
                coords[1],
                relocate(coords[2], up=1, left=1),
                relocate(coords[3], left=2)]

    def rotate_1_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, left=1),
                coords[1],
                relocate(coords[2], up=1, right=1),
                relocate(coords[3], up=2)]

    def rotate_2_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, left=1),
                coords[1],
                relocate(coords[2], down=1, right=1),
                relocate(coords[3], right=2)]

    def rotate_3_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, right=1),
                coords[1],
                relocate(coords[2], down=1, left=1),
                relocate(coords[3], down=2)]


class TetrominoO(Tetromino):

    def __init__(self) -> None:
        super(TetrominoO, self).__init__(consts.TETROMINO_O)

    def get_initial_coords(
        self, row
    ) -> list[Tuple[int, int]]:
        #    0 1 2 3 4 5 6 7 8 9
        # 0          A B
        # 1          D C
        # 2
        return [
            (row+1, self._initial_x),
            (row+1, self._initial_x + 1),
            (row, self._initial_x + 1),
            (row, self._initial_x),
        ]

    def rotate_0_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return coords

    def rotate_1_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return coords

    def rotate_2_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return coords

    def rotate_3_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return coords

    def rotate_0_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return coords

    def rotate_1_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return coords

    def rotate_2_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return coords

    def rotate_3_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return coords


class TetrominoS(Tetromino):

    def __init__(self) -> None:
        super(TetrominoS, self).__init__(consts.TETROMINO_S)

    def perform_rotate(self, rotation) -> None:
        pass

    def get_initial_coords(
        self, row
    ) -> list[Tuple[int, int]]:
        #    0 1 2 3 4 5 6 7 8 9
        # 0          C D
        # 1        A B
        # 2
        return [
            (row, self._initial_x),
            (row, self._initial_x + 1),
            (row+1, self._initial_x + 1),
            (row+1, self._initial_x + 2)
        ]

    def rotate_0_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, right=1),
                coords[1],
                relocate(coords[2], down=1, right=1),
                relocate(coords[3], down=2)]

    def rotate_1_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, right=1),
                coords[1],
                relocate(coords[2], down=1, left=1),
                relocate(coords[3], left=2)]

    def rotate_2_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [
            relocate(coords[0], down=1, left=1),
            coords[1],
            relocate(coords[2], up=1, left=1),
            relocate(coords[3], up=2)]

    def rotate_3_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [
            relocate(coords[0], up=1, left=1),
            coords[1],
            relocate(coords[2], up=1, right=1),
            relocate(coords[3], right=2)]

    def rotate_0_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [
            relocate(coords[0], down=1, right=1),
            coords[1],
            relocate(coords[2], down=1, left=1),
            relocate(coords[3], left=2)]

    def rotate_1_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, left=1),
                coords[1],
                relocate(coords[2], up=1, left=1),
                relocate(coords[3], up=2)]

    def rotate_2_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, left=1),
                coords[1],
                relocate(coords[2], up=1, right=1),
                relocate(coords[3], right=2)]

    def rotate_3_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [
            relocate(coords[0], up=1, right=1),
            coords[1],
            relocate(coords[2], down=1, right=1),
            relocate(coords[3], down=2)]


class TetrominoT(Tetromino):

    def __init__(self) -> None:
        super(TetrominoT, self).__init__(consts.TETROMINO_T)

    def get_initial_coords(
        self, row
    ) -> list[Tuple[int, int]]:
        #    0 1 2 3 4 5 6 7 8 9
        # 0          D
        # 1        A B C
        # 2
        return [
            (row, self._initial_x),
            (row, self._initial_x + 1),
            (row, self._initial_x + 2),
            (row + 1, self._initial_x + 1)
        ]

    def rotate_0_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, right=1),
                coords[1],
                relocate(coords[2], down=1, left=1),
                relocate(coords[3], down=1, right=1)]

    def rotate_1_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, right=1),
                coords[1],
                relocate(coords[2], up=1, left=1),
                relocate(coords[3], down=1, left=1)]

    def rotate_2_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, left=1),
                coords[1],
                relocate(coords[2], up=1, right=1),
                relocate(coords[3], up=1, left=1)]

    def rotate_3_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, left=1),
                coords[1],
                relocate(coords[2], down=1, right=1),
                relocate(coords[3], up=1, right=1)]

    def rotate_0_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, right=1),
                coords[1],
                relocate(coords[2], up=1, left=1),
                relocate(coords[3], down=1, left=1)]

    def rotate_1_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=1, left=1),
                coords[1],
                relocate(coords[2], up=1, right=1),
                relocate(coords[3], up=1, left=1)]

    def rotate_2_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, left=1),
                coords[1],
                relocate(coords[2], down=1, right=1),
                relocate(coords[3], up=1, right=1)]

    def rotate_3_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=1, right=1),
                coords[1],
                relocate(coords[2], down=1, left=1),
                relocate(coords[3], down=1, right=1)]


class TetrominoZ(Tetromino):

    def __init__(self) -> None:
        super(TetrominoZ, self).__init__(consts.TETROMINO_Z)

    def get_initial_coords(
        self, row
    ) -> list[Tuple[int, int]]:
        #    0 1 2 3 4 5 6 7 8 9
        # 0        A B
        # 1          C D
        # 2
        return [
            (row+1, self._initial_x),
            (row+1, self._initial_x + 1),
            (row, self._initial_x + 1),
            (row, self._initial_x + 2),
        ]

    def rotate_0_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=2),
                relocate(coords[1], down=1, right=1),
                coords[2],
                relocate(coords[3], down=1, left=1)]

    def rotate_1_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=2),
                relocate(coords[1], down=1, left=1),
                coords[2],
                relocate(coords[3], up=1, left=1)]

    def rotate_2_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], left=2),
                relocate(coords[1], up=1, left=1),
                coords[2],
                relocate(coords[3], up=1, right=1)]

    def rotate_3_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=2),
                relocate(coords[1], up=1, right=1),
                coords[2],
                relocate(coords[3], down=1, right=1)]

    def rotate_0_to_3(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], down=2),
                relocate(coords[1], down=1, left=1),
                coords[2],
                relocate(coords[3], up=1, left=1)]

    def rotate_1_to_0(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], left=2),
                relocate(coords[1], up=1, left=1),
                coords[2],
                relocate(coords[3], up=1, right=1)]

    def rotate_2_to_1(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], up=2),
                relocate(coords[1], up=1, right=1),
                coords[2],
                relocate(coords[3], down=1, right=1)]

    def rotate_3_to_2(
        self, coords: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [relocate(coords[0], right=2),
                relocate(coords[1], down=1, right=1),
                coords[2],
                relocate(coords[3], down=1, left=1)]


class Figure2:

    def __init__(
        self,
        figure_type: int
    ) -> None:
        # self.figure_type = figure_type
        self.figure_type = consts.TETROMINO_I
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
