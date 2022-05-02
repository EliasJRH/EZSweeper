from ast import Pass
import sys
import pyautogui as pag
import time
import webbrowser

from consts.mouse_positions import (
    CENTER_X_MP_EASY,
    CENTER_X_MP_HARD,
    CENTER_X_MP_MED,
    CENTER_Y_MP_EASY,
    CENTER_Y_MP_HARD,
    CENTER_Y_MP_MED,
)

DIFFICULTY = 2

difficulty_imgs = {
    0: "pag_images/easybtn.png",
    1: "pag_images/medbtn.png",
    2: "pag_images/hardbtn.png",
}

# Functions related to initially starting the game

# Opens minesweeper in browser
def open_minesweeper():
    webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=minesweeper")
    time.sleep(2)


# Changes difficulty to hard, might change to add more difficulties later
def select_difficulty():
    pag.useImageNotFoundException()
    while True:
        try:
            btn_pos = pag.locateOnScreen(
                "pag_images/playbtn.png", region=(186, 290, 832, 625)
            )
            pag.moveTo(pag.center(btn_pos))
            pag.click()
            break
        except pag.ImageNotFoundException as err:
            continue

    while True:
        try:
            btn_pos = pag.locateOnScreen(
                "pag_images/diffbtn.png", region=(560, 0, 300, 500)
            )
            pag.moveTo(pag.center(btn_pos))
            pag.click()
            break
        except pag.ImageNotFoundException as err:
            continue

    btn_img = difficulty_imgs[DIFFICULTY]
    while True:
        try:
            btn_pos = pag.locateOnScreen(btn_img, region=(560, 0, 300, 500))
            pag.moveTo(pag.center(btn_pos))
            pag.click()
            break
        except pag.ImageNotFoundException as err:
            continue


# Clicks on center tile
def start_game():
    if DIFFICULTY == 0:
        pag.moveTo(CENTER_X_MP_EASY, CENTER_Y_MP_EASY)
    elif DIFFICULTY == 1:
        pag.moveTo(CENTER_X_MP_MED, CENTER_Y_MP_MED)
    else:
        pag.moveTo(CENTER_X_MP_HARD, CENTER_Y_MP_HARD)
    pag.click()


for x in range(1, len(sys.argv)):
    cur_arg = sys.argv[x].split("=")
    if cur_arg[0] == "-d":
        if cur_arg[1].lower() == "easy":
            DIFFICULTY = 0
        elif cur_arg[1].lower() == "medium":
            DIFFICULTY = 1
        else:
            DIFFICULTY = 2
