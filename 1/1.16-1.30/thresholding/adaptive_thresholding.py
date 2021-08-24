# 用法
# python adaptive_thresholding.py --image license_plate.png
import imutils
import numpy as np
from matplotlib import pyplot as plt
from skimage.filters import threshold_local
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
# cv2.namedWindow('Image', cv2.WINDOW_KEEPRATIO)
# cv2.imshow("blurred", blurred)

# canvas = np.zeros((300, 300), dtype="uint8")
# black = (0, 0, 0)
# blurred = cv2.rectangle(canvas, (50, 200), (200, 225), black, -1)
# cv2.imshow("Canvas", blurred)
# 我们不再使用全局的阈值，而是在每个像素的位置使用特定的阈值
# 在这个例子中，我们使用邻域的25个像素的平均值作为参考，并且根据这个平均值来计算出
# 这个像素点的阈值，C是一个给定的值，15

thresh = cv2.adaptiveThreshold(blurred, 255,
                               cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 23, 45)
# cv2.imshow("OpenCV Mean Thresh", thresh)
plt.imshow(imutils.opencv2matplotlib(thresh))
plt.show()
# scikit-image中的adaptive thresholding
T = threshold_local(blurred, 29, offset=5, method="gaussian")
thresh = (blurred < T).astype("uint8") * 255
# cv2.imshow("scikit-image Mean Thresh", thresh)
plt.imshow(imutils.opencv2matplotlib(thresh))
plt.show()
# cv2.waitKey(0)
