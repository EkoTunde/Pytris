import pygame
from game import Game
import settings

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.CAPTION)

start_time = 0


# def draw_window(game: Game, stack: list, elapsed_time) -> None:
#     WIN.fill(settings.BACKGROUND)
#     game.draw(WIN, elapsed_time)
#     pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    game = Game(WIN)
    # last_record = 0
    while run:
        elapsed_time = (pygame.time.get_ticks() - start_time)
        clock.tick(settings.FPS)
        # print("ticks", pygame.time.get_ticks())
        # print("time", clock.get_time())
        # print("fps", clock.get_fps())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game = Game(WIN)
                game.handle_user_input(event)
                # if event.key == pygame.K_UP or event.key == pygame.K_x:
                #     game.rotate_right()
                # if event.key == pygame.K_z:
                #     game.rotate_left()
                # if event.key == pygame.K_LEFT:
                #     game.move_left()
                # if event.key == pygame.K_RIGHT:
                #     game.move_right()
                # if event.key == pygame.K_DOWN:
                #     game.move_down()
        # if elapsed_time // 100 > (last_record // 100):
        #     print("elapsed_time", elapsed_time //
        #           100, "last_record", last_record // 100)
        #     keys_pressed = pygame.key.get_pressed()
        #     if keys_pressed[pygame.K_LEFT]:
        #         game.move_left()
        #     if keys_pressed[pygame.K_RIGHT]:
        #         game.move_right()
        #     if keys_pressed[pygame.K_DOWN]:
        #         game.move_down()

        # last_record = elapsed_time
        game.update(elapsed_time)

    pygame.quit()


if __name__ == '__main__':
    main()
