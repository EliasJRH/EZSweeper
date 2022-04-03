import keyboard
import pyautogui as pag
from consts import *
from funcs.startup import *
from funcs.tile_identification import get_tile
from funcs.actions import click_adj_tiles, flag_and_ignore_adj_tiles
from funcs.utils import *
from funcs.advanced_searching import advanced_search
import copy

# Plays the game
def play():
    print("BOT IS RUNNING")
    print("Press 'q' to quit")
    pag.PAUSE = 0

    NEW_T = copy.deepcopy(TILES)
    T = copy.deepcopy(TILES)

    change_made = (
        True  # Flag that determines whether or not we should check the entire board
    )
    adv_search_flag = (
        False  # Flag that determines whether or not advanced searching should be used
    )

    ignore = set(
        {}
    )  # Contains all indicies of the board with no information (dirt, flagged or completed tiles)
    new_t_set = set({})  # Contains all indicies to be searched again, no duplicates

    while T:
        ind = 0

        if not change_made and not adv_search_flag:
            T = copy.deepcopy(TILES)
            adv_search_flag = True
        elif not change_made and adv_search_flag:
            adv_search_flag = False
            advanced_search(T, ignore)
            T = copy.deepcopy(TILES)
        else:
            T = copy.deepcopy(NEW_T)

        NEW_T = []
        new_t_set.clear()

        # continue with this idea, this is good
        # need to have a dual flag once for resetting searching, second for advanced searching
        # the ignore set is good, use that to make the reset search shorter

        change_made = False

        while ind < len(T):
            coords = T[ind]
            x_c, y_c = coords[0], coords[1]
            print(f"\r{x_c}, {y_c}", end="")

            if (x_c, y_c) not in ignore:
                x_mp = START_X_MP + (25 * x_c)
                y_mp = START_Y_MP + (25 * y_c)

                tile = get_tile(x_mp, y_mp)

                if tile == "dirt" or tile == "flag":
                    ignore.add((x_c, y_c))
                    pass
                elif tile in NUMBERS:
                    adj_tiles = count_adj_tiles(x_mp, y_mp)
                    if adj_tiles[1] == tile:
                        ignore.add((x_c, y_c))
                        if click_adj_tiles(x_mp, y_mp):
                            change_made = True
                            for adj_c in ADJ_C:
                                # fmt: off
                                if ((x_c + adj_c[0], y_c + adj_c[1]) not in ignore
                                    and is_valid_coordinate(x_mp, y_mp, (adj_c[0] * 25), (adj_c[1] * 25))
                                    and (x_c + adj_c[0],y_c + adj_c[1]) not in new_t_set):
                                        NEW_T.append([x_c + adj_c[0], y_c + adj_c[1]])
                                        new_t_set.add((x_c + adj_c[0],y_c + adj_c[1]))
                                # fmt: on
                    elif adj_tiles[0] + adj_tiles[1] == tile:
                        ignore.add((x_c, y_c))
                        if flag_and_ignore_adj_tiles(x_mp, y_mp, ignore):
                            change_made = True
                            for adj_c in ADJ_C:
                                # fmt: off
                                if ((x_c + adj_c[0], y_c + adj_c[1]) not in ignore
                                    and is_valid_coordinate(x_mp, y_mp, (adj_c[0] * 25), (adj_c[1] * 25))
                                    and (x_c + adj_c[0],y_c + adj_c[1]) not in new_t_set):
                                        NEW_T.append([x_c + adj_c[0], y_c + adj_c[1]])
                                        new_t_set.add((x_c + adj_c[0],y_c + adj_c[1]))
                                # fmt: on
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
