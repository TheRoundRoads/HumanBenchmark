import pyautogui
import time
import pyscreenshot
from PIL import Image, ImageGrab
import numpy as np

X = 500
Y = 500

def click():
    pyautogui.click(x=X, y=Y)

clicked = 0
if __name__ == "__main__":
    time.sleep(2)
    pyautogui.click(x=1000, y=600)
    time.sleep(0.1)
    while clicked < 5:
        px = ImageGrab.grab().load()
        if 72 <= px[X, Y][0] <= 78:
            click()
            clicked += 1
        
            time.sleep(0.2)
            click()
            time.sleep(0.1)
        