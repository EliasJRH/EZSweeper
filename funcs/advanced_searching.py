from consts import TO_SEARCH, COLORS
from funcs.utils import *
from funcs.actions import click_tile, flag_tile


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


def advanced_search(T, ignore):
    ind = 0
    while ind < len(T):
        coords = T[ind]
        x_c, y_c = coords[0], coords[1]

        if (x_c, y_c) not in ignore:
            x_mp = START_X_MP + (25 * x_c)
            y_mp = START_Y_MP + (25 * y_c)

            tile = get_tile(x_mp, y_mp)

            if tile == "dirt":
                T.pop(ind)
                ind -= 1
            elif tile != "grass" and tile != "flag":
                adj_tiles = count_adj_tiles(x_mp, y_mp)
                remaining_bombs = tile - adj_tiles[1]
                cur_grass_set = get_grass_tile_set(x_mp, y_mp)
                for c in TO_SEARCH:
                    if is_valid_coordinate(x_mp, y_mp, c[0], c[1]):
                        adj_tile = get_tile(x_mp + c[0], y_mp + c[1])
                        if adj_tile in COLORS.values():
                            adj_remaining_bombs = (
                                adj_tile - count_adj_tiles(x_mp + c[0], y_mp + c[1])[1]
                            )
                            adj_tile_grass_set = get_grass_tile_set(
                                x_mp + c[0], y_mp + c[1]
                            )

                            if len(cur_grass_set) >= len(adj_tile_grass_set):
                                larger_bomb_no = remaining_bombs
                                larger = cur_grass_set
                                smaller_bomb_no = adj_remaining_bombs
                                smaller = adj_tile_grass_set
                            else:
                                larger_bomb_no = adj_remaining_bombs
                                larger = adj_tile_grass_set
                                smaller_bomb_no = remaining_bombs
                                smaller = cur_grass_set

                            # in order for advanced searching techniques to hold true, the set difference of
                            # the smaller set - the larger set must be the empty set, this is to ensure that only
                            # 1 tile contains extra tiles
                            none_check = smaller - larger

                            if len(none_check) == 0:
                                dif = larger - smaller
                                # if the number of bombs between the two tiles is equal
                                # that means that the tiles contained in the larger adj grass set
                                # and not the smaller adj grass set are unnecesarry
                                if remaining_bombs == adj_remaining_bombs:
                                    if len(dif) > 0:
                                        for mp in dif:
                                            click_tile(mp[0], mp[1])
                                elif larger_bomb_no > len(dif):
                                    if len(dif) > 0:
                                        for mp in dif:
                                            flag_tile(mp[0], mp[1])

        ind += 1
