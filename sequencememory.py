import mss
import pyautogui
import time
from PIL import ImageGrab
positions = [[858, 366], [992, 361], [1129, 364], [859, 491], [998, 493], [1126, 497], [862, 626], [991, 620], [1123, 624]]

def read_pixel_with_mss(x, y):
    with mss.mss() as sct:
        pixel = sct.pixel(x, y)
        return pixel


if __name__ == "__main__":
    time.sleep(2)
    # start test
    pyautogui.click(x=990, y=597)
    
    time.sleep(1)
    stage = 1
    white_tiles = []
    new_tile = []
    count = 0

    while True:
        if count == stage:  # start clicking
            white_tiles.append(positions[i])
            time.sleep(0.2)
            for x, y in white_tiles:
                pyautogui.click(x=x, y=y)
                time.sleep(0.1)
            stage += 1
            count = 0

            time.sleep(0.5)

        px = ImageGrab.grab().load()
        for i, (x, y) in enumerate(positions):
            if px[x, y] != (37, 115, 193):  # start of stage
                count += 1
                while True:
                    px = ImageGrab.grab().load()
                    if px[x, y] == (37, 115, 193):
                        break
                if count == stage:
                    new_tile = i
                break