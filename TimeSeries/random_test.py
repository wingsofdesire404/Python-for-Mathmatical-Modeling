import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

# 读取数据
data = pd.read_csv('chem.csv', index_col='date', parse_dates=True)

# 对数据进行平稳化处理
diff_data = data.diff().dropna()

# 进行6阶ADF检验
result_6 = adfuller(data, maxlag=6)

# 打印结果
# p < 0.05 为非随机
print('ADF Statistic (6 lags): %f' % result_6[0])
print('p-value (6 lags): %f' % result_6[1])
print('Critical Values (6 lags):')
for key, value in result_6[4].items():
    print('\t%s: %.3f' % (key, value))

# 进行12阶ADF检验
result_12 = adfuller(data, maxlag=12)

# 打印结果
print('ADF Statistic (12 lags): %f' % result_12[0])
print('p-value (12 lags): %f' % result_12[1])
print('Critical Values (12 lags):')
for key, value in result_12[4].items():
    print('\t%s: %.3f' % (key, value))

