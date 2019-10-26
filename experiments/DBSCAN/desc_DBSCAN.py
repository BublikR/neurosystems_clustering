from sklearn.cluster import DBSCAN
import math
import numpy as np
#from sklearn.metrics import pairwise_distances_argmin_min as pdam
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
ListVal = [x for x in ListVal if not math.isnan(x[0]) and (x[0] != 1 and x[1] != 1)]
ListKey = [y for x,y in zip(ListVal, ListKey) if not math.isnan(x[0]) and (x[0] != 1 and x[1] != 1)]

DictF = {x: y for x, y in zip(ListKey, ListVal)}
################################################################
import matplotlib.pyplot as plt
countClust=[]
for k,i in enumerate(np.linspace(0.005, 0.1, 50)):
    subcountClust = []
    for j in range(8, 59):
        db = DBSCAN(eps=i, min_samples=j, metric='euclidean')
        y_db = db.fit_predict(ListVal)
        subcountClust.append(max(Counter(y_db).keys())+1)
    countClust.append(subcountClust)
y = np.arange(8, 59, 1)
z = np.arange(0.005, 0.1, 0.0019)
Y, Z = np.meshgrid(y, z)
X = np.array(countClust)
'''
print(X)
print('++++++++')
print(Y)
print('++++++++')
print(Z)
'''
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
axes = Axes3D(fig)
axes.plot_surface(X, Y, Z)
plt.show()

#plt.plot(countClust, np.linspace(0.01, 0.04, 11), marker='o')
#plt.show()




'''
print("Оброблено {0} дескрипторів".format(len(ListKey)))
print("Отримано {0} кластери з".format(NClust), end = " ")
for i in Count:
    print(Count[i], end = ", ")
print(" елементами.")
for i, j in enumerate(closest):
    print("Медіана {0}-го кластера: {1}".format(i+1, ListKey[j]))
for i, j in enumerate(ListDesc):
    print("{0}-й кластер включає в себе: {1}".format(i+1, j))
'''

