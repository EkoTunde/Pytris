from typing import List, Tuple
import pygame
from assets import ASSETS
import assets
from cache.cache import Cache
from cache.field import Field
from cache.title import Title
import consts
from tetrominoes import Tetromino
from provider import Provider
import settings
from grid import Grid
from utils.text import x_y_for_text_centered_aligned

X = "x"
Y = "y"
WIDTH = "width"
HEIGHT = "height"
RECT = "rect"
HIDDEN_RECT = "hidden rect"
TITLE = "title"
FONT = "font"
LINES_FIELD = "lines_field"
LEVEL_FIELD = "level_field"
SCORE_FIELD = "score_field"


class Screen:

    def __init__(
        self,
        window: pygame.Surface,
        font: pygame.font.Font,
        bold_font: pygame.font.Font
    ) -> None:
        self.win = window
        self._font = font
        self._bold = bold_font
        # self._cache2 = Cache(self._font, self._bold)
        self._cache = {
            # 'lines cache': Field(
            #     x=settings.DEFAULT_INFO_FIELD_X,
            #     y=settings.LINES_FIELD_Y,
            #     width=settings.DEFAULT_INFO_FIELD_WIDTH,
            #     height=settings.DEFAULT_INFO_FIELD_HEIGHT,
            #     title=Title(font=self._font, title=consts.LINES_FIELD_TITLE)
            # ),
            'score_title': self._font.render(
                'Score', False, (255, 255, 255)),
            # 'level_title': self._font.render(
            #     'Level', False, (255, 255, 255)),
            'lines_title': self._font.render(
                'Lines', False, (255, 255, 255)),
            consts.NEXT_FIELD_TITLE_CACHE: self._bold.render(
                consts.NEXT_FIELD_TITLE, False, consts.WHITE),
            consts.HOLD_FIELD_TITLE_CACHE: self._font.render(
                consts.HOLD_FIELD_TITLE, False, consts.WHITE),
            consts.SCORE_FIELD_TITLE_CACHE: self._font.render(
                consts.SCORE_FIELD_TITLE, False, consts.WHITE),
            consts.LEVEL_FIELD_TITLE_CACHE: self._font.render(
                consts.LEVEL_FIELD_TITLE, False, consts.WHITE),
            consts.LINES_FIELD_TITLE_CACHE: self._font.render(
                consts.LINES_FIELD_TITLE, False, consts.WHITE),
            consts.LINES_FIELD: {
                RECT: None,
                HIDDEN_RECT: None,
                TITLE: {
                    RECT: None,
                    FONT: self._font.render(
                        consts.LINES_FIELD_TITLE, False, consts.WHITE)
                },
            },
            consts.LEVEL_FIELD: {
                X: settings.DEFAULT_INFO_FIELD_X,
                Y: None,
                WIDTH: settings.DEFAULT_INFO_FIELD_WIDTH,
                HEIGHT: settings.DEFAULT_INFO_FIELD_HEIGHT,
                RECT: None,
                HIDDEN_RECT: None,
                TITLE: {
                    RECT: None,
                    FONT: self._font.render(
                        consts.LINES_FIELD_TITLE, False, consts.WHITE)
                }
            }
        }

    def draw(
        self,
        is_paused: bool = False,
        grid: Grid = None,
        provider: Provider = None,
        on_hold: Tetromino = None,
        ghost_coords: List[Tuple[int, int]] = None,
        score: int = settings.INITIAL_SCORE,
        level: int = settings.INITIAL_LEVEL,
        lines: int = settings.INITIAL_LINES,
    ) -> None:
        if is_paused is False:
            self.win.fill(settings.BACKGROUND)
            self.__draw_playfield()
            self.__draw_next_field()
            self.__draw_next_field_title()
            self.__draw_hold_field()
            self.__draw_hold_field_title()
            if grid:
                self.__draw_grid(grid)
            if provider:
                self.__draw_falling_tetromino(provider.peek())
                self.__draw_next_tetrominoes(provider)
            if on_hold:
                self.__draw_tetromino_on_hold(on_hold)
            if ghost_coords:
                self.__draw_ghost_tetromino(ghost_coords)
            self.__draw_lines_field()
            self.__draw_line_hidden_field()
            self.__draw_lines_title()
            self.__draw_current_lines(lines)
            # self.__draw_level_field()
            # self.__draw_level_title()
            # self.__draw_current_level(level)
            # self.__draw_score_field()
            # self.__draw_score_title()
            # self.__draw_current_score(score)
        pygame.display.update()

    def __draw_playfield(self):
        # Draw a tetris board
        pygame.draw.rect(self.win, settings.FIELDS_BACKGROUND,
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

    def __draw_grid(self, grid: Grid):
        for i in range(0, grid.size):
            for j in range(0, settings.COLS):
                if grid.items[i][j] != 0:
                    x = settings.PLAYFIELD_X + j * settings.BASE_SQUARE_SIZE
                    y = settings.PLAYFIELD_Y + (settings.ROWS - i-1) * \
                        settings.BASE_SQUARE_SIZE
                    self.win.blit(ASSETS[grid.items[i][j]], (x, y))

    def __draw_falling_tetromino(self, tetromino: Tetromino) -> None:
        for row, col in tetromino.coords:
            x = settings.PLAYFIELD_X + col*settings.BASE_SQUARE_SIZE
            y = settings.PLAYFIELD_Y + (settings.ROWS - 1 - row) * \
                settings.BASE_SQUARE_SIZE
            self.win.blit(tetromino.asset, (x, y))

    def __draw_ghost_tetromino(
        self,
        ghost_coords: List[Tuple[int, int]]
    ) -> None:
        for row, col in ghost_coords:
            x = settings.PLAYFIELD_X + col*settings.BASE_SQUARE_SIZE
            y = settings.PLAYFIELD_Y + (settings.ROWS - 1 - row) * \
                settings.BASE_SQUARE_SIZE
            self.win.blit(assets.ASSETS[consts.GHOST], (x, y))

    def __draw_next_field(self):
        self._cache[consts.NEXT_FIELD_CACHE] = pygame.draw.rect(
            self.win, settings.FIELDS_BACKGROUND, (
                settings.NEXT_FIELD_X, settings.NEXT_FIELD_Y,
                settings.NEXT_FIELD_WIDTH, settings.NEXT_FIELD_HEIGHT))

    def __draw_next_field_title(self):
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

    def __draw_next_tetrominoes(self, provider: Provider) -> None:
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

    def __draw_hold_field(self) -> None:
        self._cache[consts.HOLD_FIELD_CACHE] = pygame.draw.rect(
            self.win, settings.FIELDS_BACKGROUND, (
                settings.HOLD_FIELD_X, settings.HOLD_FIELD_Y,
                settings.HOLD_FIELD_WIDTH, settings.HOLD_FIELD_HEIGHT))

    def __draw_hold_field_title(self):
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

    def __draw_tetromino_on_hold(self, tetromino: Tetromino) -> None:
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

    def __draw_lines_field(self) -> None:
        self._cache[LINES_FIELD][RECT] = pygame.draw.rect(
            self.win,
            settings.FIELDS_BACKGROUND,
            settings.LINES_FIELD_RECT_VALUE)

    def __draw_line_hidden_field(self) -> None:
        self._cache[LINES_FIELD][HIDDEN_RECT] = pygame.draw.rect(
            self.win,
            (255, 0, 0),
            # settings.BACKGROUND,
            settings.LINES_FIELD_HIDDEN_RECT_VALUE)

    def __draw_lines_title(self) -> None:
        title = self._cache[LINES_FIELD][TITLE][FONT]
        if self._cache[LINES_FIELD][TITLE][RECT] is None:
            x, y = x_y_for_text_centered_aligned(
                title, self._cache[LINES_FIELD][HIDDEN_RECT])
        else:
            x = self._cache[LINES_FIELD][TITLE][RECT].left
            y = self._cache[LINES_FIELD][TITLE][RECT].top
        self._cache[LINES_FIELD][TITLE][RECT] = self.win.blit(title, (x, y))

    def __get_lines_title_x(self, title: pygame.font.Font) -> int:
        lines_field = self._cache[LEVEL_FIELD][RECT]
        lines_field_center_x = lines_field.left + lines_field.width / 2
        title_center_x = title.get_width() / 2
        return lines_field_center_x - title_center_x

    def __get_lines_title_y(self, title: pygame.font.Font) -> int:
        lines_field_top = self._cache[LEVEL_FIELD][RECT].top
        title_center_y = title.get_height() / 2
        return lines_field_top - title_center_y*2

    def __draw_level_field(self) -> None:
        self._cache[consts.LEVEL_FIELD_CACHE] = pygame.draw.rect(
            self.win, settings.FIELDS_BACKGROUND, (
                settings.DEFAULT_INFO_FIELD_X,
                self._cache[LINES_FIELD][TITLE][RECT].top -
                settings.DEFAULT_INFO_FIELD_HEIGHT-settings.BASE_SQUARE_SIZE/2,
                # settings.PLAYFIELD_Y +
                # settings.PLAYFIELD_HEIGHT -
                # (settings.BASE_SQUARE_SIZE*6),
                settings.DEFAULT_INFO_FIELD_WIDTH,
                settings.DEFAULT_INFO_FIELD_HEIGHT))

    def __draw_level_title(self) -> None:
        pass
        # title = self._cache[consts.LEVEL_FIELD_TITLE_CACHE]
        # if consts.LEVEL_FIELD_TITLE_RECT_CACHE in self._cache:
        #     x = self._cache[consts.LEVEL_FIELD_TITLE_RECT_CACHE].left
        # else:
        #     level_field = self._cache[consts.LEVEL_FIELD_CACHE]
        #     level_field_center_x = level_field.left + level_field.width / 2
        #     title_center_x = title.get_width() / 2
        #     x = level_field_center_x - title_center_x
        # rect = self.win.blit(
        #     title, (x, settings.PLAYFIELD_Y +
        #             settings.PLAYFIELD_HEIGHT-settings.BASE_SQUARE_SIZE*6))
        # self._cache[consts.LEVEL_FIELD_TITLE_RECT_CACHE] = rect

    def __draw_current_level(self, level) -> None:
        pass

    def __draw_current_score(self, score) -> None:
        pass

    def __draw_score_field(self) -> None:
        pass

    def __draw_score_title(self) -> None:
        pass

    def __draw_current_lines(self, lines) -> None:
        pass
