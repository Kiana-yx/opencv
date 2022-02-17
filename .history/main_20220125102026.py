import cv2
import numpy as np

image = cv2.imread('canvas.png', 0)
cv2.imshow('first',image)
cv2.waitKey(0)
ball=image[280:340,330:390]
image[273:333,100:160]=ball
cv2.imshow('second',image)
cv2.waitKey(0)
