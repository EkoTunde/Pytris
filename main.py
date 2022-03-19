import pygame
from game import Game
import settings

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.CAPTION)

start_time = 0


def draw_window(game: Game, stack: list, elapsed_time) -> None:
    WIN.fill(settings.BACKGROUND)
    game.draw(WIN, elapsed_time)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    game = Game(WIN)
    while run:
        elapsed_time = pygame.time.get_ticks() - start_time
        clock.tick(settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game = Game(WIN)
                # if event.key == pygame.K_UP:
                #     game.rotate()
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()
        game.update(elapsed_time)
        # draw_window(game, stack, elapsed_time)

    pygame.quit()


if __name__ == '__main__':
    main()
