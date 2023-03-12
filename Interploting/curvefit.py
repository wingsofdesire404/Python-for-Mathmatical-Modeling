import numpy as np
from scipy.optimize import curve_fit

# 定义非线性模型
y = lambda x, a, b, c: a * x ** 2 + b * x + c

# 生成一些模拟数据
x0 = np.arrange(0, 1.1, 0.1)
y0 = np.array([])

# 使用curve_fit拟合模型参数
popt, pcov = curve_fit(y, x0, y0)

# 打印拟合参数
print("拟合参数:", popt)
