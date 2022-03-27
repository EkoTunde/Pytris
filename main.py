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
    while run:
        clock.tick(settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys_pressed = pygame.key.get_pressed()
            left_DAS = False
            right_DAS = False
            down_DAS = False
            if keys_pressed[pygame.K_LEFT]:
                left_DAS = True
                tetrion.left_long_pressed()
                tetrion.add_DAS_action(consts.MOVE_LEFT)
                tetrion.add_action(consts.MOVE_LEFT)
            if keys_pressed[pygame.K_RIGHT]:
                right_DAS = True
                tetrion.add_DAS_action(consts.MOVE_RIGHT)
                tetrion.add_action(consts.MOVE_RIGHT)
            if keys_pressed[pygame.K_DOWN]:
                down_DAS = True
                tetrion.add_DAS_action(consts.MOVE_DOWN)
                tetrion.add_action(consts.MOVE_DOWN)
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_r:
                    tetrion = Tetrion(WIN, FONT)
                if key == pygame.K_UP or key == pygame.K_x:
                    if not left_DAS and not right_DAS and not down_DAS:
                        tetrion.add_action(consts.ROTATE_RIGHT)
                if key == pygame.K_z:
                    if not left_DAS and not right_DAS and not down_DAS:
                        tetrion.add_action(consts.ROTATE_LEFT)
                if key == pygame.K_LEFT:
                    if not left_DAS:
                        tetrion.add_action(consts.MOVE_LEFT)
                if key == pygame.K_RIGHT:
                    if not right_DAS:
                        tetrion.add_action(consts.MOVE_RIGHT)
                if key == pygame.K_DOWN:
                    if not down_DAS:
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
