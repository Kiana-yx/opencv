# green=np.uint8([[[0,255,0]]])
# hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

cap = cv2.VideoCapture(0)
while 1:
    ret, frame = cap.read()

    # 在 HSV 颜色空间中要比在 BGR 空间中更容易表示一个特定颜
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 设定蓝色的阈值
    lower_blue = np.array([2, 88, 117])
    upper_blue = np.array([113, 188, 201])
    # 根据阈值构建掩模
    mask_B = cv2.inRange(hsv, lower_blue, upper_blue)

    lower_green = np.array([10, 110, 110])
    upper_green = np.array([130, 255, 255])
    mask_G = cv2.inRange(hsv, lower_green, upper_green)

    mask = mask_B + mask_G
    # 对原图像和掩模进行位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # 显示图像
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyWindow()


