import pyautogui as pag
import time
import webbrowser

#block width: 25px
#block height: 25px

# Grass pixel 1 = (162, 209, 73)
# Grass pixel 2 = (185, 221, 119)

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
    pag.PAUSE = 5
    # pag.PAUSE = 0.001
    colors = set()

    # TODO:
    # Have to analyze each number box and find where the numbers intersect at the same position in the box
    # Use that position as a way of grabbing the color and identify the number of adjacent bombs by that color
    
    while True:
        x = 655
        y = 365
        for yy in range(20):
            for xx in range(23):
                x += 25
                pag.moveTo(x, y)
                for z in range(15):
                    cur = pag.screenshot()
                    print(cur.getpixel((x, y)))
                    pag.move(1, 0)
            y += 25
            x = 655

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