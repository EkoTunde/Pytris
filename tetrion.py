import consts
import settings
import pygame
from provider import Provider
from screen import Screen
from grid import Grid
from utils.coords import calc_initial_coords, calculate_ghost_coords
from utils.movement import (
    get_move_down_coords, get_move_left_coords, get_move_right_coords)
from utils.rotation import get_rotate_right_coords, get_rotate_left_coords


class Tetrion:

    def __init__(
        self,
        window: pygame.Surface,
        font: pygame.font.Font,
        bold_font: pygame.font.Font
    ) -> None:
        self._score = settings.INITIAL_SCORE
        self._level = settings.INITIAL_LEVEL
        self._lines = settings.INITIAL_LINES
        self._is_paused = settings.INITIAL_PAUSE
        self._screen = Screen(window, font, bold_font)
        self._ticker = settings.INITIAL_TICKER
        self._grid = Grid()
        self._lock_counter = settings.INITIAL_LOCK_COUNTER
        self._first_available_row = settings.DEFAULT_AVAILABLE_ROW
        self._provider = Provider()
        initial_coords = calc_initial_coords(self._provider.peek(), self._grid)
        self._provider.load(initial_coords)
        self._actions = []
        self._DAS_actions = []
        self._on_hold = settings.INITIAL_ON_HOLD
        self._can_hold = settings.INITIAL_CAN_HOLD
        self._is_droping = settings.INITIAL_IS_DROPPING
        self._right_DAS_ticks = settings.DAS_MAX
        self._left_DAS_ticks = settings.DAS_MAX
        self._down_DAS_ticks = settings.DAS_MAX

    def add_action(self, key: int):
        """
        Adds a consumable user input to the actions queue.

        Args:
            key (int): an event.key event from pygame.
        """
        self._actions.insert(0, key)

    def reset_right_DAS(self):
        self._right_DAS_ticks = settings.DAS_MAX

    def reset_left_DAS(self):
        self._left_DAS_ticks = settings.DAS_MAX

    def reset_down_DAS(self):
        self._down_DAS_ticks = settings.DAS_MAX

    def pause(self):
        self._is_paused = not self._is_paused
        self._actions = []

    @property
    def ACTIONABLES(self):
        return {
            consts.HOLD: {
                "callable": self.__hold, "needs_args": False},
            consts.DROP: {
                "callable": self.__drop, "needs_args": False},
            consts.ROTATE_RIGHT: {
                "callable": get_rotate_right_coords, "needs_args": True},
            consts.ROTATE_LEFT: {
                "callable": get_rotate_left_coords, "needs_args": True},
            consts.MOVE_RIGHT: {
                "callable": get_move_right_coords, "needs_args": True},
            consts.MOVE_LEFT: {
                "callable": get_move_left_coords, "needs_args": True},
            consts.MOVE_DOWN: {
                "callable": get_move_down_coords, "needs_args": True},
        }

    def __apply_movements_from_user_input(self) -> bool:
        for action in self._actions:
            if self.ACTIONABLES[action]["needs_args"]:
                new_coords = self.ACTIONABLES[action]["callable"](
                    self._provider.peek(), self._grid)
                if new_coords is not None:

                    # IF MOVING RIGHT
                    if action == consts.MOVE_RIGHT:
                        self.reset_left_DAS()
                        if (self._right_DAS_ticks == settings.DAS_MAX or
                                self._right_DAS_ticks < 0):
                            if not self._is_droping:
                                self._provider.peek().coords = new_coords
                        self._right_DAS_ticks -= 1

                    # IF MOVING LEFT
                    elif action == consts.MOVE_LEFT:
                        self.reset_right_DAS()
                        if (self._left_DAS_ticks == settings.DAS_MAX or
                                self._left_DAS_ticks < 0):
                            if not self._is_droping:
                                self._provider.peek().coords = new_coords
                        self._left_DAS_ticks -= 1

                    # IF MOVING DOWN
                    elif action == consts.MOVE_DOWN:
                        if (self._down_DAS_ticks == settings.DAS_MAX or
                                self._down_DAS_ticks < 0):
                            if not self._is_droping:
                                self._provider.peek().coords = new_coords
                        self._down_DAS_ticks -= 1

                    elif (action == consts.ROTATE_RIGHT
                          or action == consts.ROTATE_LEFT):
                        if not self._is_droping:
                            self._provider.peek().coords = new_coords

                    # ANYTHING ELSE
                    else:
                        self._provider.peek().coords = new_coords

                    if action == consts.ROTATE_RIGHT and not self._is_droping:
                        self._provider.peek().rotate_right()
                    if action == consts.ROTATE_LEFT and not self._is_droping:
                        self._provider.peek().rotate_left()
                    if action != consts.MOVE_DOWN:
                        self._lock_counter = 0
                    if action == consts.HOLD or action == consts.DROP:
                        self.__clear_DAS()
            else:
                new_coords = self.ACTIONABLES[action]["callable"]()
                # self._provider.peek().coords = new_coords
        self._actions = []

    def __clear_DAS(self):
        self.reset_right_DAS()
        self.reset_left_DAS()
        self.reset_down_DAS()

    def __increase_ticker(self):
        self._ticker += 1

    def update(self, current_ticks: int) -> None:
        self.__increase_ticker()
        if not self._is_paused and self._ticker > 0:
            self.__apply_movements_from_user_input()

            coords = get_move_down_coords(
                self._provider.peek(), self._grid)
            if coords is not None:
                if self._is_droping:
                    self._provider.peek().coords = coords
                    coords = get_move_down_coords(
                        self._provider.peek(), self._grid)
                    if coords is not None:
                        self._provider.peek().coords = coords
                    self._lock_counter = 0
                elif self._ticker % (settings.GRAVITY*self._level) == 0:
                    self._provider.peek().coords = coords
            else:
                if self._is_droping:
                    self._is_droping = False
                    self.__lock_tetromino()
                    self._lock_counter = 0
                else:
                    self._lock_counter += 1
                    if self._lock_counter == 30:
                        self.__lock_tetromino()
                        self._lock_counter = 0
            self._lines += self._grid.update()
            self.__update_level()
        self.__draw()

    def __draw(self):
        """
        Signal screen to draw game data.
        """
        self._screen.draw(
            is_paused=self._is_paused,
            grid=self._grid,
            provider=self._provider,
            on_hold=self._on_hold,
            ghost_coords=calculate_ghost_coords(
                self._provider.peek(), self._grid),
            score=self._score,
            level=self._level,
            lines=self._lines,
        )

    def __lock_tetromino(self):
        tetromino = self._provider.dequeue()
        self._first_available_row = self._grid.add(
            coords=tetromino.coords,
            figure_type=tetromino.figure_type)
        self._provider.load(calc_initial_coords(
            self._provider.peek(), self._grid))
        self._can_hold = True
        self._is_droping = False

    def __hold(self) -> None:
        if self._can_hold:
            self._can_hold = False
            if self._on_hold is not None:
                self._on_hold = self._provider.replace_first(self._on_hold)
            else:
                self._on_hold = self._provider.dequeue()
            self._on_hold.coords = calc_initial_coords(
                self._on_hold, self._grid)
            initial_coords = calc_initial_coords(
                self._provider.peek(), self._grid)
            self._provider.load(initial_coords)

    def __drop(self) -> None:
        self._is_droping = True

    def pause_game(self) -> None:
        """
        Pause the game by inverting pause (bool).
        """
        self._is_paused = not self._is_paused

    def __update_level(self):
        self._level = self._lines // 10 + 1

    @property
    def level(self):
        return self._level

    def __update_score(self):
        self._score += self._lines * settings.SCORE_PER_LINE
        self._lines = 0
