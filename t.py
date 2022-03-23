import pyautogui
import consts
while True:
    print(pyautogui.position())
    x = int(input())
    pyautogui.moveTo(x, 370)
    x, y = pyautogui.position()
    sc = pyautogui.screenshot(region=(x - 12.5, y - 12.5, 25, 23))
    sc.save("1.png")
    print(sc.getcolors())