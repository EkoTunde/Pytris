TETROMINO_I = 1
TETROMINO_Z = 2
TETROMINO_S = 3
TETROMINO_T = 4
TETROMINO_J = 5
TETROMINO_L = 6
TETROMINO_O = 7


DEGREES_0 = 0
DEGREES_90 = 1
DEGREES_180 = 2
DEGREES_270 = 3

ROTATION_DATA = {
    TETROMINO_I: {
        (0, 1): (
            # ^ >  v  <
            {'up': 1, 'right': 2, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 2, 'left': 1}
        ),
        (1, 0): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 1, 'left': 2},
            {'up': 0, 'right': 0, 'down': 0, 'left': 1},
            {'up': 1, 'right': 0, 'down': 0, 'left': 0},
            {'up': 2, 'right': 1, 'down': 0, 'left': 0}
        ),
        (1, 2): (
            # ^ >  v  <
            {'up': 0, 'right': 1, 'down': 2, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 1},
            {'up': 1, 'right': 0, 'down': 0, 'left': 2}
        ),
        (2, 1): (
            # ^ >  v  <
            {'up': 2, 'right': 0, 'down': 0, 'left': 1},
            {'up': 1, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 2, 'down': 1, 'left': 0}
        ),
        (2, 3): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 1, 'left': 2},
            {'up': 0, 'right': 0, 'down': 0, 'left': 1},
            {'up': 1, 'right': 0, 'down': 0, 'left': 0},
            {'up': 2, 'right': 1, 'down': 0, 'left': 0}
        ),
        (3, 2): (
            # ^ >  v  <
            {'up': 1, 'right': 2, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 2, 'left': 1}
        ),
        (3, 0): (
            # ^ >  v  <
            {'up': 2, 'right': 0, 'down': 0, 'left': 1},
            {'up': 1, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 2, 'down': 1, 'left': 0}
        ),
        (0, 3): (
            # ^ >  v  <
            {'up': 0, 'right': 1, 'down': 2, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 1},
            {'up': 1, 'right': 0, 'down': 0, 'left': 2}
        ),
    },
    TETROMINO_Z: {
        (0, 1): (
            # ^ >  v  <
            {'up': 0, 'right': 2, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1}
        ),
        (1, 0): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 0, 'left': 2},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0}
        ),
        (1, 2): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 2, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1}
        ),
        (2, 1): (
            # ^ >  v  <
            {'up': 2, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0}
        ),
        (2, 3): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 0, 'left': 2},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0}
        ),
        (3, 2): (
            # ^ >  v  <
            {'up': 0, 'right': 2, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1}
        ),
        (3, 0): (
            # ^ >  v  <
            {'up': 2, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0}
        ),
        (0, 3): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 2, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1}
        ),
    },
    TETROMINO_S: {
        (0, 1): (
            # ^ >  v  <
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 2, 'left': 0}
        ),
        (1, 0): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 2, 'right': 0, 'down': 0, 'left': 0}
        ),
        (1, 2): (
            # ^ >  v  <
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 2}
        ),
        (2, 1): (
            # ^ >  v  <
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 2, 'down': 0, 'left': 0}
        ),
        (2, 3): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 2, 'right': 0, 'down': 0, 'left': 0}
        ),
        (3, 2): (
            # ^ >  v  <
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 2, 'left': 0}
        ),
        (3, 0): (
            # ^ >  v  <
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 2, 'down': 0, 'left': 0}
        ),
        (0, 3): (
            # ^ >  v  <
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 2}
        ),
    },
    TETROMINO_T: {
        (0, 1): (
            # ^ >  v  <
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0}
        ),
        (1, 0): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1}
        ),
        (1, 2): (
            # ^ >  v  <
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1}
        ),
        (2, 1): (
            # ^ >  v  <
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0}
        ),
        (2, 3): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1}
        ),
        (3, 2): (
            # ^ >  v  <
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0}
        ),
        (3, 0): (
            # ^ >  v  <
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0}
        ),
        (0, 3): (
            # ^ >  v  <
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1}
        ),
    },
    TETROMINO_J: {
        (0, 1): (
            # ^ >  v  <
            {'up': 0, 'right': 2, 'down': 0, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1}
        ),
        (1, 0): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 0, 'left': 2},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0}
        ),
        (1, 2): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 2, 'left': 0},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1}
        ),
        (2, 1): (
            # ^ >  v  <
            {'up': 2, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0}
        ),
        (2, 3): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 0, 'left': 2},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0}
        ),
        (3, 2): (
            # ^ >  v  <
            {'up': 0, 'right': 2, 'down': 0, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1}
        ),
        (3, 0): (
            # ^ >  v  <
            {'up': 2, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0}
        ),
        (0, 3): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 2, 'left': 0},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1}
        ),
    },
    TETROMINO_L: {
        (0, 1): (
            # ^ >  v  <
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 0, 'down': 2, 'left': 0}
        ),
        (1, 0): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 2, 'right': 0, 'down': 0, 'left': 0}
        ),
        (1, 2): (
            # ^ >  v  <
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 2}
        ),
        (2, 1): (
            # ^ >  v  <
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 0, 'right': 2, 'down': 0, 'left': 0}
        ),
        (2, 3): (
            # ^ >  v  <
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 2, 'right': 0, 'down': 0, 'left': 0}
        ),
        (3, 2): (
            # ^ >  v  <
            {'up': 1, 'right': 1, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 0, 'down': 1, 'left': 1},
            {'up': 0, 'right': 0, 'down': 2, 'left': 0}
        ),
        (3, 0): (
            # ^ >  v  <
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 0, 'right': 2, 'down': 0, 'left': 0}
        ),
        (0, 3): (
            # ^ >  v  <
            {'up': 0, 'right': 1, 'down': 1, 'left': 0},
            {'up': 0, 'right': 0, 'down': 0, 'left': 0},
            {'up': 1, 'right': 0, 'down': 0, 'left': 1},
            {'up': 0, 'right': 0, 'down': 0, 'left': 2}
        ),
    },
}

