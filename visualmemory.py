import pyautogui
import pyscreenshot
from PIL import ImageGrab
import time
import numpy as np

DARK_BLUE = np.array([37, 115, 193])
START_COL = 621
WIDTH = 798
START_ROW = 274
HEIGHT = 428

SCORE = 50

def isDark(arr):
    return (tuple(arr) == DARK_BLUE).all()

if __name__ == "__main__":
    time.sleep(2)
    pyautogui.click(x=989, y=588)
    time.sleep(0.1)

    # while True:
    #     
    for _ in range(SCORE):
        # get blank squares
        print("Grabbing first image")
        img = pyscreenshot.grab(bbox=(START_COL, START_ROW, START_COL+WIDTH, START_ROW+HEIGHT))
        img.save("HumanBenchmark/ss.png")
        img = np.array(img)
        time.sleep(0.6)
        # get white squares
        print("Grabbing second image")
        img1 = pyscreenshot.grab(bbox=(START_COL, START_ROW, START_COL+WIDTH, START_ROW+HEIGHT))
        img1.save("HumanBenchmark/ss1.png")
        img1 = np.array(img1)
        
        time.sleep(2)
        
        dims = img.shape
        found = False
        start_row, start_col = -1, -1
        for row in range(dims[0]):
            for col in range(dims[1]):
                if isDark(img[row][col]):
                    found = True
                    start_row = row
                    start_col = col
                    break

            if found:
                break
        
        print(f"Starting position: ({start_col}, {start_row})")
        light = True
        avg_cols = []
        temp_start_col = -1

        for col in range(dims[1]):
            isdark = isDark(img[start_row][col])
            if isdark and light:
                temp_start_col = col
                light = False
            elif (not isdark) and (not light):
                avg_cols.append((temp_start_col + col) // 2)
                light = True

        print("Average Cols:", avg_cols)
        light = True
        avg_rows = []
        temp_start_row = -1

        for row in range(dims[0]):
            isdark = isDark(img[row][start_col])
            if isdark and light:
                temp_start_row = row
                light = False
            elif (not isdark) and (not light):
                avg_rows.append((temp_start_row + row) // 2)
                light = True
        
        print("Average Rows:", avg_rows)
        for row in avg_rows:
            for col in avg_cols:
                if not isDark(img1[row][col]):
                    print(f"Clicking: ({col}, {row})")
                    pyautogui.click(x=START_COL+col, y=START_ROW+row)
                    # time.sleep(0.1)
                    # whites.append([row, col])
        
    
            
        time.sleep(0.9)
