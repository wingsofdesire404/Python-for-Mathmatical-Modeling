import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as tsaplots
import statsmodels.api as sm

# 读取时间序列数据
ts = pd.read_csv('texture.csv', index_col='date', parse_dates=True)

# 对时间序列进行一阶差分
# diff = ts.diff().dropna()

# 1阶12步差分
diff = ts.diff(periods=6).dropna()

# 对时间序列进行二阶差分
diff2 = ts.diff().diff().dropna()

# draw timeseries plot
plt.plot(diff)
plt.show()

# draw acf and pacf plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12,8))
tsaplots.plot_acf(diff, ax=ax1)#, lags=20)
tsaplots.plot_pacf(diff, ax=ax2, method = 'ywm')#, lags=20)
plt.show()