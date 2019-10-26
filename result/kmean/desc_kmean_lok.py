from sklearn.cluster import KMeans
import math
from sklearn.metrics import pairwise_distances_argmin_min as pdam
from collections import Counter
import numpy as np
from matplotlib import pyplot as plt

f = open("file_new.txt", 'r')
StrF = f.read()
f.close()
ListF = StrF.split()
ListKey = ListF[0::8]
ListKey = [x[10:] for x in ListKey]
#ListKey = [x[:-4] for x in ListKey]
ListKey = ["https://chimera.biomed.kiev.ua/video/pendel-3d/tst.php?res=" + x.split('/')[0] + "#" + x + '/' for x in ListKey]
del ListF[0::8]
ListF = [float(x) for x in ListF]
a = 0
b = 7
ListVal = []
while b <= len(ListF):
    ListVal.append(ListF[a:b])
    a = b
    b = b + 7

# Del NaN and 1
ListKey = [y for x,y in zip(ListVal, ListKey) if not (math.isnan(x[0]) or (x[0] == 1 and x[1] == 1))]
ListVal = [x for x in ListVal if not (math.isnan(x[0]) or (x[0] == 1 and x[1] == 1))]

DictF = {x: y for x, y in zip(ListKey, ListVal)}

# The optimal number of clusters: 
dist = []
for i in range(1,11):
    km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=300,random_state=0)
    km.fit(ListVal)
    dist.append(km.inertia_)

fig, ax = plt.subplots()
ax.plot(range(1,11), dist, marker='o')
ax.grid()
ax.set_xlabel('Number of clusters')
ax.set_ylabel('Total Within Sum of Square')
plt.show()

# max distance
distance = []
for i in range(2,10):
    distance.append(math.fabs((dist[-1]-dist[0])*i - 9*dist[i-1] + 10*dist[0] - dist[-1])/math.sqrt((dist[-1]-dist[0])*(dist[-1]-dist[0]) + 9*9))

print(distance)
NClust = distance.index(max(distance))+2

km = KMeans(n_clusters=NClust, init='k-means++', n_init=10, max_iter=300, random_state=0)
y_km = km.fit_predict(ListVal)
Count = Counter(y_km)
ListDesc = [[] for i in range(NClust)]
for i,j in enumerate(y_km):
    ListDesc[j].append(ListKey[i])
    
# Medians:
closest, _ = pdam(km.cluster_centers_, ListVal)
print("Оброблено {0} дескрипторів".format(len(ListKey)))
print("Отримано {0} кластери з".format(NClust), end = " ")
for i in Count:
    print(Count[i], end = ", ")
print(" елементами.")
for i, j in enumerate(closest):
    print("Медіана {0}-го кластера: {1}".format(i+1, ListKey[j]))
for i, j in enumerate(ListDesc):
    print("{0}-й кластер включає в себе: {1}".format(i+1, j))
