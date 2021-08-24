import argparse
import cv2
import matplotlib.pyplot as plt
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# 加载图像，并转换为灰度图像
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Original", image)
plt.figure("Original")
plt.imshow(imutils.opencv2matplotlib(image))

# 分别计算X和Y方向的梯度值
# gX = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
# gY = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1)
# Scharr
gX = cv2.Scharr(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
gY = cv2.Scharr(gray, ddepth=cv2.CV_64F, dx=0, dy=1)

# 将浮点型图像转换为uint8图像，这样opencv才能够处理
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

# 将这两幅图像融合在一起
sobelCombined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

# 显示结果
# cv2.imshow("Sobel X", gX)
# cv2.imshow("Sobel Y", gY)
# cv2.imshow("Sobel Combined", sobelCombined)
# cv2.waitKey(0)
plt.figure("Sobel X")
plt.imshow(imutils.opencv2matplotlib(gX), cmap='gray')
# plt.show()
plt.figure("Sobel Y")
plt.imshow(imutils.opencv2matplotlib(gY), cmap='gray')
# plt.show()
plt.figure("Sobel Combined")
plt.imshow(imutils.opencv2matplotlib(sobelCombined), cmap='gray')
plt.show()
