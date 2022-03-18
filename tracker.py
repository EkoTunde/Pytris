import settings
from stack import Stack


class Tracker:

    def __init__(self) -> None:
        self.stack = Stack()
        self.places = [[0 for _ in range(settings.COLS)]
                       for _ in range(settings.ROWS)]

    def move_left(self) -> bool:
        return False

    def move_right(self) -> bool:
        return False

    def move_down(self) -> bool:
        return False

    def rotate(self) -> bool:
        return False
