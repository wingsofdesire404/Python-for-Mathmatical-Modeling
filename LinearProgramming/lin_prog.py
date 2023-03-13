import numpy as np
from scipy.optimize import linprog
c = np.array([-3100, -3800, -3500, -2850, -3100, -3800, -3500, -2850, -3100, -3800, -3500, -2850])
A_ub = np.array([[18, 15, 23, 12, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 18, 15, 23, 12, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 18, 15, 23, 12],
                 [480, 650, 580, 390, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 480, 650, 580, 390, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 480, 650, 580, 390]
                 ])
b_ub = np.array([10, 16, 8, 1800, 8700, 5300])
# A_eq = np.array([[-2.0, 0.0, 1.0], [0.0, 0.0, 0.0]])
# b_eq = np.array([1.0, 0.0])
x1_bound = (0.0, np.inf)
x2_bound = (0.0, np.inf)
x3_bound = (0.0, np.inf)
x4_bound = x5_bound = x6_bound = x7_bound= x8_bound = x9_bound = x10_bound = x11_bound = x12_bound= (0.0, np.inf)
bounds = [x1_bound, x2_bound, x3_bound, x4_bound, x5_bound, x6_bound, x7_bound, x8_bound, x9_bound, x10_bound, x11_bound, x12_bound]
result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq= None, b_eq= None, bounds=bounds)
print(result.fun)