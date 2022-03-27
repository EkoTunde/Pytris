import consts
from typing import Dict, List, Tuple, Union
from grid import Grid
from tetrominoes import Tetromino
from utils.coords import relocate


def get_rotate_right_coords(
    tetromino: Tetromino,
    stack: Grid
) -> Union[List[Tuple[int, int]], None]:
    position_from = tetromino.rotation
    position_to = position_from + 1
    if position_to == consts.DEGREES_270 + 1:
        position_to = consts.DEGREES_0
    rotation_flow = (position_from, position_to)
    return get_rotation_coords(tetromino, stack, rotation_flow)


def get_rotate_left_coords(
    tetromino: Tetromino,
    stack: Grid
) -> Union[List[Tuple[int, int]], None]:
    position_from = tetromino.rotation
    position_to = position_from - 1
    if position_to == consts.DEGREES_0 - 1:
        position_to = consts.DEGREES_270
    rotation_flow = (position_from, position_to)
    return get_rotation_coords(tetromino, stack, rotation_flow)


def get_rotation_coords(
    tetromino: Tetromino,
    stack: Grid,
    rotation_flow: Tuple[int, int]
) -> Union[List[Tuple[int, int]], None]:
    if tetromino.figure_type == consts.TETROMINO_O:
        return None
    how_to_rotate = consts.ROTATION_DATA[tetromino.figure_type][rotation_flow]
    if how_to_rotate is None:
        return None
    rotated_coords = get_rotated_coords(tetromino, how_to_rotate)

    if tetromino.figure_type == consts.TETROMINO_I:
        wall_kick_data = consts.I_WALL_KICK_DATA[rotation_flow]
    else:
        wall_kick_data = consts.J_L_S_T_Z_WALL_KICK_DATA[rotation_flow]

    for i in range(5):
        candidates = test_case_kick_coords(rotated_coords, wall_kick_data[i])
        if stack.is_valid_position(candidates):
            return candidates
    return None


def get_rotated_coords(
    tetromino: Tetromino,
    how_to_rotate: Dict[str, int]
) -> List[Tuple[int, int]]:
    coords = []
    for i in range(len(tetromino.coords)):
        coords.append(relocate(tetromino.coords[i], **how_to_rotate[i]))
    return coords


def test_case_kick_coords(
    coords: List[Tuple[int, int]],
    test_case_scalar: Tuple[int, int]
) -> List[Tuple[int, int]]:
    candidates = []
    for coord in coords:
        row = coord[0] + test_case_scalar[1]
        col = coord[1] + test_case_scalar[0]
        candidates.append((row, col))
    return candidates
