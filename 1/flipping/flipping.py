import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# 水平翻转
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)
a = flipped[235,259]
img2 = imutils.rotate(flipped,45)
img3 = cv2.flip(img2,0)
a = img3[189,441]
# 垂直翻转
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# 两个方向都翻转
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)