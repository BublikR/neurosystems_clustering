from matplotlib import pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, dendrogram
import pandas as pd
import math
import numpy as np
from collections import Counter

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
#print('Processed {} descriptors'.format(len(DictF)))

df = pd.DataFrame(ListVal)
row_clusters = linkage(pdist(df, metric='euclidean'), method='complete')
#labels = ['' for _ in range(len(ListVal))]
row_dendr = dendrogram(row_clusters, no_labels=True, color_threshold=0.505*max(row_clusters[:,2]))
plt.tight_layout()
plt.ylabel('Евклідова відстань')
plt.xlabel('Індекси станів')
plt.show()
print(Counter(row_dendr['color_list']))

g = row_dendr['color_list'].count('g')
r = row_dendr['color_list'].count('r')
c = row_dendr['color_list'].count('c')
m = row_dendr['color_list'].count('m')
y = row_dendr['color_list'].count('y')

clusters = {}
clusters[1] = [ListKey[x] for x in row_dendr['leaves'][:g+1]]
clusters[2] = [ListKey[x] for x in row_dendr['leaves'][g+1:g+1+r+1]]
clusters[3] = [ListKey[x] for x in row_dendr['leaves'][g+1+r+1:g+1+r+1+c+1]]
clusters[4] = [ListKey[x] for x in row_dendr['leaves'][g+1+r+1+c+1:g+1+r+1+c+1+m+1]]
clusters[5] = [ListKey[x] for x in row_dendr['leaves'][g+1+r+1+c+1+m+1:g+1+r+1+c+1+m+1+y+1]]

print('Length of clusters: {0}, {1}, {2}'.format(len(clusters[3]), len(clusters[4]), len(clusters[5])))
print('Medians:')
print(clusters[3][len(clusters[3])//2])
print(clusters[4][len(clusters[4])//2])
print(clusters[5][len(clusters[5])//2])
for i in clusters.items():
    if i[0] != 1 and i[0] != 2:
        print('{0}-th cluster includes: {1}'.format(i[0], i[1]))
