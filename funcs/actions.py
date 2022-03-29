import pyautogui as pag
from funcs.utils import is_valid_coordinate
from funcs.tile_identification import get_tile
from consts import TO_SEARCH

# Flags a single tile of a given x and y coordinate
def flag_tile(x, y):
    if is_valid_coordinate(x, y):
        pag.moveTo(x, y)
        pag.click(button="right")


# Clicks a single tile of a given x and y coordinate
def click_tile(x, y):
    if is_valid_coordinate(x, y):
        pag.moveTo(x, y)
        pag.click(button="left")

# Flags all adjacent tiles
def flag_adj_tiles(x, y):
    clicked = False
    for c in TO_SEARCH:
        if is_valid_coordinate(x, y, c[0], c[1]):
            tile = get_tile(x + c[0], y + c[1])
            if tile == "grass":
                clicked = True
                pag.click(button="right")
    return clicked


# Clicks all adjacent tiles
def click_adj_tiles(x, y):
    clicked = False
    for c in TO_SEARCH:
        if is_valid_coordinate(x, y, c[0], c[1]):
            # pag.moveTo(x + c[0], y + c[1])
            tile = get_tile(x + c[0], y + c[1])
            if tile == "grass":
                clicked = True
                pag.click(button="left")
    return clicked