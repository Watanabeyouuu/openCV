import cv2
import imutils

# 加载图像
image = cv2.imread("images/4.jpg")
image = imutils.resize(image, width=800)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (15, 15), 0)
# gray = cv2.bilateralFilter(gray,41, 40, 41)
# edged = imutils.auto_canny(gray,sigma=0.9)
# edged = cv2.Canny(gray, 75, 200)
edged = cv2.Canny(gray, 30, 50)

cv2.imshow("Original", image)
cv2.imshow("Edge Map", edged)

# 找到轮廓，按面积大小排列
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = imutils.grab_contours(cnts)
# cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
# cnts = cnts[0]
clone = image.copy()
cv2.drawContours(clone, cnts, -1, (0, 255, 0), -1)
print("Found {} contours".format(len(cnts)))
# print(cnts)

# 显示结果
cv2.imshow("All Contours", clone)
cv2.waitKey(0)
for i, c in enumerate(cnts):

    peri = cv2.arcLength(c, True)
    c = cv2.convexHull(c)
    approx = cv2.approxPolyDP(c, 0.05 * peri, True)
    # cv2.waitKey(9999)
    #
    print("original: {}, approx: {}".format(len(c), len(approx)))

    # 如果可以压缩为4个点，就判断为四边形
    if len(approx) == 4:
        # 绘制轮廓
        print('4个')
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
        cv2.imshow('TEMP{}'.format(i), image)
        print('--------------------------------------------')
        break
# 显示结果
cv2.imshow("Output", image)
cv2.waitKey(0)
