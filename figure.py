import os
import pygame
import settings
import consts


class Figure:

    def __init__(
        self,
        figure_type: int,
        x: int,
        y: int
    ) -> None:
        # self.figure_type = figure_type
        self.figure_type = consts.FIGURE_1
        if (not isinstance(self.figure_type, int)
                and self.figure_type < 1
                or self.figure_type > 7):
            raise ValueError("Figure type must be an integer between 1 and 7")
        self._image = pygame.image.load(os.path.join(
            'assets', f'figure_{self.figure_type}.png'))
        self.figure = pygame.transform.scale(
            self._image, settings.FIGURES_SIZES[self.figure_type])
        self.x = x
        self.y = y
        self.rotation = 0
        self.moving = True
        self.col = 5

    def rotate(self):
        self.rotation += 1
        if self.rotation > 3:
            self.rotation = 0
        self.figure = pygame.transform.rotate(self.figure, 90)

    def draw(self, win):
        win.blit(self.figure, (self.x, self.y))
