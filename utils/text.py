from typing import Tuple
import pygame


def x_y_for_text_centered_aligned(
    text_surface: pygame.Surface,
    key_rect: pygame.Rect,
    offset_x: int = 0,
    offset_y: int = 0
) -> Tuple[int, int]:
    """
    Returns an x and y coordinate for the text to be centered
    aligned to indicated rect.
    """
    x = (key_rect.left + key_rect.width / 2) - (text_surface.get_width() / 2)
    y = (key_rect.top + key_rect.height / 2) - (text_surface.get_height() / 2)
    return (x+offset_x, y+offset_y)
