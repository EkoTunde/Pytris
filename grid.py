import consts
import settings
from typing import List, Tuple


class Grid():

    def __init__(self, *args):
        self._items = [[0 for _ in range(settings.COLS)]
                       for _ in range(settings.ROWS)]
        # self._items = [
        #     # 0 1  2  3  4  5  6  7  8  9
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 00
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 01
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 02
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 03
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 04
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 05
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 06
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 07
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 08
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 09
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 14
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 15
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 17
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 18
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 19
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 20
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 21
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 22
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 23
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 24
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 25
        # ]

    @property
    def items(self) -> List[List[int]]:
        return self._items

    def add(
        self,
        coords: List[Tuple[int, int]],
        figure_type: List[Tuple[int, int]],
    ) -> None:
        """
        Adds a figure to the stack at it's coords (row, col).
        """
        # print(self._items)
        for row, col in coords:
            self._items[row][col] = figure_type

    def is_valid_position(
        self,
        coords: List[Tuple[int, int]]
    ) -> bool:
        for row, col in coords:
            if row < 0 or row > settings.ROWS - 1:
                return False
            if col < 0 or col > settings.COLS - 1:
                return False
            if self._items[row][col] != 0:
                return False
        return True

    @property
    def size(self):
        return len(self._items)

    @property
    def is_empty(self):
        return len(self._items) == 0

    def __str__(self):
        s = ""
        for i, row in enumerate(reversed(self._items)):
            s += str(len(self._items) - 1 - i).zfill(2) + row.__str__() + "\n"
        return s

    def __is_row_full(self, row: List[int]) -> bool:
        for col in row:
            if col == consts.EMPTY_CELL:
                return False
        return True

    def update(self) -> int:
        """
        Updates stack clearing full rows.

        Returns:
            int: the amount of cleared rows.
        """
        cursor = 0
        rows_cleared = 0
        while cursor < len(self._items):
            if self.__is_row_full(self._items[cursor]):
                self._items.pop(cursor)
                self._items.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                rows_cleared += 1
            else:
                cursor += 1
        return rows_cleared
