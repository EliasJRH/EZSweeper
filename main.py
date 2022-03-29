import keyboard
import pyautogui as pag
from consts import *
from funcs.startup import *
from funcs.tile_identification import get_tile
from funcs.actions import click_adj_tiles, flag_adj_tiles
from funcs.utils import count_adj_tiles
from funcs.advanced_searching import advanced_search
import copy

# Plays the game
def play():
    print("BOT IS RUNNING")
    print("Press 'q' to quit")
    # pag.PAUSE = 1
    pag.PAUSE = 0

    NEW_T = copy.deepcopy(TILES)
    T = copy.deepcopy(TILES)
    change_made = True

    while T:
        ind = 0

        T = copy.deepcopy(NEW_T)

        if not change_made:
            advanced_search(T)

        NEW_T = []

        change_made = False

        while ind < len(T):
            cur_tile = T[ind]
            tx, ty = cur_tile[0], cur_tile[1]
            cur_x = START_X + (25 * tx)
            cur_y = START_Y + (25 * ty)

            tile = get_tile(cur_x, cur_y)

            if tile == "dirt" or tile == "flag":
                pass
            elif tile in NUMBERS:
                adj_tiles = count_adj_tiles(cur_x, cur_y)
                if adj_tiles[1] == tile:
                    if click_adj_tiles(cur_x, cur_y):
                        change_made = True
                elif adj_tiles[0] + adj_tiles[1] == tile:
                    if flag_adj_tiles(cur_x, cur_y):
                        change_made = True
                else:
                    NEW_T.append([tx, ty])
            else:
                NEW_T.append([tx, ty])

            ind += 1
            if keyboard.is_pressed("q"):
                quit()
        if keyboard.is_pressed("q"):
            quit()
        ind = 0


def main():
    open_minesweeper()
    select_difficulty()
    start_game()
    play()


if __name__ == "__main__":
    main()