J_L_S_T_Z_WALL_KICK_DATA = {
    #        ┌─1─┐    ┌─2─┐    ┌─3─┐     ┌─4─┐    ┌─5─┐
    (0, 1): [(0, 0), (-1, 0), (-1, 1),  (0, -2), (-1, -2)],
    (1, 0): [(0, 0), (1, 0),  (1, -1),  (0, 2),  (1, 2)],
    (1, 2): [(0, 0), (1, 0),  (1, -1),  (0, 2),  (1, 2)],
    (2, 1): [(0, 0), (-1, 0), (-1, 1),  (0, -2), (-1, -2)],
    (2, 3): [(0, 0), (1, 0),  (1, 1),   (0, -2), (1, -2)],
    (3, 2): [(0, 0), (-1, 0), (-1, -1), (0, 2),  (-1, 2)],
    (3, 0): [(0, 0), (-1, 0), (-1, -1), (0, 2),  (-1, 2)],
    (0, 3): [(0, 0), (1, 0),  (1, 1),   (0, -2), (1, -2)],
}

I_WALL_KICK_DATA = {
    #        ┌─1─┐    ┌─2─┐    ┌─3─┐     ┌─4─┐    ┌─5─┐
    (0, 1): [(0, 0), (-2, 0), (1, 0),  (-2, -1), (1, 2)],
    (1, 0): [(0, 0), (2, 0),  (-1, 0), (2, 1),   (-1, -2)],
    (1, 2): [(0, 0), (-1, 0), (2, 0),  (-1, 2),  (2, -1)],
    (2, 1): [(0, 0), (1, 0),  (-2, 0), (1, -2),  (-2, 1)],
    (2, 3): [(0, 0), (2, 0),  (-1, 0), (2, 1),   (-1, -2)],
    (3, 2): [(0, 0), (-2, 0), (1, 0),  (-2, -1), (1, 2)],
    (3, 0): [(0, 0), (1, 0),  (-2, 0), (1, -2),  (-2, 1)],
    (0, 3): [(0, 0), (-1, 0), (2, 0),  (-1, 2),  (2, -1)],
}
