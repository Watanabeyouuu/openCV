import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# 加载并显示图片 构建双边滤波的参数，这些参数包括卷积核的半径，sigma color，sigma space
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

#
for (diameter, sigmaColor, sigmaSpace) in params:
	# 应用双边滤波
	blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
	title = "Blurred d={}, sc={}, ss={}".format(diameter, sigmaColor, sigmaSpace)
	cv2.imshow(title, blurred)
cv2.waitKey(0)