import colorsys
import pyautogui as pag
import time
import webbrowser

# block width: 25px
# block height: 25px

# Grass pixel 1 = (162, 209, 73)
# Grass pixel 2 = (185, 221, 119)

# Flag = (242, 54, 7)

GRASS = set({(162, 209, 73), (185, 221, 119), (191, 225, 125), (170, 215, 81)})

IGNORE = set({(162, 209, 73), (185, 221, 119), (191, 225, 125),
             (170, 215, 81), (215, 184, 153), (229, 194, 159), (242, 54, 7)})

FLAG = (242, 54, 7)

COLORS = {
    (25, 118, 210): 1,
    (56, 142, 60): 2,
    (211, 47, 47): 3,
    (123, 31, 162): 4,
    (255, 143, 0): 5,
    (0, 151, 167): 6,
    (66, 66, 66): 7,
    (160, 155, 152): 8
}

TO_SEARCH = [[-25, -25], [0, -25], [25, -25],
             [-25, 0], [25, 0], [-25, 25], [0, 25], [25, 25]]


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


def count_adj_tiles(x, y):
    # [unmarked tiles, flagged tiles]
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

def flag_adj_tiles(x, y):
    for c in TO_SEARCH:
        pag.move(c[0], c[1])
        cur_sc = pag.screenshot()
        cur_col = cur_sc.getpixel((x + c[0], y + c[1]))
        if (cur_col != FLAG):
            pag.click(button='right')
        pag.moveTo(x, y)

def click_adj_tiles(x, y):
    for c in TO_SEARCH:
        pag.move(c[0], c[1])
        pag.click(button='left')
        pag.moveTo(x, y)

def process():
    # pag.PAUSE = 1
    pag.PAUSE = 0

    # TODO:
    # Have to analyze each number box and find where the numbers intersect at the same position in the box
    # Use that position as a way of grabbing the color and identify the number of adjacent bombs by that color

    while True:
        x = 665
        y = 365
        for yy in range(20):
            for xx in range(23):
                x += 25
                pag.moveTo(x, y)
                for z in range(15):
                    cur_sc = pag.screenshot()
                    cur_col = cur_sc.getpixel((x, y))
                    if cur_col in IGNORE:
                        break
                    if cur_col in COLORS:
                        res = count_adj_tiles(x, y)
                        if (res[0] + res[1] == COLORS[cur_col]):
                            flag_adj_tiles(x, y)
                        elif (res[1] == COLORS[cur_col]):
                            click_adj_tiles(x, y)
                        break
                    pag.move(0.1, 0)
            y += 25
            x = 665

    # while True:
    #     time.sleep(1)
    #     x,y = pag.position()
    #     cur = pag.screenshot()
    #     print(cur.getpixel((x,y)))


def main():

    open_minesweeper()
    select_difficulty()
    start_game()
    process()


if __name__ == "__main__":
    main()
