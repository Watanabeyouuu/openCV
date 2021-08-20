import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
plt.imshow(imutils.opencv2matplotlib(image))
plt.show()

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (0, 80), (1593, 2131), 255, -1)
plt.imshow(mask, cmap='gray')
plt.show()

# 显示身体部分
masked = cv2.bitwise_and(image, image, mask=mask)
# cv2.imshow("Mask Applied to Image", masked)
plt.imshow(imutils.opencv2matplotlib(masked))
plt.show()
cv2.waitKey(0)

# 显示脸
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (941, 411), 200, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
# cv2.imshow("Mask", mask)
# cv2.imshow("Mask Applied to Image", masked)
# plt.imshow(mask, cmap='gray')
plt.imshow(imutils.opencv2matplotlib(mask))
plt.show()

# plt.imshow(mask, cmap='gray')
plt.imshow(imutils.opencv2matplotlib(masked))
plt.show()
