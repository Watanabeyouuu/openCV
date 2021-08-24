import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-l", "--lower-angle", type=float, default=175.0,
	help="Lower orientation angle")
ap.add_argument("-u", "--upper-angle", type=float, default=180.0,
	help="Upper orientation angle")
args = vars(ap.parse_args())

# 加载图像，转换为灰度图像
image = cv2.imread(args["image"])
#################################################
face = image[90:750,1003:1704]
gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Original", image)
plt.figure()
plt.imshow(imutils.opencv2matplotlib(image))

gX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
gY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
cv2.imshow('gX',gX)
cv2.imshow('gY',gY)
# 计算梯度的振幅和方向
mag = np.sqrt((gX ** 2) + (gY ** 2))
orientation = np.arctan2(gY, gX) * (180 / np.pi) % 180
orientation = orientation.astype(np.uint8)
hist = cv2.calcHist([orientation], [0], None, [180], [0, 180])
plt.figure()
plt.imshow(orientation,cmap='gray')
plt.figure()
plt.imshow(mag,cmap='gray')
plt.figure('histogram')
cv2.imshow('face',face)
cv2.waitKey()
a = hist.shape
y_pos = np.arange(a[0])
plt.plot(hist)
plt.bar(y_pos, np.ravel(hist), align='center', alpha=0.5)
plt.show()
###########################################
# 得到所有梯度方向在这个区域内的点
idxs = np.where(orientation >= args["lower_angle"], orientation, -1)
idxs = np.where(orientation <= args["upper_angle"], idxs, -1)
mask = np.zeros(gray.shape, dtype="uint8")
mask[idxs > -1] = 255

# 显示这些点的位置
cv2.imshow("Mask", mask)
cv2.waitKey(0)