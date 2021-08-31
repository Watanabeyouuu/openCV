# 加载 OpenCV and numpy
import cv2
import numpy as np

cap = cv2.VideoCapture('1917.mp4')
# cap = cv2.VideoCapture(0)
# 查看视频是否成功打开
if (cap.isOpened() == False):
    print("Error opening video stream or file")

while (cap.isOpened()):
    # 一帧一帧的读取
    ret, frame = cap.read()
    if ret == True:

        # 显示当前读到的帧
        cv2.imshow('Frame', frame)

        # 点击 esc 退出播放
        if cv2.waitKey(42) & 0xFF == 27:
            break

    # Break the loop
    else:
        break

# 释放资源
cap.release()

# 关掉所有窗口
cv2.destroyAllWindows()
