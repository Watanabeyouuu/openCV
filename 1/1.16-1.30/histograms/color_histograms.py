from matplotlib import pyplot as plt
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
a = image[:, :, 0]
a.shape

chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chans, colors):
    # create a histogram for the current channel and plot it
    hist = cv2.calcHist([chan], [0], None, [256], [0, 255])
    plt.plot(hist, color=color)
    plt.xlim([0, 255])
plt.show()
# 绘制2D的直方图，32*32
fig = plt.figure()

# 绘制绿蓝直方图
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32],
                    [0, 255, 0, 255])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

# 绘制绿红直方图
ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32],
                    [0, 255, 0, 255])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

# 绘制蓝红直方图
ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32],
                    [0, 255, 0, 255])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

# 查看2D直方图的尺寸
print("2D histogram shape: {}, with {} values".format(
    hist.shape, hist.flatten().shape[0]))

hist = cv2.calcHist([image], [0, 1, 2],
                    None, [256, 256, 256], [0, 255, 0, 255, 0, 255])
print("3D histogram shape: {}, with {} values".format(
    hist.shape, hist.flatten().shape[0]))

plt.figure()
plt.axis("off")
plt.imshow(imutils.opencv2matplotlib(image))

plt.show()
