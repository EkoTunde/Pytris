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
    x = 3
    if figure_type == consts.TETROMINO_I:
        #    0 1 2 3 4 5 6 7 8 9
        # 0
        # 1        o o o o
        # 2
        return [
            (row, x),
            (row, x + 1),
            (row, x + 2),
            (row, x + 3)
        ]
    elif figure_type == consts.TETROMINO_O:
        #    0 1 2 3 4 5 6 7 8 9
        # 0          o o
        # 1          o o
        # 2
        x = 4
        return [
            (row, x),
            (row, x + 1),
            (row+1, x),
            (row+1, x + 1)
        ]
    elif figure_type == consts.TETROMINO_T:
        #    0 1 2 3 4 5 6 7 8 9
        # 0          o
        # 1        o o o
        # 2
        return [
            (row, x),
            (row, x + 1),
            (row, x + 2),
            (row+1, x + 1)
        ]
    elif figure_type == consts.TETROMINO_L:
        #    0 1 2 3 4 5 6 7 8 9
        # 0            o
        # 1        o o o
        # 2
        return [
            (row, x),
            (row, x + 1),
            (row, x + 2),
            (row+1, x + 2)
        ]
    elif figure_type == consts.TETROMINO_J:
        #    0 1 2 3 4 5 6 7 8 9
        # 0        o
        # 1        o o o
        # 2
        return [
            (row, x),
            (row, x + 1),
            (row, x + 2),
            (row+1, x)
        ]
    elif figure_type == consts.TETROMINO_S:
        #    0 1 2 3 4 5 6 7 8 9
        # 0          o o
        # 1        o o
        # 2
        return [
            (row, x),
            (row, x + 1),
            (row+1, x + 1),
            (row+1, x + 2)
        ]
    elif figure_type == consts.TETROMINO_Z:
        #    0 1 2 3 4 5 6 7 8 9
        # 0        o o
        # 1          o o
        # 2
        return [
            (row+1, x),
            (row+1, x + 1),
            (row, x+1),
            (row, x + 2),
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
    return False


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


def rotate_figure_i(
    coords: List[Tuple[int, int]],
    current_rotation: int = 0,
) -> List[Tuple[int, int]]:
    """
    Rotate figure I.
    """
    A, B, C, D = coords[0], coords[1], coords[2], coords[3]
    if current_rotation == 0:
        A = relocate(A, up=1, right=2)
        # A = (A[0]+1, A[1]+2)
        B = relocate(B, right=1)
        # B = (B[0], B[1]+1)
        C = relocate(C, down=1)
        # C = (C[0]-1, C[1])
        D = relocate(D, down=1, left=1)
        # D = (D[0]-2, D[1]-1)
    if current_rotation == 1:
        A = relocate(A, down=1, right=1)
        # A = (A[0]-1, A[1]+1)
        C = relocate(C, up=1, left=1)
        # C = (C[0]+1, C[1]-1)
        D = relocate(D, up=2, left=1)
        # D = (D[0]+2, D[1]-2)
    if current_rotation == 2:
        A = relocate(A, down=2, left=2)
        # A = (A[0]-2, A[1]-2)
        B = relocate(B, down=1, left=1)
        # B = (B[0]-1, B[1]-1)
        D = relocate(D, up=1, right=1)
        # D = (D[0]+1, D[1]+1)
    if current_rotation == 3:
        A = relocate(A, up=2, left=1)
        # A = (A[0]+2, A[1]-1)
        B = relocate(B, up=1)
        # B = (B[0]+1, B[1])
        C = relocate(C, right=1)
        # C = (C[0], C[1]+1)
        D = relocate(D, right=2, down=1)
        # D = (D[0]-1, D[1]+2)
    coords = [A, B, C, D]
    return coords


def rotate_figure_z(
    coords: List[Tuple[int, int]],
    current_rotation: int = 0,
) -> List[Tuple[int, int]]:
    """
    Rotate figure I.
    """
    A, B, C, D = coords[0], coords[1], coords[2], coords[3]
    if current_rotation == 0:
        A = (A[0], A[1]+2)
        B = (B[0]-1, B[1]+1)
        D = (D[0]-1, D[1]-1)
    if current_rotation == 1:
        A = (A[0]-1, A[1])
        B = (B[0], B[1]-1)
        C = (C[0]+1, C[1])
        D = (D[0]+2, D[1]-1)
    if current_rotation == 2:
        A = (A[0]-1, A[1]-1)
        C = (C[0]-1, C[1]+1)
        D = (D[0], D[1]+2)
    if current_rotation == 3:
        A = (A[0]+2, A[1]-1)
        B = (B[0]+1, B[1])
        C = (C[0], C[1]-1)
        D = (D[0]-1, D[1])
    coords = [A, B, C, D]
    return coords
