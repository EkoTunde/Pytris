import settings


class Board:

    def __init__(self):
        self.board = [[0 for _ in range(settings.COLS)]
                      for _ in range(settings.ROWS)]
