# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from sdl2 import SDL_Color


DEBUG = True

GAME_TITLE = b"Puzzle"

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
SCREEN_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
SCREEN_FPS = 60
SCREEN_TICKS_PER_FRAME = 1000 // SCREEN_FPS

CELL_SIZE = 23
BOARD_SIZE = 8
BOARD_POSITION = (SCREEN_CENTER[0] - BOARD_SIZE * CELL_SIZE // 2, SCREEN_CENTER[1] - BOARD_SIZE * CELL_SIZE // 2)
PIECES_COUNT = BOARD_SIZE * BOARD_SIZE // 4

WHITE_COLOR = SDL_Color(255, 255, 255, 0)
BLACK_COLOR = SDL_Color(0, 0, 0, 0)
RED_COLOR = SDL_Color(255, 0, 0, 0)
BLUE_COLOR = SDL_Color(0, 255, 0, 0)
GREEN_COLOR = SDL_Color(0, 0, 255, 0)
YELLOW_COLOR = SDL_Color(255, 255, 0, 0)

COLORS = (BLACK_COLOR, WHITE_COLOR, BLUE_COLOR, RED_COLOR, GREEN_COLOR, YELLOW_COLOR)

I1 = (
    (1, 0, 0, 0),
    (1, 0, 0, 0),
    (1, 0, 0, 0),
    (1, 0, 0, 0),
)

I2 = (
    (1, 1, 1, 1),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
)

O1 = (
    (1, 1, 0, 0),
    (1, 1, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
)

L1 = (
    (1, 0, 0, 0),
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (0, 0, 0, 0),
)

L2 = (
    (1, 1, 0, 0),
    (1, 0, 0, 0),
    (1, 0, 0, 0),
    (0, 0, 0, 0),
)

L3 = (
    (1, 1, 1, 0),
    (1, 0, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
)

L4 = (
    (1, 1, 0, 0),
    (0, 1, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 0, 0),
)

T1 = (
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (1, 0, 0, 0),
    (0, 0, 0, 0),
)

T2 = (
    (1, 1, 1, 0),
    (0, 1, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
)

Z1 = (
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 0, 0),
)

Z2 = (
    (1, 1, 0, 0),
    (0, 1, 1, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
)

SHAPES = (I1, I2, O1, L1, L2, L3, T1, T2, Z1, Z2)
SHAPES_TEMPLATES = (
    # (O1, O1, O1, O1),  # test template
    (L1, L3, O1, I2),
    (L1, Z1, L4, I2),
    (L2, L4, O1, I2),
    (I1, I1, O1, O1),
)


if __name__ == "__main__":
    print(SCREEN_CENTER)
    print(SCREEN_TICKS_PER_FRAME)
    print(BOARD_POSITION)
