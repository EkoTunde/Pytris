import os
import pygame
from game import Game
import settings
from figure import Figure

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.CAPTION)

FIGURE_1_IMAGE = pygame.image.load(os.path.join('assets', 'figure_1.png'))
FIGURE_1 = pygame.transform.scale(FIGURE_1_IMAGE, settings.FIGURES_SIZES[1])
FIGURE_2_IMAGE = pygame.image.load(os.path.join('assets', 'figure_2.png'))
FIGURE_2 = pygame.transform.scale(FIGURE_2_IMAGE, settings.FIGURES_SIZES[2])
FIGURE_3_IMAGE = pygame.image.load(os.path.join('assets', 'figure_3.png'))
FIGURE_3 = pygame.transform.scale(FIGURE_3_IMAGE, settings.FIGURES_SIZES[3])
FIGURE_4_IMAGE = pygame.image.load(os.path.join('assets', 'figure_4.png'))
FIGURE_4 = pygame.transform.scale(FIGURE_4_IMAGE, settings.FIGURES_SIZES[4])
FIGURE_5_IMAGE = pygame.image.load(os.path.join('assets', 'figure_5.png'))
FIGURE_5 = pygame.transform.scale(FIGURE_5_IMAGE, settings.FIGURES_SIZES[5])
FIGURE_6_IMAGE = pygame.image.load(os.path.join('assets', 'figure_6.png'))
FIGURE_6 = pygame.transform.scale(FIGURE_6_IMAGE, settings.FIGURES_SIZES[6])
FIGURE_7_IMAGE = pygame.image.load(os.path.join('assets', 'figure_7.png'))
FIGURE_7 = pygame.transform.scale(FIGURE_7_IMAGE, settings.FIGURES_SIZES[7])


def draw_window(game: Game) -> None:
    WIN.fill(settings.BACKGROUND)
    game.draw(WIN)
    WIN.blit(FIGURE_1, (0, 0))
    WIN.blit(FIGURE_2, (30*2, 50*.2))
    WIN.blit(FIGURE_3, (30*3, 50*.3))
    WIN.blit(FIGURE_4, (30*4, 50*.4))
    WIN.blit(FIGURE_5, (30*5, 50*.5))
    WIN.blit(FIGURE_6, (30*6, 50*.6))
    WIN.blit(FIGURE_7, (30*7, 50*.7))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    game = Game()
    while run:
        clock.tick(settings.FPS)
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            game.move_left()
        if keys_pressed[pygame.K_RIGHT]:
            game.move_right()
        if keys_pressed[pygame.K_DOWN]:
            game.move_down()
        if keys_pressed[pygame.K_UP]:
            game.rotate()
        if keys_pressed[pygame.K_c]:
            game.hold()
        if keys_pressed[pygame.K_SPACE]:
            game.drop()
        if keys_pressed[pygame.K_ESCAPE]:
            run = False
        if keys_pressed[pygame.K_r]:
            game = Game()
        if keys_pressed[pygame.K_p]:
            game.pause()
        if keys_pressed[pygame.K_q]:
            run = False

        draw_window(game)

    pygame.quit()


if __name__ == '__main__':
    main()
