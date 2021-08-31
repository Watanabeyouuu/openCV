# 加载 OpenCV and numpy
import cv2
import numpy as np

# 建立 VideoCapture object
cap = cv2.VideoCapture(0)

# 查看摄像头是否正确打开
if (cap.isOpened() == False):
    print("Unable to read camera feed")

frame_width = int(cap.get(3))  # 得到摄像头拍摄影片的宽和高
frame_height = int(cap.get(4))

out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

# 读取摄像头保存到输出视频中直到esc被按下
while (True):
    ret, frame = cap.read()

    if ret == True:
        # 将图片写入 'output.avi'
        out.write(frame)

        #
        cv2.imshow('frame', frame)
        # 按下esc停止录制
        if cv2.waitKey(1) & 0xFF == 27:
            break

        # Break the loop
    else:
        break

        # When everything done, release the video capture and video write objects
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows()
