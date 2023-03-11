import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 创建邻接矩阵和边权矩阵
adj_matrix = np.array([[0, 0, 1, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0],
                       [1 ,0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0, 1],
                       [0, 1, 0, 0, 0, 0]])
weight_matrix = np.array([[0, 0, 3, 0, 0, 0],
                       [7, 0, 1, 0, 0, 0],
                       [0, 0, 0, 8, 0, 0],
                       [12,0, 0, 0, 0, 0],
                       [0, 0, 0, 9, 0, 3],
                       [0, 1, 0, 0, 0, 0]])

# 创建空的有向赋权图
graph = nx.DiGraph()

# 向有向赋权图中添加边和边权
for i in range(adj_matrix.shape[0]):
    for j in range(adj_matrix.shape[1]):
        if adj_matrix[i][j] == 1:
            graph.add_weighted_edges_from([(i+1, j+1, weight_matrix[i][j])])

# 绘制图形
pos = nx.circular_layout(graph)  # 定义节点布局
nx.draw_networkx_nodes(graph, pos, node_color='white', node_size=500)
nx.draw_networkx_edges(graph, pos)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
nx.draw_networkx_labels(graph, pos)
plt.axis('off')
plt.show()
