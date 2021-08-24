import numpy as np
import argparse
import cv2
import imutils
import random
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# 加载图像并转换为灰度图像
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = imutils.auto_canny(gray)
# cv2.imshow("Original", auto)
# cv2.waitKey(0)
cv2.imshow("Original", image)
cv2.waitKey(0)

# 找到所有的轮廓，并且绘制出来，在绘制之前，我们一定要备份我们的原图
# 因为这个函数会破坏原图
# 建议使用CHAIN_APPROX_SIMPLE，而不是CHAIN_APPROX_NONE，后者会保留所有像素，占用很多内存，而效果差不多
cnts = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# cnts = cv2.findContours(auto.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("gray", gray)
cv2.waitKey(0)
cnts = imutils.grab_contours(cnts)  # 固定用法
clone = image.copy()
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)  # -1表示画出所有contours，2代表线宽为2
print("Found {} contours".format(len(cnts)))

# 显示结果
cv2.imshow("All Contours", clone)
cv2.waitKey(0)

clone = image.copy()
cv2.destroyAllWindows()

# 将轮廓逐个绘制出来
for (i, c) in enumerate(cnts):
    print("Drawing contour #{}".format(i + 1))
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    cv2.drawContours(clone, [c], -1, (b, g, r), 4)
cv2.imshow("Single Contour", clone)
cv2.waitKey(0)

clone = image.copy()
cv2.destroyAllWindows()

# 找到图片中的轮廓，这次仅仅绘制外层的轮廓。cv2.RETR_EXTERNAL
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cv2.findContours(auto.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(cnts)
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
print("Found {} EXTERNAL contours".format(len(cnts)))

# 显示结果
cv2.imshow("All Contours", clone)
cv2.waitKey(0)

clone = image.copy()
cv2.destroyAllWindows()

# 依次显示各个轮廓
for c in cnts:
    # 建立当前轮廓的掩模
    mask = np.zeros(gray.shape, dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1)

    # 显示图片
    cv2.imshow("Image", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Image + Mask", cv2.bitwise_and(image, image, mask=mask))
    cv2.waitKey(0)
