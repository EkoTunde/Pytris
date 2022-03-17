WIDTH, HEIGHT = 800, 600
BOARD_HEIGHT = 500
BOARD_WIDTH = BOARD_HEIGHT / 2
BOARD_X = 300
BOARD_Y = (HEIGHT - BOARD_HEIGHT) / 2
CAPTION = "Pytris"
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOARD_BACKGROUND = (31, 33, 64)
BACKGROUND = (10, 11, 23)
FPS = 60
COLS = 10
ROWS = 20

BASE_SQUARE_SIZE = BOARD_HEIGHT / 20
FIGURES_SIZES = {
    1: (BASE_SQUARE_SIZE*4, BASE_SQUARE_SIZE),
    2: (BASE_SQUARE_SIZE*3, BASE_SQUARE_SIZE*2),
    3: (BASE_SQUARE_SIZE*3, BASE_SQUARE_SIZE*2),
    4: (BASE_SQUARE_SIZE*3, BASE_SQUARE_SIZE*2),
    5: (BASE_SQUARE_SIZE*3, BASE_SQUARE_SIZE*2),
    6: (BASE_SQUARE_SIZE*3, BASE_SQUARE_SIZE*2),
    7: (BASE_SQUARE_SIZE*2, BASE_SQUARE_SIZE*2),
}