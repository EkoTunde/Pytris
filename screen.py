import pygame
from assets import ASSETS
import assets
import consts
from tetrominoes import Tetromino
from provider import Provider
import settings
from grid import Grid
from utils.coords import calc_coords_from_row, calc_initial_coords


class Screen:

    def __init__(self, window: pygame.Surface, font: pygame.font.Font):
        self.win = window
        self.current_figure = None
        self.next_figure = None
        self.hold_figure = None
        self.score = 0
        self.level = 1
        self.lines = 0
        self._font = font
        self._cache = {
            'score_title': self._font.render(
                'Score', False, (255, 255, 255)),
            'level_title': self._font.render(
                'Level', False, (255, 255, 255)),
            'lines_title': self._font.render(
                'Lines', False, (255, 255, 255)),
            consts.NEXT_FIELD_TITLE_CACHE: self._font.render(
                consts.NEXT_FIELD_TITLE, False, consts.WHITE),
            consts.HOLD_FIELD_TITLE_CACHE: self._font.render(
                consts.HOLD_FIELD_TITLE, False, consts.WHITE),
        }

    def draw(
        self,
        is_paused: bool = False,
        grid: Grid = None,
        provider: Provider = None,
        on_hold: Tetromino = None,
    ) -> None:
        if is_paused is False:
            self.win.fill(settings.BACKGROUND)
            self.draw_playfield()
            self.draw_next_field()
            self.draw_next_field_title()
            self.draw_hold_field()
            self.draw_hold_field_title()
            if grid:
                self.draw_grid(grid)
            if provider:
                self.draw_falling_tetromino(provider.peek())
                self.draw_next_tetrominoes(provider)
            if on_hold:
                self.draw_tetromino_on_hold(on_hold)
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
        for i in range(0, grid.size):
            for j in range(0, settings.COLS):
                if grid.items[i][j] != 0:
                    x = settings.PLAYFIELD_X + j * settings.BASE_SQUARE_SIZE
                    y = settings.PLAYFIELD_Y + (settings.ROWS - i-1) * \
                        settings.BASE_SQUARE_SIZE
                    self.win.blit(ASSETS[grid.items[i][j]], (x, y))

    def draw_falling_tetromino(self, tetromino: Tetromino) -> None:
        for row, col in tetromino.coords:
            x = settings.PLAYFIELD_X + col*settings.BASE_SQUARE_SIZE
            y = settings.PLAYFIELD_Y + (settings.ROWS - 1 - row) * \
                settings.BASE_SQUARE_SIZE
            self.win.blit(tetromino.asset, (x, y))

    def draw_next_field(self):
        self._cache[consts.NEXT_FIELD_CACHE] = pygame.draw.rect(
            self.win, settings.PLAYFIELD_BACKGROUND, (
                settings.NEXT_FIELD_X, settings.NEXT_FIELD_Y,
                settings.NEXT_FIELD_WIDTH, settings.NEXT_FIELD_HEIGHT))

    def draw_next_field_title(self):
        title = self._cache[consts.NEXT_FIELD_TITLE_CACHE]
        if consts.NEXT_FIELD_TITLE_RECT_CACHE in self._cache:
            x = self._cache[consts.NEXT_FIELD_TITLE_RECT_CACHE].left
        else:
            next_field = self._cache[consts.NEXT_FIELD_CACHE]
            next_field_center_x = next_field.left + next_field.width / 2
            title_center_x = title.get_width() / 2
            x = next_field_center_x - title_center_x
        rect = self.win.blit(
            title, (x, settings.PLAYFIELD_Y + settings.HOLD_FIELD_MARGIN_TOP))
        self._cache[consts.NEXT_FIELD_TITLE_RECT_CACHE] = rect

    def draw_next_tetrominoes(self, provider: Provider) -> None:
        next_field = self._cache[consts.NEXT_FIELD_CACHE]
        next_field_center_x = next_field.left + next_field.width / 2
        base_y = next_field.top + settings.BASE_NEXT_FIELD_PADDING
        for i, tetromino in enumerate(provider.get_next(3)):
            asset = assets.TETROMINOES_ASSETS[tetromino.figure_type]
            asset_center = asset.get_width() / 2
            x = next_field_center_x - asset_center
            y = base_y + i * settings.MAX_TETROMINO_HEIGHT + \
                i * settings.BASE_NEXT_FIELD_PADDING
            if tetromino.figure_type == consts.TETROMINO_I:
                y += settings.BASE_NEXT_FIELD_PADDING
            self.win.blit(asset, (x, y))

    def draw_hold_field(self) -> None:
        self._cache[consts.HOLD_FIELD_CACHE] = pygame.draw.rect(
            self.win, settings.PLAYFIELD_BACKGROUND, (
                settings.HOLD_FIELD_X, settings.HOLD_FIELD_Y,
                settings.HOLD_FIELD_WIDTH, settings.HOLD_FIELD_HEIGHT))

    def draw_hold_field_title(self):
        title = self._cache[consts.HOLD_FIELD_TITLE_CACHE]
        if consts.HOLD_FIELD_TITLE_RECT_CACHE in self._cache:
            x = self._cache[consts.HOLD_FIELD_TITLE_RECT_CACHE].left
        else:
            hold_field = self._cache[consts.HOLD_FIELD_CACHE]
            hold_field_center_x = hold_field.left + hold_field.width / 2
            title_center_x = title.get_width() / 2
            x = hold_field_center_x - title_center_x
        rect = self.win.blit(
            title, (x, settings.PLAYFIELD_Y + settings.HOLD_FIELD_MARGIN_TOP))
        self._cache[consts.HOLD_FIELD_TITLE_RECT_CACHE] = rect

    def draw_tetromino_on_hold(self, tetromino: Tetromino) -> None:
        hold_field = self._cache[consts.HOLD_FIELD_CACHE]
        hold_field_center_x = hold_field.left + hold_field.width / 2
        base_y = hold_field.top + settings.BASE_HOLD_FIELD_PADDING
        asset = assets.TETROMINOES_ASSETS[tetromino.figure_type]
        asset_center = asset.get_width() / 2
        x = hold_field_center_x - asset_center
        y = base_y
        if tetromino.figure_type == consts.TETROMINO_I:
            y += settings.BASE_NEXT_FIELD_PADDING
        self.win.blit(asset, (x, y))
