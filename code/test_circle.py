import cv2
import numpy as np

img = cv2.imread('/home/kiana/Code/openCV_learning/img/people.png', -1)
h = img.shape[0]  # 高度
w = img.shape[1]  # 宽度

vec = np.array([0, 0])
for row in range(h):
    for col in range(w):
        if img[col, row] == 255:
            temp = np.array([row, col])  # 注意这儿数组与图像坐标是反过来的？
            vec = np.c_[vec, temp]
vec = np.transpose(vec)  # 转置一下
vec = np.delete(vec, 0, 0)  # 获取轮廓点集合

# 寻找凸包并绘制凸包（轮廓）
hull = cv2.convexHull(vec)
hull = np.squeeze(hull)  # 去除多维数组中，维度为1的维度
print(hull)

# 绘制凸包
# length = len(hull)
# for i in range(len(hull)-1):
#     # cv2.circle(img, (hull[i][1], hull[i][0]), radius=1, color=255, thickness=2)
#     cv2.line(img, hull[i], hull[i+1], color=255, thickness=2)

# 绘制外接椭圆
ellipse = cv2.fitEllipse(hull)
[(x, y), (a, b), angle] = cv2.fitEllipse(hull)
img = cv2.ellipse(img, ellipse, 255, 2)
print("中心坐标：%f,%f", x, y)
print("长轴：%f；短轴%f", a, b)
print("旋转角度：%f", angle)
cv2.circle(img, (round(x), round(y)), radius=1, color=255, thickness=2)


# 显示图片
cv2.imshow('img', img)
cv2.waitKey()
