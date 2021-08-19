import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# 围绕图像中心旋转
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)

# 作业
# rotated = imutils.rotate(image, 5, (cX, cY), 1.0)
# cv2.imshow("Rotated by 5 Degrees", rotated)
# print(rotated[34, 67])

# 旋转5度
M = cv2.getRotationMatrix2D((cX, cY), 5, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
a = rotated[34, 67]
print(a)
cv2.imshow("Rotated by 45 Degrees", rotated)

M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

# 换一个旋转中心
M = cv2.getRotationMatrix2D((cX - 50, cY - 50), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by Offset & 45 Degrees", rotated)

# 练习使用imutilus.rotate
rotated = imutils.rotate(image, 180, (cX - 50, cY - 50), 2.0)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)
