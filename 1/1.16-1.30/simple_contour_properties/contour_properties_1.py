import numpy as np
import argparse
import cv2
import imutils
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 找到外部轮廓,这里设置成CHAIN_APPROX_NONE就可以把矩形拟合椭圆，否则会因为轮廓小于5个点无法拟合椭圆
# 可以再这里看到CHAIN_APPROX_NONE和CHAIN_APPROX_SIMPLE的区别
# cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cnts = imutils.grab_contours(cnts)
clone = image.copy()

# 遍历所有的轮廓
for c in cnts:
    # 计算重心
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    print(cX, cY, image.shape)
    # 绘制轮廓的重心
    cv2.circle(clone, (cX, cY), 10, (0, 255, 0), -1)

cv2.imshow("Centroids", clone)
cv2.waitKey(0)
clone = image.copy()

for (i, c) in enumerate(cnts):
    # 计算轮廓的面积和周长
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    print("Contour #{} -- area: {:.2f}, perimeter: {:.2f}".format(i + 1, area, perimeter))

    # 绘制轮廓
    cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)

    # 在轮廓的中心显示轮廓的序号
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.putText(clone, "#{}".format(i + 1), (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX,
                1.25, (255, 255, 255), 4)
# cv2.putText(clone, "#{}".format(perimeter), (cX - 40, cY), cv2.FONT_HERSHEY_SIMPLEX,
# 			0.5, (255, 255, 255), 2)

cv2.imshow("Contours", clone)
cv2.waitKey(0)

clone = image.copy()

for c in cnts:
    # 计算外接矩形
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(clone, (x, y), (x + w, y + h), (0, 255, 0), 2)
    print(x, y, x + w, y + h)
cv2.imshow("Bounding Boxes", clone)
cv2.waitKey(0)
clone = image.copy()

for c in cnts:
    # 计算带旋转的外接矩形
    box = cv2.minAreaRect(c)
    box = np.int0(cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box))
    cv2.drawContours(clone, [box], -1, (0, 255, 0), 2)
cv2.imshow("Rotated Bounding Boxes", clone)
cv2.waitKey(0)
clone = image.copy()

for c in cnts:
    # 计算最小外接圆
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(clone, (int(x), int(y)), int(radius), (0, 255, 0), 2)
    print(radius)
cv2.imshow("Min-Enclosing Circles", clone)
cv2.waitKey(0)
clone = image.copy()

for c in cnts:
    # 小于5个点拟合椭圆会报错
    if len(c) >= 3:
        # 拟合椭圆
        ellipse = cv2.fitEllipse(c)
        cv2.ellipse(clone, ellipse, (0, 255, 0), 2)

# show the output image
cv2.imshow("Ellipses", clone)
cv2.waitKey(0)
