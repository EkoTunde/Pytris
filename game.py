import consts
import settings
import pygame
from randomizer import randint
from tetrominoes import (Tetromino, TetrominoI, TetrominoJ, TetrominoL,
                         TetrominoO, TetrominoS, TetrominoT, TetrominoZ)
from provider import Provider
from screen import Screen
from stack import Stack
from utils import will_collide_bellow


class Game:

    def __init__(self, window: pygame.Surface) -> None:
        self.start_time = 0
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
        self.current_figure = None
        self.current_figure_type = None
        self.current_figure_x = settings.BOARD_X
        self.current_figure_y = settings.BOARD_Y
        self.current_figure_rotation = None
        self.current_figure_image = None
        self.current_figure_figure = None
        self.game_velocity = settings.GAME_BASE_VELOCITY
        self.reset_figure()
        self.pause = False
        self.last_placed_figure_y = 0
        self.last_elapsed_time = 0
        self.should_move = True
        self._screen = Screen(window)
        self._ticker = 0
        figures = []
        used_nums = []
        for _ in range(4):
            rand = randint(1, 7, *figures)
            fig = self.get_figure_by_consts(rand)()
            used_nums.append(rand)
            figures.append(fig)
        # self._provider = Provider(*figures)
        self._provider = Provider()
        self._stack = Stack()
        self._lock_counter = 0

    def get_figure_by_consts(
        self, const: int
    ) -> Tetromino:
        """
        Return a figure subclass by the const.

        Args:
            const (int): represents the figure type.

        Raises:
            ValueError: if the const is not a valid figure type.

        Returns:
            Figure: the figure subclass.
        """
        if const == consts.TETROMINO_I:
            return TetrominoI
        elif const == consts.TETROMINO_J:
            return TetrominoJ
        elif const == consts.TETROMINO_L:
            return TetrominoL
        elif const == consts.TETROMINO_O:
            return TetrominoO
        elif const == consts.TETROMINO_S:
            return TetrominoS
        elif const == consts.TETROMINO_T:
            return TetrominoT
        elif const == consts.TETROMINO_Z:
            return TetrominoZ
        else:
            raise ValueError(
                "Invalid figure type= {const}".format(const=const))

    def apply_changes(self):
        if not self.pause:
            pass

    def update(self, elapsed_time):
        # print(self._provider)
        self._ticker += 1
        self._lock_counter += 1
        if will_collide_bellow(self._stack, self._provider.peek().coords):
            if self._lock_counter == settings.FPS / 2:
                self.lock_and_add_to_stack()
        else:
            if self._ticker % (settings.GRAVITY*self.level) == 0:
                self.__move_down()
        self._screen.draw(self._stack, self._provider)

    def lock_and_add_to_stack(self):
        self._lock_counter = 0
        tetromino = self._provider.dequeue()
        self._stack.add(coords=tetromino.coords,
                        figure_type=tetromino.figure_type)

    def add_figure(self, figure):
        self.pile.append(figure)

    def reset_figure(self):
        random_int = randint(1, 7)
        if random_int == consts.TETROMINO_I:
            self.current_figure_type = consts.TETROMINO_I
        else:
            self.current_figure = Tetromino(random_int)

    def draw_score(self, win):
        pass

    def draw_level(self, win):
        pass

    def draw_lines(self, win):
        pass

    def handle_user_input(self, event):
        if event.key == pygame.K_UP or event.key == pygame.K_x:
            self.__rotate_right()
        if event.key == pygame.K_z:
            self.__rotate_left()
        if event.key == pygame.K_LEFT:
            self.__move_left()
        if event.key == pygame.K_RIGHT:
            self.__move_right()
        if event.key == pygame.K_DOWN:
            self.__move_down()

    def __move_left(self):
        self._lock_counter = 0
        # if not will_collide_left(self._stack, self._provider.peek().coords):
        #     self._provider.peek().move_left()
        self._provider.peek().move_left(self._stack)

    def __move_right(self):
        self._lock_counter = 0
        # if not will_collide_right(self._stack, self._provider.peek().coords):
        #     self._provider.peek().move_right()
        self._provider.peek().move_right(self._stack)

    def __move_down(self):
        self._lock_counter = 0
        # if not will_collide_bellow(self._stack,
        #       self._provider.peek().coords):
        #     self._provider.peek().move_down()
        self._provider.peek().move_down(self._stack)

    def __rotate_right(self):
        self._lock_counter = 0
        self._provider.peek().attempt_rotate(
            clockwise=True, terrain=self._stack)
        # self.queue.peek().rotate_clockwise()

    def __rotate_left(self):
        self._lock_counter = 0
        self._provider.peek().attempt_rotate(
            clockwise=False, terrain=self._stack)
        # self.queue.peek().rotate_counterclockwise()

    def hold(self):
        pass

    def drop(self):
        pass

    def pause(self) -> None:
        """
        Pause the game by inverting pause (bool).
        """
        self.pause = not self.pause

    def reset(self):
        pass

    def update_level(self):
        self.level += 1
        self.game_velocity += 5
