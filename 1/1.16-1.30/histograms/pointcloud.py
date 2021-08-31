import cv2
from matplotlib import pyplot as plt

image = cv2.imread('beach.png')
r = image[:, :, 2]
g = image[:, :, 2]
b = image[:, :, 2]

rf = []
for n in range(0, len(r)):
    for i in r[n]:
        rf.append(i)

gf = []
for n in range(0, len(g)):
    for i in g[n]:
        gf.append(i)

bf = []
for n in range(0, len(b)):
    for i in b[n]:
        bf.append(i)

plt.figure()
ax = plt.subplot(111, projection='3d')
ax.scatter(rf, gf, bf, color='b')
plt.show()

plt.figure()
plt.imshow(image)
plt.show()
