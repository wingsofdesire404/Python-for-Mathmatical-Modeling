import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# input data
x = np.array([0, 3, 5, 7, 9, 11, 12, 13, 14, 15])
y = np.array([0, 1.2, 1.7, 2.0, 2.1, 2.0, 1.8, 1.2, 1.0, 1.6])

# interplot fuction
f = interpolate.interp1d(x, y)

# cordinate to be interplot
xnew = np.arange(0, 15, 0.1)

# interplot
ynew = f(xnew)   # use interpolation function returned by `interp1d`
plt.plot(x, y, 'o', xnew, ynew, '-')
plt.show()