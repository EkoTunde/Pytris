import pygame
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
        current_figure: pygame.Rect,
        next_figure_type: int,

    ) -> None:
        self.win.fill(settings.BACKGROUND)
        self.draw_board()
        pygame.display.update()

    def draw_board(self, stack):
        # Draw a tetris board
        pygame.draw.rect(self.win, settings.BOARD_BACKGROUND,
                         (settings.BOARD_X, settings.BOARD_Y,
                          settings.BOARD_WIDTH, settings.BOARD_HEIGHT))
        for i in range(0, 10):
            for j in range(0, 20):
                pygame.draw.rect(self.win, settings.BACKGROUND, (
                    settings.BOARD_X + i * settings.BASE_SQUARE_SIZE + 1,
                    settings.BOARD_Y + j * settings.BASE_SQUARE_SIZE + 1,
                    settings.BASE_SQUARE_SIZE-2,
                    settings.BASE_SQUARE_SIZE-2),
                    border_radius=2)

    def draw_stack(self, stack: Stack):
        for i in range(0, len(stack.stack)):
            for j in range(0, len(stack.stack[i])):
                if stack.stack[i][j] != 0:
                    pygame.draw.rect(self.win, settings.COLORS[stack.stack[i][j]],
                                     (settings.BOARD_X + i * settings.BASE_SQUARE_SIZE,
                                      settings.BOARD_Y + j * settings.BASE_SQUARE_SIZE,
                                      settings.BASE_SQUARE_SIZE,
                                      settings.BASE_SQUARE_SIZE))
        pass
