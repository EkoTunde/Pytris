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
    consts.TETROMINO_I: pygame.transform.scale(
        figure_image(consts.TETROMINO_I),
        SIZE
    ),
    consts.TETROMINO_Z: pygame.transform.scale(
        figure_image(consts.TETROMINO_Z),
        SIZE
    ),
    consts.TETROMINO_S: pygame.transform.scale(
        figure_image(consts.TETROMINO_S),
        SIZE
    ),
    consts.TETROMINO_T: pygame.transform.scale(
        figure_image(consts.TETROMINO_T),
        SIZE
    ),
    consts.TETROMINO_J: pygame.transform.scale(
        figure_image(consts.TETROMINO_J),
        SIZE
    ),
    consts.TETROMINO_L: pygame.transform.scale(
        figure_image(consts.TETROMINO_L),
        SIZE
    ),
    consts.TETROMINO_O: pygame.transform.scale(
        figure_image(consts.TETROMINO_O),
        SIZE
    ),
}
