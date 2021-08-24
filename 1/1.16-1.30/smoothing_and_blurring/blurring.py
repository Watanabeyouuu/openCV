import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# 加载显示图像，确定卷积核的尺寸
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (9, 9), (15, 15)]

# 应用均值滤波
for (kX, kY) in kernelSizes:
	blurred = cv2.blur(image, (kX, kY))
	cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
cv2.waitKey(0)

# 清空
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# 应用高斯滤波
for (kX, kY) in kernelSizes:
	blurred = cv2.GaussianBlur(image, (kX, kY), 0)
	cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)
cv2.waitKey(0)

# 清空
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# 使用中值滤波
for k in (3, 9, 15):
	blurred = cv2.medianBlur(image, k)
	cv2.imshow("Median {}".format(k), blurred)
cv2.waitKey(0)