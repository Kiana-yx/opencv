import cv2
import numpy as np

# 载入图片
frame = cv2.imread('/home/kiana/Code/openCV_learning/img/ball_blue.png')
# 设置窗口
cv2.namedWindow('Canny')

targetPos_x = 0
targetPos_y = 0

# 定义回调函数
def nothing(x):
    pass


# 创建两个滑动条，分别控制threshold1，threshold2
cv2.createTrackbar('lower_blue', 'Canny', 50, 400, nothing)
cv2.createTrackbar('upper_blue', 'Canny', 100, 400, nothing)
while 1:
    # 返回滑动条所在位置的值
    threshold1 = cv2.getTrackbarPos('lower_blue', 'Canny')  # 第一个是轨迹栏名称，第二个是窗口名称
    threshold2 = cv2.getTrackbarPos('upper_blue', 'Canny')
    # 在 HSV 颜色空间中要比在 BGR 空间中更容易表示一个特定颜
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 设定蓝色的阈值
    lower_blue = np.array([0, 50, 50])
    upper_blue = np.array([53, 255, 255])

    # 根据阈值构建掩模
    mask_B = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = mask_B

    # # 对原图像和掩模进行位运算
    # res = cv2.bitwise_and(frame, frame, mask=mask)
    # # 显示图像
    # cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    # cv2.imshow('res', res)

    # 下面的代码查找包围框，并绘制
    x, y, w, h = 0, 0, 0, 0
    for cnt in blueContours:
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        targetPos_x = int(x + w / 2)
        targetPos_y = int(y + h / 2)
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, (targetPos_x, targetPos_y), 2, (0, 255, 0), 4)
    cv2.imshow('Horizontal Stacking', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
