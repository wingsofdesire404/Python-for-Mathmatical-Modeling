def max_flow(graph, source, sink):
    # 计算残量图
    def residual_graph(graph, flow):
        res_graph = [[0] * len(graph) for _ in range(len(graph))]
        for i in range(len(graph)):
            for j in range(len(graph)):
                res_graph[i][j] = graph[i][j] - flow[i][j]
        return res_graph

    n = len(graph)  # 获取顶点数
    flow = [[0] * n for _ in range(n)]  # 初始化流量矩阵

    while True:
        res_graph = residual_graph(graph, flow)  # 计算残量图
        parent = [-1] * n  # 存储增广路径
        parent[source] = source  # 源点的父节点为自身

        # 使用BFS查找增广路径
        queue = [source]
        while queue:
            u = queue.pop(0)
            for v in range(n):
                if parent[v] == -1 and res_graph[u][v] > 0:
                    parent[v] = u
                    queue.append(v)
                    if v == sink:  # 找到汇点，结束BFS
                        break

        if parent[sink] == -1:  # 没有增广路径，结束循环
            break

        # 查找增广路径上的最小流量
        path_flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, res_graph[u][v])
            v = u

        # 更新流量矩阵
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u

    # 计算总流量
    max_flow = 0
    for i in range(n):
        max_flow += flow[source][i]

    return max_flow

graph = [[0, 4, 5, 0, 0, 0],
         [0, 0, 0, 3, 3, 0],
         [0, 0, 0, 6, 2, 0],
         [0, 0, 0, 0, 0, 4],
         [0, 0, 0, 0, 0, 6],
         [0, 0, 0, 0, 0, 0]]
source = 0
sink = 5
max_flow_value = max_flow(graph, source, sink)
print(f"The maximum flow of the given graph is: {max_flow_value}")
