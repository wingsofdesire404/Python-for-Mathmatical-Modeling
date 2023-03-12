import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import quad

# 定义输入数据
x = np.array([0.15, 0.16, 0.17, 0.18])
y = np.array([3.5, 1.5, 2.5, 2.8])

# 创建三次样条插值函数
cs = CubicSpline(x, y)

# 定义插值点
x_interp = np.linspace(0.15, 0.18, num=101, endpoint=True)

# 进行插值
y_interp = cs(x_interp)

# 绘制插值结果
import matplotlib.pyplot as plt
plt.plot(x, y, 'o', label='data')
plt.plot(x_interp, y_interp, '-', label='cubic spline')
plt.legend()
plt.show()


# 定义积分下限和积分上限
a = 0.15
b = 0.18

# 计算积分面积
integral, error = quad(cs, a, b)

# 输出积分面积
print('The integral area is:', integral)