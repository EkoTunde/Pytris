import random
import settings
import pygame
from figure import Figure
from figures_queue import FiguresQueue
from screen import Screen
from stack import Stack
from utils import (will_collide_bellow, will_collide_left, will_collide_right)


class Game:

    def __init__(self, window: pygame.Surface) -> None:
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
        self.figure_playing = Figure(1)
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
        self.screen = Screen(window)
        self.queue = FiguresQueue(
            *[Figure(random.randint(1, 7)) for _ in range(4)])
        self.stack = Stack()

    def apply_changes(self):
        if not self.pause:
            pass

    def update(self, elapsed_time):
        self.screen.draw(self.stack, self.queue)

    def draw(self, win, elapsed_time):
        # delay_fraction = settings.GAME_BASE_VELOCITY * settings.DELAY_UNIT
        # delay = settings.INITIAL_DELAY - delay_fraction
        # pygame.time.delay(delay)
        self.should_move = elapsed_time // 1000 > self.last_elapsed_time // 1000
        self.last_elapsed_time = elapsed_time
        self.apply_changes()
        self.draw_board(win)
        # if self.current_figure is not None:
        #     self.current_figure.draw(win, elapsed_time)
        # self.draw_current_figure(win, elapsed_time)
        # self.draw_score(win)
        # self.draw_level(win)
        # self.draw_lines(win)

    def add_figure(self, figure):
        self.pile.append(figure)

    def reset_figure(self):
        random_int = random.randint(1, 7)
        self.current_figure = Figure(random_int)

    def draw_current_figure(self, win, elapsed_time):
        print(elapsed_time)
        if elapsed_time // 1000 > self.last_placed_figure_y:
            self.current_figure_y += settings.BASE_SQUARE_SIZE
        self.last_placed_figure_y = elapsed_time // 1000
        # Draw the next figure
        coords = (self.current_figure_x, self.current_figure_y)
        self.current_figure.draw(win, coords)

    def draw_score(self, win):
        pass

    def draw_level(self, win):
        pass

    def draw_lines(self, win):
        pass

    def move_left(self):
        if not will_collide_left(self.stack, self.queue.peek().coords):
            self.queue.peek().move_left()
        # self.queue.peek().move_left()
        # mov = self.current_figure.x - settings.BASE_SQUARE_SIZE
        # if mov >= settings.BOARD_X:
        #     self.current_figure_x = mov

    def move_right(self):
        if not will_collide_right(self.stack, self.queue.peek().coords):
            self.queue.peek().move_right()
        # self.queue.peek().move_right()
        # mov = self.current_figure.x + settings.BASE_SQUARE_SIZE
        # end = mov+self.current_figure.width
        # max = settings.BOARD_X + settings.BOARD_WIDTH
        # if end <= max:
        #     self.current_figure_x = mov

    def move_down(self):
        if not will_collide_bellow(self.stack, self.queue.peek().coords):
            self.queue.peek().move_down()
        # Add to stack
        # self.queue.peek().move_down()

    def rotate(self):
        self.queue.peek().rotate()

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

    # def get_first_available_row(self):
    #     if self.stack.size < 19:
    #         return settings.DEFAULT_AVAILABLE_ROW
    #     if self.stack.size < 20:
    #         return settings.DEFAULT_AVAILABLE_ROW+1
    #     return settings.DEFAULT_AVAILABLE_ROW+2

    # def draw_board(self, win):
    #     # Draw a tetris board
    #     pygame.draw.rect(win, settings.BOARD_BACKGROUND, (settings.BOARD_X,
    #                      settings.BOARD_Y, settings.BOARD_WIDTH,
    #                      settings.BOARD_HEIGHT))
    #     for i in range(0, 10):
    #         for j in range(0, 20):
    #             pygame.draw.rect(win, settings.BACKGROUND, (
    #                 (settings.BOARD_X + i * settings.BASE_SQUARE_SIZE) + 1,
    #                 (settings.BOARD_Y + j * settings.BASE_SQUARE_SIZE) + 1,
    #                 settings.BASE_SQUARE_SIZE-2,
    #                 settings.BASE_SQUARE_SIZE-2),
    #                 border_radius=2)
