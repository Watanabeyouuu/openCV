from skimage import measure
import numpy as np
import cv2

plate = cv2.imread("license_plate.png")

V = cv2.split(cv2.cvtColor(plate, cv2.COLOR_BGR2HSV))[2]
thresh = cv2.adaptiveThreshold(V, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY_INV, 17, 3)

cv2.imshow("License Plate", plate)
cv2.imshow("Thresh", thresh)

# 计算连通区域，8连通
labels = measure.label(thresh, background=0, connectivity=2)  # 1代表4邻接，2代表8邻接
mask = np.zeros(thresh.shape, dtype="uint8")
print("[INFO] found {} blobs".format(len(np.unique(labels))))

# 遍历所有连通域
for (i, label) in enumerate(np.unique(labels)):
    # 如果是背景，忽略
    if label == 0:
        print("[INFO] label: 0 (background)")
        continue

    # 展示当前的连通区域
    print("[INFO] label: {} (foreground)".format(i))
    labelMask = np.zeros(thresh.shape, dtype="uint8")
    labelMask[labels == label] = 255
    numPixels = cv2.countNonZero(labelMask)  # 返回非0的像素个数，由于0是背景，非0为前景，即求面积。
    # 判断区域是否满足面积要求
    if numPixels > 300 and numPixels < 1500:
        mask = cv2.add(mask, labelMask)

    # 显示label
    cv2.imshow("Label", labelMask)
    cv2.waitKey(0)

# 全部满足要求的连通域
cv2.imshow("Large Blobs", mask)
cv2.waitKey(0)
