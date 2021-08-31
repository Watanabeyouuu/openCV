import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = [1, 2, 3, 4]
Y = [1, 5, 3, 4]
Z = [1, 2, 3, 5]
ax.plot_trisurf(X, Y, Z)
plt.show()
