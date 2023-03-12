import numpy as np
import matplotlib.pyplot as plt

# 生成一些模拟数据
x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.array([27.0, 26.8, 26.5, 26.3, 26.1, 25.7, 25.3, 24.8])

# 使用polyfit拟合多项式系数
coeffs = np.polyfit(x, y, 2) # 多项式阶数为2, y(x) = ax^2 + bx^2 + c

# 打印拟合多项式系数
print("拟合多项式系数:", coeffs)

# 绘制拟合曲线
x_fit = np.linspace(0, 7, 100)
y_fit = np.polyval(coeffs, x_fit)
plt.plot(x, y, 'o', label='data')
plt.plot(x_fit, y_fit, label='fit')
plt.legend()
plt.show()
