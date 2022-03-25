import settings
from typing import List, Tuple


class Stack():

    def __init__(self, *args):
        self._items = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    @property
    def items(self) -> list:
        return self._items

    # def add_figure(self, figure: Figure) -> None:
    #     """
    #     Adds a figure to the stack.

    #     Returns:
    #         [int]: the first available row.
    #     """
    #     for coord in figure.coords:
    #         self._items.add(coord, figure.figure_type)

    def add(
        self,
        coords: List[Tuple[int, int]],
        figure_type: List[Tuple[int, int]],
    ) -> int:
        """
        Adds a figure to the stack at it's coords (row, col).

        Returns first available row from 19 and on.
        """
        # print(self._items)
        for row, col in coords:
            # print("row", row, "and col", col)
            # if row == 0:
            #     print("debug")
            try:
                # if not self._has_row(row):
                #     self._items.append([0] * settings.COLS)
                self._items[row][col] = figure_type
            except IndexError:
                # print("INDEX ERROR")
                return False
        return settings.DEFAULT_AVAILABLE_ROW

    def _has_row(self, row: int):
        try:
            if self.is_empty:
                return False
            return self.size > row
        except IndexError:
            return False

    def clear_full_rows(self):
        for i in reversed(range(len(self))):
            if self._items.is_row_full(self[i]):
                self.pop(i)

    def is_row_full(self, row: List[int]) -> bool:
        if 0 in row:
            return False

    def reset_row(self, index):
        self._items[index] = [0] * settings.COLS

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


if __name__ == '__main__':
    stack = Stack()
    # print(stack)
