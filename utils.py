from typing import List, Tuple
import consts
import settings
from stack import Stack


def get_initial_coords(
    figure_type: int,
    row: int = settings.DEFAULT_AVAILABLE_ROW,
) -> list[Tuple[int, int]]:
    """
    Process coordinates for figure.
    """
    if figure_type == consts.FIGURE_I:
        y = 3
        #    0 1 2 3 4 5 6 7 8 9
        # 0
        # 1        o o o o
        # 2
        return [
            (row, y),
            (row, y + 1),
            (row, y + 2),
            (row, y + 3)
        ]
    elif figure_type == consts.FIGURE_O:
        #    0 1 2 3 4 5 6 7 8 9
        # 0          o o
        # 1          o o
        # 2
        y = 4
        return [
            (row, y),
            (row, y + 1),
            (row+1, y),
            (row+1, y + 1)
        ]
    elif figure_type == consts.FIGURE_T:
        #    0 1 2 3 4 5 6 7 8 9
        # 0          o
        # 1        o o o
        # 2
        y = 3
        return [
            (row, y),
            (row, y + 1),
            (row, y + 2),
            (row+1, y + 1)
        ]
    elif figure_type == consts.FIGURE_L:
        #    0 1 2 3 4 5 6 7 8 9
        # 0            o
        # 1        o o o
        # 2
        y = 3
        return [
            (row, y),
            (row, y + 1),
            (row, y + 2),
            (row+1, y + 2)
        ]
    elif figure_type == consts.FIGURE_J:
        #    0 1 2 3 4 5 6 7 8 9
        # 0        o
        # 1        o o o
        # 2
        y = 3
        return [
            (row, y),
            (row, y + 1),
            (row, y + 2),
            (row+1, y)
        ]
    elif figure_type == consts.FIGURE_S:
        #    0 1 2 3 4 5 6 7 8 9
        # 0          o o
        # 1        o o
        # 2
        y = 3
        return [
            (row, y),
            (row, y + 1),
            (row+1, y + 1),
            (row+1, y + 2)
        ]
    elif figure_type == consts.FIGURE_Z:
        #    0 1 2 3 4 5 6 7 8 9
        # 0        o o
        # 1          o o
        # 2
        y = 3
        return [
            (row, y+1),
            (row, y + 2),
            (row+1, y),
            (row+1, y + 1)
        ]


def will_collide_bellow(
        stack: Stack,
        figure_coords: List[Tuple[int, int]]
) -> bool:
    for row, col in figure_coords:
        # Is in the lowest row or there's a figure below
        if row == 0:
            return True
        if not stack.is_empty:
            try:
                if stack.items[settings.ROWS - row - 1][col] != 0:
                    return True
            except IndexError:
                pass
    return False


def will_collide_left(
    stack: Stack,
    figure_coords: List[Tuple[int, int]]
) -> bool:
    for row, col in figure_coords:
        if col == 0:
            return True
        if not stack.is_empty:
            try:
                if stack.items[settings.ROWS - row][col - 1] != 0:
                    return True
            except IndexError:
                pass
        # if stack.size == 0:
        #     return False
        # if stack.size >= row:
        #     if stack.items[row][col - 1] != 0:
        #         return True
    return False


def will_collide_right(
    stack: Stack,
    figure_coords: List[Tuple[int, int]]
) -> bool:
    for row, col in figure_coords:
        if col == settings.COLS - 1:
            return True
        if not stack.is_empty:
            try:
                if stack.items[settings.ROWS - row][col + 1] != 0:
                    return True
            except IndexError:
                pass
        # if stack.size == 0:
        #     return False
        # if stack.size >= row:
        #     if stack.items[row][col + 1] != 0:
        #         return True
    return False


def rotate_figure_i(
        coords: List[Tuple[int, int]],
        current_rotation: int = 0,
) -> List[Tuple[int, int]]:
    """
    Rotate figure I.
    """
    A = coords[0]
    B = coords[1]
    C = coords[2]
    D = coords[3]
    if current_rotation == 0:
        A = (A[0]+1, A[1]+2)
        B = (B[0], B[1]+1)
        C = (C[0]-1, C[1])
        D = (D[0]-2, D[1]-1)
    if current_rotation == 1:
        A = (A[0]+1, A[1]+1)
        C = (C[0]-1, C[1]+1)
        D = (D[0]-1, D[1]+2)
    if current_rotation == 2:
        A = (A[0]-2, A[1]+2)
        B = (B[0]+1, B[1]-1)
        D = (D[0]-1, D[1]+1)
    if current_rotation == 3:
        A = (A[0]-1, A[1]+1)
        B = (B[0]+1, B[1])
        C = (C[0], C[1]-1)
        D = (D[0]+1, D[1]-1)

    new_coords = []
    for row, col in coords:
        new_coords.append((col, row))
    return new_coords
