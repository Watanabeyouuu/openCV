import numpy as np
import cv2
import imutils

image = cv2.imread("images/more_shapes_example.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)[1]
# thresh = cv2.adaptiveThreshold(blurred, 255,
#                                cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)

cv2.imshow("Original", image)
cv2.imshow("Gray", gray)
cv2.imshow("Thresh", thresh)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
hullImage = np.zeros(gray.shape[:2], dtype="uint8")

for (i, c) in enumerate(cnts):
    area = cv2.contourArea(c)
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.putText(image, "{}".format(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (240, 0, 159), 2)
    # 计算aspect ratio
    aspectRatio = w / float(h)

    # 计算extent
    extent = area / float(w * h)

    # 计算solidity
    hull = cv2.convexHull(c)
    hullArea = cv2.contourArea(hull)
    solidity = area / float(hullArea)
    print(i + 1, aspectRatio, solidity, extent)
    cv2.drawContours(hullImage, [hull], -1, 255, -1)
    cv2.drawContours(image, [c], -1, (240, 0, 159), 3)
    shape = ""
    cv2.imshow("Marked", image)
cv2.waitKey(0)
