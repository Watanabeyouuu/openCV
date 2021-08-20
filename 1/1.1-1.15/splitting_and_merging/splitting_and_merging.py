# 加载必要的包
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
print((B), B.shape, image.shape)
# 分别显示每个通道
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
plt.imshow(imutils.opencv2matplotlib(image))
plt.show()
# 将各个通道拼接回去，尝试融合超过三个通道。
# merged = cv2.merge([B, G, R, R])
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.imshow(imutils.opencv2matplotlib(merged))
plt.show()
a = R[94, 180]
a = G[5, 80]
a = B[78, 13]
a
# 观察彩色化的各个通道
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)
