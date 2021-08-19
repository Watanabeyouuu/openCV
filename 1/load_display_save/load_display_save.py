# 使用方法
# python load_display_save.py --image James_Blunt_2.jpg

# import the necessary packages
import argparse
import cv2
import imutils
import matplotlib.pyplot as plt

# 构建 argument parser 并设置参数
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# 加载一幅图像并显示它的基本信息
image = cv2.imread(args["image"])
print("width: {w} pixels".format(w=image.shape[1]))
print("height: {h}  pixels".format(h=image.shape[0]))
print("channels: {c}".format(c=image.shape[2]))
print("all: {all}".format(all=image.shape))

# 显示一幅图像直到你按下一个按键（注意在中文输入法时，你按下按键不一定有反应，因为在你输入
# 汉字的时候，并不是马上就有输出）
cv2.imshow("Image", image)
cv2.waitKey(0)
# b, g, r
# plt可以更方便的显示图像，配合v使用非常方便
plt.imshow(imutils.opencv2matplotlib(image))
# plt.show()

# 保存图像-- OpenCV 可以将你的图片保存成任何你想要的格式
cv2.imwrite("newimage99.bmp", image)
