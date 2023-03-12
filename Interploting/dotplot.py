import matplotlib.pyplot as plt
import numpy as np

# 创建一个包含-2*pi到2*pi之间的等间距点的数组
x = np.array([i for i in range(0, 8)])

# 计算sin(x)的值
y = np.array([27.0, 26.8, 26.5, 26.3, 26.1, 25.7, 25.3, 24.8])

# 创建一个点阵图
plt.scatter(x, y, s=5)

# 显示图形
plt.show()
