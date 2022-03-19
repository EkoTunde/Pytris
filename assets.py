import os
import pygame
import consts
import settings


def figure_dir(figure_type):
    return os.path.join('assets', f'figure_{figure_type}_block.png')


def figure_image(figure_type):
    return pygame.image.load(figure_dir(figure_type))


SIZE = (settings.BASE_SQUARE_SIZE, settings.BASE_SQUARE_SIZE)

ASSETS = {
    consts.FIGURE_I: pygame.transform.scale(
        figure_image(consts.FIGURE_I),
        SIZE
    ),
    consts.FIGURE_Z: pygame.transform.scale(
        figure_image(consts.FIGURE_Z),
        SIZE
    ),
    consts.FIGURE_S: pygame.transform.scale(
        figure_image(consts.FIGURE_S),
        SIZE
    ),
    consts.FIGURE_T: pygame.transform.scale(
        figure_image(consts.FIGURE_T),
        SIZE
    ),
    consts.FIGURE_J: pygame.transform.scale(
        figure_image(consts.FIGURE_J),
        SIZE
    ),
    consts.FIGURE_L: pygame.transform.scale(
        figure_image(consts.FIGURE_L),
        SIZE
    ),
    consts.FIGURE_O: pygame.transform.scale(
        figure_image(consts.FIGURE_O),
        SIZE
    ),
}
