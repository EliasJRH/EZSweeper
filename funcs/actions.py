import sys
import pyautogui as pag
from funcs.utils import is_valid_mouse_pos
from funcs.tile_identification import get_tile
from consts.mouse_positions import START_X_MP_EASY, START_Y_MP_EASY, START_X_MP_MED, START_Y_MP_MED, START_X_MP_HARD, START_Y_MP_HARD
from consts.other import TILE_WIDTH_EASY, TILE_WIDTH_MED, TILE_WIDTH_HARD, ADJ_COORDS

TILE_WIDTH = TILE_WIDTH_HARD
START_X_MP = START_X_MP_HARD
START_Y_MP = START_Y_MP_HARD


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
def flag_and_ignore_adj_tiles(x_mp, y_mp, ignore):
    flagged = False
    bombs_flagged = 0
    for c in ADJ_COORDS:
        if is_valid_mouse_pos(x_mp + (c[0] * TILE_WIDTH), y_mp + (c[1] * TILE_WIDTH)):
            tile = get_tile(x_mp + (c[0] * TILE_WIDTH), y_mp + (c[1] * TILE_WIDTH))
            if tile == "grass":
                flagged = True
                ignore.add(
                    (
                        ((x_mp + (c[0] * TILE_WIDTH) - START_X_MP) // TILE_WIDTH),
                        ((y_mp + (c[1] * TILE_WIDTH) - START_Y_MP) // TILE_WIDTH),
                    )
                )
                print(f"ignoring {((x_mp + (c[0] * TILE_WIDTH) - START_X_MP) // TILE_WIDTH)}, {((y_mp + (c[1] * TILE_WIDTH) - START_Y_MP) // TILE_WIDTH)} because flag two from {((x_mp - START_X_MP) // TILE_WIDTH)}, {((y_mp - START_Y_MP) // TILE_WIDTH)}")
                pag.moveTo(x_mp + (c[0] * TILE_WIDTH), y_mp + (c[1] * TILE_WIDTH))
                pag.click(button="right")
                bombs_flagged += 1
    return flagged, bombs_flagged


# Clicks all adjacent tiles
# Returns true if a tile was clicked, false otherwise
def click_adj_tiles(x_mp, y_mp):
    clicked = False
    for c in ADJ_COORDS:
        if is_valid_mouse_pos(x_mp + (c[0] * TILE_WIDTH), y_mp + (c[1] * TILE_WIDTH)):
            tile = get_tile(x_mp + (c[0] * TILE_WIDTH), y_mp + (c[1] * TILE_WIDTH))
            if tile == "grass":
                clicked = True
                pag.moveTo(x_mp + (c[0] * TILE_WIDTH), y_mp + (c[1] * TILE_WIDTH))
                pag.click(button="left")
    return clicked


for x in range(1, len(sys.argv)):
    cur_arg = sys.argv[x].split("=")
    if cur_arg[0] == "-d":
        if cur_arg[1].lower() == "easy":
            TILE_WIDTH = TILE_WIDTH_EASY
            START_X_MP = START_X_MP_EASY
            START_Y_MP = START_Y_MP_EASY
        elif cur_arg[1].lower() == "medium":
            TILE_WIDTH = TILE_WIDTH_MED
            START_X_MP = START_X_MP_MED
            START_Y_MP = START_Y_MP_MED
        else:
            TILE_WIDTH = TILE_WIDTH_HARD
            START_X_MP = START_X_MP_HARD
            START_Y_MP = START_Y_MP_HARD
