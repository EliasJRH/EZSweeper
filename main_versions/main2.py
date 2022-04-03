import keyboard
import pyautogui as pag
from consts import *
from funcs.startup import *
from funcs.tile_identification import get_tile
from funcs.actions import click_adj_tiles, flag_adj_tiles
from funcs.utils import *
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

    ignore = set({})
    cur_new_t = set({})

    while T:
        ind = 0

        T = copy.deepcopy(NEW_T)

        if not change_made:
            advanced_search(T)

        NEW_T = []
        cur_new_t.clear()

        change_made = False

        while ind < len(T):
            cur_tile = T[ind]
            tx, ty = cur_tile[0], cur_tile[1]
            print(f"\r{tx}, {ty}", end="")

            if (tx, ty) not in ignore:
                cur_x = START_X_MP + (25 * tx)
                cur_y = START_Y_MP + (25 * ty)

                tile = get_tile(cur_x, cur_y)

                if tile == "dirt" or tile == "flag":
                    ignore.add((tx, ty))
                    pass
                elif tile in NUMBERS:
                    adj_tiles = count_adj_tiles(cur_x, cur_y)
                    if adj_tiles[1] == tile:
                        ignore.add((tx, ty))
                        if click_adj_tiles(cur_x, cur_y):
                            change_made = True
                            for t in ADJ_C:
                                if (
                                    tx + t[0],
                                    ty + t[1],
                                ) not in ignore and is_valid_coordinate(
                                    cur_x, cur_y, (t[0] * 25), (t[1] * 25)
                                ):
                                    T.insert(
                                        ind + 1,
                                        [cur_tile[0] + t[0], cur_tile[1] + t[1]],
                                    )
                    elif adj_tiles[0] + adj_tiles[1] == tile:
                        ignore.add((tx, ty))
                        if flag_adj_tiles(cur_x, cur_y):
                            change_made = True
                    else:
                        # Don't want to add ignored tiles or duplicate tiles to NEW_T
                        if (tx, ty) not in cur_new_t and (tx, ty) not in ignore:
                            NEW_T.insert(0, [tx, ty])
                            cur_new_t.add((tx, ty))
                else:
                    if (tx, ty) not in cur_new_t and (tx, ty) not in ignore:
                        NEW_T.append([tx, ty])
                        cur_new_t.add((tx, ty))

            ind += 1
            if keyboard.is_pressed("q"):
                quit()
        if keyboard.is_pressed("q"):
            quit()


def main():
    open_minesweeper()
    select_difficulty()
    start_game()
    play()


if __name__ == "__main__":
    main()
