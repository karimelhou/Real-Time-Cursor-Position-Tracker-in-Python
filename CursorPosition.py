import pyautogui
from time import sleep

while pyautogui.position()[0] != 0:
    position = pyautogui.position()
    print("The cursor is currently at " + str(position))
    sleep(1)

