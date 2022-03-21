import pygame
from assets import ASSETS
from tetrominoes import Tetromino
from figures_queue import FiguresQueue
import settings
from stack import Stack


class Screen:

    def __init__(self, window: pygame.Surface):
        self.win = window
        self.current_figure = None
        self.next_figure = None
        self.hold_figure = None
        self.score = 0
        self.level = 1
        self.lines = 0

    def draw(
        self,
        stack: Stack = None,
        queue: FiguresQueue = None,
        first_available_row: int = settings.DEFAULT_AVAILABLE_ROW
    ) -> None:
        self.win.fill(settings.BACKGROUND)
        self.draw_playfield()
        if stack:
            self.draw_stack(stack)
        if queue:
            figure = queue.peek()
            self.draw_figure(figure, first_available_row)
        pygame.display.update()

    def draw_playfield(self):
        # Draw a tetris board
        pygame.draw.rect(self.win, settings.PLAYFIELD_BACKGROUND,
                         (settings.BOARD_X, settings.BOARD_Y,
                          settings.PLAYFIELD_WIDTH, settings.PLAYFIELD_HEIGHT))
        for i in range(0, 10):
            for j in range(0, 20):
                pygame.draw.rect(self.win, settings.BACKGROUND, (
                    settings.BOARD_X + i * settings.BASE_SQUARE_SIZE + 1,
                    settings.BOARD_Y + j * settings.BASE_SQUARE_SIZE + 1,
                    settings.BASE_SQUARE_SIZE-2,
                    settings.BASE_SQUARE_SIZE-2),
                    border_radius=2)

    def draw_stack(self, stack: Stack):
        for i in range(0, stack.size):
            for j in range(0, settings.COLS):
                if stack.items[i][j] != 0:
                    self.win.blit(
                        ASSETS[stack.items[i][j]],
                        (settings.BOARD_X + j * settings.BASE_SQUARE_SIZE),
                        (settings.BOARD_Y + (settings.ROWS - i)
                         * settings.BASE_SQUARE_SIZE)
                    )

    def draw_figure(self, figure: Tetromino, first_available_row: int):
        if figure.coords is None:
            figure.please_get_coords(first_available_row)
        for row, col in figure.coords:
            print("row is", row, " and col is", col)
            x = settings.BOARD_X + col*settings.BASE_SQUARE_SIZE
            y = settings.BOARD_Y + (settings.ROWS - 1 - row) * \
                settings.BASE_SQUARE_SIZE
            self.win.blit(figure.asset, (x, y))
