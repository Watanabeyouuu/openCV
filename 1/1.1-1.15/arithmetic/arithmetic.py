import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
import imutils
import numpy as np

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
plt.figure('Original')
plt.imshow(imutils.opencv2matplotlib(image))

# numpy的uint加减法会在0-255之间循环，或者说求模，
# 而opencv的加减法只会在0-255之间截止，小于0都当做0，大于255，都当做255
print("max of 255: {}".format(str(cv2.add(np.uint8([200]), np.uint8([100])))))
print("min of 0: {}".format(str(cv2.subtract(np.uint8([50]), np.uint8([100])))))

print("wrap around: {}".format(str(np.uint8([200]) + np.uint8([100]))))
print("wrap around: {}".format(str(np.uint8([50]) - np.uint8([100]))))

M = np.ones(image.shape, dtype="uint8") * 75
added = cv2.add(image, M)
plt.figure('added')
plt.imshow(imutils.opencv2matplotlib(added))

M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
plt.figure('Subtracted')
plt.imshow(imutils.opencv2matplotlib(subtracted))

cv2.copyTo(image, image, M)
M[448:582, 764:1072] = [0, 0, 255]
alpha = 0.5
mixed = cv2.add((alpha * M).astype(np.uint8), ((1 - alpha) * image).astype(np.uint8))
plt.figure('mixed')
plt.imshow(imutils.opencv2matplotlib(mixed))
plt.show()
