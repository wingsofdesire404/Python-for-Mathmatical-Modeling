import numpy as np
from sklearn import preprocessing as pp
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
a = np.loadtxt("Pdata11_11.txt")
b = pp.minmax_scale(a.T) # standerlise data
d = sch.distance.pdist(b) # to cal distance between 2 obj
dd = sch.distance.squareform(d) # transform to matrix form
z = sch.linkage(d) # to cluster and show
print(z) # to cluster and show
s = [str(i+1) for i in range(7)]; 
plt.rc('font', size = 16)  
sch.dendrogram(z, labels = s) # draw clustring pic
plt.show() # draw clustering pic
