import pyautogui as pag
import time
import webbrowser

# Functions related to initially starting the game

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


# Clicks on center tile
def start_game():
    pag.moveTo(940, 555)
    pag.click()
    pag.moveTo(665, 365)
