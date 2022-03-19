import cv2
import numpy as np

found = {}

for cell in cells:
    for i in range(cell.cX, cell.x + cell.w):
        if (img[i][cY]):
            found[img[i][cY]] += 1
    print(found)
    break
    

