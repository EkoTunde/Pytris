
# Class Queue
from typing import List, Union
from random import shuffle

from tetrominoes import Tetromino


class Provider:

    def __init__(self, *args: Tetromino) -> None:
        self._items = []
        if not args:
            self.__refill()
        else:
            for tetromino in args:
                if isinstance(tetromino, Tetromino):
                    self.enqueue(tetromino)

    def __refill(self):
        tetrominoes = [1, 2, 3, 4, 5, 6, 7].copy()
        shuffle(tetrominoes)
        for tetromino in tetrominoes:
            self.enqueue(Tetromino(tetromino))

    def is_empty(self) -> bool:
        return self._items == []

    def __needs_refill(self) -> bool:
        return len(self._items) == 4

    def enqueue(self, tetromino: Tetromino) -> None:
        self._items.append(tetromino)

    def dequeue(self) -> Union[Tetromino, None]:
        if self.is_empty() or self.__needs_refill():
            self.__refill()
        return self._items.pop(0)

    def size(self) -> int:
        return len(self._items)

    def peek(self) -> Tetromino:
        return self._items[0]

    def get_next(
        self, n: int
    ) -> List[Tetromino]:
        return self._items[1:n+1]

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + ", ".join([str(item) for item in self._items]) + "]"
