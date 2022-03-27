import consts
import settings
import pygame
from provider import Provider
from screen import Screen
from grid import Grid
from utils.coords import calc_initial_coords
from utils.movement import (
    get_move_down_coords,
    get_move_left_coords,
    get_move_right_coords
)
from utils.rotation import (
    get_rotate_right_coords,
    get_rotate_left_coords
)


class Tetrion:

    def __init__(self, window: pygame.Surface, font: pygame.font.Font) -> None:
        self.score = 0
        self.level = 1
        self.lines = 0
        self._is_paused = False
        self._screen = Screen(window, font)
        self._ticker = 0
        self._grid = Grid()
        self._lock_counter = 0
        self._first_available_row = settings.DEFAULT_AVAILABLE_ROW
        self._provider = Provider()
        initial_coords = calc_initial_coords(self._provider.peek(), self._grid)
        self._provider.load(initial_coords)
        self._actions = []
        self._on_hold = None
        self._can_hold = True
        self._is_droping = False

    def add_action(self, key: int):
        """
        Adds a consumable user input to the actions queue.

        Args:
            key (int): an event.key event from pygame.
        """
        self._actions.insert(0, key)

    def __apply_movements_from_user_input(
        self
    ) -> bool:
        actionables = {
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
        for i, action in reversed(list(enumerate(self._actions))):
            if actionables[action]["needs_args"]:
                new_coords = actionables[action]["callable"](
                    self._provider.peek(), self._grid)
                if new_coords is not None:
                    self._provider.peek().coords = new_coords
                    # current_rotation = self._provider.peek().rotation
                    if action == consts.ROTATE_RIGHT:
                        # self._provider.peek().rotation = current_rotation + 1
                        self._provider.peek().rotate_right()
                    if action == consts.ROTATE_LEFT:
                        # self._provider.peek().rotation = current_rotation - 1
                        self._provider.peek().rotate_left()
                    if action != consts.MOVE_DOWN:
                        self._lock_counter = 0
            else:
                new_coords = actionables[action]["callable"]()
            del self._actions[i]

    def __increase_ticker(self):
        self._ticker += 1

    def update(self, current_ticks: int) -> None:
        self.__increase_ticker()
        if consts.PAUSE in self._actions:
            self.pause_game()
        else:
            self.__apply_movements_from_user_input()

        if not self._is_paused and self._ticker > 0:
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
                elif self._ticker % (settings.GRAVITY*self.level) == 0:
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
            self._grid.update()
        self.__draw()

    def __draw(self):
        """
        Signal screen to draw game data.
        """
        self._screen.draw(
            grid=self._grid,
            provider=self._provider,
            is_paused=self._is_paused,
            on_hold=self._on_hold
        )

    def __lock_tetromino(self):
        tetromino = self._provider.dequeue()
        self._first_available_row = self._grid.add(
            coords=tetromino.coords,
            figure_type=tetromino.figure_type)
        self._can_hold = True

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

    def __drop(self):
        self._is_droping = True

    def pause_game(self) -> None:
        """
        Pause the game by inverting pause (bool).
        """
        self._is_paused = not self._is_paused
