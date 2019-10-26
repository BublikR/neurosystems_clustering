from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min as pdam
from collections import Counter
from matplotlib import pyplot as plt
import math, os, hashlib
import numpy as np
import urllib.request as req
from PIL import Image

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

os.chdir('/media/roman/10A2FE37A2FE20C0/Clustering/') # path to image

print('Processed {} descriptors'.format(len(DictF)))

for i in range(10,51):
    km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=300, random_state=0)
    y_km = km.fit_predict(ListVal)
    result = Counter(y_km)
    clustElem = {}
    for ind, val in enumerate(y_km):
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
        new_image_size = math.ceil(math.sqrt(len(j[1])))
        img = Image.new('RGBA', (new_image_size*100, new_image_size*100))
        count = 0
        for k in range(new_image_size):
            for g in range(new_image_size):
                if count < len(j[1]):
                    img.paste(Image.open(hashlib.sha1(j[1][count].encode()).hexdigest() + '.png'), (g*100, k*100))
                    count += 1
        img.save('/media/roman/10A2FE37A2FE20C0/Clustering_result_image/KMeans/' + str(i) + '_' + str(j[0]) + '_' + str(len(j[1])) + '.png')

