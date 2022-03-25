import pyautogui as pag
import time
import webbrowser
from consts import *
import copy

# Opens minesweeper in browser
def open_minesweeper():
    webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=minesweeper")
    time.sleep(2)

# Changes difficulty to hard, might change to add more difficulties later
def select_difficulty():
    pag.moveTo(500, 600)
    pag.click()
    pag.moveTo(725, 355)
    pag.click()
    pag.moveTo(725, 435)
    pag.click()

# Clicks on center tiles
def start_game():
    pag.moveTo(940, 555)
    pag.click()
    pag.moveTo(665, 365)

# Checks if coordinate is valid
# Coordinate is not valid if it falls outside the playing screen, see dimensions in consts.py
def is_valid_coordinate(x, y, xp, yp):
    return (x + xp >= START_X and x + xp <= MAX_X) and (
        y + yp >= START_Y and y + yp <= MAX_Y
    )


# Counts adjacent tiles and returns the number of unmarked tiles and the number of flagged tiles
def count_adj_tiles(x, y):
    # data = [unmarked tiles, flagged tiles]
    data = [0, 0]
    for c in TO_SEARCH:
        if is_valid_coordinate(x, y, c[0], c[1]):
            tile = get_tile(x + c[0], y + c[1])
            if tile == "flag":
                data[1] += 1
            elif tile == "grass":
                data[0] += 1
    return data


# Flags all adjacent tiles
def flag_adj_tiles(x, y):
    for c in TO_SEARCH:
        if is_valid_coordinate(x, y, c[0], c[1]):
            tile = get_tile(x + c[0], y + c[1])
            if tile == "grass":
                pag.click(button="right")


# Clicks all adjacent tiles
def click_adj_tiles(x, y):
    for c in TO_SEARCH:
        if is_valid_coordinate(x, y, c[0], c[1]):
            pag.moveTo(x + c[0], y + c[1])
            pag.click(button="left")


# Only to be used with filter
# Removes any color that doesn't have a frequency of more than 20 pixels
def reduce_sc_colors(color):
    if color[0] > 20:
        return True
    return False


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
        elif color[1] in DIRT:
            return "dirt"
    pass


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
    tile_colors = list(filter(reduce_sc_colors, tile_colors))
    return identify_tile_by_colors(tile_colors)


# Plays the game
def play():
    # pag.PAUSE = 1
    pag.PAUSE = 0

    T = copy.deepcopy(TILES)

    ind = 0

    while T:
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
            if adj_tiles[1] == tile:
                click_adj_tiles(cur_x, cur_y)
                T.pop(ind)
                ind -= 1
            elif adj_tiles[0] + adj_tiles[1] == tile:
                flag_adj_tiles(cur_x, cur_y)

        ind += 1
        if ind == len(T) - 1:
            ind = 0

def main():
    open_minesweeper()
    select_difficulty()
    start_game()
    play()


if __name__ == "__main__":
    main()
