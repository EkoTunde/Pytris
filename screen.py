import pygame
from assets import ASSETS
from tetrominoes import Tetromino
from provider import Provider
import settings
from grid import Grid
from utils.coords import calc_initial_coords


class Screen:

    def __init__(self, window: pygame.Surface):
        self.win = window
        self.current_figure = None
        self.next_figure = None
        self.hold_figure = None
        self.score = 0
        self.level = 1
        self.lines = 0
        self._font = pygame.font.Font(pygame.font.get_default_font(), 16)

    def draw(
        self,
        grid: Grid = None,
        provider: Provider = None,
        is_paused: bool = False,
    ) -> None:
        if is_paused is False:
            self.win.fill(settings.BACKGROUND)
            self.draw_playfield()
            self.draw_preview_field()
            if grid:
                self.draw_grid(grid)
            if provider:
                tetromino = provider.peek()
                self.draw_tetromino(tetromino, grid)
        pygame.display.update()

    def draw_playfield(self):
        # Draw a tetris board
        pygame.draw.rect(self.win, settings.PLAYFIELD_BACKGROUND,
                         (settings.PLAYFIELD_X, settings.PLAYFIELD_Y,
                          settings.PLAYFIELD_WIDTH, settings.PLAYFIELD_HEIGHT))
        for i in range(settings.COLS):
            for j in range(settings.ROWS):
                pygame.draw.rect(self.win, settings.BACKGROUND, (
                    settings.PLAYFIELD_X + i * settings.BASE_SQUARE_SIZE + 1,
                    settings.PLAYFIELD_Y + j * settings.BASE_SQUARE_SIZE + 1,
                    settings.BASE_SQUARE_SIZE-2,
                    settings.BASE_SQUARE_SIZE-2),
                    border_radius=2)

    def draw_grid(self, grid: Grid):
        # os.system('cls')
        # print(stack)
        for i in range(0, grid.size):
            for j in range(0, settings.COLS):
                if grid.items[i][j] != 0:
                    x = settings.PLAYFIELD_X + j * settings.BASE_SQUARE_SIZE
                    y = settings.PLAYFIELD_Y + (settings.ROWS - i-1) * \
                        settings.BASE_SQUARE_SIZE
                    self.win.blit(ASSETS[grid.items[i][j]], (x, y))

    def draw_tetromino(self, tetromino: Tetromino, grid: Grid):
        if tetromino.coords is None:
            tetromino.coords = calc_initial_coords(tetromino, grid)
        for row, col in tetromino.coords:
            # print("row is", row, " and col is", col)
            x = settings.PLAYFIELD_X + col*settings.BASE_SQUARE_SIZE
            y = settings.PLAYFIELD_Y + (settings.ROWS - 1 - row) * \
                settings.BASE_SQUARE_SIZE
            self.win.blit(tetromino.asset, (x, y))

    def draw_preview_field(self):
        shifted_x = settings.PLAYFIELD_X + settings.PLAYFIELD_WIDTH
        padding_horizontal = settings.BASE_SQUARE_SIZE * 2
        margin_top = settings.BASE_SQUARE_SIZE
        x = shifted_x + padding_horizontal
        y = settings.PLAYFIELD_Y + margin_top
        width = ((settings.PLAYFIELD_WIDTH / settings.COLS) * 6)
        height = settings.PLAYFIELD_HEIGHT / 2
        title = self._font.render('Some Text', False, (255, 255, 255))
        self.win.blit(title, (x, settings.PLAYFIELD_Y))
        pygame.draw.rect(
            self.win, settings.PLAYFIELD_BACKGROUND, (x, y, width, height))
        for i in range(settings.PREVIEW_COLS):
            for j in range(settings.PREVIEW_ROWS):
                pygame.draw.rect(self.win, settings.BACKGROUND, (
                    x + i * settings.BASE_SQUARE_SIZE + 1,
                    y + j * settings.BASE_SQUARE_SIZE + 1,
                    settings.BASE_SQUARE_SIZE-2,
                    settings.BASE_SQUARE_SIZE-2),
                    border_radius=2)
