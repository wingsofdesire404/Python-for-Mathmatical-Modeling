import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 读取数据
data = pd.read_csv('elbow.csv')
X = data.iloc[:, [0, 1]].values # 选取所有行和第1，2列

# 计算离差平方和
wcss = []
for i in range(1, 11): # 第2行到第12行，即忽略标题行
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# 绘制离差平方和与k值之间的关系图
plt.plot(range(1, 11), wcss) # 第2行到第12行，即忽略标题行
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# 使用k均值聚类将数据集分为3类
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(X)

# 绘制聚类结果
k = 3
# 可视化聚类结果
colors = ['red', 'blue', 'green', 'black', 'cyan', 'magenta'] # 适当拓展颜色以防k过大而用光颜色集
for i in range(k):
    plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s = 100, c = colors[i], label = 'Cluster {}'.format(i+1))
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

