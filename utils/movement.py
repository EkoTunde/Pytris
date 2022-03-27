from grid import Grid
from tetrominoes import Tetromino
from typing import List, Tuple
from utils.coords import relocate


def get_move_left_coords(
    tetromino: Tetromino,
    stack: Grid
) -> List[Tuple[int, int]]:
    coords = get_moved_coords(tetromino, left=1)
    if stack.is_valid_position(coords):
        return coords
    return None


def get_move_right_coords(
    tetromino: Tetromino,
    stack: Grid
) -> List[Tuple[int, int]]:
    coords = get_moved_coords(tetromino, right=1)
    if stack.is_valid_position(coords):
        return coords
    return None


def get_move_down_coords(
    tetromino: Tetromino,
    stack: Grid,
) -> List[Tuple[int, int]]:
    coords = get_moved_coords(tetromino, down=1)
    if stack.is_valid_position(coords):
        return coords
    return None


def get_moved_coords(
    self, down=0, left=0, right=0
) -> List[Tuple[int, int]]:
    result = []
    for coord in self._coords:
        relocated = relocate(coord, down=down, left=left, right=right)
        result.append(relocated)
    return result
