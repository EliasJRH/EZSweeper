import pyautogui as pag
import time
import webbrowser
from consts import *
import copy


def open_minesweeper():
    webbrowser.open(
        "https://www.google.com/search?client=firefox-b-d&q=minesweeper")
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

# Counts adjacent tiles and returns the number of unmarked tiles and the number of flagged tiles


def count_adj_tiles(x, y):
    # data = [unmarked tiles, flagged tiles]
    data = [0, 0]
    for c in TO_SEARCH:
        pag.move(c[0], c[1])
        cur_sc = pag.screenshot()
        cur_col = cur_sc.getpixel((x + c[0], y + c[1]))
        if cur_col == FLAG:
            data[1] += 1
        elif cur_col in GRASS:
            data[0] += 1
        pag.moveTo(x, y)
    return data

# Flags all adjacent tiles


def flag_adj_tiles(x, y):
    for c in TO_SEARCH:
        pag.move(c[0], c[1])
        cur_sc = pag.screenshot()
        cur_col = cur_sc.getpixel((x + c[0], y + c[1]))
        if (cur_col != FLAG):
            pag.click(button='right')
        pag.moveTo(x, y)

# TODO: change searching to account for the edges of the screen
# Have to create TO_SEARCH_L, TO_SEARCH_R, TO_SEARCH_U, TO_SEARCH_D
# All with associated tiles

# Clicks all adjacent tiles


def click_adj_tiles(x, y):
    for c in TO_SEARCH:
        pag.move(c[0], c[1])
        pag.click(button='left')
        pag.moveTo(x, y)

# Plays the game


def play():
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
        pag.moveTo(cur_x, cur_y)
        for z in range(15):
            cur_sc = pag.screenshot()
            cur_col = cur_sc.getpixel((cur_x, cur_y))
            if cur_col in IGNORE:
                if cur_col in DIRT:
                    T.pop(ind)
                    ind -= 1
                break
            if cur_col in COLORS:
                res = count_adj_tiles(cur_x, cur_y)
                if (res[0] + res[1] == COLORS[cur_col]):
                    flag_adj_tiles(cur_x, cur_y)
                    T.pop(ind)
                    ind -= 1
                elif (res[1] == COLORS[cur_col]):
                    click_adj_tiles(cur_x, cur_y)
                    T.pop(ind)
                    ind -= 1
                break
            pag.move(0.1, 0)
        ind += 1
        if (ind == len(TILES)):
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
    # pag.PAUSE = 1
    pag.PAUSE = 0
    open_minesweeper()
    select_difficulty()
    start_game()
    play()


if __name__ == "__main__":
    main()
