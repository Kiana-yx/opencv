import cv2
import pyrealsense2 as rs
import numpy as np

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()

# Get device product line for setting a supporting resolution
pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()
device_product_line = str(device.get_info(rs.camera_info.product_line))

config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)

face_cascade = cv2.CascadeClassifier(
    '/home/kiana/anaconda3/envs/py38/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    '/home/kiana/anaconda3/envs/py38/lib/python3.8/site-packages/cv2/data/haarcascade_eye.xml')

try:
    while True:
        frames = pipeline.wait_for_frames()

        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        # Convert images to numpy arrays 把图像转换为numpy data
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        gray = cv2.cvtColor(color_image, cv2.COLOR_RGB2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 5, cv2.CASCADE_SCALE_IMAGE, (10, 10), (200, 200))
        for (x, y, w, h) in faces:
            img = cv2.rectangle(color_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # roi_gray = gray[y:y + h, x:x + w]
            # roi_color = img[y:y + h, x:x + w]
            # eyes = eye_cascade.detectMultiScale(roi_gray)
            # for (ex, ey, ew, eh) in eyes:
            #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # 显示图像
        # Show images
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', color_image)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
finally:

    # Stop streaming
    pipeline.stop()
