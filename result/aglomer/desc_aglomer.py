from sklearn.cluster import AgglomerativeClustering as AC
from collections import Counter
from matplotlib import pyplot as plt
import math
import numpy as np

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
print('Processed {} descriptors'.format(len(DictF)))

for i in range(2,7):
    agg = AC(n_clusters=i,linkage='ward')
    assignment = agg.fit_predict(ListVal)
    result = Counter(assignment)
    clustElem = {}
    for ind, val in enumerate(assignment):
        if val+1 not in clustElem.keys():
            clustElem[val+1] = [ListKey[ind]]
        else:
            clustElem[val+1].append(ListKey[ind])
    clustMedian = {i[0]:i[1][len(i[1])//2] for i in clustElem.items()}
    print('========== {} lavel =========='.format(i-1))
    print('{} clusters'.format(i))
    cE = list(clustElem.items())
    cE.sort()
    for j in cE:
        print('Number of elements in {0} cluster: {1}'.format(j[0], len(j[1])))
    cM = list(clustMedian.items())
    cM.sort()
    for k in cM:
        print('Median of {0} cluster: {1}'.format(k[0], k[1]))
    for q in cE:
        print('The {0} cluster includes: {1}'.format(q[0], q[1]))
    print()
