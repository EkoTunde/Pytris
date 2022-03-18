import random
from figure import Figure
import settings
import pygame


class Stack:

    def __init__(self):
        self.stack = [[0 for _ in range(settings.COLS)]
                      for _ in range(settings.ROWS)]

    def replace(self, figure: int, row: int, col: int) -> None:
        self.stack[row][col] = figure

    def clean_line(self):
        

    def search_lines(self):
        for row in range(settings.ROWS):
            if self.is_row_full(row):
                return row

    def is_row_full(self, row: int) -> bool:
        for col in range(settings.COLS):
            if self.stack[row][col] == 0:
                return False
        return True

    def add(self, figure: Figure):
        self.stack.append(figure)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def draw(self, win):
        for figure in self.stack:
            figure.draw(win)



class Game:

    def __init__(self) -> None:
        self.pile = []
        self.board = []
        for _ in range(0, 10):
            row = []
            for _ in range(0, 20):
                row.append(0)
            self.board.append(row)
        self.score = 0
        self.level = 1
        self.lines = 0
        self.next_figure = None
        self.current_figure = None
        self.figure_type = None
        self.figure_x = None
        self.figure_y = None
        self.figure_rotation = None
        self.figure_image = None
        self.figure_figure = None
        self.load_next_figure()
        self.pause = False

    def draw_board(self, win):
        # Draw a tetris board
        pygame.draw.rect(win, settings.BOARD_BACKGROUND, (settings.BOARD_X,
                         settings.BOARD_Y, settings.BOARD_WIDTH,
                         settings.BOARD_HEIGHT))
        for i in range(0, 10):
            for j in range(0, 20):
                pygame.draw.rect(win, settings.BACKGROUND, (
                    settings.BOARD_X + i * settings.BASE_SQUARE_SIZE + 1,
                    settings.BOARD_Y + j * settings.BASE_SQUARE_SIZE + 1,
                    settings.BASE_SQUARE_SIZE-2,
                    settings.BASE_SQUARE_SIZE-2),
                    border_radius=2)

    def apply_changes(self):
        if not self.pause:
            print("apply changes")

    def draw(self, win):
        self.apply_changes()
        self.draw_board(win)
        if self.current_figure is not None:
            self.current_figure.draw(win)
        self.draw_next_figure(win)
        self.draw_score(win)
        self.draw_level(win)
        self.draw_lines(win)

    def add_figure(self, figure):
        self.pile.append(figure)

    def load_next_figure(self):
        random_int = random.randint(1, 7)
        self.next_figure = Figure(random_int,
                                  settings.BOARD_X,
                                  settings.BOARD_Y)

    def draw_next_figure(self, win):
        # Draw the next figure
        self.next_figure.draw(win)

    def draw_score(self, win):
        pass

    def draw_level(self, win):
        pass

    def draw_lines(self, win):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass

    def move_down(self):
        pass

    def rotate(self):
        pass

    def hold(self):
        pass

    def drop(self):
        pass

    def pause(self) -> None:
        """
        Pause the game by inverting pause (bool).
        """
        self.pause = not self.pause
