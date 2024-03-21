import pytesseract
import time
import pyscreenshot
from pynput.keyboard import Controller

if __name__ == "__main__":
    time.sleep(2)

    pic = pyscreenshot.grab(bbox=(520, 450, 1471, 570))

    result_string = pytesseract.image_to_string(pic).replace("\n", " ")
    print(result_string)

    keyboard = Controller()
    for c in result_string:
        keyboard.press(c)