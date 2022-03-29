from consts import TO_SEARCH, COLORS
from funcs.utils import *
from funcs.actions import click_tile


# fmt: off
"""Gets and returns of set of all grass tiles around a given tile

:param x: the position of the tile along the x axis
:type x: int
:param y: the position of the tile along the y axis
:type y: int

:returns: set containing tuples of x and y coordinates of grass tiles
:rtype: set((int, int),...)
"""
# fmt: on
def get_grass_tile_set(x, y):
    grass_set = set()
    for c in TO_SEARCH:
        if is_valid_coordinate(x, y, c[0], c[1]):
            tile = get_tile(x + c[0], y + c[1])
            if tile == "grass":
                grass_set.add((x + c[0], y + c[1]))
    return grass_set

def advanced_search(T):
    ind = 0
    while ind < len(T):
        cur_tile = T[ind]
        tx = cur_tile[0]
        ty = cur_tile[1]
        cur_x = START_X + (25 * tx)
        cur_y = START_Y + (25 * ty)

        tile = get_tile(cur_x, cur_y)

        if tile == "dirt":
            T.pop(ind)
            ind -= 1
        elif tile != "grass" and tile != "flag":
            adj_tiles = count_adj_tiles(cur_x, cur_y)
            remaining_bombs = tile - adj_tiles[1]
            cur_grass_set = get_grass_tile_set(cur_x, cur_y)
            for c in TO_SEARCH:
                if is_valid_coordinate(cur_x, cur_y, c[0], c[1]):
                    adj_tile = get_tile(cur_x + c[0], cur_y + c[1])
                    if adj_tile in COLORS.values():
                        adj_remaining_bombs = (
                            adj_tile - count_adj_tiles(cur_x + c[0], cur_y + c[1])[1]
                        )
                        adj_tile_grass_set = get_grass_tile_set(
                            cur_x + c[0], cur_y + c[1]
                        )
                        if len(cur_grass_set) >= len(adj_tile_grass_set):
                            larger = cur_grass_set
                            smaller = adj_tile_grass_set
                        else:
                            larger = adj_tile_grass_set
                            smaller = cur_grass_set

                        none_check = smaller - larger

                        if len(none_check) == 0:
                            dif = larger - smaller
                            # if the number of bombs between the two tiles is equal
                            # that means that the tiles contained in the larger adj grass set
                            # and not the smaller adj grass set are unnecesarry
                            if remaining_bombs == adj_remaining_bombs:
                                if len(dif) > 0:
                                    for coord in dif:
                                        click_tile(coord[0], coord[1])
                            # elif (
                            #     remaining_bombs - adj_remaining_bombs > 0
                            #     and len(smaller) > 0
                            # ):
                            #     if len(dif) > 0:
                            #         for coord in dif:
                            #             flag_tile(coord[0], coord[1])

        ind += 1