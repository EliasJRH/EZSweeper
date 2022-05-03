import keyboard
import pyautogui as pag
from consts.other import *
from consts.mouse_positions import *
from funcs.startup import *
from funcs.tile_identification import get_tile
from funcs.actions import click_adj_tiles, click_tile, flag_and_ignore_adj_tiles
from funcs.utils import *
from funcs.advanced_searching import advanced_search_tile
import copy

# Plays the game
def play():
    print("BOT IS RUNNING")
    print("Press 'q' to quit")
    pag.PAUSE = 0

    bombs = 99
    grass_length = 24
    START_X_MP = START_X_MP_HARD
    START_Y_MP = START_Y_MP_HARD
    TILE_WIDTH = TILE_WIDTH_HARD

    for x in range(1, len(sys.argv)):
        cur_arg = sys.argv[x].split("=")
        if cur_arg[0] == "-d":
            if cur_arg[1].lower() == "easy":
                bombs = 10
                grass_length = 10
                START_X_MP = START_X_MP_EASY
                START_Y_MP = START_Y_MP_EASY
                TILE_WIDTH = TILE_WIDTH_EASY
            elif cur_arg[1].lower() == "medium":
                bombs = 40
                grass_length = 18
                START_X_MP = START_X_MP_MED
                START_Y_MP = START_Y_MP_MED
                TILE_WIDTH = TILE_WIDTH_MED
            else:
                bombs = 99
                grass_length = 24
                START_X_MP = START_X_MP_HARD
                START_Y_MP = START_Y_MP_HARD
                TILE_WIDTH = TILE_WIDTH_HARD

    TILE_COORDS = generate_tile_list()

    NEW_T = copy.deepcopy(TILE_COORDS)
    T = copy.deepcopy(TILE_COORDS)

    # fmt: off
    # Flag that determines whether or not we should check the entire board
    change_made = True
    
    # Flag that determines whether or not advanced searching should be used
    adv_search_flag = False
    adv_search = False
    
    # Contains all indicies of the board with no information (dirt, flagged or completed tiles)
    ignore = set({})
    
    # Contains all indicies to be searched again, no duplicates
    new_t_set = set({})

    # Contains all pairs of tiles that are searched during advanced searching
    adv_search_pairs = set({})  
    # fmt: on

    while len(ignore) < len(TILE_COORDS):
        end = False
        ind = 0

        if not change_made and not adv_search_flag:
            adv_search_flag = True
            T = copy.deepcopy(TILE_COORDS)
        elif not change_made and adv_search_flag:
            adv_search = True
            adv_search_flag = False
            T = copy.deepcopy(TILE_COORDS)
        else:
            adv_search = False
            adv_search_flag = False
            if NEW_T:
                T = copy.deepcopy(NEW_T)
            else:
                T = copy.deepcopy(TILE_COORDS)

        NEW_T.clear()
        new_t_set.clear()
        adv_search_pairs.clear()

        change_made = False

        grass_count = 0
        first_non_grass = False

        while ind < len(T):
            coords = T[ind]
            x_c, y_c = coords[0], coords[1]
            
            if grass_count == grass_length and first_non_grass:
                break
            elif x_c == 0:
                grass_count = 0

            print(f"\r{x_c}, {y_c}", f"bombs: {bombs}", len(TILE_COORDS), len(ignore), end=" ")

            if (x_c, y_c) not in ignore:
                x_mp = START_X_MP + (TILE_WIDTH * x_c)
                y_mp = START_Y_MP + (TILE_WIDTH * y_c)

                tile = get_tile(x_mp, y_mp)

                if tile == "dirt" or tile == "flag":
                    ignore.add((x_c, y_c))
                elif tile == "grass":
                    grass_count += 1
                    if bombs == 0:
                        click_tile(x_mp, y_mp)
                elif tile in NUMBERS:
                    first_non_grass = True
                    adj_tiles = count_adj_tiles(x_mp, y_mp)
                    cur_change_made = False
                    if adj_tiles[1] == tile:
                        ignore.add((x_c, y_c))
                        if click_adj_tiles(x_mp, y_mp):
                            change_made = True
                            cur_change_made = True

                    elif adj_tiles[0] + adj_tiles[1] == tile:
                        ignore.add((x_c, y_c))
                        flagged, bombs_flagged = flag_and_ignore_adj_tiles(x_mp, y_mp, ignore)
                        if flagged:
                            change_made = True
                            cur_change_made = True
                        if bombs_flagged > 0:
                            bombs -= bombs_flagged

                    elif adv_search:
                        #fmt: off
                        if advanced_search_tile(x_mp, y_mp, tile, x_c, y_c, ignore, adv_search_pairs, bombs):
                        #fmt: on
                            change_made = True
                            cur_change_made = True

                    if cur_change_made:
                        for adj_c in ADJ_COORDS:
                            # fmt: off
                            if ((x_c + adj_c[0], y_c + adj_c[1]) not in ignore # we're not ignoring the adjacent coordinate
                                and is_valid_mouse_pos(x_mp + (adj_c[0] * TILE_WIDTH), y_mp + (adj_c[1] * TILE_WIDTH)) # it's a valid coordinate
                                and (x_c + adj_c[0], y_c + adj_c[1]) not in new_t_set): # we're not already going to search it
                                    NEW_T.append([x_c + adj_c[0], y_c + adj_c[1]])
                                    new_t_set.add((x_c + adj_c[0],y_c + adj_c[1]))
                            # fmt: on
                elif tile == "end":
                    end = True
                    break
            ind += 1
            if keyboard.is_pressed("q"):
                quit()

        if keyboard.is_pressed("q"):
            quit()

        if end:
            break


def main():
    open_minesweeper()
    select_difficulty()
    start_game()
    play()


if __name__ == "__main__":
    main()
