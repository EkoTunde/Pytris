import random
from figure import Figure
import settings
import pygame


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

    def pause(self, pause: bool = True) -> None:
        self.pause = pause
        print("pause")
