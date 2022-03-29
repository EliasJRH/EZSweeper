from consts import COLORS, FLAG_COLORS, DIRT, GRASS
import pyautogui as pag

# # Only to be used with filter
# # Removes any color that doesn't have a frequency of more than 20 pixels
# def reduce_sc_colors(color):
#     if color[0] > 20:
#         return True
#     return False


# fmt: off
"""Screenshot and return screenshot of game board at given x and y coordinates

:param x: the position of the tile along the x axis
:type x: int
:param y: the position of the tile along the y axis
:type y: int

:returns: a pillow image object of the tile
:rtype: Pillow image object
"""
# fmt: on
def screenshot_tile(x, y):
    return pag.screenshot(region=(x - 10.5, y - 10.5, 20, 20))


# fmt: off
"""Identifies a tile given it's colors

:param colors: An unsorted list containing tuples of RGB colors and their frequency
:type colors: list

:returns: string representing tile type or int representing tile number
:rtype: string or int
"""
# fmt: on
def identify_tile_by_colors(colors):
    # this is a very crude way of checking for colors
    # basically, I'm running through the whole list and checking if a color exists in order of priority
    # given, the list would be at most 3 elements long so relatively it's quite a small operation

    for color in colors:
        if color[1] in COLORS:
            return COLORS[color[1]]
    for color in colors:
        if color[1] in FLAG_COLORS:
            return "flag"

    for color in colors:
        if color[1] in GRASS:
            return "grass"
        # A dirt tile will only ever consist of a single color with a frequency of 400 pixels
        elif color[1] in DIRT and color[0] == 400:
            return "dirt"

    return "redo"


# fmt: off
"""Gets and returns the tile type

:param x: the position of the tile along the x axis
:type x: int
:param y: the position of the tile along the y axis
:type y: int

:returns: string representing tile type or int representing tile number
:rtype: string or int
"""
# fmt: on
def get_tile(x, y):
    pag.moveTo(x, y)
    tile_screenshot = screenshot_tile(x, y)
    tile_colors = tile_screenshot.getcolors()
    return identify_tile_by_colors(tile_colors)
