from grid import Grid
from tetrominoes import Tetromino


class Score:

    def __init__(self):
        self.__total = 0

    def update(
        self,
        lines: int,
        tetromino: Tetromino,
        grid: Grid
    ) -> int:
        return self.__total
