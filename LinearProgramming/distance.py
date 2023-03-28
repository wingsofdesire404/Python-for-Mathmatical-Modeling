from scipy.spatial.distance import pdist, squareform

# 一组数据点的坐标
points1 = [[5, 1], [1.25, 1.25], [8.75, 0.75], [0.5, 4.75], [5.75, 5], [3, 6.5], [7.25, 7.75]]
points2 = [[2, 7], [1.25, 1.25], [8.75, 0.75], [0.5, 4.75], [5.75, 5], [3, 6.5], [7.25, 7.75]]

# 计算距离矩阵
distance_matrix = squareform(pdist(points2, metric='euclidean'))

print(distance_matrix)