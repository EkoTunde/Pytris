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
        self.__score = settings.INITIAL_SCORE
        self.__level = settings.INITIAL_LEVEL
        self.__lines = settings.INITIAL_LINES
        self.__is_paused = settings.INITIAL_PAUSE
        self._screen = Screen(window, font, bold_font)
        self.__ticker = settings.INITIAL_TICKER
        self.__grid = Grid()
        self._lock_counter = settings.INITIAL_LOCK_COUNTER
        self._first_available_row = settings.DEFAULT_AVAILABLE_ROW
        self.__provider = Provider()
        initial_coords = calc_initial_coords(
            self.__provider.peek(), self.__grid)
        self.__provider.load(initial_coords)
        self.__actions = []
        self._DAS_actions = []
        self.__on_hold = settings.INITIAL_ON_HOLD
        self.__can_hold = settings.INITIAL_CAN_HOLD
        self.__is_droping = settings.INITIAL_IS_DROPPING
        self._right_DAS_ticks = settings.DAS_MAX
        self.__left_DAS_ticks = settings.DAS_MAX
        self.__down_DAS_ticks = settings.DAS_MAX

    def add_action(self, key: int):
        """
        Adds a consumable user input to the actions queue.

        Args:
            key (int): an event.key event from pygame.
        """
        self.__actions.insert(0, key)

    def reset_right_DAS(self):
        self._right_DAS_ticks = settings.DAS_MAX

    def reset_left_DAS(self):
        self.__left_DAS_ticks = settings.DAS_MAX

    def reset_down_DAS(self):
        self.__down_DAS_ticks = settings.DAS_MAX

    def pause(self):
        self.__is_paused = not self.__is_paused
        self.__actions = []

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
        for action in self.__actions:
            if self.ACTIONABLES[action]["needs_args"]:
                new_coords = self.ACTIONABLES[action]["callable"](
                    self.__provider.peek(), self.__grid)
                if new_coords is not None:

                    # IF MOVING RIGHT
                    if action == consts.MOVE_RIGHT:
                        self.reset_left_DAS()
                        if (self._right_DAS_ticks == settings.DAS_MAX or
                                self._right_DAS_ticks < 0):
                            if not self.__is_droping:
                                self.__provider.peek().coords = new_coords
                        self._right_DAS_ticks -= 1

                    # IF MOVING LEFT
                    elif action == consts.MOVE_LEFT:
                        self.reset_right_DAS()
                        if (self.__left_DAS_ticks == settings.DAS_MAX or
                                self.__left_DAS_ticks < 0):
                            if not self.__is_droping:
                                self.__provider.peek().coords = new_coords
                        self.__left_DAS_ticks -= 1

                    # IF MOVING DOWN
                    elif action == consts.MOVE_DOWN:
                        if (self.__down_DAS_ticks == settings.DAS_MAX or
                                self.__down_DAS_ticks < 0):
                            if not self.__is_droping:
                                self.__provider.peek().coords = new_coords
                        self.__down_DAS_ticks -= 1

                    elif (action == consts.ROTATE_RIGHT
                          or action == consts.ROTATE_LEFT):
                        if not self.__is_droping:
                            self.__provider.peek().coords = new_coords

                    # ANYTHING ELSE
                    else:
                        self.__provider.peek().coords = new_coords

                    if action == consts.ROTATE_RIGHT and not self.__is_droping:
                        self.__provider.peek().rotate_right()
                    if action == consts.ROTATE_LEFT and not self.__is_droping:
                        self.__provider.peek().rotate_left()
                    if action != consts.MOVE_DOWN:
                        self._lock_counter = 0
                    if action == consts.HOLD or action == consts.DROP:
                        self.__clear_DAS()
            else:
                new_coords = self.ACTIONABLES[action]["callable"]()
        self.__actions = []

    def __clear_DAS(self):
        self.reset_right_DAS()
        self.reset_left_DAS()
        self.reset_down_DAS()

    def __increase_ticker(self):
        self.__ticker += 1

    def update(self, current_ticks: int) -> None:
        self.__increase_ticker()
        if not self.__is_paused and self.__ticker > 0:
            self.__apply_movements_from_user_input()

            coords = get_move_down_coords(
                self.__provider.peek(), self.__grid)
            if coords is not None:
                if self.__is_droping:
                    self.__provider.peek().coords = coords
                    coords = get_move_down_coords(
                        self.__provider.peek(), self.__grid)
                    if coords is not None:
                        self.__provider.peek().coords = coords
                    self._lock_counter = 0
                elif self.__ticker % (settings.GRAVITY*self.__level) == 0:
                    self.__provider.peek().coords = coords
            else:
                if self.__is_droping:
                    self.__is_droping = False
                    self.__lock_tetromino()
                    self._lock_counter = 0
                else:
                    self._lock_counter += 1
                    if self._lock_counter == 30:
                        self.__lock_tetromino()
                        self._lock_counter = 0
            self.__lines += self.__grid.update()
            self.__level = self.__lines // 10 + 1
        self.__draw()

    def __draw(self):
        """
        Signal screen to draw game data.
        """
        self._screen.draw(
            is_paused=self.__is_paused,
            grid=self.__grid,
            provider=self.__provider,
            on_hold=self.__on_hold,
            ghost_coords=calculate_ghost_coords(
                self.__provider.peek(), self.__grid),
            score=self.__score,
            level=self.__level,
            lines=self.__lines,
        )

    def __lock_tetromino(self):
        tetromino = self.__provider.dequeue()
        self._first_available_row = self.__grid.add(
            coords=tetromino.coords,
            figure_type=tetromino.figure_type)
        self.__provider.load(calc_initial_coords(
            self.__provider.peek(), self.__grid))
        self.__can_hold = True
        self.__is_droping = False

    def __hold(self) -> None:
        if self.__can_hold:
            self.__can_hold = False
            if self.__on_hold is not None:
                self.__on_hold = self.__provider.replace_first(self.__on_hold)
            else:
                self.__on_hold = self.__provider.dequeue()
            self.__on_hold.coords = calc_initial_coords(
                self.__on_hold, self.__grid)
            initial_coords = calc_initial_coords(
                self.__provider.peek(), self.__grid)
            self.__provider.load(initial_coords)

    def __drop(self) -> None:
        self.__is_droping = True

    def pause_game(self) -> None:
        """
        Pause the game by inverting pause (bool).
        """
        self.__is_paused = not self.__is_paused

    @property
    def level(self):
        return self.__level

    def __update_score(self):
        self.__score += self.__lines * settings.SCORE_PER_LINE
        self.__lines = 0
