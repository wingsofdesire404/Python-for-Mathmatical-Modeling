def graph_coloring(adj_matrix):
    n = len(adj_matrix)
    color = [-1] * n  # 初始化颜色数组，-1表示未着色

    # 对每个顶点进行着色
    for v in range(n):
        used = set(color[i] for i in range(n) if adj_matrix[v][i])  # 获取相邻顶点已经使用的颜色
        for c in range(n):  # 遍历所有颜色
            if c not in used:  # 如果该颜色未被使用
                color[v] = c  # 对该顶点着色
                break

    return color

adj_matrix = [[0, 1, 1, 1, 0],
              [1, 0, 1, 1, 1],
              [1, 1, 0, 1, 1],
              [1, 1, 1, 0, 0],
              [0, 1, 1, 0, 0]]

colors = graph_coloring(adj_matrix)

print("顶点颜色分别为：", colors)
