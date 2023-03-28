import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as tsaplots
import statsmodels.api as sm
# draw timeseries graph
data = pd.read_csv('milk.csv', index_col='date', parse_dates=True) # index_col included in the src file
plt.plot(data)
plt.show()
# draw acf and pacf plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12,8))
tsaplots.plot_acf(data, ax=ax1)#, lags=20)
tsaplots.plot_pacf(data, ax=ax2, method = 'ywm')#, lags=20)
plt.show()
# 单位根检验
result = sm.tsa.stattools.adfuller(data)
print('ADF Statistic:', result[0])
print('p-value:', result[1])
print('Critical Values:', result[4])
