import consts
import pygame
import settings
from assets import ASSETS
from typing import Dict, List, Tuple, Union
from grid import Grid


def relocate(
    coords: Tuple[int, int],
    up=0,
    right=0,
    down=0,
    left=0,
) -> Tuple[int, int]:
    """Returns a new Tuple with the coordinates relocated."""
    return (coords[0] + up - down, coords[1] + right - left)


def rotate_coord_by_kick(
    coord: Tuple[int, int],
    kick: Tuple[int, int]
) -> Tuple[int, int]:
    """
    Returns a new Tuple with the coordinates rotated by kick.
    """
    horizontal, vertical = kick[0], kick[1]
    return (coord[0] + vertical, coord[1] + horizontal)


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

    def please_get_coords(self, row) -> List[Tuple[int, int]]:
        self._coords = self.get_initial_coords(row)
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

    def get_initial_coords(self, row):
        initial_coords = consts.INITIAL_COORDS_DATA.get(self._figure_type)
        return [
            (row + initial_coords[0][0],
             self._initial_x + initial_coords[0][1]),
            (row + initial_coords[1][0],
             self._initial_x + initial_coords[1][1]),
            (row + initial_coords[2][0],
             self._initial_x + initial_coords[2][1]),
            (row + initial_coords[3][0],
             self._initial_x + initial_coords[3][1]),
        ]

    @property
    def asset(self) -> pygame.Surface:
        return self._asset

    def move_left(self) -> None:  # , terrain: List[List[int]] = None) -> None:
        # candidates = self.__get_moved_coords(left=1)
        # if self.are_coords_valid(candidates, terrain):
        #     self._coords = candidates
        self._coords = self.__get_moved_coords(left=1)
        # for i, coord in enumerate(self._coords):
        #     self._coords[i] = (coord[0], coord[1] - 1)

    def move_right(self) -> None:  # , terrain: List[List[int]]) -> None:
        self._coords = self.__get_moved_coords(right=1)
        # candidates = self.__get_moved_coords(right=1)
        # if self.are_coords_valid(candidates, terrain):
        #     self._coords = candidates
        # for i, coord in enumerate(self._coords):
        #     self._coords[i] = (coord[0], coord[1] + 1)

    def move_down(self) -> None:  # , terrain: List[List[int]]) -> None:
        self._coords = self.__get_moved_coords(down=1)
        # candidates = self.__get_moved_coords(down=1)
        # if self.are_coords_valid(candidates, terrain):
        #     self._coords = candidates
        # for i, coord in enumerate(self._coords):
        #     self._coords[i] = (coord[0] - 1, coord[1])

    def __get_moved_coords(
        self, down=0, left=0, right=0
    ) -> List[Tuple[int, int]]:
        coords = []
        for coord in self._coords:
            coords.append((coord[0] - down, coord[1] - left + right))
        # for coord in self._coords:
        #     coords.append(relocate(coord, down=down, left=left, right=right))
        return coords

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

    def attempt_rotate(
        self,
        clockwise: bool = True,
        terrain: List[List[int]] = None,
    ) -> None:
        position_from = self._rotation
        position_to = position_from + 1 if clockwise else position_from - 1
        if clockwise and position_to == consts.DEGREES_270 + 1:
            position_to = consts.DEGREES_0
        if not clockwise and position_to == consts.DEGREES_0 - 1:
            position_to = consts.DEGREES_270
        positions = (position_from, position_to)
        candidates = None
        if self._figure_type == consts.TETROMINO_O:
            return
        how_to_rotate = consts.ROTATION_DATA[self._figure_type][positions]
        if how_to_rotate is None:
            return
        rotated_coords = self.get_rotated_coords(how_to_rotate)

        wall_kick_data = None
        if self._figure_type == consts.TETROMINO_I:
            wall_kick_data = consts.I_WALL_KICK_DATA[positions]
        else:
            wall_kick_data = consts.J_L_S_T_Z_WALL_KICK_DATA[positions]
        for i in range(5):
            candidates = self.test_case_kick_coords(
                rotated_coords, wall_kick_data[i])
            if self.are_coords_valid(candidates, terrain) is True:
                # Rotate
                # self._coords = candidates
                return self.rotate(candidates, clockwise)

    def get_rotated_coords(self, how_to_rotate: Dict[str, int]):
        coords = []
        for i in range(len(self._coords)):
            coords.append(relocate(self._coords[i], **how_to_rotate[i]))
        return coords

    def test_case_kick_coords(
        self,
        coords: List[Tuple[int, int]],
        test_case_scalar: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        candidates = []
        for coord in coords:
            row = coord[0] + test_case_scalar[1]
            col = coord[1] + test_case_scalar[0]
            candidates.append((row, col))
        return candidates

    def are_coords_valid(
        self,
        coords: List[Tuple[int, int]],
        terrain: List[List[int]]
    ) -> bool:
        for row, col in coords:
            print("row", row, "and col", col)
            if row < 0 or col < 0 or col > settings.COLS-1:
                print('returning False')
                return False
            if not terrain.is_empty:
                try:
                    if terrain.items[settings.ROWS - row][col] != 0:
                        return False
                except IndexError:
                    pass
        return True

    def rotate(
        self,
        coords: List[Tuple[int, int]],
        clockwise: bool = True,
    ) -> None:
        self._coords = coords
        if clockwise:
            self._rotation += 1
            if self._rotation > consts.DEGREES_270:
                self._rotation = consts.DEGREES_0
        else:
            self._rotation -= 1
            if self._rotation < consts.DEGREES_0:
                self._rotation = consts.DEGREES_270

    def check_test_case_for_coords(
        self,
        index: int,
        positions: Tuple[int, int],
        how_to_rotate: Dict[str, int],
        terrain: List[List[int]],
    ) -> Union[List[Tuple[int, int]], None]:
        current_coords = self._coords.copy()
        test_coords = None
        for i, coord in enumerate(current_coords):
            if self._figure_type == consts.TETROMINO_I:
                kick = consts.I_WALL_KICK_DATA[positions][index]
            else:
                kick = consts.J_L_S_T_Z_WALL_KICK_DATA[positions][index]
            test_coords = rotate_coord_by_kick(
                relocate(coord, **how_to_rotate[i]), kick)
            if not self.are_valid_coords(test_coords, terrain):
                break
        return test_coords

    def are_valid_coords(
        self,
        coords: Tuple[int, int],
        terrain: Grid,
    ) -> bool:
        print("coords:", coords)

        row, col = coords
        # Is in the lowest row or there's a figure below
        if row < 0:
            return False
        if col < 0 or col >= settings.PLAYFIELD_WIDTH:
            return False
        if not terrain.is_empty:
            try:
                if terrain.items[settings.ROWS - row][col] != 0:
                    return False
            except IndexError:
                pass
        return True

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
