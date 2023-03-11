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
    [0, 3, 8, float('inf')], 
    [float('inf'), 0, float('inf'), 1], 
    [float('inf'), 4, 0, 1], 
    [2, float('inf'), float('inf'), 0]
]

result = floyd(graph)
print(result)
