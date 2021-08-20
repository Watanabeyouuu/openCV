import argparse
import imutils
import cv2
import matplotlib.pyplot as plt
from logging import FileHandler
from vlogging import VisualRecord
import logging

logger = logging.getLogger("visual_logging")
fh = FileHandler("resize.html", mode="w")
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
resized = imutils.resize(image, width=image.shape[1] * 2, inter=cv2.INTER_NEAREST)
a = resized[59, 56]
print(a)
# 考虑到长宽比，我们计算缩放比例
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

# 缩放图像
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

# 确定高度的图片缩放
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)
plt.imshow(imutils.opencv2matplotlib(image))
plt.show()
# 缩放图像
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)

# 使用imutuls进行缩放
resized = imutils.resize(image, width=image.shape[1] * 2, inter=cv2.INTER_NEAREST)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)

# 使用不同的方法进行缩放
methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_AREA", cv2.INTER_AREA),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
    ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]

# 使用各种方法进行缩放
for (name, method) in methods:
    # 放大三倍，更容易观察到缩放方法的不同
    resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
    # 演示使用Visual-logger
    logger.debug(VisualRecord((name), [resized], fmt="png"))
    cv2.imshow("Method: {}".format(name), resized)
    cv2.waitKey(0)
