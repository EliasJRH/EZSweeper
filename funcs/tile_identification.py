import sys
from consts.colors import *
import pyautogui as pag

MOVE = True

# fmt: off
"""Screenshot and return screenshot of game board at given x and y coordinates

:param x_mp: the position of the mouse along the x axis
:type x_mp: int
:param y_mp: the position of the mouse along the y axis
:type y_mp: int

:returns: a pillow image object of the tile
:rtype: Pillow image object
"""
# fmt: on
def screenshot_tile(x_mp, y_mp):
    return pag.screenshot(region=(x_mp - 10.5, y_mp - 10.5, 20, 20))


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

    for color in colors:
        if color[1] in COLORS:
            return COLORS[color[1]]
    for color in colors:
        if color[1] in FLAG_COLORS:
            return "flag"

    for color in colors:
        if color[1] in GRASS and color[0] == 400:
            return "grass"
        # A dirt tile will only ever consist of a single color with a frequency of 400 pixels
        elif color[1] in DIRT and color[0] == 400:
            return "dirt"

    for color in colors:
        if color[1] in END_GRASS or color[1] in WATER:
            return "end"

    return "redo"


# Filters out minimal colors
def reduce_sc_colors(color):
    if color[0] > 20:
        return True
    return False


# fmt: off
"""Gets and returns the tile type

:param x_mp: the position of the mouse along the x axis
:type x_mp: int
:param y_mp: the position of the mouse along the y axis
:type y_mp: int

:returns: string representing tile type or int representing tile number
:rtype: string or int
"""
# fmt: on
def get_tile(x_mp, y_mp):
    if MOVE:
        pag.moveTo(x_mp, y_mp)
    error = True
    while error:
        error = False
        tile_screenshot = screenshot_tile(x_mp, y_mp)
        tile_colors = tile_screenshot.getcolors()
        tile_colors = list(filter(reduce_sc_colors, tile_colors))
        tile = identify_tile_by_colors(tile_colors)
        if tile == "redo":
            error = True
    return identify_tile_by_colors(tile_colors)


for x in range(1, len(sys.argv)):
    cur_arg = sys.argv[x].split("=")
    if cur_arg[0] == "-m" and cur_arg[1].lower() == "off":
        MOVE = False
