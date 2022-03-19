import pyautogui as pag
import time
import webbrowser

#block width: 25px
#block height: 25px

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

def process():
    # TODO:
    # Have to analyze each number box and find where the numbers intersect at the same position in the box
    # Use that position as a way of grabbing the color and identify the number of adjacent bombs by that color
    x, y = pag.position()

def main():
    open_minesweeper()
    select_difficulty()
    start_game()
    process()


if __name__ == "__main__":
    main()