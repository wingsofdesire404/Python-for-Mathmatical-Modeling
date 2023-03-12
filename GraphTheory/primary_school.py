import numpy  as np
def floyd(graph):
    """
    :param graph: 邻接矩阵表示的图
    :return: 所有节点之间的最短路径矩阵
    """
    n = len(graph)
    dist = graph.copy()

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

graph = [
    [0, 2, 7, float('inf'), float('inf'), float('inf')],
    [2, 0, 4, 6, 8, float('inf')],
    [7, 4, 0, 1, 3, float('inf')],
    [float('inf'), 6, 1, 0, 1, 6],
    [float('inf'), 8, 3, 1, 0, 3],
    [float('inf'), float('inf'), float('inf'), 6, 3, 0]
]

result = floyd(graph)
r = np.array(result)
v = np.array([[50],
             [40],
             [60],
             [20],
             [70],
             [90]])
print(np.dot(r, v))