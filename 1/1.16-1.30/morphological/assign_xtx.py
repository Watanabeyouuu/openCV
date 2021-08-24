"""

练习 腐蚀、膨胀、开运算、闭运算、梯度、白帽（礼帽）、黑帽

"""
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# 加载图片并把图像转换为灰度图像
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Original", image)
# cv2.imshow("Original_gray", gray)
cv2.waitKey(0)


def erode():
    # 腐蚀
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    for i in range(0, 3):
        eroded = cv2.erode(gray.copy(), kernel, iterations=i + 1)
        cv2.imshow("Eroded {} times".format(i + 1), eroded)
        cv2.waitKey(0)


def dilate():
    # 膨胀
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    for i in range(0, 3):
        dilated = cv2.dilate(gray.copy(), kernel, iterations=i + 1)
        cv2.imshow("Dilated {} times".format(i + 1), dilated)
        cv2.waitKey(0)


kernelSizes = [(7, 7), (11, 11), (13, 13)]


def open():
    # 运算
    for kernelSize in kernelSizes:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)
        cv2.waitKey(0)


def close():
    # 闭运算
    for kernelSize in kernelSizes:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
        cv2.imshow("Closing: ({}, {})".format(kernelSize[0], kernelSize[1]), closing)
        cv2.waitKey(0)


def gradient():
    # 梯度
    for kernelSize in kernelSizes:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
        cv2.imshow("Gradient: ({}, {})".format(kernelSize[0], kernelSize[1]), gradient)
        cv2.waitKey(0)


def black():
    # 黑帽
    for kernelSize in kernelSizes:
        rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
        cv2.imshow('black [kernel {}]'.format(kernelSize), blackhat)
        cv2.waitKey(0)


def white():
    # 白帽
    for kernelSize in kernelSizes:
        rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
        tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)
        cv2.imshow('black [kernel {}]'.format(kernelSize), tophat)
        cv2.waitKey(0)


if __name__ == '__main__':
    # erode()
    # dilate()
    # open()
    # close()
    # gradient()
    black()
    white()
