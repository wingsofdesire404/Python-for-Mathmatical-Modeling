import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox

# 读取数据
data = pd.read_csv('chem.csv', index_col='date', parse_dates=True)

# 对数据进行平稳化处理
diff_data = data.diff().dropna()

# 进行Ljung-Box检验
lbvalue, pvalue = sm.stats.acorr_ljungbox(diff_data, lags=20)

# 输出结果
print("Ljung-Box统计量: ", lbvalue)
print("p值: ", pvalue)


