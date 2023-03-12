import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import quad

# 定义输入数据
x = np.array([7.0, 10.5, 13.0, 17.5, 34.0, 40.5, 44.5, 48.0, 56.0,
              61.0,68.5, 76.5, 80.5, 91.0, 96.0, 101.0, 104.0, 106.5,
              111.5, 118.0, 123.5, 136.5, 142.0, 146.0, 150.0, 157.0, 158.0])
y1 = np.array([44, 45, 47, 50, 50, 38, 30, 30, 34,
               36, 34, 41, 45, 46, 43, 37, 33, 28,
               32, 65, 55, 54, 52, 50, 66, 66, 68])
y2 = np.array([44, 59, 70, 72, 93, 100, 110, 110, 110,
               117, 118, 116, 118, 118, 121, 124, 121, 121,
               121, 122, 116, 83, 81, 82, 86, 85, 68])
# 创建三次样条插值函数
cs1 = CubicSpline(x, y1)
cs2 = CubicSpline(x, y2)
# 定义插值点
x_interp = np.linspace(7.0, 158.0, num=101, endpoint=True)

# 进行插值
y_interp1 = cs1(x_interp)
y_interp2 = cs2(x_interp)

# 绘制插值结果
import matplotlib.pyplot as plt
plt.plot(x, y1, 'o', label='upper data')
plt.plot(x_interp, y_interp1, '-', label='upper bound')
plt.plot(x, y2, 'o', label='lower data')
plt.plot(x_interp, y_interp2, '-', label='lower bound')
plt.legend()
plt.show()

# 定义积分下限和积分上限
a = 7.0
b = 158.0

# 计算积分面积
integral1, error1 = quad(cs1, a, b, limit = 100)
integral2, error2 = quad(cs2, a, b, limit = 100)

# 输出积分面积
print('The integral area is:', (integral2 - integral1) * (18 / 40))