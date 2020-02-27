#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(-1, 1, 1000)

x = 1-(t**2)
y = 2*t
z = 1+(t**2)

x_2d = x/z
y_2d = y/z
z_2d = np.ones_like(y_2d)

x_3d = x
y_3d = y
z_3d = z

x_plot = np.concatenate([x_2d, x_3d])
y_plot = np.concatenate([y_2d, y_3d])
z_plot = np.concatenate([z_2d, z_3d])

fig = plt.figure(); ax = fig.add_subplot(1, 1, 1, projection='3d');
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.scatter(x_plot, y_plot, z_plot, c='b', marker='o')

plt.show(block=True)
