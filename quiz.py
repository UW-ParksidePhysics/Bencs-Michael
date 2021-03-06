from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

points_x = np.linspace(-20, 20, 7)
points_y = np.linspace(-20, 20, 7)
points_z = np.linspace(-20, 20, 7)
x,y,z = np.meshgrid(points_x, points_y, points_z)

u = -1*y
v = x
w = 0

ax.quiver(x, y, z, u, v, w, linewidths=2, normalize=True)

plt.show()