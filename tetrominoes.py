import os
import consts
import pygame
import settings
from assets import ASSETS
from typing import Dict, List, Tuple, Union
from stack import Stack
from utils import relocate, rotate_coord_by_kick
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
        # A esta rotación le comprobamos si entra,
        # y sino usamos el siguiente test case
        wall_kick_data = None
        if self._figure_type == consts.TETROMINO_I:
            wall_kick_data = consts.I_WALL_KICK_DATA[positions]
        else:
            wall_kick_data = consts.J_L_S_T_Z_WALL_KICK_DATA[positions]
        for i in range(5):
            candidates = self.test_case_kick_coords(
                rotated_coords, wall_kick_data[i])
            print(candidates)
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
            print("coord to apply test case:", coord, "with scalara", test_case_scalar,
                  "row is", row, "col is", col)
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

    # def __update_rotation(self, decrease: bool = False) -> None:
    #     if decrease:
    #         self._rotation -= 1
    #         if self._rotation < consts.DEGREES_0:
    #             self._rotation = consts.DEGREES_270
    #     else:
    #         self._rotation += 1
    #         if self._rotation > consts.DEGREES_270:
    #             self._rotation = consts.DEGREES_0

    def are_valid_coords(
        self,
        coords: Tuple[int, int],
        terrain: Stack,
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
