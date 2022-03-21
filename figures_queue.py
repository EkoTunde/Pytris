
# Class Queue
from typing import Union

from tetrominoes import Tetromino


class FiguresQueue:
    """Figures' queue class."""

    def __init__(self, *args: Tetromino) -> None:
        self.items = []
        for figure in args:
            self.items.insert(0, figure)

    def is_empty(self) -> bool:
        return self.items == []

    def enqueue(self, item) -> None:
        self.items.insert(0, item)

    def dequeue(self) -> Union[Tetromino, None]:
        if self.is_empty():
            return None
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> Tetromino:
        return self.items[-1]

    def __str__(self):
        return str(self.items)
