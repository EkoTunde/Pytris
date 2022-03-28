import consts
import settings

from grid import Grid
from tetrominoes import Tetromino
from typing import List, Tuple

from utils.movement import get_moved_coords


def calc_initial_coords(
    tetromino: Tetromino,
    grid: Grid
) -> List[Tuple[int, int]]:
    """Returns the coordinates of the tetromino in the initial position."""
    row = calc_first_available_row(
        grid, consts.FIRST_NEEDED_ROWS_DATA[tetromino.figure_type])
    initial_coords = consts.INITIAL_COORDS_DATA.get(tetromino.figure_type)
    return [
        (row + initial_coords[0][0],
         tetromino.initial_x + initial_coords[0][1]),
        (row + initial_coords[1][0],
         tetromino.initial_x + initial_coords[1][1]),
        (row + initial_coords[2][0],
         tetromino.initial_x + initial_coords[2][1]),
        (row + initial_coords[3][0],
         tetromino.initial_x + initial_coords[3][1]),
    ]


def calc_first_available_row(grid: Grid, cols: Tuple[int, ...]) -> int:
    result = settings.DEFAULT_AVAILABLE_ROW
    row = settings.DEFAULT_AVAILABLE_ROW
    max = settings.DEFAULT_MAX_AVAILABLE_ROW
    for col in cols:
        if grid.items[settings.DEFAULT_AVAILABLE_ROW][col] != 0:
            row += 1
            result = row
        if row > max:
            raise ValueError("This row isn't playable.")
    return result


def calc_coords_from_row(
    tetromino: Tetromino,
    row: int
) -> List[Tuple[int, int]]:
    """
    Returns the coordinates of the tetromino
    in the initial position for provided row
    """
    initial_coords = consts.INITIAL_COORDS_DATA.get(tetromino.figure_type)
    return [
        (row + initial_coords[0][0] - 6,
         tetromino.initial_x + initial_coords[0][1] - 3),
        (row + initial_coords[1][0] - 6,
         tetromino.initial_x + initial_coords[1][1] - 3),
        (row + initial_coords[2][0] - 6,
         tetromino.initial_x + initial_coords[2][1] - 3),
        (row + initial_coords[3][0] - 6,
         tetromino.initial_x + initial_coords[3][1] - 3),
    ]


def calculate_ghost_coords(
    tetromino: Tetromino,
    grid: Grid
) -> List[Tuple[int, int]]:
    return lowest_coords(tetromino.coords, grid)


def lowest_coords(
    coords: List[Tuple[int, int]],
    grid: Grid
) -> List[Tuple[int, int]]:
    """
    Returns the coordinates of the tetromino
    in the lowest available position.
    """
    # return coords
    lowered_coords = get_moved_coords(coords, down=1)
    if not grid.is_valid_position(lowered_coords):
        return coords
    return lowest_coords(lowered_coords, grid)
