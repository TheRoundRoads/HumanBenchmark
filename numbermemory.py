import pyautogui
import time
import pytesseract
import PIL
import pyscreenshot
from pynput.keyboard import Key, Controller

white_image = PIL.Image.new('RGB', (1000, 1000), color=(255, 255, 255))

def get_number(img):
    fn = lambda x : 255 if x > 125 else 0
    r = img.convert('L').point(fn, mode='1')
    inverted_image = PIL.ImageOps.invert(r)
    white_image.paste(inverted_image, (400, 400))
    inverted_image.save("HumanBenchmark/ss1.png")
    # result_string = pytesseract.image_to_string(inverted_image).strip()
    result_string = pytesseract.image_to_string(inverted_image, lang='eng', config='digits')
    print("Resulting number is: " + result_string)
    return result_string

x1 = 950
x2 = 1050
keyboard = Controller()
if __name__ == "__main__":
    time.sleep(2)
    pyautogui.click(x=994, y=610)
    
    time.sleep(0.1)
    while True:
        img = pyscreenshot.grab(bbox=(x1, 379, x2, 486))

        num = get_number(img)
        time.sleep(3)
        for c in num:
            keyboard.press(c)
            time.sleep(0.1)
        
        pyautogui.click(x=1005, y=557)

        time.sleep(5)

        pyautogui.click(x=998, y=619)

        x1 -= 50
        x2 += 50
