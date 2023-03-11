import numpy as np

def tsp_greedy(city_distances):
    """
    使用贪心算法求解TSP问题
    :param city_distances: 城市距离矩阵
    :return: 最短回路长度和路径
    """
    n = city_distances.shape[0]  # 城市数量
    visited = [False] * n  # 是否访问过
    visited[0] = True  # 从第0个城市开始访问
    path = [0]  # 路径
    length = 0  # 总路程
    while len(path) < n:
        last = path[-1]  # 上一个城市
        min_dist = np.inf  # 最小距离
        min_index = -1  # 最小距离城市的索引
        for i in range(n):
            if not visited[i] and city_distances[last][i] < min_dist:
                min_dist = city_distances[last][i]
                min_index = i
        visited[min_index] = True
        path.append(min_index)
        length += min_dist
    length += city_distances[path[-1]][0]  # 加上回到第一个城市的距离
    path.append(0)
    return length, path

city_distances = np.array([
    [0, 10, 20, 30],
    [10, 0, 15, 25],
    [20, 15, 0, 35],
    [30, 25, 35, 0]
])

length, path = tsp_greedy(city_distances)
print(length, path)