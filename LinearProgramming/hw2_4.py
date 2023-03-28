# 导入PuLP库
from pulp import *

# 创建LP问题实例，并指定最大化目标
lp_prob = LpProblem("LP Problem", LpMaximize)

# 创建变量
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x4 = LpVariable("x4", lowBound=0)
y1 = LpVariable("y1", lowBound=0)
z1 = LpVariable("z1", lowBound=0)
y2 = LpVariable("y2", lowBound=0)
z2 = LpVariable("z2", lowBound=0)

# 添加目标函数
lp_prob += (9 - 6*x1 - 16*x2 - 15*x4)*y1 + (15 - 6*x1 - 16*x2 - 15*x4)*y2 + (9 - 10)*z1 + (15 - 10)*z2

# 添加约束
lp_prob += x4*(y1 + y2) <= 50
lp_prob += y1 + z1 <= 100
lp_prob += y2 + z2 <= 200
lp_prob += (3*x1 + x2 + x4)*y1 + 2*z1 <= 2.5*(y1 + z1)
lp_prob += (3*x1 + x2 + x4 - 1.5)*y2 + 0.5*z2 <= 0
lp_prob += x1 + x2 + x4 == 1

# 解决问题
status = lp_prob.solve()

# 打印结果
print("Status:", LpStatus[status])
print("Optimal Solution:")
print("x1 =", value(x1))
print("x2 =", value(x2))
print("x4 =", value(x4))
print("y1 =", value(y1))
print("z1 =", value(z1))
print("y2 =", value(y2))
print("z2 =", value(z2))
print("Optimal Objective Value:", value(lp_prob.objective))
