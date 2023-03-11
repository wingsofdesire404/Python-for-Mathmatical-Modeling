import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 创建邻接矩阵
adj_matrix = np.array([[0, 1, 1, 1, 0, 0],
                       [1, 0, 1, 0, 0, 1],
                       [1, 1, 0, 1, 0, 0],
                       [1, 0, 1, 0, 1, 0],
                       [0, 0, 0, 1, 0, 1],
                       [0, 1, 0, 0, 1, 0]])

# 创建空的无向图
graph = nx.Graph()

# 向无向图中添加边
for i in range(adj_matrix.shape[0]):
    for j in range(i, adj_matrix.shape[1]):
        if adj_matrix[i][j] == 1:
            graph.add_edge(i+1, j+1)

# 绘制图形
nx.draw(graph, with_labels=True)
plt.show()


