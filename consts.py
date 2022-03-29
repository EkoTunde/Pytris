"""
Store an int representing a tretromino shape.
"""
TETROMINO_I = 1
TETROMINO_Z = 2
TETROMINO_S = 3
TETROMINO_T = 4
TETROMINO_J = 5
TETROMINO_L = 6
TETROMINO_O = 7
GHOST = 8
EMPTY_CELL = 0


"""
How to call a tetromino when querying by its type.
"""
TETROMINOES_NAMES = {
    1: "I",
    2: "Z",
    3: "S",
    4: "T",
    5: "J",
    6: "L",
    7: "O",
}

"""
This constants represents the different user actions.
"""
ROTATE_RIGHT = 0
ROTATE_LEFT = 1
MOVE_RIGHT = 2
MOVE_DOWN = 3
MOVE_LEFT = 4
HOLD = 5
DROP = 6
PAUSE = 7
CANCEL_RIGHT_DAS = 8
CANCEL_DOWN_DAS = 9
CANCEL_LEFT_DAS = 10


"""
Represent the posible rotation states.
"""
DEGREES_0 = 0
DEGREES_90 = 1
DEGREES_180 = 2
DEGREES_270 = 3

NEXT_FIELD_TITLE = "NEXT"
NEXT_FIELD_CACHE = "next_field_cache"
NEXT_FIELD_TITLE_CACHE = "next_field_title_cache"
NEXT_FIELD_TITLE_RECT_CACHE = "next_field_title_rect_cache"

HOLD_FIELD_TITLE = "HOLD"
HOLD_FIELD_CACHE = "hold_field_cache"
HOLD_FIELD_TITLE_CACHE = "hold_field_title_cache"
HOLD_FIELD_TITLE_RECT_CACHE = "hold_field_title_rect_cache"


SCORE_FIELD_TITLE = "SCORE"
SCORE_FIELD_CACHE = "score_field_cache"
SCORE_FIELD_TITLE_CACHE = "score_field_title_cache"
SCORE_FIELD_TITLE_RECT_CACHE = "score_field_title_rect_cache"

LEVEL_FIELD_TITLE = "LEVEL"
LEVEL_FIELD_CACHE = "level_field_cache"
LEVEL_FIELD_TITLE_CACHE = "level_field_title_cache"
LEVEL_FIELD_TITLE_RECT_CACHE = "level_field_title_rect_cache"

LINES_FIELD_TITLE = "LINES"
LINES_FIELD_CACHE = "lines_field_cache"
LINES_FIELD_TITLE_CACHE = "lines_field_title_cache"
LINES_FIELD_TITLE_RECT_CACHE = "lines_field_title_rect_cache"

WHITE = (255, 255, 255)

BLOCKS_WIDTH = {
    TETROMINO_I: 4,
    TETROMINO_J: 3,
    TETROMINO_L: 3,
    TETROMINO_O: 2,
    TETROMINO_S: 3,
    TETROMINO_T: 3,
    TETROMINO_Z: 3,
}

"""
This data consists of a dictionary which provides a way to
then calculate how to place a tetromino on the board at first.
The keys represent tetrominoes types, and the values are tuples
of the form (x, y) which represent how to transform the coordinates
of the tetromino's blocks.
"""
INITIAL_COORDS_DATA = {
    TETROMINO_I: (
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3)
    ),
    TETROMINO_J: (
        (1, 0),
        (0, 0),
        (0, 1),
        (0, 2)
    ),
    TETROMINO_L: (
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 2)
    ),
    TETROMINO_O: (
        (1, 0),
        (1, 1),
        (0, 1),
        (0, 0)
    ),
    TETROMINO_S: (
        (0, 0),
        (0, 1),
        (1, 1),
        (1, 2)
    ),
    TETROMINO_T: (
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ),
    TETROMINO_Z: (
        (1, 0),
        (1, 1),
        (0, 1),
        (0, 2)
    ),
}

"""
This data is used to calculate what row is
available for a tetromino to be placed on.
"""
FIRST_NEEDED_ROWS_DATA = {
    TETROMINO_I: (3, 4, 5, 6,),
    TETROMINO_J: (3, 4, 5,),
    TETROMINO_L: (3, 4, 5,),
    TETROMINO_O: (4, 5,),
    TETROMINO_S: (3, 4,),
    TETROMINO_T: (3, 4, 5,),
    TETROMINO_Z: (4, 5,),
}

"""
Provides the coordinates of the blocks composing
a Tetromino when a rotation from some degree to
another is performed.
The key defines the tetromino type. For each type,
the value is a dict, with the keys being every
posible rotation, for whom is assigned a tuple, made
up from the current rotation and the pretended rotation.
For each posible rotation flow, the value is a tuple
with dictionaries containing how to move a block (up,
right, down, left), in terms of integers.
"""
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


"""
This data indicates how to rotate a tetromino of type J, L,
S, T or Z. It provides test cases for the rotate function,
do it can attempt to rotate 5 times, using the next case if
the first one fails, and so on.
It consists of a dictionary with the following structure:
a tuple of two integers, as keys, representing the current
rotation state and the pretended one and, as values, a list
containg tuples which indicate how to transform the rotation,
being the first value how to move it in x axis, and the second
how to move it in y axis.
"""
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


"""
Does the same as J_L_S_T_Z_WALL_KICK_DATA, but for I tetrominos.
"""
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
