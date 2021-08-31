import numpy as np
import cv2
import imutils

image = cv2.imread("images/tetris_blocks.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

cv2.imshow("Original", image)
cv2.imshow("Thresh", thresh)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
hullImage = np.zeros(gray.shape[:2], dtype="uint8")

for (i, c) in enumerate(cnts):

    area = cv2.contourArea(c)
    (x, y, w, h) = cv2.boundingRect(c)

    # 计算aspect ratio
    aspectRatio = w / float(h)

    # 计算extent
    extent = area / float(w * h)

    # 计算solidity
    hull = cv2.convexHull(c)
    hullArea = cv2.contourArea(hull)
    solidity = area / float(hullArea)

    cv2.drawContours(hullImage, [hull], -1, 255, -1)
    cv2.drawContours(image, [c], -1, (240, 0, 159), 3)
    shape = ""

    # 如果aspect ratio接近1，那就是一个方块
    if aspectRatio >= 0.98 and aspectRatio <= 1.02:
        shape = "SQUARE"

    # 如果宽是高的三倍以上，那就是一个长方形
    elif aspectRatio >= 3.0:
        shape = "RECTANGLE"

    # 如果extent足够小就是L-piece
    elif extent < 0.65:
        shape = "L-PIECE"

    # 如果solidity足够大, 那就是Z-piece
    elif solidity > 0.80:
        shape = "Z-PIECE"

    cv2.putText(image, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (240, 0, 159), 2)

    print("Contour #{} -- aspect_ratio={:.2f}, extent={:.2f}, solidity={:.2f}"
          .format(i + 1, aspectRatio, extent, solidity))

    cv2.imshow("Convex Hull", hullImage)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
