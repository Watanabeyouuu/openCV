# 加载需要的库
import argparse
import cv2

# python文件的参数
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# 加载图片，得到图片尺寸，显示图片
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
print('shape:', image.shape)
cv2.imshow("Original", image)

# 图片就是Numpy数组，左上角是 (0, 0)
(b, g, r) = image[162, 145]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

# 改变 (0, 0) 处像素值，改为红色
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
# print(image)
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

# 计算图像的中心，就是把长和宽除以2
(cX, cY) = (w // 2, h // 2)

# 因为图片是NumPy数组, 我们可以使用切片操作来得到图片的局部，得到左上角
tl = image[0:cY, 0:cX]
cv2.imshow("Top-Left Corner", tl)
print(image[162, 145])
# 我们同样的可以得到右上角，右下角，左下角，并且显示出来
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)

# 左上角重置为绿色
image[0:cY, 0:cX] = (0, 255, 0)

# 显示结果
cv2.imshow("Updated", image)
cv2.waitKey(0)
