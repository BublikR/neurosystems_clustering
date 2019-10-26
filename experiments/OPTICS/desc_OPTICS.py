from sklearn.cluster import OPTICS
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

opt = OPTICS(min_samples=14)
y_opt = opt.fit_predict(ListVal)
ListKeyN = np.array(ListKey)
print(Counter(y_opt))
#print("Noise: {0}".format(ListKeyN[y_opt==-1]))
print("1-th cluster: {0}".format(ListKeyN[y_opt==20]))

'''
import matplotlib.pyplot as plt
countClust = []
Noise = []
for i in range(8, 109):
    opt = OPTICS(min_samples=i)
    y_opt = opt.fit_predict(ListVal)
    countClust.append(max(Counter(y_opt).keys()))
    Noise.append(Counter(y_opt)[-1])

plt.plot(countClust, range(8, 109), marker='o')
plt.show()
'''
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

