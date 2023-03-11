import sys

def dijkstra(graph, start):
    """
    Dijkstra算法实现
    :param graph: 图的邻接矩阵
    :param start: 起点
    :return: 从起点到其他节点的最短距离和路径
    """
    num_vertices = len(graph)  # 图中节点的数量
    distances = [sys.maxsize] * num_vertices  # 到各节点的最短距离
    distances[start] = 0  # 起点到自身的距离为0
    visited = [False] * num_vertices  # 记录每个节点是否已经被访问
    parents = [-1] * num_vertices  # 记录每个节点的前驱节点
    for _ in range(num_vertices):
        # 找到未访问过的距离起点最近的节点
        current_vertex = get_min_distance_vertex(distances, visited)
        visited[current_vertex] = True  # 标记为已访问
        # 更新其邻居节点的最短距离
        for neighbor in range(num_vertices):
            if graph[current_vertex][neighbor] != 0 and not visited[neighbor]:
                new_distance = distances[current_vertex] + graph[current_vertex][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    parents[neighbor] = current_vertex
    # 计算每个节点到起点的最短路径
    shortest_paths = get_shortest_paths(start, parents)
    return distances, shortest_paths

def get_min_distance_vertex(distances, visited):
    """
    找到未访问过的距离起点最近的节点
    """
    min_distance = sys.maxsize
    min_vertex = -1
    for vertex in range(len(distances)):
        if not visited[vertex] and distances[vertex] < min_distance:
            min_distance = distances[vertex]
            min_vertex = vertex
    return min_vertex

def get_shortest_paths(start, parents):
    """
    根据每个节点的前驱节点计算出每个节点到起点的最短路径
    """
    num_vertices = len(parents)
    shortest_paths = [[] for _ in range(num_vertices)]
    for vertex in range(num_vertices):
        path = []
        current_vertex = vertex
        while current_vertex != start:
            path.insert(0, current_vertex)
            current_vertex = parents[current_vertex]
        path.insert(0, start)
        shortest_paths[vertex] = path
    return shortest_paths

graph = [
    [0, 2, 4, 0, 0, 0, 0],
    [0, 0, 0, 3, 3, 1, 0],
    [0, 0, 0, 2, 3, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0]
]
distances, shortest_paths = dijkstra(graph, 0)
print("距离：", distances) # 起点到各顶点的最短路径长度
print("最短路径：", shortest_paths) # 起点到各顶点的最短路径轨迹
