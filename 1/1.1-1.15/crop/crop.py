import cv2
import matplotlib.pyplot as plt
import imutils


image = cv2.imread("James_Blunt2.jpg")
plt.imshow(imutils.opencv2matplotlib(image))
plt.show()

# 把上尉诗人的脸部截取出来
face = image[155:639, 725:1086]
cv2.imshow("Face", face)
cv2.waitKey(0)

# 把吉他的部分截取出来
body = image[1467:2125, 0:1675]
cv2.imshow("Body", body)
cv2.waitKey(0)

