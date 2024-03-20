import pyautogui
import time
import pyscreenshot
from PIL import Image, ImageGrab
import numpy as np

X = 200
Y = 200

def click():
    pyautogui.click(x=X, y=Y)

if __name__ == "__main__":
    time.sleep(2)

    while True:
        px = ImageGrab.grab().load()
        if px[200, 200][0] == 75:
            click()
            break
        