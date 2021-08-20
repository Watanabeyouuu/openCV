import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# 围绕图像中心旋转
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)

# 水平翻转
image = cv2.flip(image, 1)
# 旋转45度
image = imutils.rotate(image, 45, (cX, cY), 1.0)
# 垂直翻转
image = cv2.flip(image, 0)
cv2.imshow("Flipped Horizontally", image)
a = image[189, 441]
print(a)
# 垂直翻转
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# 两个方向都翻转
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)
