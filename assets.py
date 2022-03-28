import os
import pygame
import consts
import settings


def tetromino_block_dir(figure_type) -> str:
    return os.path.join('assets', f'figure_{figure_type}_block.png')


def tetromino_block_image(figure_type) -> pygame.Surface:
    return pygame.image.load(tetromino_block_dir(figure_type))


def tetromino_dir(figure_type) -> str:
    return os.path.join('assets', f'figure_{figure_type}.png')


def tetromino_image(figure_type) -> pygame.Surface:
    return pygame.image.load(tetromino_dir(figure_type))


SIZE = (settings.BASE_SQUARE_SIZE, settings.BASE_SQUARE_SIZE)

ASSETS = {
    consts.TETROMINO_I: pygame.transform.scale(
        tetromino_block_image(consts.TETROMINO_I),
        SIZE
    ),
    consts.TETROMINO_Z: pygame.transform.scale(
        tetromino_block_image(consts.TETROMINO_Z),
        SIZE
    ),
    consts.TETROMINO_S: pygame.transform.scale(
        tetromino_block_image(consts.TETROMINO_S),
        SIZE
    ),
    consts.TETROMINO_T: pygame.transform.scale(
        tetromino_block_image(consts.TETROMINO_T),
        SIZE
    ),
    consts.TETROMINO_J: pygame.transform.scale(
        tetromino_block_image(consts.TETROMINO_J),
        SIZE
    ),
    consts.TETROMINO_L: pygame.transform.scale(
        tetromino_block_image(consts.TETROMINO_L),
        SIZE
    ),
    consts.TETROMINO_O: pygame.transform.scale(
        tetromino_block_image(consts.TETROMINO_O),
        SIZE
    ),
    consts.GHOST: pygame.transform.scale(
        pygame.image.load(os.path.join('assets', 'ghost_block.png')),
        SIZE
    ),
}

TETROMINOES_ASSETS = {
    consts.TETROMINO_I: pygame.transform.scale(
        tetromino_image(consts.TETROMINO_I),
        settings.FIGURES_SIZES[consts.TETROMINO_I]
    ),
    consts.TETROMINO_Z: pygame.transform.scale(
        tetromino_image(consts.TETROMINO_Z),
        settings.FIGURES_SIZES[consts.TETROMINO_Z]
    ),
    consts.TETROMINO_S: pygame.transform.scale(
        tetromino_image(consts.TETROMINO_S),
        settings.FIGURES_SIZES[consts.TETROMINO_S]
    ),
    consts.TETROMINO_T: pygame.transform.scale(
        tetromino_image(consts.TETROMINO_T),
        settings.FIGURES_SIZES[consts.TETROMINO_T]
    ),
    consts.TETROMINO_J: pygame.transform.scale(
        tetromino_image(consts.TETROMINO_J),
        settings.FIGURES_SIZES[consts.TETROMINO_J]
    ),
    consts.TETROMINO_L: pygame.transform.scale(
        tetromino_image(consts.TETROMINO_L),
        settings.FIGURES_SIZES[consts.TETROMINO_L]
    ),
    consts.TETROMINO_O: pygame.transform.scale(
        tetromino_image(consts.TETROMINO_O),
        settings.FIGURES_SIZES[consts.TETROMINO_O]
    ),
}
