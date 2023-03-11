def lagrange_interpolation(x_values, y_values, x):
    """
    实现拉格朗日插值的函数。

    参数:
    x_values -- 数据点的x坐标，数组形式
    y_values -- 数据点的y坐标，数组形式
    x -- 插值点的x坐标

    返回:
    y -- 插值点的y坐标
    """

    n = len(x_values)
    y = 0
    for i in range(n):
        xi, yi = x_values[i], y_values[i]
        # 计算插值基函数
        basis = 1
        for j in range(n):
            if j != i:
                xj = x_values[j]
                basis *= (x - xj) / (xi - xj)
        # 计算插值点的y坐标
        y += yi * basis
    return y

x_values = [0, 1, 2]
y_values = [1, 3, 5]
x = 1.5 # insert where x = 1.5
y = lagrange_interpolation(x_values, y_values, x)
print(y)  # 输出: 4.0
