import pyautogui as pag
from funcs.utils import is_valid_mouse_pos
from funcs.tile_identification import get_tile
from consts import START_X_MP, START_Y_MP, TO_SEARCH

# Flags a single tile of a given x and y coordinate
def flag_tile(x_mp, y_mp, bombs):
    if is_valid_mouse_pos(x_mp, y_mp):
        pag.moveTo(x_mp, y_mp)
        tile = get_tile(x_mp, y_mp)
        if tile == "grass":
            pag.click(button="right")
            bombs -= 1


# Clicks a single tile of a given x and y coordinate
def click_tile(x_mp, y_mp):
    if is_valid_mouse_pos(x_mp, y_mp):
        pag.moveTo(x_mp, y_mp)
        tile = get_tile(x_mp, y_mp)
        if tile == "grass":
            pag.click(button="left")


# Flags and ignores all adjacent tiles
# Returns true if a tile was flagged, false otherwise
def flag_and_ignore_adj_tiles(x_mp, y_mp, ignore, bombs):
    flagged = False
    for c in TO_SEARCH:
        if is_valid_mouse_pos(x_mp + c[0], y_mp + c[1]):
            tile = get_tile(x_mp + c[0], y_mp + c[1])
            if tile == "grass":
                flagged = True
                ignore.add(
                    (
                        ((x_mp + c[0] - START_X_MP) // 25),
                        ((y_mp + c[1] - START_Y_MP) // 25),
                    )
                )
                pag.moveTo(x_mp + c[0], y_mp + c[1])
                pag.click(button="right")
                bombs -= 1
    return flagged


# Clicks all adjacent tiles
# Returns true if a tile was clicked, false otherwise
def click_adj_tiles(x_mp, y_mp):
    clicked = False
    for c in TO_SEARCH:
        if is_valid_mouse_pos(x_mp + c[0], y_mp + c[1]):
            tile = get_tile(x_mp + c[0], y_mp + c[1])
            if tile == "grass":
                clicked = True
                pag.moveTo(x_mp + c[0], y_mp + c[1])
                pag.click(button="left")
    return clicked
