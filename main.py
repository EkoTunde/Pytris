import consts
import pygame
import settings
from tetrion import Tetrion


def handle_user_input(key, tetrion: Tetrion):
    if key == pygame.K_UP or key == pygame.K_x:
        tetrion.add_action(consts.ROTATE_RIGHT)
    if key == pygame.K_z:
        tetrion.add_action(consts.ROTATE_LEFT)
    if key == pygame.K_LEFT:
        tetrion.add_action(consts.MOVE_LEFT)
    if key == pygame.K_RIGHT:
        tetrion.add_action(consts.MOVE_RIGHT)
    if key == pygame.K_DOWN:
        tetrion.add_action(consts.MOVE_DOWN)
    if key == pygame.K_c:
        tetrion.add_action(consts.HOLD)
    if key == pygame.K_SPACE:
        tetrion.add_action(consts.DROP)
    if key == pygame.K_p:
        tetrion.add_action(consts.PAUSE)


def main():
    WIN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption(settings.CAPTION)
    clock = pygame.time.Clock()
    run = True
    tetrion = Tetrion(WIN)
    while run:
        clock.tick(settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_r:
                    tetrion = Tetrion(WIN)
                if key == pygame.K_UP or key == pygame.K_x:
                    tetrion.add_action(consts.ROTATE_RIGHT)
                if key == pygame.K_z:
                    tetrion.add_action(consts.ROTATE_LEFT)
                if key == pygame.K_LEFT:
                    tetrion.add_action(consts.MOVE_LEFT)
                if key == pygame.K_RIGHT:
                    tetrion.add_action(consts.MOVE_RIGHT)
                if key == pygame.K_DOWN:
                    tetrion.add_action(consts.MOVE_DOWN)
                if key == pygame.K_c:
                    tetrion.add_action(consts.HOLD)
                if key == pygame.K_SPACE:
                    tetrion.add_action(consts.DROP)
                if key == pygame.K_p:
                    tetrion.add_action(consts.PAUSE)
        tetrion.update(pygame.time.get_ticks())

    pygame.quit()


if __name__ == '__main__':
    main()
