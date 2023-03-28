import numpy as np
from sklearn import preprocessing as pp
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
a = np.loadtxt("cluster1.txt")
b = pp.minmax_scale(a.T) # standerlise data
d = sch.distance.pdist(b, metric = 'euclidean') # to cal distance between 2 obj
# metric = 'euclidean', 'cityblock', 'minkowski', 'chebychev', 'mahalanobis'
dd = sch.distance.squareform(d) # transform to matrix form
z = sch.linkage(d, method = 'complete') # to cluster and show
# method = 'single', 'average', 'centroid', 'complete', 'ward'
# 最短距离， 无权平均距离， 重心距离， 最大距离， 离差平方和方法（ward方法）
print(z) # to cluster and show
s = [str(i+1) for i in range(7)]; 
plt.rc('font', size = 16)  
sch.dendrogram(z, labels = s) # draw clustring pic
plt.show() # draw clustering pic