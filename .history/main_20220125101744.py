import cv2
import numpy as np

image = cv2.imread('canvas.png', 0)
cv2.imshow('first',image)
idKey = cv2.waitKey(0)
if idKey == 27:     # 27 为 ESC 键对应的 ASCII 码
    # 关闭指定窗口
    cv2.destroyWindow('imgBgr')