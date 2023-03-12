import numpy as np
from scipy.interpolate import CubicSpline

# 定义输入数据
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])

# 创建三次样条插值函数
cs = CubicSpline(x, y)

# 定义插值点
x_interp = np.linspace(0, 5, num=101, endpoint=True)

# 进行插值
y_interp = cs(x_interp)

# 绘制插值结果
import matplotlib.pyplot as plt
plt.plot(x, y, 'o', label='data')
plt.plot(x_interp, y_interp, '-', label='cubic spline')
plt.legend()
plt.show()
