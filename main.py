import consts
import pygame
import settings
from tetrion import Tetrion


def main():
    WIN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption(settings.CAPTION)
    pygame.font.init()
    FONT = pygame.font.Font(pygame.font.get_default_font(), 16)
    clock = pygame.time.Clock()
    run = True
    tetrion = Tetrion(WIN, FONT)
    paused = False
    while run:
        clock.tick(settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                tetrion.pause()
                paused = not paused
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    tetrion.add_action(consts.HOLD)
                if event.key == pygame.K_SPACE:
                    tetrion.add_action(consts.DROP)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    tetrion.reset_left_DAS()
                if event.key == pygame.K_RIGHT:
                    tetrion.reset_right_DAS()
                if event.key == pygame.K_DOWN:
                    tetrion.reset_down_DAS()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    tetrion = Tetrion(WIN, FONT)
                if event.key == pygame.K_UP or event.key == pygame.K_x:
                    tetrion.add_action(consts.ROTATE_RIGHT)
                if event.key == pygame.K_z:
                    tetrion.add_action(consts.ROTATE_LEFT)
        if not paused:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LEFT]:
                tetrion.add_action(consts.MOVE_LEFT)
            if keys_pressed[pygame.K_RIGHT]:
                tetrion.add_action(consts.MOVE_RIGHT)
            if keys_pressed[pygame.K_DOWN]:
                tetrion.add_action(consts.MOVE_DOWN)
        tetrion.update(pygame.time.get_ticks())

    pygame.quit()


if __name__ == '__main__':
    main()
    # ! TODO:
    # - Add ghost.
    # - Add score.
    # - Add levels.
    # - Add increase gravity with levels.
