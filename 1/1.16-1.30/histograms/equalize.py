
import argparse
import cv2
import matplotlib.pyplot as plt
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# 加载图像，转化为灰度
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 应用直方图均衡化，拉伸我们的直方图
eq = cv2.equalizeHist(image)

# s对比直方图均衡化前后的差异
cv2.imshow("Original", image)
cv2.imshow("Histogram Equalization", eq)
cv2.waitKey(0)
hist2 = cv2.calcHist([image], [0], None, [256], [0, 256])

hist = cv2.calcHist([eq], [0], None, [256], [0, 256])
a = eq[272,146]
print(a)
acc = np.add.accumulate(hist)
# matplotlib 显示灰度图像的两种方法
plt.figure()
plt.axis("off")
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))
plt.imshow(eq,cmap='gray')
# 绘制histogram
plt.figure()
plt.title("Equalized Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])

plt.figure()
plt.title(" Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist2)
plt.xlim([0, 256])

plt.figure()
plt.title("Acc Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(acc)
plt.xlim([0, 256])
plt.show()