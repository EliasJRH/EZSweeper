from consts import START_X_MP, START_Y_MP, MAX_X_MP, MAX_Y_MP, TO_SEARCH
from funcs.tile_identification import get_tile

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
    return (x_mp >= START_X_MP and x_mp <= MAX_X_MP) and (
        y_mp >= START_Y_MP and y_mp <= MAX_Y_MP
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
    for c in TO_SEARCH:
        if is_valid_mouse_pos(x_mp + c[0], y_mp + c[1]):
            tile = get_tile(x_mp + c[0], y_mp + c[1])
            if tile == "flag":
                data[1] += 1
            elif tile == "grass":
                data[0] += 1
    return data
