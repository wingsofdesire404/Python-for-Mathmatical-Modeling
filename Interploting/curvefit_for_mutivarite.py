import numpy as np
from scipy.optimize import curve_fit

# 定义非线性模型
def pfun(t, a, b, c): # like z = a * x + b * y + c
    return a * t[0] + b * t[1] + c

# 生成一些模拟数据
x0 = np.array([12.0, 13.0, 15.0])
y0 = np.array([11.0, 12.0, 13.0])
z0 = np.array([13.0, 15.0, 16.0])
xy0 = np.vstack((x0, y0))
# 使用curve_fit拟合模型参数
popt, pcov = curve_fit(pfun, xy0, z0)

# 打印拟合参数
print("拟合参数:", popt)