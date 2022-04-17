from consts import START_X_MP, START_Y_MP, MAX_X_MP, MAX_Y_MP, TO_SEARCH
from funcs.tile_identification import get_tile

# Checks if coordinate is valid
# Coordinate is not valid if it falls outside the playing screen, see dimensions in consts.py


def is_valid_mouse_pos(x, y):
    return (x >= START_X_MP and x <= MAX_X_MP) and (y >= START_Y_MP and y <= MAX_Y_MP)


# Counts adjacent tiles and returns the number of unmarked tiles and the number of flagged tiles
def count_adj_tiles(x, y):
    # data = [unmarked tiles, flagged tiles]
    data = [0, 0]
    for c in TO_SEARCH:
        if is_valid_mouse_pos(x + c[0], y + c[1]):
            tile = get_tile(x + c[0], y + c[1])
            if tile == "flag":
                data[1] += 1
            elif tile == "grass":
                data[0] += 1
    return data


# def find_starting_coordinates(x, y):
#     while get_tile(x, y) != "grass":
#         y -= 25
#     y += 25
#     while get_tile(x, y) != "grass":
#         x -= 25
#     x += 25
#     return (x, y)


# def find_ending_coordinates(x, y):
#     while get_tile(x, y) != "grass":
#         y += 25
#     y -= 25
#     while get_tile(x, y) != "grass":
#         x += 25
#     x -= 25
#     return (x, y)
