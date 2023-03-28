import pandas as pd
import numpy as np
import statsmodels.api as sm

# 加载数据
data = pd.read_csv('mile.csv', index_col='date', parse_dates=True)

# 定义AR模型
ar_model = sm.tsa.AutoReg(data, lags=2)

# 拟合模型并估计参数
ar_result = ar_model.fit()

# 打印估计参数结果
print(ar_result.params)

