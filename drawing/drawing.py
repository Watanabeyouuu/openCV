# 使用方法
# python drawing.py

# 加载需要的python包
import numpy as np
import cv2
import imutils
import matplotlib.pyplot as plt

canvas = np.zeros((200, 300, 3), dtype="uint8")
cv2.rectangle(canvas, (10, 10), (60, 60), (255, 0, 0), -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 初始化我们的画布
canvas = np.zeros((300, 300, 3), dtype="uint8")
   
# 画一条从左上角到右下角的绿线
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 画一条3像素宽的从右上角到左下角的红线
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 绘制一个50*50的绿色矩形
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 画另一个5像素宽的红色矩形
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 绘制一个蓝色的填充矩形
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 绘制一系列同心圆
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 绘制25个随机圆形，位置，大小和颜色
for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))

    # draw our random circle
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 加载JamesBlunt的图片
image = cv2.imread("JamesBlunt_1.jpg")
plt.imshow(imutils.opencv2matplotlib(image))
plt.show()
# 在头部区域画一个椭圆
cv2.ellipse(image, (903, 129), (90, 60), 90, 0, 360, [0, 255, 0], 3)
plt.imshow(imutils.opencv2matplotlib(image))
points = [[100, 100], [100, 200], [200, 200], [50, 90], [67, 12], [89, 34]]
points = np.asarray(points)
cv2.polylines(image, pts=[points], isClosed=True, color=(0, 0, 255), thickness=3)
plt.show()

# 用opencv显示
cv2.imshow("Ouput", image)
cv2.waitKey(0)
