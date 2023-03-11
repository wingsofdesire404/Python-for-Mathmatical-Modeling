import sys

def prim(adj_matrix):
    num_vertices = len(adj_matrix)
    INF = sys.maxsize  # 无穷大

    # 初始化
    selected = [False] * num_vertices
    min_weight = [INF] * num_vertices
    min_weight[0] = 0
    parent = [-1] * num_vertices

    for _ in range(num_vertices):
        # 从未选择的节点中找到权重最小的节点
        u = -1
        for i in range(num_vertices):
            if not selected[i] and (u == -1 or min_weight[i] < min_weight[u]):
                u = i

        # 将该节点标记为已选择
        selected[u] = True

        # 更新与该节点相邻的节点的权重和父节点
        for v in range(num_vertices):
            if adj_matrix[u][v] != 0 and not selected[v] and adj_matrix[u][v] < min_weight[v]:
                min_weight[v] = adj_matrix[u][v]
                parent[v] = u

    # 构建最小生成树
    tree_weight = 0
    for i in range(1, num_vertices):
        tree_weight += adj_matrix[i][parent[i]]

    return tree_weight, parent

# 例子：构建一个带权无向图的邻接矩阵
#  0  1  2  3  4
#  ----------------
#  0|0  2  0  6  0
#  1|2  0  3  8  5
#  2|0  3  0  0  7
#  3|6  8  0  0  9
#  4|0  5  7  9  0
adj_matrix = [[0, 20, 0, 0, 15, 0],
              [20, 0, 20, 60, 25, 0],
              [0, 20, 0, 30, 18, 0],
              [0, 60, 30, 0, 35, 10],
              [15, 25, 18, 35, 0, 15],
              [0, 0, 0, 10, 15, 0]]

tree_weight, parent = prim(adj_matrix)

print(f"最小生成树权重为：{tree_weight}")
print("最小生成树的边为：")
for i in range(1, len(parent)):
    print(f"{parent[i]} - {i}")
