from grid import Grid
from tetrominoes import Tetromino
from typing import List, Tuple
from utils.base import relocate


def get_move_left_coords(
    tetromino: Tetromino,
    grid: Grid
) -> List[Tuple[int, int]]:
    coords = get_moved_coords(tetromino.coords, left=1)
    if grid.is_valid_position(coords):
        return coords
    return None


def get_move_right_coords(
    tetromino: Tetromino,
    grid: Grid
) -> List[Tuple[int, int]]:
    coords = get_moved_coords(tetromino.coords, right=1)
    if grid.is_valid_position(coords):
        return coords
    return None


def get_move_down_coords(
    tetromino: Tetromino,
    grid: Grid,
    how_much: int = 1
) -> List[Tuple[int, int]]:
    coords = get_moved_coords(tetromino.coords, down=how_much)
    if grid.is_valid_position(coords):
        return coords
    return None


def get_moved_coords(
    coords: List[Tuple[int, int]], down=0, left=0, right=0
) -> List[Tuple[int, int]]:
    result = []
    for coord in coords:
        relocated = relocate(coord, down=down, left=left, right=right)
        result.append(relocated)
    return result
