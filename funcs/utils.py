import sys
from consts.other import TILE_WIDTH_EASY, TILE_WIDTH_MED, TILE_WIDTH_HARD, ADJ_COORDS
from consts.mouse_positions import (
    START_X_MP_EASY,
    START_Y_MP_EASY,
    MAX_X_MP_EASY,
    MAX_Y_MP_EASY,
    START_X_MP_MED,
    START_Y_MP_MED,
    MAX_X_MP_MED,
    MAX_Y_MP_MED,
    START_X_MP_HARD,
    START_Y_MP_HARD,
    MAX_X_MP_HARD,
    MAX_Y_MP_HARD,
)
from funcs.tile_identification import get_tile

DIFFICULTY = 2
TILE_WIDTH = TILE_WIDTH_HARD

# fmt: off
"""Determines if mouse position is within the game border 

:param x_mp: the position of the tile along the x axis
:type x_mp: int
:param y_mp: the position of the tile along the y axis
:type y_mp: int

:returns: list of size two with indexes: [# of adjacent grass tiles, # of adjacent flagged tiles]
:rtype: list
"""
# fmt: on
def is_valid_mouse_pos(x_mp, y_mp):
    if DIFFICULTY == 0:
        return (x_mp >= START_X_MP_EASY and x_mp <= MAX_X_MP_EASY) and (
            y_mp >= START_Y_MP_EASY and y_mp <= MAX_Y_MP_EASY
        )
    elif DIFFICULTY == 1:
        return (x_mp >= START_X_MP_MED and x_mp <= MAX_X_MP_MED) and (
            y_mp >= START_Y_MP_MED and y_mp <= MAX_Y_MP_MED
        )
    else:
        return (x_mp >= START_X_MP_HARD and x_mp <= MAX_X_MP_HARD) and (
            y_mp >= START_Y_MP_HARD and y_mp <= MAX_Y_MP_HARD
        )


# fmt: off
"""Counts adjacent tiles and returns the number of unmarked tiles and the number of flagged tiles

:param x_mp: the position of the mouse along the x axis
:type x_mp: int
:param y_mp: the position of the mouse along the y axis
:type y_mp: int

:returns: list of size two with indexes: [# of adjacent grass tiles, # of adjacent flagged tiles]
:rtype: list
"""
# fmt: on
def count_adj_tiles(x_mp, y_mp):
    # data = [unmarked tiles, flagged tiles]
    data = [0, 0]
    for c in ADJ_COORDS:
        if is_valid_mouse_pos(x_mp + (c[0] * TILE_WIDTH), y_mp + (c[1] * TILE_WIDTH)):
            tile = get_tile(x_mp + (c[0] * TILE_WIDTH), y_mp + (c[1] * TILE_WIDTH))
            if tile == "flag":
                data[1] += 1
            elif tile == "grass":
                data[0] += 1
    return data


def generate_tile_list():
    if DIFFICULTY == 0:
        return [[x, y] for y in range(8) for x in range(10)]
    elif DIFFICULTY == 1:
        return [[x, y] for y in range(14) for x in range(18)]
    else:
        return [[x, y] for y in range(20) for x in range(24)]


for x in range(1, len(sys.argv)):
    cur_arg = sys.argv[x].split("=")
    if cur_arg[0] == "-d":
        if cur_arg[1].lower() == "easy":
            DIFFICULTY = 0
            TILE_WIDTH = TILE_WIDTH_EASY
        elif cur_arg[1].lower() == "medium":
            DIFFICULTY = 1
            TILE_WIDTH = TILE_WIDTH_MED
        else:
            DIFFICULTY = 2
            TILE_WIDTH = TILE_WIDTH_HARD
