import pyautogui
import pytesseract
import pyscreenshot
import time

WORDS = set()

SCORE = 1000  # set what score you want to get

def seen():
    pyautogui.click(x=926, y=540)

def new():
    pyautogui.click(x=1061, y=549)

if __name__ == "__main__":
    time.sleep(2)
    pyautogui.click(x=997, y=631)
    time.sleep(0.5)

    for _ in range(SCORE):
        pic = pyscreenshot.grab(bbox=(592, 410, 1435, 493))

        result_string = pytesseract.image_to_string(pic).strip()

        if result_string in WORDS:
            seen()
        else:
            WORDS.add(result_string)
            new()

        time.sleep(0.1)