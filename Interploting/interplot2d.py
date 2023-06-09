import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d
from mpl_toolkits.mplot3d import Axes3D

# 构造数据
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 2, 3, 4])
z = np.array([[1, 4, 9, 16, 25],
              [4, 5, 6, 7, 8],
              [9, 6, 3, 2, 1],
              [16, 7, 2, 1, 4],
              [25, 8, 1, 4, 9]])

# 定义插值函数
f = interp2d(x, y, z, kind='cubic')

# 定义插值点
x_new = np.linspace(0, 4, num=41)
y_new = np.linspace(0, 4, num=41)

# 进行插值
z_new = f(x_new, y_new)

# 绘制原始数据和插值结果
#fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
#axs[0].pcolormesh(x, y, z, cmap='cool')
#axs[0].set_title('Original Data')
#axs[1].pcolormesh(x_new, y_new, z_new, cmap='cool')
#axs[1].set_title('Interpolated Data')
#plt.show()

# 创建数据
#x = np.linspace(-1, 1, 100)
#y = np.linspace(-1, 1, 100)
#X, Y = np.meshgrid(x, y)
#Z = X**2 + Y**2

# 绘制三维图像
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_new, y_new, z_new)
plt.show()
