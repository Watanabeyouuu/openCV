from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

#
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 构建一个灰度直方图
hist = cv2.calcHist([image], [0], None, [256], [0, 255])

# matplotlib 显示灰度图像的两种方法
# plt.figure()
# plt.axis("off")
# # plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))
# plt.imshow(image, cmap='gray')
# # 绘制histogram
# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(hist)
# plt.xlim([0, 255])
plt.plot(hist, color='gray')
plt.xlim([0, 256])
plt.show()
# 直方图归一化
hist /= hist.sum()

# 绘制归一化的直方图
plt.figure()
plt.title("Grayscale Histogram (Normalized)")
plt.xlabel("Bins")
plt.ylabel("% of Pixels")
plt.plot(hist)
plt.xlim([0, 255])
plt.show()
