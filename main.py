from lib2to3.pgen2.token import STAR
import pyautogui as pag
import time
import webbrowser
from consts import *
import copy

# search bar is 112px tall any y coordinate obtained from firefox extension must be offset by 112px

# Opens
def open_minesweeper():
    webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=minesweeper")
    time.sleep(2)


def select_difficulty():
    pag.moveTo(500, 600)
    pag.click()
    pag.moveTo(725, 355)
    pag.click()
    pag.moveTo(725, 435)
    pag.click()


def start_game():
    pag.moveTo(940, 555)
    pag.click()
    pag.moveTo(665, 365)

def is_valid_coordinate(x, y, xp, yp):
    return ((x + xp >= START_X or x + xp <= START_X) and (y + yp >= START_Y or y + yp <= START_Y))

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


# TODO: change searching to account for the edges of the screen
# Have to create TO_SEARCH_L, TO_SEARCH_R, TO_SEARCH_U, TO_SEARCH_D
# All with associated tiles

# Clicks all adjacent tiles
def click_adj_tiles(x, y):
    for c in TO_SEARCH:
        if is_valid_coordinate(x, y, c[0], c[1]):
            pag.moveTo(x + c[0], y + c[1])
            pag.click(button="left")


# Only to be used with a filter function
def reduce_sc_colors(color):
    if color[0] > 20:
        return True
    return False


"""Screenshot and return screenshot of game board at given x and y coordinates

:param x: the position of the tile along the x axis
:type x: int
:param y: the position of the tile along the y axis
:type y: int

:returns: a pillow image object of the tile
:rtype: Pillow image object
"""
def screenshot_tile(x, y):
    return pag.screenshot(region=(x - 10.5, y - 10.5, 20, 20))


"""Identifies a tile given it's colors

:param colors: An unsorted list containing tuples of RGB colors and their frequency
:type colors: list

:returns: string representing tile type or int representing tile number
:rtype: string or int
"""
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


"""Gets and returns the tile type

:param x: the position of the tile along the x axis
:type x: int
:param y: the position of the tile along the y axis
:type y: int

:returns: string representing tile type or int representing tile number
:rtype: string or int
"""
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

    # TODO:
    # Have to analyze each number box and find where the numbers intersect at the same position in the box
    # Use that position as a way of grabbing the color and identify the number of adjacent bombs by that color
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
            if adj_tiles[0] + adj_tiles[1] == tile:
                flag_adj_tiles(cur_x, cur_y)
                T.pop(ind)
                ind -= 1
            elif adj_tiles[1] == tile:
                click_adj_tiles(cur_x, cur_y)
                T.pop(ind)
                ind -= 1
        ind += 1
        if ind == len(T) - 1:
            ind = 0
    # while True:
    #     x = 665
    #     y = 365
    #     for yy in range(20):
    #         for xx in range(23):
    #             x += 25
    #             pag.moveTo(x, y)
    #             for z in range(15):
    #                 cur_sc = pag.screenshot()
    #                 cur_col = cur_sc.getpixel((x, y))
    #                 if cur_col in IGNORE:
    #                     break
    #                 if cur_col in COLORS:
    #                     res = count_adj_tiles(x, y)
    #                     if (res[0] + res[1] == COLORS[cur_col]):
    #                         flag_adj_tiles(x, y)
    #                     elif (res[1] == COLORS[cur_col]):
    #                         click_adj_tiles(x, y)
    #                     break
    #                 pag.move(0.1, 0)
    #         y += 25
    #         x = 665

    # while True:
    #     time.sleep(1)
    #     x,y = pag.position()
    #     cur = pag.screenshot()
    #     print(cur.getpixel((x,y)))


def main():
    open_minesweeper()
    select_difficulty()
    start_game()
    play()


if __name__ == "__main__":
    main()
