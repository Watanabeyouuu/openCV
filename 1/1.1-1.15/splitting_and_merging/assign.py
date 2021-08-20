import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
import imutils

# 构建 argument parser 并且写入输入变量
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# 加载一幅图像并得到RGB三通道. 注意图像通道的顺序是B，G，R
image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)
# plt.imshow(imutils.opencv2matplotlib(image))
# plt.show()

print(R[94, 180], B[78, 13], G[5, 80])
