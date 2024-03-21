import pyautogui
import time
from PIL import ImageGrab

# x from 529 to 1535, y from 281 to 643
if __name__ == "__main__":
    time.sleep(2)
    # start test
    pyautogui.click(x=1000, y=450)
    time.sleep(0.01)

    for i in range(30):
        px = ImageGrab.grab().load()
        found = False
        for x in range(529, 1536):
            for y in range(281, 644):
                if px[x, y] != (43, 135, 209):
                    pyautogui.click(x=x+10, y=y+10)
                    found = True
                    break

            if found:
                break

    # px = ImageGrab.grab().load()
    # print(px[529, 281])