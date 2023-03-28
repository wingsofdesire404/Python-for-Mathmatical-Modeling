import pandas as pd
import numpy as np
import statsmodels.api as sm

# 加载数据
data = pd.read_csv('mile.csv', index_col='date', parse_dates=True)

# 定义ARIMA模型
arima_model = sm.tsa.ARIMA(data, order=(2, 0, 0)) # p, d, q = 1, 1, 1; d表示差分阶数

# 拟合模型并估计参数
arima_result = arima_model.fit()

# 打印估计参数结果
#print(arima_result.summary())

# 预测未来5个时间步
forecast_result = arima_result.forecast(steps=5)

# 打印预测结果
print(forecast_result)