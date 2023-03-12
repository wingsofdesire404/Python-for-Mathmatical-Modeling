import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# 定义数据
x = np.array([129, 140, 103.5, 88, 185.5, 195, 105, 157.5, 107.5, 77, 81, 162, 162, 117.5])
y = np.array([7.5, 141.5, 23, 147, 22.5, 137.5, 85.5, -6.5, -81, 3, 56.5, -66.5, 84, -33.5])
z = np.array([4, 8, 6, 8, 6, 8, 8, 9, 9, 8, 8, 9, 4, 9])

# 定义插值点
xi = np.linspace(77, 195, 100) # x_min = 77, x_max = 195
yi = np.linspace(-81, 147, 100) # y_min = -81, y_max = 147
xi, yi = np.meshgrid(xi, yi)

# 进行二维散点插值
zi = griddata((x, y), z, (xi, yi), method='linear')

# 绘制插值结果
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
ax.plot_surface(xi, yi, zi)
plt.show()
