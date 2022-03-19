import settings
from typing import Dict, List, Tuple


class Stack():

    def __init__(self, *args):
        self._items = []

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
        coord: Tuple[int, int],
        figure_type: int
    ) -> int:
        """
        Adds a figure to the stack at given coords (row, col).

        Args:
            coord (Tuple[int, int]): The coords of the figure (i, j).
            figure_type (int): The type of the figure.
        """
        self._items[coord[0]][coord[1]] = figure_type

    def get_collisions(self, figure) -> Dict[str, bool]:
        bellow, left, right = False, False, False
        for row, col in figure.coords:
            if not bellow:
                bellow = self.will_collide_bellow(row, col)
            if not left:
                left = self.will_collide_left(row, col)
            if not right:
                right = self.will_collide_right(row, col)
            if bellow and left and right:
                break
        return {
            "bellow": bellow,
            "left": left,
            "right": right
        }

    def will_collide_bellow(self, row, col) -> bool:
        # Is in the lowest row
        if row == settings.ROWS - 1:
            return True
        # There's a figure below
        if self._items[settings.ROWS - row + 1][col] != 0:
            return True
        return False

    def will_collide_left(self, row, col) -> bool:
        if col == 0:
            return True
        if self._items[row][settings.COLS + col - 1] != 0:
            return True
        return False

    def will_collide_right(self, row, col) -> bool:
        if col == settings.COLS - 1:
            return True
        if self._items[row][settings.COLS + col + 1] != 0:
            return True
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


if __name__ == '__main__':
    stack = Stack()
    print(stack)
