import numpy as np
import cv2
import imutils
import matplotlib.pyplot as plt

image = cv2.imread("JamesBlunt_1.jpg")
plt.imshow(imutils.opencv2matplotlib(image))
plt.show()
#
cv2.ellipse(image, (903, 129), (90, 60), 90, 0, 360, [0, 255, 0], 3)
points = [[100, 100], [100, 200], [200, 200], [34, 56]]
points = np.asarray(points)
cv2.polylines(image, pts=[points], isClosed=True, color=(0, 0, 255), thickness=3)
plt.imshow(imutils.opencv2matplotlib(image))
plt.show()
