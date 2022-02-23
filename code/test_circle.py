import cv2
import numpy as np

img = cv2.imread('/home/kiana/Code/openCV_learning/img/people.png', -1)
size = img.shape
w = size[1]  # 宽度
h = size[0]     #高度

vec = np.array([0, 0])
for row in range(h):
    for col in range(w):
        if img[row, col] == 255:
            temp = np.array([row, col])
            vec = np.c_[vec, temp]
# indexes = [3, 5, 7]
# modifiedArray = np.delete(myArray, indexes)
# vec = np.array(vec, dtype=np.float32)
vec = np.transpose(vec)

# 寻找凸包并绘制凸包（轮廓）
hull = cv2.convexHull(vec)
# hull = np.squeeze(hull)  # 去除多维数组中，维度为1的维度
print(hull)

length = len(hull)
for i in range(len(hull)):
    cv2.line(img, tuple(hull[i][0]), tuple(hull[(i+1)%length][0]), 255, 2)

# 显示图片
cv2.imshow('line', img)
cv2.waitKey()
