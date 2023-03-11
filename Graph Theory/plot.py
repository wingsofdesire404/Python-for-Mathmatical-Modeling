import networkx as nx
import matplotlib.pyplot as plt

# 创建一个空的无向图
G = nx.Graph()

# 添加节点
G.add_node(1)
G.add_node(2)
G.add_node(3)

# 添加边
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# 绘制图形
pos = nx.spring_layout(G)  # 为节点确定一个位置
nx.draw(G, pos)  # 绘制图形
plt.show()  # 显示图形
