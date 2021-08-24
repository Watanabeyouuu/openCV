import argparse
import cv2
import imutils
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# 加载图像并转化为灰度图像
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray.shape, image.shape)
# 设计一个矩形的卷积核，并用于黑帽变换，这可以让我们找到包含在明亮区域内的暗的区域
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (66, 66))

blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, rectKernel)
r2 = closing - gray
# cv2.imshow('r2', r2)

# 类似的，应用一个顶帽变换（白帽变换），这可以让我们找到包含在暗区域中的亮区域
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, rectKernel)
r3 = gray - opening
# cv2.imshow('r3', r3)

# 显示结果
# plt.imshow(imutils.opencv2matplotlib(image))

cv2.imshow("Blackhat", blackhat)
cv2.imshow("Tophat", tophat)
cv2.waitKey(0)
